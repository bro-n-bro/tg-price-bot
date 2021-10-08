from telegram.ext import Updater, Dispatcher, CommandHandler

from command_price import start

updater = Updater(token='YOUR TOKEN HERE')
dispatcher: Dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('stats', start))
dispatcher.add_handler(CommandHandler('juno', start))
updater.start_polling()
