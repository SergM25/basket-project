from aiogram.utils import executor 
from create_bot import dp
from data_base import sqlite_db
from data_base2 import sqlite_db2, sqlite_db3

async def on_startup(_):
  print('Бот вышел в онлайн')
  sqlite_db.sql_start()
  sqlite_db2.sql_start()
  sqlite_db3.sql_start()

from handlers import admin, client


#admin.register_handlers_admin(dp)
client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)