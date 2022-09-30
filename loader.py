from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from plate import Plate

import database
from config import bot_config

import logging
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_config.token, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher()
db = database.Client(
            host='localhost',
            username='root',
            password='<tDAXfuU7>',
            name=bot_config.project)

if 'database' in os.getcwd():
    os.chdir('../')

plate = Plate(root='translation')
locales = {'en': 'en_US'}
