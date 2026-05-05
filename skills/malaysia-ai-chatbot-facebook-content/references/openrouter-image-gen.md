# OpenRouter Image Generation - Correct Approach

## The Problem (Common Mistake)
OpenRouter does NOT support the standard `/v1/images/generations` endpoint for image generation. Attempting to use it returns HTML error pages.

## The Solution (Official Method)
Use the **CHAT COMPLETIONS endpoint** with `modalities: ["image"]` parameter.

### Working Code Pattern

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer <OPENROUTER_API_KEY>",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "bytedance-seed/seedream-4.5",
        "messages": [
            {
                "role": "user",
                "content": "Your image prompt here"
            }
        ],
        "modalities": ["image"]  # THIS enables image generation
    })
)

result = response.json()

# Extract generated image
if result.get("choices"):
    message = result["choices"][0]["message"]
    if message.get("images"):
        for image in message["images"]:
            image_url = image["image_url"]["url"]  # Base64 data URL
            # Decode base64: image_url.split(",", 1)[1] -> base64 data
```

## Key Points

1. **Endpoint:** `https://openrouter.ai/api/v1/chat/completions` (NOT `/v1/images/generations`)
2. **Model:** `bytedance-seed/seedream-4.5` (or other image-capable models)
3. **Parameter:** `"modalities": ["image"]` in the request body
4. **Response:** Images come as base64 data URLs in `message["images"][0]["image_url"]["url"]`
5. **Format:** `data:image/png;base64,<base64_data>`

## Tested With
- Model: `bytedance-seed/seedream-4.5`
- Session: 2026-05-04
- Generated: 9 Z-Image visuals (2048x2048 JPEG)
- Output: Base64 data URLs successfully decoded to PNG files

## Common Errors
- Using `/v1/images/generations` → Returns HTML error page
- Forgetting `modalities: ["image"]` → Returns text only
- Not decoding base64 from data URL → Gets raw base64 string instead of image bytes
