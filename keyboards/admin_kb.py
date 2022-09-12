from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_load2 = KeyboardButton('/Загрузить_сеты')
button_load = KeyboardButton('/Загрузить_холодные_роллы')
button_delete = KeyboardButton('/Удалить')
button_delete2 = KeyboardButton('/Удалить_сеты')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
            .add(button_delete).add(button_load2).add(button_delete2)