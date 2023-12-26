from telegram import Update

def ban_user(update, context):
    if len(context.args) > 0:
        user_id = context.args[0]
        context.bot.kick_chat_member(update.message.chat_id, user_id)

def unban_user(update, context):
    if len(context.args) > 0:
        user_id = context.args[0]
        context.bot.unban_chat_member(update.message.chat_id, user_id)

def pin_message(update, context):
    message = update.message.reply_to_message
    if message:
        context.bot.pin_chat_message(update.message.chat_id, message.message_id)

def unpin_message(update, context):
    context.bot.unpin_chat_message(update.message.chat_id)
