import telebot
from telebot import types # для указание типов
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('7334847049:AAF9TkMIbX5XwNXq2qn5ho-qx3xUM8qBgbI')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('консультация', callback_data='консультация')
    btn2 = types.InlineKeyboardButton('записаться на прием', callback_data = 'записаться на прием', url= 'https://fomin-clinic.ru/booking/')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я твой лучший друг по здоровью".format(message.from_user),parse_mode='html', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback:True)
def callback_query(callback):
    if(callback.data == 'консультация'):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Да есть', callback_data='Да')
        btn2 = types.InlineKeyboardButton('Нет', callback_data='Нет')
        back = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='Вернуться в главное меню')
        markup.add(btn1, btn2)
        markup.add(back)
        bot.send_message(callback.message.chat.id, text="ДИАГНОЗЫ ПРИ КОТОРЫХ ВОТ ВОТ СДОХНЕТ", reply_markup=markup)
    elif(callback.data == 'Да'):
        bot.send_message(callback.message.chat.id, "вызов скорой")
    
    elif callback.data == 'Нет':
        bot.send_message(callback.message.chat.id, text="скажите что беспокоит вас? Дальше писать и писать кнопки")
    else:
        bot.send_message(callback.message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)