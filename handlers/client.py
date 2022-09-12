from email.message import Message
from email.policy import default
from sre_parse import State
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
#from data_base import sqlite_db
from aiogram.types import ReplyKeyboardRemove
from data_base2 import sqlite_db2, sqlite_db3
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from data_base import sqlite_db

import sqlite3

@dp.message_handler(Command('start'))
async def start(message: Message):
  connect = sqlite3.connect('users.db')
  cursor = connect.cursor()
  cursor.execute("""INSERT INTO users (user_id, name) VALUES (?, ?)""", [message.chat.id, message.chat.first_name])
  cursor.close()
  connect.commit()
  connect.close()
  await bot.send_message(message.from_user.id, 'Здравствуйте, для заказа и уточнений обращайтесь по номеру телефона +7', reply_markup=kb_client)
  await message.delete()
# @dp.message_handler(Command('start'))
# async def start(message : Message):
#   await sqlite_db3.sql_add_userid(message)
#   try:
#     await bot.send_message(message.from_user.id, 'Здравствуйте, для заказа и уточнений обращайтесь по номеру телефона +7', reply_markup=kb_client)
#     await message.delete()
#   except:
#     await message.reply('Общение с ботом через лс: \n@Cpus_bot')

@dp.message_handler(commands=['Холодные_роллы'])
async def catalog_command(message : types.Message):
  await sqlite_db3.sql_read3(message)
  


  #  connect = sqlite3.connect('users.db')
  #  cursor = connect.cursor()
  #  for ret in cursor.execute('SELECT * FROM menu (img, name, description, price)').fetchall():
  #       await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[3]}\nID {ret[-1]}')


@dp.message_handler(commands=['Сеты'])
async def set_catalog_command(message : types.Message):
   await sqlite_db2.sql_read3(message)

def register_handlers_client(dp : Dispatcher):
  #dp.register_message_handler(command_start, commands=['start', 'help'])
  #dp.register_message_handler(catalog_command, commands=['Холодные роллы'])
  dp.register_message_handler(set_catalog_command, commands=['Сеты'])