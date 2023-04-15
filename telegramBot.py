import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define a function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am UNIC EventBot.")


if __name__ == '__main__':
    # Create a new ApplicationBuilder object and set the bot token
    application = ApplicationBuilder().token('YOUR_TOKEN_HERE').build()

    # Add a handler for the /start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Start the bot and begin polling for updates
    application.run_polling()
