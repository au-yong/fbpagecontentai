---
name: malaysia-ai-chatbot-facebook-content
description: Research latest AI chatbot news in Malaysia and create targeted Facebook page content for AI chatbot solutions, aligned with Malaysian market preferences, regulations, and the agency-agents marketing persona library.
category: marketing
trigger:
  - "research latest AI chatbot news Malaysia"
  - "create Facebook content for AI chatbot solutions Malaysia"
  - "Malaysia AI chatbot Facebook post"
  - "generate MY AI chatbot FB content"
  - "generate MY AI chatbot FB content in Chinese"
  - "generate MY AI chatbot FB content in BM"
  - "generate MY AI chatbot FB content with video"
  - "generate MY AI chatbot FB content without video"
  - "create AI chatbot FB post English BM Chinese"
  - "generate MY AI chatbot content for XHS"
  - "generate MY AI chatbot content for TikTok"
  - "generate MY AI chatbot content for Instagram"
  - "generate MY AI chatbot content multi-platform"
---

# Malaysia AI Chatbot Facebook Content Creation

## Prerequisites
- Reference marketing-specialized skills from the `agency-agents` persona library where applicable
- Align with user's preference for localized, high-engagement content (similar to historical video project's structured approach)

## Support Files
- `references/openrouter-image-gen.md` - Correct OpenRouter image generation technique (chat completions + modalities)
- `scripts/generate_zimages.py` - Reusable script to generate Z-Images from content JSON
- `references/posting-workflow.md` - Facebook posting workflow (Graph API, anti-bot measures, user preferences)

## Step1: Research Latest Malaysian AI Business Automation News
1. **Primary method: Google News RSS (avoids bot detection on MY news sites)**
   Run via terminal with multiple keyword sets for comprehensive coverage:
   ```bash
   # Core chatbot news
   curl -s "https://news.google.com/rss/search?q=Malaysia+AI+chatbot+2026&hl=en-MY&gl=MY&ceid=MY:en" | grep -oP '(?<=<title>).*?(?=</title>)' | head -5
   
   # HR automation (connect to chatbot HR FAQ/leave applications)
   curl -s "https://news.google.com/rss/search?q=Malaysia+AI+HR+automation+recruitment+payroll&hl=en-MY&gl=MY&ceid=MY:en" | grep -oP '(?<=<title>).*?(?=</title>)' | head -3
   
   # Finance automation (connect to chatbot invoicing/expense queries)
   curl -s "https://news.google.com/rss/search?q=Malaysia+AI+finance+automation+accounting&hl=en-MY&gl=MY&ceid=MY:en" | grep -oP '(?<=<title>).*?(?=</title>)' | head -3
   
   # Sales automation (connect to chatbot lead gen/customer service)
   curl -s "https://news.google.com/rss/search?q=Malaysia+AI+sales+automation+lead+generation&hl=en-MY&gl=MY&ceid=MY:en" | grep -oP '(?<=<title>).*?(?=</title>)' | head -3
   
   # Admin automation (connect to chatbot document/scheduling queries)
   curl -s "https://news.google.com/rss/search?q=Malaysia+AI+admin+automation+document+processing&hl=en-MY&gl=MY&ceid=MY:en" | grep -oP '(?<=<title>).*?(?=</title>)' | head -3
   
   # Viral business stories (high engagement)
   curl -s "https://news.google.com/rss/search?q=Malaysia+SME+digital+transformation+success+story&hl=en-MY&gl=MY&ceid=MY:en" | grep -oP '(?<=<title>).*?(?=</title>)' | head -3
   ```
2. **Fallback: web_search (if RSS fails)**
   Call `web_search` with keyword sets (expect blocks on local sites):
   - `"Malaysia AI chatbot 2026 news" "last 7 days"`
   - `"AI adoption SME Malaysia 2026"`
   - `"Malaysia AI HR automation recruitment 2026"`
   - `"Malaysia business automation viral 2026"`
3. Prioritize sources from Google News RSS (automatically filters to MY-local sources):
   - Local mainstream media: The Star, New Straits Times, Malay Mail
   - Regional tech portals: e27, Digital News Asia
   - Business portals: The Edge Malaysia, Focus Malaysia, SME Magazine
   - Official agencies: MDEC, Ministry of Communications
4. Extract 3-5 trending topics from diverse categories:
   - Aim for 1 chatbot-specific + 1-2 vertical automation (HR/Finance/Sales/Admin) + 1 viral business story
   - Discard anything older than 7 days
5. **Content angle strategy:** For each non-chatbot news item, identify the "chatbot connection":
   - *HR automation trend* → "Chatbots can automate HR FAQ, leave applications, and employee onboarding 24/7"
   - *Finance automation trend* → "Chatbots can handle invoice queries, expense approvals, and payment reminders instantly"
   - *Sales automation trend* → "Chatbots qualify leads, answer product questions, and schedule demos while you sleep"
   - *Admin automation trend* → "Chatbots automate document requests, appointment scheduling, and routine inquiries"

## Step 2: Malaysian Market Context Mapping
1. Enforce these market-specific factors in all content:
   - Language: Default to English + Bahasa Malaysia mix (Manglish) unless brand voice specifies otherwise
   - Key verticals: E-commerce, banking, F&B, tourism (high chatbot adoption in MY)
   - Regulatory: Explicitly mention PDPA compliance for Malaysian businesses
   - Pain points: Cost-effectiveness, 24/7 local language support, integration with WhatsApp (dominant MY messaging app)
2. Use localized examples only: e.g., "boost sales for Malaysian F&B chains like Secret Recipe" instead of generic global brands.

## Step3: Multi-Platform Content Generation

### Platform Options (specify in trigger or prompt)
- **Facebook**: Text + image (mandatory) + optional video, longer copy (150-200 words), supports multiple images/carousel
- **XHS (小红书)**: Chinese-focused, 9-image carousels preferred, shorter text (50-100 words), heavy use of emojis, Chinese hashtags (#AI聊天机器人)
- **TikTok**: Video-first (15s/30s/60s), vertical 9:16, hook in first 3 seconds, trending sounds, English/BM/Manglish audio
- **Instagram**: 3 formats - Feed (image + caption), Reels (video 9:16), Stories (disappearing, 15s clips)

### Language Options (specify in trigger or prompt)
- **English**: Professional marketing tone, suitable for corporate audiences
- **Bahasa Malaysia (BM)**: Full BM content, formal to colloquial depending on brand voice
- **Chinese (中文)**: Traditional or Simplified Chinese, target Chinese-Malaysian SMEs (MUST for XHS)
- **Manglish**: English + BM mix (default), colloquial "boss" tone, highly engaging for local SMEs

### Content Format Options
- **With Video**: Full package - text + Z-Image visuals + video scenes (30s/60s)
- **Without Video**: Text + Z-Image visuals only (no video generation)
- **Image is MANDATORY**: Every content package must include Z-Image prompts/visuals (except TikTok which is video-only)

1. Supported content formats by platform:
   - **Facebook**: Short text posts (150-200 words), carousels (3-5 cards), optional video (30s-60s)
   - **XHS**: 9-image carousel posts (mandatory), short caption (50-100 words), Chinese hashtags
   - **TikTok**: Video-only (15s/30s/60s), structured production table, pattern interrupt hooks
   - **Instagram Feed**: Single/Multiple images + caption (125-300 words), hashtags (30 max)
   - **Instagram Reels**: Video (15s-90s), vertical 9:16, trending audio integration
   - **Instagram Stories**: 15s video clips (3-5 slides), interactive stickers (polls, Q&A)

2. Mandatory elements for every post:
   - Localized CTA: e.g., "WhatsApp us at +60 12-345 6789 for a free demo"
   - PDPA compliance mention where relevant
   - No generic global examples
   - **Image content**: Always generate Z-Image prompts/visuals (mandatory for FB/XHS/IG Feed)

3. Platform-specific visual content generation:
   - **Facebook/XHS/IG Feed**: Z-Image prompts (MANDATORY) - 2-3 high-fidelity prompts optimized for Z-Image/Tongyi-MAI
   - **TikTok/IG Reels**: Video motion prompts (MANDATORY) - structured production table with hook/loop
   - **XHS**: 9-image carousel prompts (MANDATORY) - each image needs unique Z-Image prompt
   - **IG Stories**: 15s video clips with interactive elements (polls, Q&A prompts)

4. **Generate visuals via OpenRouter** (CRITICAL: use correct endpoints):
   - **Z-Image generation** (bytedance-seed/seedream-4.5):
     * Endpoint: `https://openrouter.ai/api/v1/chat/completions` (NOT `/images/generations` - that doesn't work!)
     * Payload: `{"model": "bytedance-seed/seedream-4.5", "messages": [{"role": "user", "content": prompt}], "modalities": ["image"]}`
     * Response: Base64 image in `choices[0].message.images[0].image_url.url`
     * DNS note: Use `openrouter.ai` NOT `api.openrouter.ai` (DNS fails for api subdomain)
   - **Video generation** (google/veo-3.1-lite):
     * Endpoint: `https://openrouter.ai/api/v1/videos`
     * Payload: `{"model": "google/veo-3.1-lite", "prompt": motion_prompt, "image": "data:image/png;base64,...", "duration": <4|6|8>, "aspect_ratio": "9:16"}`
     * Valid durations: ONLY 4s, 6s, or 8s (not 3s, 7s, 10s - will get 400 error)
     * Poll `polling_url` from response until status = "completed"
     * Download from `unsigned_urls[0]` (requires auth header despite "unsigned" name)
   - **Output preference**: Default to JSON export (per user's preference for JSON-first outputs), include separate sections for:
     * `platform`: Target platform (Facebook/XHS/TikTok/Instagram)
     * `language`: Selected language (English/BM/Chinese/Manglish)
     * `format`: "with_video" or "without_video" (image mandatory for most platforms)
     * `text_content`: Post copy adapted to platform (FB: 150-200w, XHS: 50-100w, IG: 125-300w)
     * `image_prompts`: Z-Image prompts (MANDATORY for FB/XHS/IG Feed, 9 images for XHS)
     * `video_production_table`: Only if format="with_video" (TikTok/IG Reels: 9:16 vertical)
     * `carousel_cards`: XHS 9-image carousel or FB 3-5 card prompts
     * `stories_clips`: IG Stories 15s clips with interactive elements

## Step 4: Verification & Quality Checks
1. Confirm all news references are from the last 7 days and from reputable MY sources
2. Check content has no global-only examples, all context is Malaysia-specific
3. Verify compliance with Facebook Community Standards and Malaysian content guidelines
4. Cross-check with `agency-agents` marketing best practices if available.

## Common Pitfalls
- **Bot detection on Malaysian news sites**: Direct access to The Star, e27, Digital News Asia via browser/web_search triggers Cloudflare blocks. Use Google News RSS (curl) as primary research method
- **OpenRouter image generation wrong endpoint**: Don't use `/images/generations` endpoint (doesn't work). Use `/v1/chat/completions` with `"modalities": ["image"]` for bytedance-seed/seedream-4.5
- **OpenRouter DNS error**: `api.openrouter.ai` doesn't exist! Use `openrouter.ai` (without `api.` subdomain) for all endpoints
- **Veo video duration limits**: Model `google/veo-3.1-lite` only supports durations: 4s, 6s, 8s. Requests with 3s, 7s, 10s will get 400 error
- **Video download auth**: `unsigned_urls` from Veo still require Authorization header despite the name "unsigned"
- **Video response field**: Completed videos are in `unsigned_urls[0]` field, NOT `video_url` (which doesn't exist in response)
- Using global AI chatbot news without a clear Malaysian tie-in
- Omitting PDPA compliance mentions for B2B Malaysian audiences
- Using formal language when the brand uses colloquial Manglish/English
- Ignoring WhatsApp integration as a key selling point for MY businesses
