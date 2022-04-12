"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""


from dotenv import load_dotenv
from pathlib import Path
import os

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from db_handler import UsersLookup


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler,
)

from telegram import (
    Bot,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


load_dotenv()
bot = Bot(os.getenv("API_KEY"))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


logger = logging.getLogger(__name__)
timespan = ''

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def startCommand(update: Update, context: CallbackContext):
    keyboardMarkup = ''
    if UsersLookup(update.message.from_user.id):    
         keyboardMarkup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Delete the user', callback_data='Deleating')]]
    )    

    keyboardMarkup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Create a new User', callback_data='creating')]]
    )
    update.message.reply_text(f'Howdy, {update.effective_user.first_name}.\nThis is the Main Menu.',
                              reply_markup=keyboardMarkup)

def userCreationHandler(update: Update, context: CallbackContext):
    if update.callback_query.data == 'creating':
        update.callback_query.edit_message_text(
            update.effective_message.text,
            reply_markup=InlineKeyboardMarkup([])
        )
        text = f"""I\'ll share the File 1 with you to your Google account.
Please, send me your gmail address.\n\nSend /end and I\'ll stop waiting."""
        bot.send_message(update.effective_chat.id, text)
        return timespan

def fallback(update, context):
       update.message.reply_text('Conv ended')

def convend(update, context):
       update.message.reply_text('Conv ended')


def callbacktest(update, context):
    update.message.reply_text('User allready created')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    load_dotenv()
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot = Bot(os.getenv("API_KEY"))
    updater = Updater(os.getenv("API_KEY"), use_context=True)

    # Get the dispatcher to register handlers

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', startCommand))
    # on different commands - answer in Telegram
    user_conv = ConversationHandler(
    entry_points = [CallbackQueryHandler(userCreationHandler)], 
    states = 
    {
        timespan : [
            MessageHandler(Filters.regex('.*@gmail.com$'), callbacktest)
        ],
    }, 
    fallbacks=[CommandHandler('end', convend)],
    )

    dispatcher.add_handler(user_conv)
    # on noncommand i.e message - echo the message on Telegram
    # log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling(drop_pending_updates=True)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()