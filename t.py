import telebot
import re
from telebot import types  # для указание типов
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
#from GPT import ask_gpt

bot = telebot.TeleBot('7334847049:AAF9TkMIbX5XwNXq2qn5ho-qx3xUM8qBgbI')

import pandas as pd
import numpy as np
#simptom = pd.read_csv('data.csv')
simptom = pd.read_excel('data.xlsx')
#print(simptom.columns.ravel())
list = simptom['simptom'].str.strip().tolist()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('консультация', callback_data='консультация')
    btn2 = types.InlineKeyboardButton('записаться на прием', callback_data='записаться на прием',
                                      url='https://fomin-clinic.ru/booking/')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я твой лучший друг по здоровью".format(message.from_user),
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_query(callback):
    if (callback.data == 'консультация'):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Да есть', callback_data='Да')
        btn2 = types.InlineKeyboardButton('Нет', callback_data='Нет')
        back = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='Вернуться в главное меню')
        markup.add(btn1, btn2)
        markup.add(back)
        bot.send_message(callback.message.chat.id, text="ДИАГНОЗЫ ПРИ КОТОРЫХ ВОТ ВОТ СДОХНЕТ", reply_markup=markup)
    elif (callback.data == 'Да'):
        bot.send_message(callback.message.chat.id, "вызов скорой")
    elif callback.data == 'Нет':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Кашель', callback_data='Кашель')
        btn2 = types.InlineKeyboardButton('Боль в груди', callback_data='Боль в груди')
        btn3 = types.InlineKeyboardButton('Боль в животе', callback_data='Боль в животе')
        btn4 = types.InlineKeyboardButton('Кровь в кале', callback_data='Кровь в кале')
        btn5 = types.InlineKeyboardButton('Запор', callback_data='Запор')
        btn6 = types.InlineKeyboardButton('Диарея (понос)', callback_data='Диарея (понос)')
        btn7 = types.InlineKeyboardButton('Проблемы с глотанием', callback_data='Проблемы с глотанием')
        btn8 = types.InlineKeyboardButton('Головокружение', callback_data='Головокружение')
        btn9 = types.InlineKeyboardButton('Покраснение глаз или дискомфорт', callback_data='Покраснение глаз или дискомфоорт')
        btn10 = types.InlineKeyboardButton('Ухудшение зрения', callback_data='Ухудшение зрения')
        btnNo = types.InlineKeyboardButton('Не это', callback_data='Не это')



        back = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='Вернуться в главное меню')
        markup.add(btn1, btn2,btn3, btn4,btn5, btn6,btn7, btn8,btn9, btn10,btnNo)
        markup.add(back)
        bot.send_message(callback.message.chat.id, text="Выберите из списка то, что вас беспокоит", reply_markup=markup)
    elif callback.data == 'Не это':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Боль в ноге или лодыжке', callback_data='Боль в ноге или лодыжке')
        btn2 = types.InlineKeyboardButton('Отек стопы или голени', callback_data='Отек стопы или голени')
        btn3 = types.InlineKeyboardButton('Головная боль', callback_data='Головная боль')
        btn4 = types.InlineKeyboardButton('Чувствуете сердцебиение в покое', callback_data='Чувствуете сердцебиение в покое')
        btn5 = types.InlineKeyboardButton('Боль в бедре', callback_data='Боль в бедре')
        btn6 = types.InlineKeyboardButton('Боль в колене', callback_data='Боль в колене')
        btn7 = types.InlineKeyboardButton('Боль в пояснице', callback_data='Боль в пояснице')
        btn8 = types.InlineKeyboardButton('Заложенность носа', callback_data='Заложенность носа')
        btn9 = types.InlineKeyboardButton('Тошнота или рвота', callback_data='Тошнота или рвота')
        btn10 = types.InlineKeyboardButton('Боль в шее', callback_data='Боль в шее')
        btnNo = types.InlineKeyboardButton('И не это', callback_data='И не это')



        back = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='Вернуться в главное меню')
        markup.add(btn1, btn2,btn3, btn4,btn5, btn6,btn7, btn8,btn9, btn10,btnNo)
        markup.add(back)
        bot.send_message(callback.message.chat.id, text="Выберите из списка то, что вас беспокоит", reply_markup=markup)
    elif callback.data == 'И не это':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Онемение или покалывание в руках', callback_data='Онемение или покалывание в руках')
        btn2 = types.InlineKeyboardButton('Боль в тазу (женщина)', callback_data='Боль в тазу (женщина)')
        btn3 = types.InlineKeyboardButton('Боль в тазу (мужчина)', callback_data='Боль в тазу (мужчина)')
        btn4 = types.InlineKeyboardButton('Отдышка', callback_data='Отдышка')
        btn5 = types.InlineKeyboardButton('Боль в плече', callback_data='Боль в плече')
        btn6 = types.InlineKeyboardButton('Боль в горле ', callback_data='Боль в горле ')
        btn7 = types.InlineKeyboardButton('Проблемы с мочеиспусканием', callback_data='Проблемы с мочеиспусканием')
        btn8 = types.InlineKeyboardButton('Свистящее дыхание', callback_data='Свистящее дыхание')
        btnNo = types.InlineKeyboardButton('И не это', callback_data='GPT')



        back = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='Вернуться в главное меню')
        markup.add(btn1, btn2,btn3, btn4,btn5, btn6,btn7, btn8,btnNo)
        markup.add(back)
        bot.send_message(callback.message.chat.id, text="Выберите из списка то, что вас беспокоит", reply_markup=markup)    #Тут показываются симптомы
    elif callback.data in list:
        text = simptom[simptom['simptom'].str.strip() == callback.data].iloc[:, [1, 2, 3]].to_string(header=False, index=False, na_rep='')
        text = re.sub(r'(?<=[а-яА-ЯёЁ])\n(?=[а-яА-ЯёЁ])', '<br>', text)
        if pd.isnull(simptom[simptom['simptom'].str.strip() == callback.data]['F'].iloc[0]):
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Да', callback_data='Да')
            markup.add(btn)
        else:
             markup = types.InlineKeyboardMarkup()
             btn6 = types.InlineKeyboardButton('записаться на прием', callback_data='записаться на прием',
                                      url='https://fomin-clinic.ru/booking/')
             markup.add(btn6)
        
        text = text.replace('\n', '<br>')
        bot.send_message(callback.message.chat.id, text=text, parse_mode='HTML',reply_markup=markup)

#urgent_symptoms(callback, symptoms[callback.data])
    #Это те, кто к врачу. Можно добавить сслыку на запись как в начале
    elif callback.data == 'Да - urgent':
        bot.send_message(callback.message.chat.id, text='Запишитесь на приём к врачу')


    elif callback.data == 'GPT':
        mesg = bot.send_message(callback.message.chat.id, text='Расскажите, что вас беспокоит')
        bot.register_next_step_handler(mesg, gpt_conversation)
    else:
        bot.send_message(callback.message.chat.id, text= 'На такую команду я не запрограмироввн')



def urgent_symptoms(callback, symptom):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Да', callback_data='Да - urgent')
    btn2 = types.InlineKeyboardButton('Нет', callback_data='GPT')
    back = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='Вернуться в главное меню')
    markup.add(btn1, btn2)
    markup.add(back)
    bot.send_message(callback.message.chat.id, text=symptom,
                     reply_markup=markup)

def gpt_conversation(message):
    bot.send_message(message.chat.id, text=ask_gpt(message.text))

bot.polling(none_stop=True)