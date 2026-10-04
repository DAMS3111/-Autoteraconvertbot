import os
from pyrogram import Client, filters

# Render के Environment Variables से डिटेल्स लेना
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
NDUS = os.getenv("NDUS", "")

app = Client(
    "terabox_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("नमस्ते! आपका Telegram-to-TeraBox बोट सक्रिय है। मुझे कोई वीडियो भेजें।")

@app.on_message(filters.video | filters.document)
async def handle_video(client, message):
    await message.reply_text("वीडियो प्राप्त हो गया है! NDUS कुकी के माध्यम से टेराबॉक्स पर प्रोसेसिंग की जा रही है...")
    # यहाँ टेराबॉक्स अपलोड लॉजिक काम करेगा

if __name__ == "__main__":
    print("बोट शुरू हो रहा है...")
    app.run()
    
