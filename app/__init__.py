import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app.config import Config
from app.utils.utils import clock

if os.path.exists(Config.log_path):
    os.rename(Config.log_path, Config.log_path + '.' + str(clock.now())[:19])

logging.basicConfig(filename=Config.log_path,
                    format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

if os.environ.get('PORT') is not None:
    bot = Bot(token=Config.TOKEN)
else:
    bot = Bot(token=Config.TOKEN, proxy=Config.PROXY_URL)

dp = Dispatcher(bot, storage=JSONStorage(Config.FSMstorage_path))

dp.middleware.setup(LoggingMiddleware())

from app.handlers import *
