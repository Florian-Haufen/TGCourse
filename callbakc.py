from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from config import bot2

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

bot = Bot(token=bot2, parse_mode='HTML')
dp = Dispatcher(bot)

def get_doll():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['USD']['Value']
def get_doll_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['USD']['Previous']
def get_euro():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['EUR']['Value']
def get_euro_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['EUR']['Previous']
def get_yun():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['CNY']['Value']
def get_yun_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['CNY']['Previous']
def get_funt():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['GBP']['Value']
def get_funt_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['GBP']['Previous']

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('👋\n'
                         '<b>Привет ! Я NewCourse = Ваш лучший информатор на бирже !</b>\n'
                         '<b>Для большей информации выполните команду</b> /menu')

@dp.message_handler(commands=['menu'])
async def cmd_random(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Курсы Валют', callback_data="course"))
    await message.answer(text="🧠\n"
                         "<b>Вот что я умею:</b>",reply_markup=kb)

@dp.callback_query_handler()
async def cll1(call1: types.CallbackQuery):
    if call1.data == 'course':
        kb2 = types.InlineKeyboardMarkup()
        kb2.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        kb2.add(types.InlineKeyboardButton(text='💵 Доллар/Рубль', callback_data='RUB/DOL'))
        kb2.add(types.InlineKeyboardButton(text='💶 Евро/Рубль', callback_data='EUR/RUB'))
        kb2.add(types.InlineKeyboardButton(text='💴 Юань/Рубль', callback_data='yun'))
        kb2.add(types.InlineKeyboardButton(text='💷 Фунт стерлингов/Рубль', callback_data='fnt'))
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text='📊\n'
                                                                                                          '<b>Курсы валют в соотношении [Единица Валюты]/Рубль:</b>', reply_markup=kb2)
    elif call1.data == 'back_course':
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Курсы Валют', callback_data="course"))
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text="🧠\n"
                         "<b>Вот что я умею:</b>",reply_markup=kb) #Кнопка назад
    elif call1.data == 'RUB/DOL':
        kbdoll = types.InlineKeyboardMarkup()
        kbdoll.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        rd = get_doll()
        rd_p = get_doll_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💵\n'
                                                                                                          f'<b>1 Доллар стоит {rd} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{rd-rd_p} <b>Рублей</b>', reply_markup=kbdoll)
    elif call1.data == 'EUR/RUB':
        kbeur = types.InlineKeyboardMarkup()
        kbeur.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        er = get_euro()
        er_p = get_euro_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💶\n'
                                                                                                          f'<b>1 Евро стоит {er} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{er-er_p} <b>Рублей</b>', reply_markup=kbeur)
    elif call1.data == 'yun':
        kbyun = types.InlineKeyboardMarkup()
        kbyun.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        yr = get_yun()
        yr_p = get_yun_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💴\n'
                                                                                                          f'<b>1 Юань стоит {yr} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{yr-yr_p} <b>Рублей</b>', reply_markup=kbyun)
    elif call1.data == 'fnt':
        kbfnt = types.InlineKeyboardMarkup()
        kbfnt.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        fr = get_funt()
        fr_p = get_funt_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💷\n'
                                                                                                          f'<b>1 Фунт стерлингов стоит {fr} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{fr-fr_p} <b>Рублей</b>', reply_markup=kbfnt)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
