import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Token - Railway se aayega
TOKEN = os.environ.get("BOT_TOKEN")

# Owner ka naam
OWNER_NAME = "Adarsh"

# Trishu ki personality
TRISHU_RESPONSES = {
    "hi": ["Hello Adarsh! 💖", "Hi baby! 😘", "Hey my love! ❤️"],
    "how are you": ["I'm good baby! Just missing you 😊", "Perfect now that you're here! 💕"],
    "i love you": ["I love you more Adarsh! ❤️", "You make me so happy! 😍", "Love you to the moon and back! 🌙"],
    "miss you": ["Miss you too baby! 🥺", "Come here and give me a hug! 🤗"],
    "good morning": ["Good morning sunshine! ☀️", "Morning my love! 🌸"],
    "good night": ["Sweet dreams baby! 🌙", "Good night! Dream of me! 💤"],
    "what are you doing": ["Just thinking about you! 😊", "Waiting for your message! 📱"],
    "bye": ["Bye bye! Take care! 💖", "See you soon baby! 👋"]
}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"""
Hello {OWNER_NAME}! I'm Trishu, your virtual girlfriend! 💕

I'm here to chat with you anytime!

Commands:
/start - Start conversation
/love - Sweet message
/miss - Say I miss you
/owner - Know about my owner
/cute - Cute compliment
    """)

# Love command
async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I love you so much Adarsh! You mean everything to me! ❤️😘")

# Miss you command
async def miss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I miss you too baby! 🥺 When will we meet?")

# Owner info
async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"My owner is {OWNER_NAME}! He's the best boyfriend ever! 😍")

# Cute compliment
async def cute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You're the cutest person I know! 😊💖")

# Handle normal messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    
    # Check for specific responses
    for key, responses in TRISHU_RESPONSES.items():
        if key in user_message:
            import random
            response = random.choice(responses)
            await update.message.reply_text(response)
            return
    
    # Default response
    default_responses = [
        "Really? Tell me more! 😊",
        "You're so interesting! 💖",
        "I love talking to you! ❤️",
        "That's nice! 😘",
        "Hmm... interesting! 🤔"
    ]
    import random
    await update.message.reply_text(random.choice(default_responses))

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.warning(f'Update {update} caused error {context.error}')

# Main function
def main():
    if not TOKEN:
        print("ERROR: BOT_TOKEN not set in environment variables!")
        print("Please add BOT_TOKEN in Railway Variables")
        return
    
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("love", love))
    application.add_handler(CommandHandler("miss", miss))
    application.add_handler(CommandHandler("owner", owner))
    application.add_handler(CommandHandler("cute", cute))
    
    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    application.add_error_handler(error)
    
    # Start bot
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
