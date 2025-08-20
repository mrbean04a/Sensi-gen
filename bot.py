import logging
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# ----------------- SECURITY -----------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not set. Please add it in Render environment variables.")

# ----------------- LOGGING -----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ----------------- RULE BASED BRAZILIAN SENSI -----------------
def generate_rule_based_sensi(phone_model: str):
    base_sensi = 1.0
    if "redmi" in phone_model.lower():
        base_sensi = 1.3
    elif "samsung" in phone_model.lower():
        base_sensi = 1.2
    elif "iphone" in phone_model.lower():
        base_sensi = 1.1
    else:
        base_sensi = 1.0
    return round(base_sensi + random.uniform(-0.05, 0.05), 2)

# ----------------- MOCK LIGHTWEIGHT ML MODEL -----------------
def ml_predict_sensi(phone_model: str):
    random.seed(sum(ord(c) for c in phone_model))  # deterministic
    return round(0.9 + random.random() * 0.6, 2)

# ----------------- TELEGRAM COMMANDS -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! I’m your free Brazilian Sensi Bot 🇧🇷\n\n"
        "Use /help to see commands."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/sensi <phone_model> - Generate Brazilian sensitivity for your phone"
    )

async def sensi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide your phone model!\nExample: /sensi Redmi Note 10")
        return

    phone_model = " ".join(context.args)
    rule_sensi = generate_rule_based_sensi(phone_model)
    ml_sensi = ml_predict_sensi(phone_model)

    await update.message.reply_text(
        f"📱 Phone: {phone_model}\n\n"
        f"🇧🇷 Rule-based Brazilian Sensi: {rule_sensi}\n"
        f"🤖 ML-predicted Sensi: {ml_sensi}\n\n"
        "⚡ Use whichever feels smoother in-game!"
    )

# ----------------- MAIN -----------------
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("sensi", sensi))

    print("✅ Bot is running...")
    await app.run_polling(close_loop=False)  # important for Render

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        # Fallback for environments (like Render, Jupyter, etc.) with existing loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())# ----------------- TELEGRAM COMMANDS -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! I’m your free Brazilian Sensi Bot 🇧🇷\n\n"
        "Use /help to see commands."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/sensi <phone_model> - Generate Brazilian sensitivity for your phone"
    )

async def sensi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide your phone model!\nExample: /sensi Redmi Note 10")
        return

    phone_model = " ".join(context.args)
    rule_sensi = generate_rule_based_sensi(phone_model)
    ml_sensi = ml_predict_sensi(phone_model)

    await update.message.reply_text(
        f"📱 Phone: {phone_model}\n\n"
        f"🇧🇷 Rule-based Brazilian Sensi: {rule_sensi}\n"
        f"🤖 ML-predicted Sensi: {ml_sensi}\n\n"
        "⚡ Use whichever feels smoother in-game!"
    )

# ----------------- MAIN -----------------
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("sensi", sensi))

    print("✅ Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        # Fix for environments where loop is already running (like Render/Notebooks)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())    return round(0.9 + random.random() * 0.6, 2)

# ----------------- TELEGRAM COMMANDS -----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! I’m your free Brazilian Sensi Bot 🇧🇷\n\n"
        "Use /help to see commands."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/sensi <phone_model> - Generate Brazilian sensitivity for your phone"
    )

async def sensi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide your phone model!\nExample: /sensi Redmi Note 10")
        return

    phone_model = " ".join(context.args)

    rule_sensi = generate_rule_based_sensi(phone_model)
    ml_sensi = ml_predict_sensi(phone_model)

    await update.message.reply_text(
        f"📱 Phone: {phone_model}\n\n"
        f"🇧🇷 Rule-based Brazilian Sensi: {rule_sensi}\n"
        f"🤖 ML-predicted Sensi: {ml_sensi}\n\n"
        "⚡ Use whichever feels smoother in-game!"
    )

# ----------------- MAIN -----------------
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("sensi", sensi))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
