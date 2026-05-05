#!/usr/bin/env python3
"""
Generate Z-Image visuals using OpenRouter API with bytedance-seed/seedream-4.5 model
Uses chat completions endpoint with modalities: ["image"] as per official docs
Reusable script for malaysia-ai-chatbot-facebook-content skill

Usage:
  python3 scripts/generate_zimages.py <content_json_path>
"""
import json
import os
import sys
import base64
import requests
from pathlib import Path

def load_api_key():
    """Load OpenRouter API key from ~/.hermes/.env"""
    env_path = Path.home() / ".hermes" / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if line.startswith("OPENROUTER_API_KEY="):
                    return line.strip().split("=", 1)[1].strip('"\'')
    return os.environ.get("OPENROUTER_API_KEY")

def extract_prompts(json_path):
    """Extract all Z-Image prompts from content JSON"""
    with open(json_path) as f:
        data = json.load(f)
    
    prompts = []
    
    # From image_prompts section
    if "image_prompts" in data and "z_image_prompts" in data["image_prompts"]:
        for item in data["image_prompts"]["z_image_prompts"]:
            prompts.append({
                "purpose": item["purpose"],
                "prompt": item["prompt"]
            })
    
    # From video production table
    if "video_production" in data and "production_table" in data["video_production"]:
        for i, scene in enumerate(data["video_production"]["production_table"]):
            if "z_image_prompt" in scene:
                prompts.append({
                    "purpose": f"Video scene {i+1} ({scene['time']})",
                    "prompt": scene["z_image_prompt"]
                })
    
    return prompts

def generate_image(api_key, prompt, model="bytedance-seed/seedream-4.5"):
    """Generate image using OpenRouter chat completions endpoint"""
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "modalities": ["image"]
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers, timeout=120)
    response.raise_for_status()
    result = response.json()
    
    if result.get("choices") and len(result["choices"]) > 0:
        message = result["choices"][0].get("message", {})
        images = message.get("images", [])
        if images:
            image_data = images[0]
            image_url = image_data.get("image_url", {}).get("url", "")
            if image_url and image_url.startswith("data:"):
                header, b64data = image_url.split(",", 1)
                return base64.b64decode(b64data)
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_zimages.py <content_json_path>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    if not Path(json_path).exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)
    
    api_key = load_api_key()
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found")
        sys.exit(1)
    
    prompts = extract_prompts(json_path)
    print(f"Found {len(prompts)} Z-Image prompts to generate")
    
    output_dir = Path(json_path).parent / ".." / "assets" / "images"
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for idx, item in enumerate(prompts):
        print(f"\n[{idx+1}/{len(prompts)}] Generating: {item['purpose']}")
        image_bytes = generate_image(api_key, item["prompt"])
        if image_bytes:
            safe_purpose = item["purpose"].replace("/", "_").replace(" ", "_")[:50]
            output_path = output_dir / f"{idx+1:02d}_{safe_purpose}.png"
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"  ✓ Saved to: {output_path}")
        else:
            print(f"  ✗ Failed to generate image")

if __name__ == "__main__":
    main()
