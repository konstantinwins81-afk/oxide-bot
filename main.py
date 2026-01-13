import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

WARNINGS = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Oxide-бот запущен!\nКоманды: /dice /warn /mute")

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = random.randint(1, 6)
    await update.message.reply_text(f"🎲 Выпало: {value}")

async def warn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return
    user = update.message.reply_to_message.from_user.id
    WARNINGS[user] = WARNINGS.get(user, 0) + 1
    await update.message.reply_text(f"⚠️ Предупреждение ({WARNINGS[user]}/3)")

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return
    await update.message.reply_text("🔇 Пользователь замучен (пример)")

def main():
    import os
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dice", dice))
    app.add_handler(CommandHandler("warn", warn))
    app.add_handler(CommandHandler("mute", mute))

    app.run_polling()

if __name__ == "__main__":
    main()
