import logging
import requests
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

BOT_KEY = "здесь ключ бота должен быть"


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def img(update, context):
    # chat_id = update.message.chat_id
    response = requests.get("http://randomfox.ca/floof/")
    link = response.json().get("image")
    print(link)

    # img = Image.open(urlopen(link))
    # bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))

    update.message.reply_photo(link)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def joke(update, context):
    response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
    update.message.reply_text(response.json().get("joke"))


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CommandHandler("img", img))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
