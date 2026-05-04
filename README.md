# FBPageContentAI - Malaysia AI Chatbot Facebook Content Generator

Automated content generation system for Malaysian AI chatbot solutions Facebook page, targeting SME market with localized content.

## Project Structure

```
fbpagecontentai/
├── README.md                    # Project documentation (this file)
├── skills/                      # Hermes Agent skill files
│   └── SKILL.md                # malaysia-ai-chatbot-facebook-content skill
├── prompts/                     # Generated image & video prompts
│   ├── z-image-prompts/        # Z-Image/Tongyi-MAI prompts
│   └── video-prompts/          # Video motion prompts (30s/60s)
├── content/                     # Generated Facebook content
│   ├── text-posts/             # Text-only Facebook posts
│   ├── carousel/               # Carousel card content
│   └── video-scripts/          # Video production tables
└── assets/                      # Media assets & references
    ├── images/                 # Generated Z-Image outputs
    └── videos/                 # Generated motion videos
```

## Skill Integration

This project uses the `malaysia-ai-chatbot-facebook-content` skill located in `skills/SKILL.md`.

### Trigger Commands
- "Research latest AI chatbot news Malaysia and create Facebook content"
- "Generate MY AI chatbot FB content with image and video prompts"
- "Create Facebook post for AI chatbot solutions Malaysia"

### Skill Features
- ✅ Latest Malaysian AI chatbot news research (past 7 days)
- ✅ PDPA compliance integration
- ✅ WhatsApp integration highlighting
- ✅ Z-Image prompt generation (optimized for Tongyi-MAI)
- ✅ Video motion prompts (30s/60s reels)
- ✅ 'Strict' safety mode for Vertex AI filters
- ✅ Pattern interrupt hooks + loop structures
- ✅ JSON-first output format

## Workflow Pipeline

1. **Research Phase**: Fetches latest Malaysian AI news via Google News RSS
2. **Content Generation**: Creates localized Facebook posts with Manglish
3. **Visual Prompts**: Generates Z-Image prompts for static visuals
4. **Video Production**: Creates production tables for motion videos
5. **Export**: Saves all content as JSON in `content/` directory

## Malaysian Market Focus

- **Language**: English + Bahasa Malaysia (Manglish)
- **Key Verticals**: E-commerce, Banking, F&B, Tourism
- **Regulatory**: PDPA 2010 compliance required
- **Platform**: WhatsApp integration (88% MY usage)
- **Examples**: Secret Recipe, Penang MBPP, local SMEs

## Usage Examples

```bash
# Generate content with skill
hermes "Research latest AI chatbot news Malaysia and create Facebook content with image and video prompts"

# Output location
ls content/malaysia-ai-chatbot-fb-content-*.json
```

## Dependencies

- Hermes Agent with `malaysia-ai-chatbot-facebook-content` skill loaded
- Access to Google News RSS (no JavaScript required)
- Z-Image/Tongyi-MAI for image generation
- Vertex AI / xAI / OpenRouter for video generation
- `historical-video-gen` project workflow (reused)

## Notes

- All generated content stored in project directory
- JSON format matches user's preference for automation
- Image prompts optimized for Z-Image high-fidelity output
- Video pipeline matches existing `historical-video-gen` workflow
- All examples are Malaysia-specific (no global brands)

---

Created: 2026-05-04
Skill: malaysia-ai-chatbot-facebook-content
Project: fbpagecontentai
