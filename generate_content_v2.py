#!/usr/bin/env python3
"""
Malaysia AI Chatbot Facebook Content Generator v2
Supports: Language options (English/BM/Chinese/Manglish)
         Format options (with_video/without_video, image mandatory)
"""
import json
import os
import sys
from datetime import datetime

def generate_content(language="Manglish", format_type="with_video"):
    """
    Generate Facebook content for Malaysia AI Chatbot solutions.
    
    Args:
        language: "English", "BM", "Chinese", "Manglish" (default)
        format_type: "with_video" or "without_video" (image always included)
    """
    
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
    
    template = templates.get(language, templates["Manglish"])
    
    # Build content JSON
    content = {
        "campaign_date": datetime.now().strftime("%Y-%m-%d"),
        "language": language,
        "format": format_type,
        "image_mandatory": True,
        "facebook_post": {
            "headline": template["headline"],
            "hook": template["hook"],
            "body": f"""{template['headline']}

Just this week:
✅ Hartamas Real Estate partnered UCAN Technologies to deploy AI in property sales
✅ WITO Technology's CEO shares how they went from 'Ground Zero to Industry Leader' powering MY SME digital revolution
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
            "local_references": ["Hartamas Real Estate", "WITO Technology", "FutureCFO", "UCAN Technologies"]
        },
        "image_prompts": {
            "z_image_prompts": [
                {
                    "purpose": "Hero image - SME digital revolution",
                    "prompt": f"Modern Malaysian SME office with diverse team celebrating digital success, laptops showing AI chatbot dashboard, warm lighting, Kuala Lumpur skyline visible, professional photography, high detail, 8K resolution, vibrant colors, text overlay: '{language} content'",
                    "style_notes": "Optimized for Z-Image/Tongyi-MAI"
                },
                {
                    "purpose": "Carousel card 1 - Finance automation",
                    "prompt": f"Clean infographic with Malaysian flag colors, CFO silhouette with chatbot icon, text 'Invoice Queries? Payment Reminders? Chatbot handles it 24/7' in {language}, dark blue gradient background",
                    "style_notes": "Dark theme, finance automation angle"
                },
                {
                    "purpose": "Carousel card 2 - Sales automation",
                    "prompt": f"Hartamas Real Estate-style property showcase with chatbot interface on smartphone, Malaysian property agent discussing with client, WhatsApp chat bubbles, bright professional lighting, text in {language}",
                    "style_notes": "Sales automation highlight"
                }
            ]
        }
    }
    
    # Add video production table ONLY if format="with_video"
    if format_type == "with_video":
        content["video_production"] = {
            "format": "30s_reel_facebook",
            "language": language,
            "production_table": [
                {
                    "time": "0-3s",
                    "audio": f"Hartamas Real Estate dah guna AI! ({language} hook)",
                    "z_image_prompt": "Close-up of surprised Malaysian SME owner reading news on smartphone",
                    "video_motion_prompt": "Camera zooms in on smartphone screen showing news article"
                },
                {
                    "time": "3-10s",
                    "audio": f"AI chatbot boleh automate semua! 24/7 PDPA compliant tau ({language})",
                    "z_image_prompt": "Split screen showing diverse Malaysian professionals with chatbot interfaces",
                    "video_motion_prompt": "Smooth transition between professions, chat bubbles animate in"
                },
                {
                    "time": "10-20s",
                    "audio": f"Customer WhatsApp tanya harga? Chatbot jawab terus ({language})",
                    "z_image_prompt": "Malaysian business owner sleeping peacefully, phone glowing with automated replies",
                    "video_motion_prompt": "Owner sleeps while notifications light up, time-lapse effect"
                },
                {
                    "time": "20-27s",
                    "audio": f"WhatsApp: +60 12-345 6789. Free demo untuk 10 syarikat pertama! ({language})",
                    "z_image_prompt": "Confident Malaysian SME owner pointing to camera, WhatsApp number highlighted",
                    "video_motion_prompt": "Owner gives thumbs up, WhatsApp number flies in with animation"
                },
                {
                    "time": "27-30s",
                    "audio": f"AI Chatbot Malaysia - SME Digital Revolution ({language})",
                    "z_image_prompt": "Company logo centered on dark blue gradient with Malaysian flag pattern",
                    "video_motion_prompt": "Logo animates in with glow effect, smooth fade out"
                }
            ]
        }
    
    return content

if __name__ == "__main__":
    # Parse command line arguments
    language = sys.argv[1] if len(sys.argv) > 1 else "Manglish"
    format_type = sys.argv[2] if len(sys.argv) > 2 else "with_video"
    
    # Validate inputs
    valid_languages = ["English", "BM", "Chinese", "Manglish"]
    valid_formats = ["with_video", "without_video"]
    
    if language not in valid_languages:
        print(f"Invalid language. Choose from: {valid_languages}")
        sys.exit(1)
    
    if format_type not in valid_formats:
        print(f"Invalid format. Choose from: {valid_formats}")
        sys.exit(1)
    
    # Generate content
    content = generate_content(language, format_type)
    
    # Save to JSON file
    output_file = f"/home/auyong/projects/fbpagecontentai/content/content_{language}_{format_type}_{datetime.now().strftime('%Y%m%d')}.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Content generated: {output_file}")
    print(f"   Language: {language}")
    print(f"   Format: {format_type}")
    print(f"   Image prompts: MANDATORY (always included)")
    print(f"   Video production: {'INCLUDED' if format_type == 'with_video' else 'EXCLUDED'}")
