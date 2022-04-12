from telegram import (
    Bot,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler,
)


def startCommand(update: Update, context: CallbackContext):
    keyboardMarkup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Share File 1', callback_data='sharingFile1')]]
    )
    update.message.reply_text(f'Howdy, {update.effective_user.first_name}.\nThis is the Main Menu.',
                              reply_markup=keyboardMarkup)


def convGetGMailAddr(update: Update, context: CallbackContext):
    update.message.reply_text('Waiting for your gmail address.\n\nSend /end and I\'ll stop waiting.')
    return convEmailAddr


def convMismatch(update: Update, context: CallbackContext):
    text = f"""Sorry, I don't understand this gmail address.
Please, send me your gmail address again.\n\nSend /end and I\'ll stop waiting.
"""
    update.message.reply_text(text)
    return convEmailAddr


def convGiveLink(update: Update, context: CallbackContext):
    link = 'https://docs.google.com/spreadsheets/d/1ZP1xZ0WaH8w2yaQTSx99gafNZWawQabcdVW5DSngavQ'
    update.message.reply_text(f'Thank you! Here\'s your link to the shared file:\n{link}')
    return ConversationHandler.END


def convEnd(update: Update, context: CallbackContext):
    update.message.reply_text('I\'ve stopped waiting.\n\nSend /start to go to the Main Menu.')
    return ConversationHandler.END


def sharingFileHandler(update: Update, context: CallbackContext):
    if update.callback_query.data == 'sharingFile1':
        update.callback_query.edit_message_text(
            update.effective_message.text,
            reply_markup=InlineKeyboardMarkup([])
        )
        text = f"""I\'ll share the File 1 with you to your Google account.
Please, send me your gmail address.\n\nSend /end and I\'ll stop waiting."""
        bot.send_message(update.effective_chat.id, text)
        return convEmailAddr


bot_token = '5294441845:AAF4eZ5OIMmOTUFtglTPZKU6WauV05ih8Zk'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
convEmailAddr = ''

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', startCommand))
conv_sharing = ConversationHandler(
    entry_points=[CallbackQueryHandler(sharingFileHandler)],
    states={
        convEmailAddr: [
            MessageHandler(~Filters.regex('.*@gmail.com$') & ~Filters.command, convMismatch),
            MessageHandler(Filters.regex('.*@gmail.com$'), convGiveLink),
        ],
    },
    fallbacks=[CommandHandler('end', convEnd)],
)
disp.add_handler(conv_sharing)

updater.start_polling(drop_pending_updates=True)
updater.idle()