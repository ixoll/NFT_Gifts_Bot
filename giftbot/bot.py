from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7378006775:AAGk9iYcFuppf1oXVfiY1Cq6V1HbMhxLkqQ"
WEBAPP_URL = "https://ваш-username.github.io/easygift-webapp/"  # Замените на ваш URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "Открыть приложение",
            web_app=WebAppInfo(url=WEBAPP_URL)  # Кнопка с WebApp
        )],
        [InlineKeyboardButton("Наш канал", url="https://t.me/NFT_Gifts_Case_Bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎁 Добро пожаловать в Easy Gift!",
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()