#!/usr/bin/env python3
"""
Generate videos using OpenRouter /v1/videos endpoint
Veo model supports durations: 4s, 6s, 8s ONLY
"""
import json
import os
import sys
import requests
import time
import base64
from pathlib import Path

# Load API key
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
print(f"Found {len(scenes)} video scenes")
print("=" * 60)

output_dir = Path("/home/auyong/projects/fbpagecontentai/assets/videos")
output_dir.mkdir(parents=True, exist_ok=True)

image_files = [
    "05_Video_scene_1_(0-3s).png",
    "06_Video_scene_2_(3-10s).png",
    "07_Video_scene_3_(10-20s).png",
    "08_Video_scene_4_(20-27s).png",
    "09_Video_scene_5_(27-30s).png"
]

url = "https://openrouter.ai/api/v1/videos"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Valid durations: 4, 6, 8 seconds
# Map original durations to valid ones
def get_valid_duration(original_duration):
    if original_duration <= 4:
        return 4
    elif original_duration <= 6:
        return 6
    else:
        return 8

for idx, scene in enumerate(scenes):
    if idx >= len(image_files):
        continue
    
    # Extract original duration
    time_str = scene['time']
    parts = time_str.replace('s', '').split('-')
    original_duration = int(parts[1]) - int(parts[0])
    duration = get_valid_duration(original_duration)
    
    print(f"\n[Scene {idx+1}/5] Original: {original_duration}s → Using: {duration}s")
    print(f"Motion: {scene['video_motion_prompt'][:50]}...")
    
    # Read image
    image_path = Path("/home/auyong/projects/fbpagecontentai/assets/images") / image_files[idx]
    if not image_path.exists():
        print(f"  ✗ Image not found: {image_path}")
        continue
    
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode('utf-8')
    
    # Payload - using valid duration
    payload = {
        "model": "google/veo-3.1-lite",
        "prompt": scene["video_motion_prompt"],
        "image": f"data:image/png;base64,{image_b64}",
        "duration": duration,
        "aspect_ratio": "9:16"
    }
    
    try:
        print(f"  → Submitting to Veo API (duration={duration}s)...")
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        # Check response format
        print(f"  → Response: {json.dumps(result)[:200]}...")
        
        # Look for video URL or polling URL
        video_url = None
        polling_url = result.get("polling_url")
        
        if polling_url:
            print(f"  → Polling URL received, waiting for completion...")
            # Poll for completion
            for attempt in range(60):  # Max 10 minutes
                time.sleep(10)
                try:
                    poll_response = requests.get(polling_url, headers=headers, timeout=30)
                    poll_response.raise_for_status()
                    poll_result = poll_response.json()
                    
                    status = poll_result.get("status", "unknown")
                    print(f"    Poll {attempt+1}: status = {status}")
                    
                    if status == "completed":
                        video_url = poll_result.get("video_url")
                        break
                    elif status == "failed":
                        print(f"    ✗ Generation failed: {poll_result}")
                        break
                except Exception as e:
                    print(f"    ✗ Poll error: {e}")
                    break
        else:
            # Maybe direct video URL in response
            video_url = result.get("video_url") or result.get("data", {}).get("video_url")
        
        if video_url:
            print(f"  ✓ Video ready: {video_url[:60]}...")
            # Download video
            video_response = requests.get(video_url, timeout=60)
            video_response.raise_for_status()
            
            output_path = output_dir / f"scene_{idx+1:02d}_source.mp4"
            with open(output_path, "wb") as f:
                f.write(video_response.content)
            print(f"  ✓ Saved to: {output_path} ({len(video_response.content)/1024:.1f} KB)")
        else:
            print(f"  ✗ No video URL in response")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        if 'response' in locals():
            print(f"  Response: {response.text[:300]}")

print("\n" + "=" * 60)
print(f"Video generation complete. Files saved to: {output_dir}")
generated = list(output_dir.glob("*.mp4"))
print(f"Generated {len(generated)} video files:")
for f in generated:
    print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
