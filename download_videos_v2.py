#!/usr/bin/env python3
"""
Download completed videos from OpenRouter using video IDs
Includes auth header for content download
"""
import json
import os
import requests
from pathlib import Path

# Video IDs from previous generation (all completed)
video_ids = [
    ("12G8xwdVh4XbTIbV0UYE", "scene_01_0-3s"),
    ("srFLtHsUBEfEm7s7xSrS", "scene_02_3-10s"),
    ("mOCZVgTaeX472yfWOujU", "scene_03_10-20s"),
    ("mAE6AS6MrRTaG0tBCMpw", "scene_04_20-27s"),
    ("xLLRfCmZhctaHaO1SvJa", "scene_05_27-30s")
]

# Get API key
env_path = Path.home() / ".hermes" / ".env"
api_key = None
with open(env_path) as f:
    for line in f:
        if line.startswith("OPENROUTER_API_KEY="):
            api_key = line.strip().split("=", 1)[1].strip('"\'')
            break

if not api_key:
    print("Error: OPENROUTER_API_KEY not found")
    exit(1)

output_dir = Path("/home/auyong/projects/fbpagecontentai/assets/videos")
output_dir.mkdir(parents=True, exist_ok=True)

print("Downloading completed videos (with auth header)...")
print("=" * 60)

headers = {"Authorization": f"Bearer {api_key}"}

for video_id, scene_name in video_ids:
    print(f"\n→ Downloading video: {scene_name}")
    print(f"  ID: {video_id}")
    
    # Get video info first
    info_url = f"https://openrouter.ai/api/v1/videos/{video_id}"
    
    try:
        response = requests.get(info_url, headers=headers, timeout=30)
        response.raise_for_status()
        info = response.json()
        
        # Get unsigned URL
        unsigned_urls = info.get("unsigned_urls", [])
        if not unsigned_urls:
            print(f"  ✗ No unsigned_urls in response")
            continue
        
        video_url = unsigned_urls[0]
        print(f"  ✓ Video content URL: {video_url[:70]}...")
        
        # Download video WITH auth header
        print(f"  → Downloading video content...")
        video_response = requests.get(video_url, headers=headers, timeout=120)
        video_response.raise_for_status()
        
        output_path = output_dir / f"{scene_name}.mp4"
        with open(output_path, "wb") as f:
            f.write(video_response.content)
        
        print(f"  ✓ Saved to: {output_path}")
        print(f"  ✓ Size: {len(video_response.content) / 1024:.1f} KB")
        
        # Verify it's a valid video file
        if video_response.content[:4] == b'\x1a\x45\xdf\xa3':  # WebM
            print(f"  ✓ Valid WebM video file")
        elif video_response.content[:4] == b'\x00\x00\x00\x1c':  # MP4
            print(f"  ✓ Valid MP4 video file")
        else:
            print(f"  ⚠ File signature: {video_response.content[:8].hex()}")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        if 'response' in locals():
            print(f"  Response: {response.text[:200]}")

print("\n" + "=" * 60)
print(f"Download complete. Files in: {output_dir}")
for f in output_dir.glob("*.mp4"):
    print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
