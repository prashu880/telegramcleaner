import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def delete_join_left_messages(update: Update, context: CallbackContext):
    message = update.message
    if message is None:
        return

    # Check if the message is a new chat member or left chat member service message
    if message.new_chat_members or message.left_chat_member:
        try:
            context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
            logger.info(f"Deleted join/left message in chat {message.chat_id}")
        except Exception as e:
            logger.error(f"Failed to delete message: {e}")

def main():
    # Temporarily set token here for testing
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # Replace with your actual token for testing

    if not TOKEN or TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        logger.error("Please set your Telegram bot token in the TOKEN variable for testing")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handler for join and left messages
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members | Filters.status_update.left_chat_member, delete_join_left_messages))

    updater.start_polling()
    logger.info("Bot started")
    updater.idle()

if __name__ == '__main__':
    main()
