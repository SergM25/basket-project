from email import message
from os import curdir
import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('users.db')
    cur = base.cursor() 
    if base:
        print('Data base connected OK!!!!!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(id INTEGER PRIMARY KEY AUTOINCREMENT, img TEXT, name TEXT, description TEXT, price INTEGER)')
    base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, FOREIGN KEY (user_id) REFERENCES menu (id))')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu (img, name, description, price) VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read3():
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await print (ret[0])
