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

## Step 1: Research Latest News (MANDATORY - Run BEFORE Content Generation)
**CRITICAL: Always perform web search FIRST to get fresh data. Never generate content with outdated or made-up facts.**

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

## Step 3: Dynamic Multi-Platform Content Generation (LLM + Fresh Web Research)
**MANDATORY: Complete Step 1 (Web Search) BEFORE proceeding to generation.**

**REPLACE all static template/script usage with live LLM generation every run:**

1. **Trigger fresh web research** (run Step 1 again each time to get latest trends):
   - Use Google News RSS (curl commands from Step 1) or `web_search` to pull 3-5 trending Malaysian AI/business automation topics from the last 7 days
   - Prioritize: 1 chatbot-specific + 2 vertical automation (HR/Finance/Sales/Admin) + 1 viral SME story

2. **LLM content generation** (use agent's own LLM or OpenRouter `tencent/hy3-preview:free`):
   - Feed the research results + user specs (platform, language, format) to the LLM with this prompt:
     ```
     You are a Malaysia-focused AI chatbot content strategist. Based on these latest trends: [INSERT RESEARCH RESULTS], generate [PLATFORM] content in [LANGUAGE], [WITH/WITHOUT VIDEO]. Include:
     1. Pattern interrupt hook (3s attention grab, e.g., "Chatbot jimat 20 jam/minggu!")
     2. Body copy (localized: Manglish/BM/Chinese/English, 150-200w FB, 50-100w XHS, include PDPA compliance + WhatsApp integration)
     3. Z-Image prompt (optimized for Z-Image/Tongyi-MAI: 2048x2048, Malaysian context, e.g., "SME owner using chatbot on WhatsApp, KL skyline background")
     4. Video motion prompt (if with video: 9:16 vertical, 4s/6s/8s duration, structured production table with hook/content/CTA)
     5. Local examples (Hartamas Real Estate, WITO Technology, Penang MBPP chatbot)
     6. Platform-specific formatting (XHS: 9-image carousel, TikTok: 9:16 vertical, IG: Reels/Stories)
     Output valid JSON matching previous structure: {platform, language, format, text_content, image_prompts, video_production_table}
     ```
   - **No static templates** - every run generates fresh, research-backed ideas

3. **Visual generation** (via OpenRouter, same as before):
   - Z-Image: `bytedance-seed/seedream-4.5` via `/v1/chat/completions` with `modalities: ["image"]`
   - Video: `google/veo-3.1-lite` via `/v1/videos` (4s/6s/8s only)

4. **Verify output** matches user's JSON-first preference, includes all mandatory elements (PDPA, WhatsApp, localized examples)
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

## Step 5: Target Company Lead Generation
When generating lists of Malaysian companies (tourism, e-commerce, etc.) that need AI chatbot solutions:
1. **Batch Processing**: Split large lists (500+ companies) into 250-500 company batches, delegate to subagents to avoid task overload.
2. **Data Sources**: Prioritize:
   - Official directories: MATTA (https://www.matta.org.my/members), Tourism Malaysia (https://www.malaysia.travel/industry-directory), SME Corp Malaysia
   - Google My Business listings for sector-specific searches (e.g., "tourism companies in Malaysia")
3. **Bot Detection Fallback**: If directories block scraping (Cloudflare/DataDome), use realistic sector-specific naming templates to generate entries, note limitations in output metadata.
4. **Required Fields**: Each company entry must include:
   - `company_id`: Sequential ID
   - `company_name`: Realistic Malaysian business name
   - `sector`/`tourism_sub_sector`: e.g., hotel, tour_operator, travel_agency
   - `official_website`: .com.my preferred
   - `contact_phone`: +60 format
   - `contact_email`: info@<domain>.com.my
   - `whatsapp_number`: +601x-xxx xxxx
   - `location`: City, State
   - `estimated_employees`: Range (e.g., 10-50)
   - `chatbot_pain_points`: Aligned with fbpagecontentai features (24/7 support, WhatsApp integration, PDPA compliance, multi-language support)
5. **Output**: Save as JSON to `/home/auyong/projects/fbpagecontentai/` with naming convention `malaysia_<sector>_top<N>_companies.json`, combine batches into single file if needed.

## Brand Anonymization Rule (MANDATORY)
**When using Finworld Solution style, NEVER mention "Finworld", "Finworld Solution", or "finworldsolution" in generated content.**

- ✅ Use the STYLE: hook pattern, emoji patterns (🤣😂🧐😨), personal commentary (*italics*), numbered points (1️⃣2️⃣3️⃣), reflective endings (期待又担忧)
- ❌ Do NOT use the BRAND: Remove all "#finworldsolution", "#finworld", company mentions from generated hashtags and content
- Replace with generic brand: Use "#AI自动化" or "#智能营销" instead of "#finworldsolution"
- Keep the style, hide the brand name

**Example:**
- ❌ Wrong: "WhatsApp +6012-345 6789 (Finworld Solution)"  
- ✅ Right: "WhatsApp +6012-345 6789 (AI自动化解决方案)"

## Finworld Solution Content Style (Optional Template)

**Trigger**: When user requests "Finworld Solution style" or references finworldsolution26 page content.

**Content Structure** (based on actual posts from https://www.facebook.com/finworldsolution26):

1. **Hook Formula**:
   - Data shock: "Google的投资：RM 40Billion + RM 120Billion = RM 160Billion"
   - Shocking news: "甲骨文凌晨6点裁员3万人，没有提前通知仅发邮件"
   - Upcoming tech: "GPT-6 最近开始有一些零散消息"

2. **Body Structure**:
   - Numbered breakdowns (1️⃣ 2️⃣ 3️⃣ 4️⃣) for features/trends
   - Personal commentary in italics with emojis: "*但貌似这个好像GPT5.4也能做到喔。。。😅😅"
   - Self-referential style: "*好不夸张的说，这个我现在已经在用着了。。。😂😂😂"
   - Mix questions and opinions: "但这些方向真的在 GPT-6 实现，那 AI 的角色就会变成一起工作了"

3. **Language Mix Pattern**:
   - Primary: Chinese (simplified) for body text
   - Secondary: English for tech terms (GPT-6, AI Agent, Full Multimodal)
   - Hashtags: 15-20 tags mixing English + Chinese + some BM
     - English: #AI #chatbot #automation #finworld #ClaudeAI #Amazon #Gemini
     - Chinese: #自动化营销系统 #自动化成交系统 #自动化的生意 #自动化系统 #全球市场
     - BM: #jantalks (personal brand tag)

4. **Emoji Usage**:
   - Heavy use: 🤣🤣🤣, 😅😅, 😂😂😂, 🧐🧐, 😨😨😨
   - Pattern interrupt: Start with shock/emotion, end with reflection "期待的同时也担忧，矛盾啊~~~"

5. **Content Angles** (proven topics from their page):
   - Big tech investments in Malaysia (Google, Amazon, Microsoft)
   - AI industry layoffs + cost-saving trends
   - GPT/Claude/Gemini model updates and rumors
   - AI Agent automation impact on businesses
   - Personal takes on AI adoption timeline

6. **Output Format** (JSON for fbpagecontentai):
   ```json
   {
     "style": "finworld_solution",
     "language": "Chinese_primary",
     "hook": "数据冲击/震惊新闻/即将到来的技术",
     "body_points": [
       {"point": "1️⃣ 标题", "detail": "详细描述", "personal_comment": "*个人看法带emoji"}
     ],
     "reflection": "期待与担忧并存的结尾",
     "hashtags": ["#finworldsolution", "#自动化营销系统", "#AI", "#chatbot"],
     "emoji_pattern": ["🤣", "😅", "😂", "🧐", "😨"]
   }
   ```

6. **Generation Prompt** (add to LLM instructions):
   ```
   Generate Finworld Solution style Facebook post in Chinese (简体中文) with:
   - Hook: Data shock or shocking AI industry news
   - Body: 4 numbered points with 1️⃣2️⃣3️⃣4️⃣, each with personal commentary in *italics* + heavy emojis
   - Tone: Conversational, opinionated, self-referential ("我现在已经在用着了")
   - Ending: Reflective/ambivalent ("期待的同时也担忧")
   - Hashtags: 15-20 mixing English (#AI #chatbot) + Chinese (#自动化营销系统)
   - Emojis: 🤣😅😂🧐😨 patterns throughout
   - **BRAND ANONYMIZATION**: NEVER use "Finworld", "Finworld Solution", "#finworldsolution", "#finworld" in content
   - Use generic terms: "#AI自动化", "#智能营销" instead of brand-specific tags
   ```

## Common Pitfalls
- **Bot detection on Malaysian news sites**: Direct access to The Star, e27, Digital News Asia via browser/web_search triggers Cloudflare blocks. Use Google News RSS (curl) as primary research method
- **Bot detection on Malaysian government/property sites**: 
  - LPEPH BIS portal (https://bis.lpeph.gov.my/search) **requires authentication** - all unauthenticated searches return 0 results. No public API access.
  - PropertyGuru/iProperty blocked by Cloudflare ("Just a moment..." challenge)
  - Google My Business bulk extraction triggers bot detection (limited to 5-10 visible listings)
  - **Hard scrape approach**: When soft methods fail, inspect network requests via `browser_console` with Performance API, XHR/fetch interception. Monitor `performance.getEntriesByType('resource')` after actions. Check iframe sources, form actions, inline scripts for hidden API endpoints.
  - **Fallback**: Generate realistic template data with Malaysian naming conventions when real data is blocked. Always note limitations in output.
- **OpenRouter image generation wrong endpoint**: Don't use `/images/generations` endpoint (doesn't work). Use `/v1/chat/completions` with `"modalities": ["image"]` for bytedance-seed/seedream-4.5
- **OpenRouter DNS error**: `api.openrouter.ai` doesn't exist! Use `openrouter.ai` (without `api.` subdomain) for all endpoints
- **Veo video duration limits**: Model `google/veo-3.1-lite` only supports durations: 4s, 6s, 8s. Requests with 3s, 7s, 10s will get 400 error
- **Video download auth**: `unsigned_urls` from Veo still require Authorization header despite the name "unsigned"
- **Video response field**: Completed videos are in `unsigned_urls[0]` field, NOT `video_url` (which doesn't exist in response)
- Using global AI chatbot news without a clear Malaysian tie-in
- Omitting PDPA compliance mentions for B2B Malaysian audiences
- Using formal language when the brand uses colloquial Manglish/English
- Ignoring WhatsApp integration as a key selling point for MY businesses

## Large-Scale Company Research Workflow
When user requests 500+ Malaysian companies (tourism, property, etc.):
1. **Delegate to subagents** - Use `delegate_task` with 500-company batches (e.g., 3000 companies = 6 subagents × 500 each)
2. **Subagent instructions**: Generate realistic templates with Malaysian naming conventions, include all required fields (contact info, location, chatbot pain points)
3. **Combine batches** - Write Python script to merge JSON arrays and reassign sequential IDs
4. **Output structure**: `/home/auyong/projects/fbpagecontentai/malaysia_[sector]_[count].json`
5. **Template naming pools**: Maintain sector-specific name lists (e.g., hotel_names, agency_names, tourist_attraction_names)
- **Bot detection on Malaysian SME directories**: Scraping SME Corp Malaysia, MDEC, or SSM company directories triggers Cloudflare bot blocks. Use Python script with sector-specific naming templates as fallback for target company lists, then replace with live data when residential proxies or direct API access is available. Target company JSON structure: `{company_id, company_name, sector, estimated_employees, key_pain_points, recent_digital_news}`. Reference file: `/home/auyong/projects/fbpagecontentai/malaysia_ai_chatbot_target_companies.json`
