#!/usr/bin/env python3
"""
Malaysia AI Chatbot Facebook Ads Funnel Generator
Generates TOFU (Awareness), MOFU (Consideration), BOFU (Conversion) ad content
Optimized for cost-saving and maximum ROAS
"""
import json
import os
import sys
from datetime import datetime

def generate_funnel_ad(funnel_stage="TOFU", language="Manglish", budget_rm=100):
    """
    Generate Facebook Ads content for specific funnel stage.
    
    Args:
        funnel_stage: "TOFU" (Awareness), "MOFU" (Consideration), "BOFU" (Conversion)
        language: "English", "BM", "Chinese", "Manglish"
        budget_rm: Daily budget in RM (default RM100)
    """
    
    # Funnel stage configurations
    funnel_config = {
        "TOFU": {
            "objective": "Brand Awareness / Reach",
            "budget_percent": 40,
            "kpi": ["Reach", "CPM", "Video Views (3s/10s)"],
            "bid_strategy": "Lowest Cost",
            "ad_formats": ["Video (15s/30s)", "Carousel (3-5 cards)", "Single Image"]
        },
        "MOFU": {
            "objective": "Lead Generation / Engagement",
            "budget_percent": 35,
            "kpi": ["CTR", "CPL (Cost Per Lead)", "Engagement Rate"],
            "bid_strategy": "Cost Cap (CPL < RM15)",
            "ad_formats": ["Lead Forms", "Video Testimonials", "Carousel (Features)"]
        },
        "BOFU": {
            "objective": "Conversions / Sales",
            "budget_percent": 25,
            "kpi": ["CPA", "ROAS", "Conversion Rate"],
            "bid_strategy": "Bid Cap / Lowest Cost (Higher Budget)",
            "ad_formats": ["Single Image/Video + CTA", "Carousel (Testimonials + Offer)", "Collection Ads"]
        }
    }
    
    # Language-specific templates
    templates = {
        "TOFU": {
            "English": {
                "hook": "Boss, still manually replying WhatsApp at 10PM?",
                "headline": "Malaysia's SME Digital Revolution is HERE!",
                "body": "88% of Malaysians use WhatsApp daily. Is your business there?",
                "cta": "WhatsApp us NOW for FREE assessment!"
            },
            "BM": {
                "hook": "Bos, masih jawab WhatsApp pukul 10 malam?",
                "headline": "Revolusi Digital SME Malaysia dah SAMPAI!",
                "body": "88% rakyat Malaysia guna WhatsApp setiap hari. Perniagaan anda ada di sana?",
                "cta": "WhatsApp kami SEKARANG untuk assessment PERCUMA!"
            },
            "Chinese": {
                "hook": "老板，还在晚上10点手动回复WhatsApp吗？",
                "headline": "马来西亚中小企业数字革命来了！",
                "body": "88%马来西亚人每天使用WhatsApp。您的企业在那里吗？",
                "cta": "立即WhatsApp我们获取免费评估！"
            },
            "Manglish": {
                "hook": "Boss, you still manually reply WhatsApp at 10PM? 😅",
                "headline": "Boss, Malaysia's SME digital revolution is HERE lah! 🇲🇾",
                "body": "88% Malaysians use WhatsApp daily. Your business ada there or not?",
                "cta": "WhatsApp us NOW for FREE assessment lah! 📱"
            }
        },
        "MOFU": {
            "English": {
                "headline": "FREE AI Readiness Assessment (Worth RM500!)",
                "body": "Chatbots save 20+ hours/week. See if your business is ready in 5 questions.",
                "cta": "Download FREE Assessment"
            },
            "BM": {
                "headline": "PENILAIAN AI PERCUMA (Bernilai RM500!)",
                "body": "Chatbot jimat 20+ jam/minggu. Tengok kalau bisnes anda ready dalam 5 soalan.",
                "cta": "Muat turun Penilaian PERCUMA"
            },
            "Chinese": {
                "headline": "免费AI准备度评估（价值RM500！）",
                "body": "聊天机器人每周节省20+小时。5个问题看看您的企业是否准备好。",
                "cta": "下载免费评估"
            },
            "Manglish": {
                "headline": "FREE AI Readiness Assessment (Worth RM500 lah!)",
                "body": "Chatbots save 20+ jam/week. Check kalau your business ready dalam 5 questions.",
                "cta": "Download FREE Assessment sekarang!"
            }
        },
        "BOFU": {
            "English": {
                "headline": "🚨 ONLY 10 SLOTS LEFT! FREE AI Demo",
                "body": "500+ SMEs transformed. PDPA compliant. WhatsApp: +60 12-345 6789 NOW!",
                "cta": "WhatsApp Now"
            },
            "BM": {
                "headline": "🚨 TINGGAL 10 SLOT JE! DEMO AI PERCUMA",
                "body": "500+ SME dah transform. PDPA compliant. WhatsApp: +60 12-345 6789 SEKARANG!",
                "cta": "WhatsApp Sekarang"
            },
            "Chinese": {
                "headline": "🚨 仅剩10个名额！免费AI演示",
                "body": "500+中小企业已转型。PDPA合规。立即WhatsApp：+60 12-345 6789！",
                "cta": "立即WhatsApp"
            },
            "Manglish": {
                "headline": "🚨 ONLY 10 SLOTS LEFT! FREE AI Demo lah!",
                "body": "500+ SMEs dah transform. PDPA compliant. WhatsApp: +60 12-345 6789 NOW bos!",
                "cta": "WhatsApp Now gerenti!"
            }
        }
    }
    
    config = funnel_config.get(funnel_stage, funnel_config["TOFU"])
    template = templates.get(funnel_stage, templates["TOFU"]).get(language, templates["TOFU"]["Manglish"])
    
    # Calculate budget allocation
    daily_budget = budget_rm
    allocated_budget = (config["budget_percent"] / 100) * daily_budget
    
    # Build ad content
    content = {
        "campaign_date": datetime.now().strftime("%Y-%m-%d"),
        "funnel_stage": funnel_stage,
        "language": language,
        "platform": "Facebook Ads",
        "campaign_objective": config["objective"],
        "budget": {
            "daily_total_rm": daily_budget,
            "allocated_percent": f"{config['budget_percent']}%",
            "allocated_daily_rm": round(allocated_budget, 2),
            "bid_strategy": config["bid_strategy"]
        },
        "target_kpis": config["kpi"],
        "ad_creative": {
            "format_options": config["ad_formats"],
            "headline": template["headline"],
            "body": template["body"],
            "hook": template.get("hook", template["headline"]),
            "cta_button": template["cta"],
            "mandatory_elements": [
                "PDPA compliance mentioned",
                "WhatsApp number: +60 12-345 6789",
                "Local examples: Hartamas Real Estate, WITO Technology",
                "Image text < 20% (Facebook rule)"
            ]
        },
        "image_prompts": {
            "z_image_prompts": [
                {
                    "purpose": f"{funnel_stage} Hero Image",
                    "prompt": f"Malaysian SME owner {'tired at desk' if funnel_stage == 'TOFU' else 'filling lead form' if funnel_stage == 'MOFU' else 'celebrating success'}, chatbot interface visible, WhatsApp icon, text overlay in {language}: {template['headline']}",
                    "style_notes": "Optimized for Z-Image, 2048x2048, high contrast"
                },
                {
                    "purpose": f"{funnel_stage} Feature Card",
                    "prompt": f"Infographic style, Malaysian flag colors, chatbot icon, feature highlights in {language}, dark blue gradient background",
                    "style_notes": "Clean typography, minimal text"
                }
            ]
        },
        "video_production": {
            "duration": "15s (TOFU) / 30s (MOFU/BOFU)",
            "aspect_ratio": "9:16 vertical (mobile-first)",
            "production_table": [
                {
                    "time": "0-3s",
                    "hook": template.get("hook", template["headline"]),
                    "visual": f"{'Surprised boss' if funnel_stage == 'TOFU' else 'Happy lead' if funnel_stage == 'MOFU' else 'Celebrating owner'} with smartphone"
                },
                {
                    "time": "3-10s",
                    "content": template["body"],
                    "visual": "Chatbot interface animation, WhatsApp chat bubbles"
                },
                {
                    "time": "10-15s",
                    "cta": template["cta"],
                    "visual": "WhatsApp number glowing, Malaysian flag overlay"
                }
            ]
        },
        "audience_targeting": {
            "TOFU": {
                "interests": ["Small Business Malaysia", "SME Association Malaysia", "MDEC"],
                "demographics": "Age 25-45, Location: MY (KL, Penang, JB)",
                "exclusions": ["Existing customers", "Job seekers"]
            },
            "MOFU": {
                "retargeting": "Page engagers, Video viewers (50%+), TOFU visitors",
                "lead_form_fields": ["Name", "Phone", "Company", "Pain Point (dropdown)"]
            },
            "BOFU": {
                "retargeting": "Lead form submitters, WhatsApp clickers, High-intent users",
                "custom_audiences": "Cart abandoners (if applicable), Existing customers (upsell)"
            }
        }.get(funnel_stage, {}),
        "cost_saving_strategies": [
            "Kill ads with CTR < 1% (TOFU) / CPL > RM20 (MOFU) / CPA > RM50 (BOFU) within 48h",
            "Use retargeting pixel (reduces CPL by 40-60%)",
            "Test 3-5 ad variations per funnel stage",
            "Reuse TOFU video for MOFU/BOFU (just change text overlay)",
            "Batch-create 5-10 variations in one session (reduce design time by 70%)"
        ],
        "success_metrics": {
            "TOFU": "CPM < RM15, CTR > 1.5%, Video views (3s) > 30%",
            "MOFU": "CPL < RM15, CTR > 2%, Lead form completion > 10%",
            "BOFU": "CPA < RM50, ROAS > 3.0, Conversion rate > 2%"
        }.get(funnel_stage, {})
    }
    
    return content

if __name__ == "__main__":
    # Parse arguments
    funnel_stage = sys.argv[1] if len(sys.argv) > 1 else "TOFU"
    language = sys.argv[2] if len(sys.argv) > 2 else "Manglish"
    budget_rm = float(sys.argv[3]) if len(sys.argv) > 3 else 100.0
    
    # Validate
    valid_funnel = ["TOFU", "MOFU", "BOFU"]
    valid_languages = ["English", "BM", "Chinese", "Manglish"]
    
    if funnel_stage not in valid_funnel:
        print(f"❌ Invalid funnel stage. Choose from: {valid_funnel}")
        sys.exit(1)
    
    if language not in valid_languages:
        print(f"❌ Invalid language. Choose from: {valid_languages}")
        sys.exit(1)
    
    # Generate
    print(f"\n🚀 Generating {funnel_stage} ad content...")
    print(f"   Language: {language}")
    print(f"   Daily Budget: RM{budget_rm}")
    print(f"   Allocated: RM{(budget_rm * [40, 35, 25][valid_funnel.index(funnel_stage)] / 100):.2f} ({['40%', '35%', '25%'][valid_funnel.index(funnel_stage)]})")
    
    content = generate_funnel_ad(funnel_stage, language, budget_rm)
    
    # Save
    output_file = f"/home/auyong/projects/fbpagecontentai/content/ads_{funnel_stage}_{language}_{datetime.now().strftime('%Y%m%d')}.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Ad content generated: {output_file}")
    print(f"   Objective: {content['campaign_objective']}")
    print(f"   KPIs: {', '.join(content['target_kpis'])}")
    print(f"   Bid Strategy: {content['budget']['bid_strategy']}")
