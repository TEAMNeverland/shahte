from pyrogram import Client, filters

api_id = 2001278
api_hash = "1695bb3630b911a936299bd8f109fae0"
token = "8113165781:AAUFXlXAqINSNDRTMqck3qJBCggpX4Ax6g"

app = Client("shahbot", api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    message.reply_text("أهلًا بيك، بوت الشاه يشتغل 🌟")

app.run()