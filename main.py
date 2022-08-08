import datetime
import random

import telebot

# open txt file with joke (new joke = new line)
j = open('Joke.txt', 'r', encoding='UTF-8')
joke = j.read().split('\n')
j.close()

# token my bot
Token = '5557506268:AAFuG4Teur8i4ojnxUvCfIA0kbI2PzWRcuk'
bot = telebot.TeleBot(Token)


# We can use any commands for example "/Help"
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Что я умею', callback_data='Info_button'))
    start_mess = f'<b>Привет <u>{message.from_user.first_name} {message.from_user.last_name}</u>,ты и есть тот ' \
                 f'простой смертный который решил побеспокоить Александра! </b> '
    bot.send_message(message.chat.id, start_mess, parse_mode='html', reply_markup=markup)


# Button in start message
@bot.callback_query_handler(func=lambda call: call.data == 'Info_button')
def query_handler(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Написать создателю', url='https://t.me/marklar08'))
    bot.answer_callback_query(callback_query_id=call.id)
    start_answer = ''
    if call.data == 'Info_button':
        start_answer = '1) Если нужно связаться с создателем нажми на кнопку.\n' \
                       '2) Если вдруг тебе нужно узнать расписание создателя напиши /Info.\n' \
                       '3) Я создан сугубо для баловства и совсем бесполезный.\n' \
                       '4) Ты можешь написать мне /joke и я расскажу тебе шутку. \n' \
                       '5) Если хочешь узнать время напиши /datetime \n' \
                       '6) Начни всё с чистого листа /start'

    bot.send_message(call.message.chat.id, start_answer, parse_mode='html', reply_markup=keyboard)


# help meny
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Написать создателю', url='https://t.me/marklar08'))
    text_help = '1) Если нужно связаться с создателем нажми на кнопку.\n' \
                '2) Если вдруг тебе нужно узнать расписание создателя напиши /Info.\n' \
                '3) Я создан сугубо для баловства и совсем бесполезный.\n' \
                '4) Ты можешь написать мне /joke и я расскажу тебе шутку. \n' \
                '5) Если хочешь узнать время напиши /datetime \n' \
                '6) Начни всё с чистого листа /start'
    bot.send_message(message.chat.id, text_help, reply_markup=keyboard)


# Timetable
@bot.message_handler(commands=['Info'])
def info_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Понедельник', callback_data='Monday'))
    markup.add(telebot.types.InlineKeyboardButton('Вторник', callback_data='Tuesday'))
    markup.add(telebot.types.InlineKeyboardButton('Среда', callback_data='Wednesday'))
    markup.add(telebot.types.InlineKeyboardButton('Четверг', callback_data='Thursday'))
    markup.add(telebot.types.InlineKeyboardButton('Пятница', callback_data='Friday'))

    bot.send_message(message.chat.id, text="Выбери день недели:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за выбор!')
    answer_timetable = ''
    if call.data == 'Monday':
        answer_timetable = '<b> Понедельник </b>\n' \
            ' \n' \
               '8:00 - Сон\n' \
            ' \n' \
                '9:00 - Подъём\n' \
            ' \n' \
                '10:00 - Завтрак\n' \
            ' \n' \
                '11:00 - 17:00 Учебный блок\n' \
            ' \n' \
                '18:00 - 23:00 Свободное время\n' \
            ' \n' \
                '23:00 - 8:00 Сон\n'
    elif call.data == 'Tuesday':
        answer_timetable = '<b> Вторник </b>\n' \
                 ' \n' \
                 '8:00 - Сон\n' \
                 ' \n' \
                 '9:00 - Подъём\n' \
                 ' \n' \
                 '10:00 - Завтрак\n' \
                 ' \n' \
                 '11:00 - 17:00 Учебный блок\n' \
                 ' \n' \
                 '18:00 - 23:00 Свободное время\n' \
                 ' \n' \
                 '23:00 - 8:00 Сон\n'
    elif call.data == 'Wednesday':
        answer_timetable = '<b> Среда </b>\n' \
                 ' \n' \
                 '7:00 - Сон\n' \
                 ' \n' \
                 '8:00 - Подъём\n' \
                 ' \n' \
                 '9:30 - 10:50 Работа(Swift)\n' \
                 ' \n' \
                 '11:00 - Обед\n' \
                 ' \n' \
                 '12:00 - 17:00 Учебный блок\n' \
                 ' \n' \
                 '18:00 - 23:00 Свободное время\n' \
                 ' \n' \
                 '23:00 - 8:00 Сон\n'
    elif call.data == 'Thursday':
        answer_timetable = '<b> Четверг </b>\n' \
                 ' \n' \
                 '8:00 - Сон\n' \
                 ' \n' \
                 '9:00 - Подъём\n' \
                 ' \n' \
                 '10:00 - Завтрак\n' \
                 ' \n' \
                 '11:00 - 17:00 Учебный блок\n' \
                 ' \n' \
                 '18:00 - 23:00 Свободное время\n' \
                 ' \n' \
                 '23:00 - 8:00 Сон\n'
    elif call.data == 'Friday':
        answer_timetable = '<b> Пятница </b>\n' \
                 ' \n' \
                 '8:00 - Сон\n' \
                 ' \n' \
                 '9:30 - Подъём\n' \
                 ' \n' \
                 '10:00 - Завтрак\n' \
                 ' \n' \
                 '11:00 - 13:20 Работа(Системное администрирование)\n' \
                 ' \n' \
                 '14:00 - 17:00 Учебный блок\n' \
                 ' \n' \
                 '18:00 - 23:00 Свободное время\n' \
                 ' \n' \
                 '23:00 - 8:00 Сон\n'
    bot.send_message(call.message.chat.id, answer_timetable, parse_mode='html')


# random Joke
@bot.message_handler(commands=['joke'])
def joke_command(message):
    answer = f'{random.choice(joke)}'
    bot.send_message(message.chat.id, answer)


# datatime
@bot.message_handler(commands=['datetime'])
def start_command(message):
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, now.strftime("Дата - %d.%m.%Y \nВремя - %H:%M"))


# test
@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "Мой id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, ты можешь написать <u>/help</u> и я покажу что я умею",
                         parse_mode='html')


bot.polling(none_stop=True)
