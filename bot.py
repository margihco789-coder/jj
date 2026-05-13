import telebot
from telebot import types
from config import BOT_TOKEN, tools_db

bot = telebot.TeleBot(BOT_TOKEN)

# --- Text constants ---
START_TEXT = """Connection established. 🌐
MARKDEW Terminal online.
Обери модуль для доступу до бази:"""

MODULE_1_TEXT = """**AI TOOLS 🤖**
База інструментів. Обери сектор:"""

# --- Keyboards ---
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🤖 AI Tools", callback_data="mod_1"),
        types.InlineKeyboardButton("🧠 Prompts", callback_data="mod_2"),
        types.InlineKeyboardButton("⚡ Automation", callback_data="mod_3"),
        types.InlineKeyboardButton("🔒 Private Drop", callback_data="mod_4"),
        types.InlineKeyboardButton("💎 Services", callback_data="mod_5")
    )
    return markup

def ai_tools_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Image AI", callback_data="cat_image"),
        types.InlineKeyboardButton("Coding AI", callback_data="cat_coding"),
        types.InlineKeyboardButton("Music AI", callback_data="cat_music"),
        types.InlineKeyboardButton("Automation AI", callback_data="cat_automation"),
        types.InlineKeyboardButton("Business AI", callback_data="cat_business"),
        types.InlineKeyboardButton("🔙 Назад", callback_data="back_main")
    )
    return markup

def send_tool(call, category_key):
    if category_key in tools_db:
        tools = tools_db[category_key]
        for tool in tools:
            text = f"""⬛️ **{tool['name']}**
**Desc:** {tool['desc']}
**Power:** {tool['power']}"""
            
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("⚡ Access Tool", url=tool['link']))
            markup.add(types.InlineKeyboardButton("🔙 Категорії", callback_data="back_ai"))
            
            bot.send_message(call.message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

# --- Handlers ---
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, START_TEXT, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "mod_1":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=MODULE_1_TEXT,
            reply_markup=ai_tools_menu(),
            parse_mode='Markdown'
        )
    elif call.data == "back_main":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=START_TEXT,
            reply_markup=main_menu()
        )
    elif call.data == "back_ai":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=MODULE_1_TEXT,
            reply_markup=ai_tools_menu(),
            parse_mode='Markdown'
        )
    elif call.data.startswith("cat_"):
        category = call.data.replace("cat_", "")
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
        send_tool(call, f"{category}_ai")

if __name__ == "__main__":
    bot.infinity_polling()