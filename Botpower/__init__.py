from telegram.ext import Updater, CommandHandler

# Define a function for the /start command
def start(update, context):
    user_name = update.message.from_user.first_name
    welcome_message = f"Hello {user_name}! Welcome to the bot. How can I assist you today?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

# Set up the updater and dispatcher
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

# Add command handler for the /start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()

