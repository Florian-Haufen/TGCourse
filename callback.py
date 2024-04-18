from aiogram import Bot, Dispatcher, types, executor
from . import urls

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

bot = Bot(token='', parse_mode='HTML')
dp = Dispatcher(bot)

menutxt = "🧠\n<b>Вот что я умею:</b>"

# Функция старта бота
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('👋\n'
                         '<b>Привет ! Я NewCourse = Ваш лучший информатор на бирже !</b>\n'
                         '<b>Для большей информации выполните команду</b> /menu')

# Функция вызова меню взаимодействия с ботом
@dp.message_handler(commands=['menu'])
async def cmd_random(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Курсы Валют', callback_data="course"))
    await message.answer(text=menutxt, reply_markup=kb)

# Хендлер реакций бота на нажатие кнопок
@dp.callback_query_handler()
async def cll1(call1: types.CallbackQuery):

    # Функция вызова меню с выбором валют
    if call1.data == 'course':
        kb2 = types.InlineKeyboardMarkup()
        kb2.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        kb2.add(types.InlineKeyboardButton(text='💵 Доллар/Рубль', callback_data='dol'))
        kb2.add(types.InlineKeyboardButton(text='💶 Евро/Рубль', callback_data='eur'))
        kb2.add(types.InlineKeyboardButton(text='💴 Юань/Рубль', callback_data='yun'))
        kb2.add(types.InlineKeyboardButton(text='💷 Фунт стерлингов/Рубль', callback_data='fnt'))
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text='📊\n'
                                                                                                          '<b>Курсы валют в соотношении [Единица Валюты]/Рубль:</b>', reply_markup=kb2)
    # Вернуться в главное меню
    elif call1.data == 'back_course':
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Курсы Валют', callback_data="course"))
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=menutxt, reply_markup=kb)

    # Курс доллар к рублю
    elif call1.data == 'dol':
        kbdoll = types.InlineKeyboardMarkup()
        kbdoll.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        rd = urls.get_doll()
        rd_p = urls.get_doll_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💵\n'
                                                                                                          f'<b>1 Доллар стоит {rd} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{rd-rd_p} <b>Рублей</b>', reply_markup=kbdoll)
    # Курс евро к рублю
    elif call1.data == 'eur':
        kbeur = types.InlineKeyboardMarkup()
        kbeur.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        er = urls.get_euro()
        er_p = urls.get_euro_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💶\n'
                                                                                                          f'<b>1 Евро стоит {er} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{er-er_p} <b>Рублей</b>', reply_markup=kbeur)
        
    # Курс юань к рублю
    elif call1.data == 'yun':
        kbyun = types.InlineKeyboardMarkup()
        kbyun.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        yr = urls.get_yun()
        yr_p = urls.get_yun_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💴\n'
                                                                                                          f'<b>1 Юань стоит {yr} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{yr-yr_p} <b>Рублей</b>', reply_markup=kbyun)
    
    # Курс фунта к рублю
    elif call1.data == 'fnt':
        kbfnt = types.InlineKeyboardMarkup()
        kbfnt.add(types.InlineKeyboardButton(text='Назад', callback_data='back_course'))
        fr = urls.get_funt()
        fr_p = urls.get_funt_previous()
        await bot.edit_message_text(chat_id=call1.from_user.id, message_id=call1.message.message_id, text=f'💷\n'
                                                                                                          f'<b>1 Фунт стерлингов стоит {fr} Рублей по ЦБ</b>\n'
                                                                                                          f'\n'
                                                                                                          f'<b>📈 Изменение</b>\n'
                                                                                                          f'<b>(По сравнению со вчерашним днём):</b>\n'
                                                                                                          f'{fr-fr_p} <b>Рублей</b>', reply_markup=kbfnt)


# Функция запуска приложения
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
