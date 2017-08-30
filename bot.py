#be name khoda
# -*- coding: utf-8 -*-
import logging
import os

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

#from commands import CommandsModule
from ping import pingModules


TOKEN="248499276:AAHr7kfvOhOPv3oiC7JUANjRc17guo9Vo6c"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, err):
    logger.warn('Update "%s" caused error "%s"' % (update, err))


def load_modules(dispatcher, modules):
    for module in modules:
        for handler in module.get_handlers():
            dispatcher.add_handler(handler)

def main ():
    updater=Updater(TOKEN)
    dp = updater.dispatcher
    load_modules(dp, [pingModules()])
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
	
if __name__ == '__main__':	
	main()
