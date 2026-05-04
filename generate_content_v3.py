#!/usr/bin/env python3
"""
Malaysia AI Chatbot Multi-Platform Content Generator v3
Supports: Platform (Facebook/XHS/TikTok/Instagram)
         Language (English/BM/Chinese/Manglish)
         Format (with_video/without_video, image mandatory for most)
"""
import json
import os
import sys
from datetime import datetime

def generate_content(platform="Facebook", language="Manglish", format_type="with_video"):
    """
    Generate social media content for Malaysia AI Chatbot solutions.
    
    Args:
        platform: "Facebook", "XHS", "TikTok", "Instagram"
        language: "English", "BM", "Chinese", "Manglish"
        format_type: "with_video" or "without_video"
    """
    
    # Platform-specific settings
    platform_settings = {
        "Facebook": {
            "text_length": "150-200 words",
            "image_count": "2-3 images or 3-5 carousel cards",
            "hashtag_count": "5-8 hashtags",
            "video_aspect": "16:9 or 9:16",
            "mandatory_image": True
        },
        "XHS": {
            "text_length": "50-100 words (Chinese)",
            "image_count": "9 images (carousel mandatory)",
            "hashtag_count": "10-15 Chinese hashtags",
            "video_aspect": "9:16 (if video)",
            "mandatory_image": True,
            "note": "XHS requires Chinese language content"
        },
        "TikTok": {
            "text_length": "Video-only (caption 50-100 words)",
            "image_count": "None (video-first platform)",
            "hashtag_count": "3-5 trending hashtags",
            "video_aspect": "9:16 vertical ONLY",
            "mandatory_image": False,
            "note": "TikTok is video-only, no image posts"
        },
        "Instagram": {
            "text_length": "125-300 words (Feed) or 50-100 (Reels)",
            "image_count": "1-10 images (Feed) or video (Reels)",
            "hashtag_count": "30 max hashtags",
            "video_aspect": "1:1 (Feed) or 9:16 (Reels)",
            "mandatory_image": True
        }
    }
    
    # Language-specific content templates
    templates = {
        "English": {
            "headline": "Malaysia's SME Digital Revolution is HERE!",
            "hook": "Boss, still manually replying customer WhatsApp at 10PM?",
            "cta": "WhatsApp us NOW for FREE demo!",
            "hashtags": ["#SMEdigitalMY", "#AIchatbotMY", "#PDPAcompliant", "#WhatsAppBusiness", "#MalaysiaBiz"]
        },
        "BM": {
            "headline": "Revolusi Digital SME Malaysia dah SAMPAI!",
            "hook": "Bos, masih jawab WhatsApp customer pukul 10 malam?",
            "cta": "WhatsApp kami SEKARANG untuk demo PERCUMA!",
            "hashtags": ["#SMEdigitalMY", "#AIchatbotMY", "#PDPAcompliant", "#WhatsAppBusiness", "#BizMalaysia"]
        },
        "Chinese": {
            "headline": "马来西亚中小企业数字革命来了！",
            "hook": "老板，还在晚上10点手动回复客户WhatsApp吗？",
            "cta": "立即WhatsApp我们获取免费演示！",
            "hashtags": ["#马来西亚AI", "#智能聊天机器人", "#PDPA合规", "#WhatsApp商业版", "#中小企业"]
        },
        "Manglish": {
            "headline": "Boss, Malaysia's SME digital revolution is HERE lah! 🇲🇾",
            "hook": "Boss, you still manually reply customer WhatsApp at 10PM? 😅",
            "cta": "WhatsApp us NOW for FREE demo lah! 📱",
            "hashtags": ["#SMEdigitalMY", "#AIchatbotMY", "#PDPAcompliant", "#WhatsAppBusiness", "#MalaysiaBiz"]
        }
    }
    
    # Override language for XHS (must be Chinese)
    if platform == "XHS" and language != "Chinese":
        print(f"⚠️  XHS requires Chinese language. Overriding to Chinese.")
        language = "Chinese"
    
    template = templates.get(language, templates["Manglish"])
    settings = platform_settings.get(platform, platform_settings["Facebook"])
    
    # Build base content
    content = {
        "campaign_date": datetime.now().strftime("%Y-%m-%d"),
        "platform": platform,
        "language": language,
        "format": format_type,
        "platform_settings": settings,
        "image_mandatory": settings["mandatory_image"]
    }
    
    # Platform-specific content generation
    if platform == "Facebook":
        content["facebook_post"] = {
            "headline": template["headline"],
            "hook": template["hook"],
            "body": f"""{template['headline']}

Just this week:
✅ Hartamas Real Estate partnered UCAN Technologies to deploy AI in property sales
✅ WITO Technology's CEO shares how they went from 'Ground Zero to Industry Leader'
✅ FutureCFO reports: Malaysia's CFOs are navigating AI transformation

{template['hook']}

At Microark AI, we make AI accessible for EVERY Malaysian SME:

💰 Finance teams - Chatbots handle invoice queries & payment reminders instantly
🏠 Sales teams - Chatbots qualify leads & schedule appointments 24/7
📱 WhatsApp integration - 88% of Malaysians use it daily
✅ PDPA compliant - Your customer data protected by Malaysian law

{template['cta']}""",
            "cta": template["cta"],
            "hashtags": template["hashtags"],
            "local_references": ["Hartamas Real Estate", "WITO Technology", "FutureCFO"]
        }
        
    elif platform == "XHS":
        content["xhs_post"] = {
            "headline": template["headline"],
            "body": f"""{template['headline']} 🇲🇾

本周热门新闻：
✅ Hartamas Real Estate与UCAN Technologies合作部署AI
✅ WITO Technology CEO分享：从"零到行业领导者"的数字化转型之路
✅ FutureCFO报道：马来西亚CFO如何引领AI转型

{template['hook']}

Microark AI让每个马来西亚中小企业都能用上AI：

💰 财务团队 - 聊天机器人即时处理发票查询
🏠 销售团队 - 24/7自动筛选潜在客户
📱 WhatsApp集成 - 88%大马人每天都在用
✅ PDPA合规 - 客户数据受马来西亚法律保护

{template['cta']}""",
            "cta": template["cta"],
            "hashtags": ["#马来西亚AI", "#智能聊天机器人", "#PDPA合规", "#WhatsApp商业版", "#中小企业数字化", "#HartamasRealEstate", "#WITO科技", "#吉隆坡AI", "#聊天机器人马来西亚", "#AI自动化"],
            "image_count": 9,
            "image_style": "Lifestyle + infographic mix, bright colors, Chinese + English text overlay"
        }
        
    elif platform == "TikTok":
        content["tiktok_post"] = {
            "format": "9:16 vertical video ONLY",
            "hook_3s": f"Hartamas Real Estate dah guna AI! ({language})",
            "body": f"""{template['hook']}

At Microark AI, we make AI accessible for EVERY Malaysian SME:
💰 Finance teams - Chatbots handle invoice queries instantly
🏠 Sales teams - Chatbots qualify leads 24/7
📱 WhatsApp integration - PDPA compliant

{template['cta']}""",
            "cta": template["cta"],
            "hashtags": ["#AIchatbotMY", "#SMEdigital", "#WhatsAppBusiness", "#PDPAcompliant"],
            "video_production": {
                "aspect_ratio": "9:16",
                "duration": "30s or 60s",
                "production_table": [
                    {"time": "0-3s", "hook": f"Hartamas Real Estate success story! ({language})", "visual": "Surprised owner reading news on phone"},
                    {"time": "3-10s", "content": "AI chatbot automation benefits", "visual": "Split screen professionals with chatbots"},
                    {"time": "10-20s", "benefit": "24/7 WhatsApp automation", "visual": "Owner sleeping, phone lighting up"},
                    {"time": "20-27s", "cta": f"WhatsApp: +60 12-345 6789 ({language})", "visual": "Owner pointing to camera"},
                    {"time": "27-30s", "brand": "Microark AI - SME Digital Revolution", "visual": "Logo animation"}
                ]
            }
        }
        
    elif platform == "Instagram":
        content["instagram_post"] = {
            "feed_post": {
                "headline": template["headline"],
                "caption": f"""{template['headline']} 🇲🇾

Just this week:
✅ Hartamas Real Estate partnered UCAN Technologies
✅ WITO Technology: 'Ground Zero to Industry Leader'
✅ FutureCFO: Malaysia CFOs navigating AI transformation

{template['hook']}

At Microark AI, we make AI accessible for EVERY Malaysian SME:
💰 Finance - Invoice queries automated
🏠 Sales - Lead qualification 24/7
📱 WhatsApp - 88% Malaysians use it daily
✅ PDPA compliant

{template['cta']}

.
.
.
#SMEdigitalMY #AIchatbotMY #PDPAcompliant #WhatsAppBusiness #MalaysiaBiz #AIMalaysia #SMEautomation #DigitalTransformation #MicroarkAI #HartamasRealEstate""",
                "image_count": "3-5 images",
                "hashtags": template["hashtags"] + ["#AIMalaysia", "#SMEautomation", "#DigitalTransformation", "#MicroarkAI"]
            },
            "reels": {
                "duration": "15-60s",
                "aspect": "9:16 vertical",
                "hook": template["hook"],
                "cta": template["cta"]
            },
            "stories": {
                "format": "15s clips x 3-5 slides",
                "interactive": "Polls, Q&A stickers",
                "cta": "Swipe up to WhatsApp"
            }
        }
    
    # Image prompts (mandatory for most platforms)
    if settings["mandatory_image"] or platform in ["Facebook", "XHS", "Instagram"]:
        if platform == "XHS":
            # XHS needs 9 images
            content["image_prompts"] = {
                "count": 9,
                "images": [
                    {"slide": 1, "purpose": "Hero image - SME digital revolution", "prompt": f"Modern Malaysian SME office with diverse team, Kuala Lumpur skyline, Chinese + English text: {template['headline']}"},
                    {"slide": 2, "purpose": "Finance automation", "prompt": f"Clean infographic, CFO with chatbot icon, text in Chinese: 发票查询？聊天机器人即时处理"},
                    {"slide": 3, "purpose": "Sales automation", "prompt": f"Hartamas Real Estate style, property agent with chatbot on phone, Chinese text: 24/7自动筛选客户"},
                    {"slide": 4, "purpose": "WhatsApp integration", "prompt": f"WhatsApp chat interface on smartphone, Malaysian flag colors, text: 88%大马人每天使用"},
                    {"slide": 5, "purpose": "PDPA compliance", "prompt": f"Shield icon with Malaysian flag, legal document, Chinese text: PDPA合规 - 客户数据受保护"},
                    {"slide": 6, "purpose": "Success story - WITO", "prompt": f"WITO Technology CEO portrait, '从零到行业领导者' text, inspiring style"},
                    {"slide": 7, "purpose": "Hartamas partnership", "prompt": f"Hartamas Real Estate property showcase, UCAN Technologies logo, modern office"},
                    {"slide": 8, "purpose": "Microark AI solution", "prompt": f"Microark AI dashboard on laptop, chatbot interface, happy Malaysian SME owner"},
                    {"slide": 9, "purpose": "CTA slide", "prompt": f"WhatsApp number: +60 12-345 6789, '免费演示' text, neon glow effect, QR code"}
                ]
            }
        else:
            # Facebook/Instagram - 2-3 images
            content["image_prompts"] = {
                "z_image_prompts": [
                    {
                        "purpose": "Hero image - SME digital revolution",
                        "prompt": f"Modern Malaysian SME office with diverse team celebrating digital success, Kuala Lumpur skyline, text overlay in {language}",
                        "style_notes": "Optimized for Z-Image/Tongyi-MAI"
                    },
                    {
                        "purpose": "Carousel card - Finance automation",
                        "prompt": f"Infographic with Malaysian flag colors, CFO with chatbot icon, text in {language}, dark blue gradient",
                        "style_notes": "Dark theme, finance angle"
                    },
                    {
                        "purpose": "Carousel card - Sales automation",
                        "prompt": f"Hartamas Real Estate style, property agent with chatbot on phone, WhatsApp bubbles, text in {language}",
                        "style_notes": "Sales automation highlight"
                    }
                ]
            }
    
    # Video production (only if with_video or TikTok)
    if format_type == "with_video" or platform == "TikTok":
        content["video_production"] = {
            "platform": platform,
            "aspect_ratio": settings["video_aspect"],
            "duration_options": ["15s", "30s", "60s"],
            "production_table": [
                {
                    "time": "0-3s",
                    "audio": f"Hartamas Real Estate success! ({language})",
                    "visual": "Surprised Malaysian SME owner reading news on smartphone",
                    "hook_type": "Pattern interrupt - local success story"
                },
                {
                    "time": "3-10s",
                    "audio": f"AI chatbot automate everything! 24/7 PDPA compliant ({language})",
                    "visual": "Split screen: CFO + Sales agent with chatbot interfaces",
                    "hook_type": "Solution presentation"
                },
                {
                    "time": "10-20s",
                    "audio": f"Customer WhatsApp query? Chatbot answers instantly! ({language})",
                    "visual": "Owner sleeping peacefully, phone glowing with automated replies",
                    "hook_type": "Benefit demonstration"
                },
                {
                    "time": "20-27s",
                    "audio": f"WhatsApp: +60 12-345 6789. Free demo! ({language})",
                    "visual": "Confident owner pointing to camera, WhatsApp number glowing",
                    "hook_type": "Call to action"
                },
                {
                    "time": "27-30s",
                    "audio": f"Microark AI - SME Digital Revolution ({language})",
                    "visual": "Logo animation with Malaysian flag pattern",
                    "hook_type": "Brand recall"
                }
            ]
        }
    
    return content

if __name__ == "__main__":
    # Parse command line arguments
    platform = sys.argv[1] if len(sys.argv) > 1 else "Facebook"
    language = sys.argv[2] if len(sys.argv) > 2 else "Manglish"
    format_type = sys.argv[3] if len(sys.argv) > 3 else "with_video"
    
    # Validate inputs
    valid_platforms = ["Facebook", "XHS", "TikTok", "Instagram"]
    valid_languages = ["English", "BM", "Chinese", "Manglish"]
    valid_formats = ["with_video", "without_video"]
    
    if platform not in valid_platforms:
        print(f"❌ Invalid platform. Choose from: {valid_platforms}")
        sys.exit(1)
    
    if language not in valid_languages:
        print(f"❌ Invalid language. Choose from: {valid_languages}")
        sys.exit(1)
    
    if format_type not in valid_formats:
        print(f"❌ Invalid format. Choose from: {valid_formats}")
        sys.exit(1)
    
    # Generate content
    print(f"\n🚀 Generating content...")
    print(f"   Platform: {platform}")
    print(f"   Language: {language}")
    print(f"   Format: {format_type}")
    
    content = generate_content(platform, language, format_type)
    
    # Save to JSON file
    output_file = f"/home/auyong/projects/fbpagecontentai/content/content_{platform}_{language}_{format_type}_{datetime.now().strftime('%Y%m%d')}.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Content generated: {output_file}")
    print(f"   Image mandatory: {content['image_mandatory']}")
    print(f"   Video included: {'YES' if format_type == 'with_video' or platform == 'TikTok' else 'NO'}")
    
    # Print summary
    if platform == "XHS":
        print(f"   📱 XHS: 9-image carousel (Chinese mandatory)")
    elif platform == "TikTok":
        print(f"   🎵 TikTok: Video-only (9:16 vertical)")
    elif platform == "Instagram":
        print(f"   📸 Instagram: Feed/Reels/Stories supported")
    else:
        print(f"   📘 Facebook: Text + Image + Optional Video")
