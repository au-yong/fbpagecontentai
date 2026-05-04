#!/usr/bin/env python3
"""
Generate videos from static images using OpenRouter
Tries multiple endpoint approaches
"""
import json
import os
import sys
import requests
import time
import base64
from pathlib import Path

# Load OpenRouter API key
env_path = Path.home() / ".hermes" / ".env"
api_key = None
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.startswith("OPENROUTER_API_KEY="):
                api_key = line.strip().split("=", 1)[1].strip('"\'')
                break

if not api_key:
    print("Error: OPENROUTER_API_KEY not found")
    sys.exit(1)

# Load content JSON
json_path = "/home/auyong/projects/fbpagecontentai/content/malaysia-ai-business-automation-20260504.json"
with open(json_path) as f:
    data = json.load(f)

scenes = data["video_production"]["production_table"]
print(f"Found {len(scenes)} video scenes to generate")
print("=" * 60)

output_dir = Path("/home/auyong/projects/fbpagecontentai/assets/videos")
output_dir.mkdir(parents=True, exist_ok=True)

# Image files mapping
image_files = [
    "05_Video_scene_1_(0-3s).png",
    "06_Video_scene_2_(3-10s).png",
    "07_Video_scene_3_(10-20s).png",
    "08_Video_scene_4_(20-27s).png",
    "09_Video_scene_5_(27-30s).png"
]

# Try Method 1: /v1/videos endpoint (fix hostname)
url_videos = "https://openrouter.ai/api/v1/videos"

# Try Method 2: /v1/chat/completions with video modality
url_chat = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

for idx, scene in enumerate(scenes):
    if idx >= len(image_files):
        continue
        
    print(f"\n[Scene {idx+1}/5] Time: {scene['time']}")
    print(f"Motion: {scene['video_motion_prompt'][:50]}...")
    
    # Extract duration
    time_str = scene['time']
    parts = time_str.replace('s', '').split('-')
    duration = int(parts[1]) - int(parts[0])
    
    # Read image
    image_path = Path("/home/auyong/projects/fbpagecontentai/assets/images") / image_files[idx]
    if not image_path.exists():
        print(f"  ✗ Image not found: {image_path}")
        continue
    
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    
    # Try Method 1: /v1/videos endpoint
    print(f"  → Trying /v1/videos endpoint...")
    payload_videos = {
        "model": "google/veo-3.1-lite",
        "prompt": scene["video_motion_prompt"],
        "image": f"data:image/png;base64,{image_b64}",
        "duration": duration,
        "aspect_ratio": "9:16"
    }
    
    try:
        response = requests.post(url_videos, json=payload_videos, headers=headers, timeout=30)
        if response.status_code == 200:
            result = response.json()
            print(f"  ✓ /v1/videos response: {json.dumps(result)[:100]}")
        else:
            print(f"  ✗ /v1/videos failed: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        print(f"  ✗ /v1/videos error: {e}")
    
    # Try Method 2: chat/completions with modalities
    print(f"  → Trying /v1/chat/completions with video modality...")
    payload_chat = {
        "model": "google/veo-3.1-lite",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}},
                    {"type": "text", "text": scene["video_motion_prompt"]}
                ]
            }
        ],
        "modalities": ["video"]
    }
    
    try:
        response = requests.post(url_chat, json=payload_chat, headers=headers, timeout=30)
        if response.status_code == 200:
            result = response.json()
            print(f"  ✓ chat/completions response: {json.dumps(result)[:150]}")
            
            # Check for video in response
            if result.get("choices"):
                message = result["choices"][0].get("message", {})
                if "videos" in message:
                    print(f"  ✓ Video generated in chat response!")
                    # Process video...
        else:
            print(f"  ✗ chat/completions failed: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        print(f"  ✗ chat/completions error: {e}")

print("\n" + "=" * 60)
print("Testing complete. Check output above for working method.")
