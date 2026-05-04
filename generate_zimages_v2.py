#!/usr/bin/env python3
"""
Generate Z-Image visuals using OpenRouter API with bytedance-seed/seedream-4.5 model
Uses chat completions endpoint with modalities: ["image"] as per official docs
"""
import json
import os
import sys
import base64
import requests
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
    print("Error: OPENROUTER_API_KEY not found in ~/.hermes/.env")
    sys.exit(1)

# Load the content JSON
json_path = "/home/auyong/projects/fbpagecontentai/content/malaysia-ai-business-automation-20260504.json"
with open(json_path) as f:
    data = json.load(f)

# Extract all Z-Image prompts
prompts = []

# From image_prompts section (key is "prompt")
if "image_prompts" in data and "z_image_prompts" in data["image_prompts"]:
    for item in data["image_prompts"]["z_image_prompts"]:
        prompts.append({
            "purpose": item["purpose"],
            "prompt": item["prompt"]
        })

# From video production table (key is "z_image_prompt")
if "video_production" in data and "production_table" in data["video_production"]:
    for i, scene in enumerate(data["video_production"]["production_table"]):
        if "z_image_prompt" in scene:
            prompts.append({
                "purpose": f"Video scene {i+1} ({scene['time']})",
                "prompt": scene["z_image_prompt"]
            })

print(f"Found {len(prompts)} Z-Image prompts to generate")
print("=" * 60)

# Create output directory
output_dir = Path("/home/auyong/projects/fbpagecontentai/assets/images")
output_dir.mkdir(parents=True, exist_ok=True)

# OpenRouter API endpoint (chat completions, not images/generations!)
url = "https://openrouter.ai/api/v1/chat/completions"

# Generate images
for idx, item in enumerate(prompts):
    print(f"\n[{idx+1}/{len(prompts)}] Generating: {item['purpose']}")
    print(f"Prompt: {item['prompt'][:80]}...")
    
    payload = {
        "model": "bytedance-seed/seedream-4.5",
        "messages": [
            {
                "role": "user",
                "content": item["prompt"]
            }
        ],
        "modalities": ["image"]  # This enables image generation
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        result = response.json()
        
        # Extract image from assistant message
        if result.get("choices") and len(result["choices"]) > 0:
            message = result["choices"][0].get("message", {})
            images = message.get("images", [])
            
            if images and len(images) > 0:
                image_data = images[0]
                image_url = image_data.get("image_url", {}).get("url", "")
                
                if image_url:
                    # Check if it's a base64 data URL or HTTP URL
                    if image_url.startswith("data:"):
                        # Base64 encoded image
                        header, b64data = image_url.split(",", 1)
                        image_bytes = base64.b64decode(b64data)
                        print(f"  ✓ Received base64 image data")
                    else:
                        # HTTP URL - download it
                        print(f"  ✓ Image URL: {image_url[:60]}...")
                        img_response = requests.get(image_url, timeout=30)
                        img_response.raise_for_status()
                        image_bytes = img_response.content
                    
                    # Save image
                    safe_purpose = item["purpose"].replace("/", "_").replace(" ", "_")[:50]
                    output_path = output_dir / f"{idx+1:02d}_{safe_purpose}.png"
                    with open(output_path, "wb") as f:
                        f.write(image_bytes)
                    print(f"  ✓ Saved to: {output_path}")
                    print(f"  ✓ Size: {len(image_bytes)} bytes")
                else:
                    print(f"  ✗ No image URL in response")
            else:
                print(f"  ✗ No images in response")
                print(f"  Response: {json.dumps(result)[:200]}")
        else:
            print(f"  ✗ Unexpected response format: {json.dumps(result)[:200]}")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        if 'response' in locals():
            print(f"  Response: {response.text[:300]}")

print("\n" + "=" * 60)
print(f"Generation complete. Images saved to: {output_dir}")
print(f"Files: {list(output_dir.glob('*.png'))}")
