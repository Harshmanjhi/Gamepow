from telegram.ext import Updater, CommandHandler
from helpers import ban_user, unban_user, pin_message, unpin_message
from your_token import TOKEN

def start(update, context):
    update.message.reply_text('Welcome! Use /ban <user_id> to ban a user, /unban <user_id> to unban, /pin to pin a message, and /unpin to unpin.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ban", ban_user, pass_args=True))
    dp.add_handler(CommandHandler("unban", unban_user, pass_args=True))
    dp.add_handler(CommandHandler("pin", pin_message))
    dp.add_handler(CommandHandler("unpin", unpin_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

