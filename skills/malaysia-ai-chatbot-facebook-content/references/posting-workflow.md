# Facebook Posting Workflow for Microark AI Page

## Page Details
- Page ID: 61586620982907
- Page URL: https://www.facebook.com/profile.php?id=61586620982907
- Login Email: microarktech@gmail.com
- User Preference: Post only image content (no videos)

## Critical Lessons Learned
1. **Avoid Browser Automation**: Facebook's anti-bot measures block scripted clicks via Hermes browser tool. The tool also cannot handle native file dialogs for local image uploads from WSL paths.
2. **Manual Posting**: Requires user to handle 2FA and file uploads directly.
3. **Graph API is Mandatory for Automation**: Only reliable automated method.

## Preferred Automated Method: Facebook Graph API
1. Generate Page Access Token at https://developers.facebook.com/tools/explorer/ with permissions:
   - `pages_manage_posts`
   - `pages_read_engagement`
2. Upload images from `/home/auyong/projects/fbpagecontentai/assets/images/` via `curl`:
   ```bash
   curl -X POST "https://graph.facebook.com/v19.0/{page-id}/photos" \
     -H "Authorization: Bearer {access-token}" \
     -F "source=@/path/to/image.png" \
     -F "message={post-caption}"
   ```
3. Use pre-generated Manglish, PDPA-compliant copy from content JSON files in `/home/auyong/projects/fbpagecontentai/content/`

## User Content Preferences
- Manglish tone with local references (Hartamas Real Estate, WITO Technology)
- PDPA compliance mentions
- WhatsApp integration highlights
- No video content included in posts