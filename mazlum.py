import pyrogram
from pyrogram 
import Client

api_id = 26606104
api_hash = "ea74a2439c1f8fff561d8d86af6f1540"
bot_token = "7232540328:AAG3c3dvlhCZdyD7XiVON4ZjnQMJ5gfFP74"

app = Client( 
    
    "Test_bot"
     api_id=api_id,
     api_hash=api_hash,
     bot_token=bot_token
)
@app.on_message(filters.command("start") & filters.private)
async def start(bot: Client, message: Message):
    chat_id = message.chat.id 
    await bot.send_mesaage(chat_id, "Selam")
