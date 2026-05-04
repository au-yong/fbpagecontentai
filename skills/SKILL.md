---
name: malaysia-ai-chatbot-fb-ads-funnel
description: Generate Facebook Ads content with TOFU/MOFU/BOFU funnel strategy for Malaysia AI chatbot solutions, optimized for cost-saving and maximum ROAS (Return on Ad Spend).
category: marketing
trigger:
  - "create FB ads for MY AI chatbot"
  - "generate TOFU MOFU BOFU ads Malaysia"
  - "Facebook ads funnel strategy AI chatbot"
  - "cost-effective FB ads for Malaysian SME"
  - "maximize ROAS AI chatbot ads"
  - "FB ads content TOFU awareness"
  - "FB ads content MOFU consideration"
  - "FB ads content BOFU conversion"
---

# Malaysia AI Chatbot Facebook Ads Funnel Strategy

## Prerequisites
- Reference `malaysia-ai-chatbot-facebook-content` skill for base content templates
- Use OpenRouter for image generation (bytedance-seed/seedream-4.5)
- Align with Malaysian market: PDPA compliance, WhatsApp integration, BM/English/Manglish
- Cost-saving focus: Minimize CPM (Cost Per Mille), maximize CTR (Click-Through Rate) and CVR (Conversion Rate)

## Facebook Ads Funnel Overview

### TOFU (Top of Funnel) - Awareness Stage
**Objective**: Brand awareness, problem agitation
**Audience**: Cold traffic, broad Malaysian SME owners
**Budget Allocation**: 40% of total ad spend
**KPIs**: Reach, Impressions, CPM, Video views (3s/10s)

**Content Strategy:**
- Problem-focused: "Boss, still manually reply WhatsApp 10PM?"
- Educational: "5 signs your SME needs AI chatbot"
- Local success stories: "Hartamas Real Estate uses AI to sell properties"
- Video preferred: 15s/30s vertical (9:16)

**Ad Formats:**
- Video (15s-30s): Pattern interrupt hook, local context
- Carousel (3-5 cards): Problem → Solution → Proof
- Single image: Bold headline, minimal text (20% rule)

### MOFU (Middle of Funnel) - Consideration Stage
**Objective**: Lead generation, retargeting TOFU visitors
**Audience**: Warm traffic, engaged users, retargeting pixel
**Budget Allocation**: 35% of total ad spend
**KPIs**: CTR, CPL (Cost Per Lead), Engagement rate

**Content Strategy:**
- Solution-focused: "How chatbots saved Hartamas 20 hours/week"
- Comparison: "Manual vs AI: Which costs more?"
- Case study: "WITO Technology: Ground Zero to Industry Leader"
- Lead magnet: "FREE AI Readiness Assessment"

**Ad Formats:**
- Lead forms: Instant Form (name, phone, company, pain point)
- Video testimonials: 30s-60s with Malaysian SME owners
- Carousel: Feature breakdown (Finance/Sales/Admin automation)

### BOFU (Bottom of Funnel) - Conversion Stage
**Objective**: Direct sales, appointment booking
**Audience**: Hot traffic, cart abandoners, high-intent users
**Budget Allocation**: 25% of total ad spend
**KPIs**: CPA (Cost Per Acquisition), ROAS, Conversion rate

**Content Strategy:**
- Offer-focused: "FREE Demo for 10 companies only!"
- Urgency: "WhatsApp +60 12-345 6789 NOW, slots running out"
- Guarantee: "PDPA compliant, 88% Malaysians use WhatsApp daily"
- Social proof: "500+ SMEs transformed"

**Ad Formats:**
- Single image/Video: Clear CTA button ("Book Demo", "WhatsApp Now")
- Carousel: Testimonials + Offer + CTA
- Collection ads: Feature showcase with product catalog

## Step 1: Research Smart Cost-Saving Strategies

1. **Audience Targeting Optimization** (reduces CPM by 30-50%):
   ```bash
   # Target Malaysian SME owners
   Interests: "Small Business Malaysia", "SME Association Malaysia", "MDEC"
   Behaviors: "Business page admins", "Frequent travelers (business)"
   Demographics: Age 25-45, Location: MY major cities (KL, Penang, JB)
   Exclusions: "Existing customers", "Job seekers"
   ```

2. **Creative Testing Strategy** (find winning ads faster):
   - Create 3-5 ad variations per funnel stage
   - Test different hooks: Problem vs Opportunity vs Success story
   - Test different visuals: Lifestyle vs Infographic vs Screenshot
   - Kill underperforming ads after 48h (CTR < 1%)

3. **Bid Strategy for Cost Efficiency**:
   - TOFU: "Lowest cost" bid strategy (maximize reach)
   - MOFU: "Cost cap" bid (CPL < RM15 target)
   - BOFU: "Bid cap" or "Lowest cost" with higher budget (CPA < RM50)

4. **Retargeting Pixel Setup**:
   - Page View: Retarget with MOFU content
   - Lead Form: Retarget with BOFU offer
   - WhatsApp Click: Retarget with testimonials

## Step2: Dynamic Funnel Ad Content Generation (LLM + Fresh Web Research)
**REPLACE all static ad templates with live LLM generation every run:**

1. **Trigger fresh web research** (each run to get latest trends):
   - Search latest Malaysian SME pain points: `web_search("Malaysia SME business challenges 2026", "last 7 days")`
   - Research competitor ads: `web_search("AI chatbot ads Malaysia Facebook 2026")`
   - Find viral SME success stories: `web_search("Malaysia SME AI transformation success 2026")`
   - Pull top 3 trending topics + 2 competitor ad angles

2. **LLM ad content generation** (use agent's own LLM or OpenRouter `tencent/hy3-preview:free`):
   - Feed research results + funnel stage (TOFU/MOFU/BOFU) + language to LLM with this prompt:
     ```
     You are a Malaysia-focused Facebook Ads strategist. Based on these latest trends: [INSERT RESEARCH RESULTS], generate [FUNNEL_STAGE] ad content in [LANGUAGE] for AI chatbot solutions. Include:
     1. Hook (problem agitation for TOFU, solution proof for MOFU, urgency offer for BOFU)
     2. Body copy (localized: Manglish/BM/Chinese/English, include PDPA compliance + WhatsApp integration)
     3. Z-Image prompt (optimized for Z-Image: 2048x2048, Malaysian SME context)
     4. Video motion prompt (if video: 9:16 vertical, 4s/6s/8s, structured production table)
     5. Local examples (Hartamas Real Estate, WITO Technology, Penang MBPP)
     6. Bid strategy (TOFU: Lowest Cost, MOFU: Cost Cap CPL<RM15, BOFU: Bid Cap CPA<RM50)
     Output valid JSON matching previous structure: {funnel_stage, language, ad_creative, audience_targeting, budget_bid_strategy}
     ```
   - **No static templates** - every run generates fresh, research-backed ad ideas

3. **Cost-saving integration** (auto-apply from Step1):
   - Auto-set bid strategy based on funnel stage
   - Include retargeting pixel setup instructions
   - Add performance kill thresholds (CTR <1%, CPL>RM20, CPA>RM50)

4. **Verify output** matches user's JSON-first preference, includes all mandatory elements (PDPA, WhatsApp, localized examples)
## Step 3: Creative Assets Generation (Image + Video)

1. **Z-Image Prompts** (mandatory for all ad types):
   - TOFU: Problem agitation imagery (tired boss, messy WhatsApp)
   - MOFU: Solution demonstration (chatbot UI, happy customers)
   - BOFU: Success celebration (handshake, thumbs up, contact info)

2. **Video Production Table** (15s/30s/60s):
   - Structure: Hook (3s) → Problem/Solution/Offer (body) → CTA (3s)
   - Safety mode: 'Strict' (euphemism replacement for Vertex AI)
   - Aspect ratio: 9:16 vertical (mobile-first for MY)

3. **Cost-Saving Creative Tips**:
   - Reuse TOFU video for MOFU/BOFU (just change text overlay)
   - Use template-based designs (reduce design time by 70%)
   - Batch-create 5-10 variations in one session

## Step 4: Campaign Structure & Budget Optimization

### Campaign Hierarchy:
```
Campaign 1: TOFU - Awareness (Budget: 40%, Bid: Lowest Cost)
  └── Ad Set 1: Cold audience (Broad MY SME)
  └── Ad Set 2: Lookalike 1% (from leads)
  └── Ad Set 3: Video viewers (50%+) 

Campaign 2: MOFU - Consideration (Budget: 35%, Bid: Cost Cap CPL<RM15)
  └── Ad Set 1: Retargeting (Page engagers, video viewers)
  └── Ad Set 2: Lead forms (Instant forms)
  └── Ad Set 3: Custom intent (researched AI chatbot)

Campaign 3: BOFU - Conversion (Budget: 25%, Bid: Lowest Cost, Higher budget)
  └── Ad Set 1: High-intent (Lead form submitters, WhatsApp clickers)
  └── Ad Set 2: Cart abandoners (if applicable)
  └── Ad Set 3: Existing customers (upsell/cross-sell)
```

### Smart Budget Allocation (Daily):
- Total Budget: RM100/day (example)
  - TOFU: RM40/day (Reach maximization)
  - MOFU: RM35/day (Lead generation)
  - BOFU: RM25/day (Direct conversion)

### Performance Monitoring (Check every 48h):
- TOFU: Kill ads with CTR < 1% or CPM > RM15
- MOFU: Kill ads with CPL > RM20 or CTR < 1.5%
- BOFU: Kill ads with CPA > RM50 or CVR < 2%

## Step 5: Generate Ad Content JSON (Output Format)

```json
{
  "campaign_date": "2026-05-04",
  "funnel_stage": "TOFU|MOFU|BOFU",
  "platform": "Facebook Ads",
  "language": "English|BM|Manglish|Chinese",
  "budget_allocation": "40%|35%|25%",
  "target_kpis": {
    "TOFU": ["Reach", "CPM", "Video views"],
    "MOFU": ["CTR", "CPL", "Leads"],
    "BOFU": ["CPA", "ROAS", "Conversions"]
  },
  "ad_creative": {
    "format": "Video|Carousel|Single Image",
    "hook": "Problem/Opportunity/Success story",
    "headline": "Main headline",
    "body": "Ad copy (50-125 words)",
    "cta_button": "WhatsApp Now|Learn More|Sign Up",
    "image_prompts": [Z-Image prompts],
    "video_production_table": [Time|Aduio|Visual|CTA]
  },
  "audience_targeting": {
    "interests": ["Small Business MY", "MDEC", "SME Association"],
    "demographics": "Age 25-45, MY cities",
    "exclusions": ["Existing customers"]
  },
  "budget_bid_strategy": {
    "daily_budget": "RM40 (TOFU example)",
    "bid_strategy": "Lowest Cost|Cost Cap|Bid Cap",
    "target_cost": "CPL < RM15 (MOFU example)"
  },
  "pixel_retargeting": "Page View → MOFU, Lead Form → BOFU"
}
```

## Step 6: Verification & Cost-Saving Checks

1. **Creative Compliance**:
   - Text-to-image ratio < 20% (Facebook 20% rule)
   - PDPA compliance mentioned (for B2B MY audiences)
   - WhatsApp number clearly visible
   - Local examples only (Hartamas, WITO, etc.)

2. **Cost Efficiency**:
   - Kill underperforming ads within 48h
   - Use retargeting pixel (reduces CPL by 40-60%)
   - Test 3-5 ad variations per funnel stage
   - Reuse creative assets across funnel stages

3. **Conversion Tracking**:
   - Setup Facebook Pixel + Conversions API
   - Track: Lead form submissions, WhatsApp clicks, Website purchases
   - ROAS target: > 3.0 (RM3 returned for every RM1 spent)

## Common Pitfalls

- **Wrong budget allocation**: Spending too much on BOFU without filling funnel top (TOFU/MOFU)
- **No retargeting**: Missing pixel setup, wasting 40-60% budget on cold traffic only
- **Ignoring creative fatigue**: Same ad running >7 days, CTR drops by 30-50%
- **Over-targeting**: Too narrow audience ( < 500K) increases CPM by 2-3x
- **No A/B testing**: Running single ad version, missing 20-30% performance gains
- **Ignoring mobile-first**: Using 16:9 horizontal videos in mobile-heavy MY market
- **Forgetting local context**: Using global examples instead of Malaysian SME stories

## Support Files
- `references/fb-ads-bid-strategies.md` - Detailed bid strategy guide
- `scripts/generate_funnel_ads.py` - Automated ad content generator
- `templates/ad-creative-brief.md` - Creative brief template for designers
