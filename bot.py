import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Render या एनवायरनमेंट वेरिएबल्स से डेटा सुरक्षित तरीके से लेना
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
NDUS_COOKIE = os.getenv("NDUS")  # टेराबॉक्स की ndus कुकी

app = Client("terabox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# टेराबॉक्स पर वीडियो प्रोसेस और लिंक जनरेट करने का फंक्शन
def upload_video_to_terabox(file_path):
    try:
        # नोट: यहाँ NDUS_COOKIE का उपयोग करके टेराबॉक्स पर फाइल अपलोड की जाती है 
        # और उसका शेयरिंग/अर्निंग लिंक जनरेट होता है।
        
        # (अभी यह उदाहरण के लिए डमी लिंक दे रहा है)
        terabox_share_link = "https://teraboxapp.com/s/example_referral_link"
        return terabox_share_link
    except Exception as e:
        print(f"Upload Error: {e}")
        return None

# जब भी आप बोट को कोई वीडियो या फाइल भेजेंगे, यह फंक्शन काम करेगा
@app.on_message(filters.video | filters.document)
async def handle_video(client: Client, message: Message):
    msg = await message.reply("⏳ **वीडियो डाउनलोड हो रहा है और टेराबॉक्स पर भेजने की तैयारी है...**")
    
    try:
        # टेलीग्राम से वीडियो डाउनलोड करें
        video_path = await message.download()
        
        await msg.edit("☁️ **टेराबॉक्स पर लिंक तैयार किया जा रहा है...**")
        
        # टेराबॉक्स लिंक प्राप्त करें
        share_link = upload_video_to_terabox(video_path)
        
        if share_link:
            file_name = message.video.file_name if message.video else "Video"
            
            caption = (
                f"✅ **वीडियो सफलतापूर्वक प्रोसेस हो गया!**\n\n"
                f"📂 **फ़ाइल नाम:** `{file_name}`\n"
                f"🔗 **टेराबॉक्स अर्निंग लिंक:**\n{share_link}"
            )
            
            # वीडियो (थंबनेल के साथ) और कैप्शन यूजर को भेजें
            await message.reply_video(
                video=video_path,
                caption=caption
            )
            await msg.delete()
        else:
            await msg.edit("❌ **लिंक जनरेट करने में विफल!** अपनी कुकी (NDUS) जांचें।")
            
        # सर्वर से लोकल वीडियो डिलीट करें ताकि स्पेस खाली रहे
        if os.path.exists(video_path):
            os.remove(video_path)
            
    except Exception as e:
        await msg.edit(f"⚠️ **एक त्रुटि आई है:** `{str(e)}`")

# बोट शुरू करें
print("🤖 बोट शुरू हो रहा है...")
app.run()
