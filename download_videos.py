#!/usr/bin/env python3
"""
Download completed videos from OpenRouter using video IDs
The videos were already generated, just need to fetch from unsigned_urls
"""
import json
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

output_dir = Path("/home/auyong/projects/fbpagecontentai/assets/videos")
output_dir.mkdir(parents=True, exist_ok=True)

print("Downloading completed videos...")
print("=" * 60)

for video_id, scene_name in video_ids:
    print(f"\n→ Fetching video: {scene_name}")
    print(f"  ID: {video_id}")
    
    # Get video info (with auth)
    info_url = f"https://openrouter.ai/api/v1/videos/{video_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(info_url, headers=headers, timeout=30)
        response.raise_for_status()
        info = response.json()
        
        # Get unsigned URL
        unsigned_urls = info.get("unsigned_urls", [])
        if not unsigned_urls:
            print(f"  ✗ No unsigned_urls in response")
            print(f"  Response: {json.dumps(info)[:200]}")
            continue
        
        video_url = unsigned_urls[0]
        print(f"  ✓ Video URL: {video_url[:70]}...")
        
        # Download video (unsigned URL shouldn't need auth)
        print(f"  → Downloading...")
        video_response = requests.get(video_url, timeout=60)
        video_response.raise_for_status()
        
        output_path = output_dir / f"{scene_name}.mp4"
        with open(output_path, "wb") as f:
            f.write(video_response.content)
        
        print(f"  ✓ Saved to: {output_path}")
        print(f"  ✓ Size: {len(video_response.content) / 1024:.1f} KB")
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        if 'response' in locals():
            print(f"  Response: {response.text[:200]}")

print("\n" + "=" * 60)
print(f"Download complete. Files in: {output_dir}")
for f in output_dir.glob("*.mp4"):
    print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
