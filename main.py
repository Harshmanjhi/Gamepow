from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6789771210:AAGBLOHOY7NAY19N20rJdrSoUhHu_5dLpTY'

# /start command handler
def start(update: Update, context: CallbackContext):
    user_name = update.message.from_user.username if update.message.from_user.username else update.message.from_user.first_name
    update.message.reply_text(f"Hello, {user_name}! I am your Telegram Bot.")

# Welcome message handler
def welcome_message(update: Update, context: CallbackContext):
    new_chat_member = update.message.new_chat_members[0]
    update.message.reply_text(f"Welcome {new_chat_member.first_name} to the group!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers for commands, messages, and new chat members
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
