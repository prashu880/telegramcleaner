import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

async def delete_join_left_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message is None:
        return

    # Check if the message is a new chat member or left chat member service message
    if message.new_chat_members or message.left_chat_member:
        try:
            await context.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            logger.info(f"Deleted join/left message in chat {message.chat.id}")
        except Exception as e:
            logger.error(f"Failed to delete message: {e}")

def main():
    import asyncio

    # Temporarily set token here for testing
    TOKEN = "8388571083:AAFnQrDnJ5wuQUOby8UY-hj1Qt1RcLb5-3E"  # Replace with your actual token for testing

    if not TOKEN or TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        logger.error("Please set your Telegram bot token in the TOKEN variable for testing")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    # Handler for join and left messages
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS | filters.StatusUpdate.LEFT_CHAT_MEMBER, delete_join_left_messages))

    logger.info("Bot started")
    app.run_polling()

if __name__ == '__main__':
    main()
