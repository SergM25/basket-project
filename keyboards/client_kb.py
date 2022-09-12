from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b3 = KeyboardButton('/Холодные_роллы')
b4 = KeyboardButton('/Сеты')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b3).add(b4)