---
name: malaysia-ai-chatbot-facebook-content
description: Research latest AI chatbot news in Malaysia and create targeted Facebook page content for AI chatbot solutions, aligned with Malaysian market preferences, regulations, and the agency-agents marketing persona library.
category: marketing
trigger:
  - "research latest AI chatbot news Malaysia"
  - "create Facebook content for AI chatbot solutions Malaysia"
  - "Malaysia AI chatbot Facebook post"
  - "generate MY AI chatbot FB content"
---

# Malaysia AI Chatbot Facebook Content Creation

## Prerequisites
- Reference marketing-specialized skills from the `agency-agents` persona library where applicable
- Align with user's preference for localized, high-engagement content (similar to historical video project's structured approach)

## Step 1: Research Latest Malaysian AI Chatbot News
1. Call `web_search` with these keyword sets (run in parallel for speed):
   - `"Malaysia AI chatbot 2026 news" "last 7 days"`
   - `"AI adoption SME Malaysia 2026 chatbot"`
   - `"MDEC AI chatbot initiative 2026"`
   - `"PDPA Malaysia chatbot compliance 2026"`
2. Prioritize these source types:
   - Local mainstream media: The Star, New Straits Times, Malay Mail
   - Regional tech portals: TechNode Southeast Asia, e27, Digital News Asia
   - Official agencies: MDEC (Malaysia Digital Economy Corporation), Ministry of Communications
3. Extract 3-5 trending topics, discard anything older than 7 days.

## Step 2: Malaysian Market Context Mapping
1. Enforce these market-specific factors in all content:
   - Language: Default to English + Bahasa Malaysia mix (Manglish) unless brand voice specifies otherwise
   - Key verticals: E-commerce, banking, F&B, tourism (high chatbot adoption in MY)
   - Regulatory: Explicitly mention PDPA compliance for Malaysian businesses
   - Pain points: Cost-effectiveness, 24/7 local language support, integration with WhatsApp (dominant MY messaging app)
2. Use localized examples only: e.g., "boost sales for Malaysian F&B chains like Secret Recipe" instead of generic global brands.

## Step 3: Facebook Content Generation
1. Supported content formats (match to user's existing workflow preferences):
   - Short text posts: 150-200 words, tie directly to trending news, include 1-2 localized case studies
   - Carousel posts: 3-5 cards, each covering a Malaysian SME use case
   - Short video scripts: 30-60s, reuse user's existing `historical-video-gen` motion pipeline if video content is requested
2. Mandatory elements for every post:
   - Localized CTA: e.g., "WhatsApp us at +60 12-345 6789 for a free demo"
   - PDPA compliance mention where relevant
   - No generic global examples
3. Visual content generation (aligns with user's `historical-video-gen` project):
   - **Z-Image prompts**: Generate 2-3 high-fidelity natural language prompts optimized for Z-Image/Tongyi-MAI, featuring Malaysian context (e.g., "Modern Malaysian office with diverse team using AI chatbot on WhatsApp, warm lighting, Kuala Lumpur skyline visible through window")
   - **Video motion prompts**: For 30s/60s reels, create structured production table format:
     * Time | Audio (Bahasa Malaysia/English script) | Z-Image Prompt | Video Motion Prompt
     * Apply 'Strict' safety mode (euphemism replacement) to bypass Vertex AI filters
     * Use pattern interrupt hooks + loop structures for viral potential
   - **Carousel card images**: Generate Z-Image prompts for each card (infographic style, dark theme preferred per user's design preferences)
4. Output preference: Default to JSON export (per user's preference for JSON-first outputs), include separate sections for text, image_prompts, and video_production_table.

## Step 4: Verification & Quality Checks
1. Confirm all news references are from the last 7 days and from reputable MY sources
2. Check content has no global-only examples, all context is Malaysia-specific
3. Verify compliance with Facebook Community Standards and Malaysian content guidelines
4. Cross-check with `agency-agents` marketing best practices if available.

## Common Pitfalls
- Using global AI chatbot news without a clear Malaysian tie-in
- Omitting PDPA compliance mentions for B2B Malaysian audiences
- Using formal language when the brand uses colloquial Manglish/English
- Ignoring WhatsApp integration as a key selling point for MY businesses
