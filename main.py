import telebot
from telebot import types
import pandas as pd
import openpyxl
from openpyxl import load_workbook
from dotenv import load_dotenv

bot = telebot.TeleBot('YOUR_TOKEN')

user_state = {}
user_results = {}
data = pd.read_excel("Quiz_tg_bot.xlsx")
data['options'] = data['options'].apply(lambda x: x.split(', '))
QUIZ = data.to_dict(orient='records')
img = open('pic.jpg', 'rb')

def markup_creation(question):
    markup = types.InlineKeyboardMarkup()
    for option in question["options"]:
        button = types.InlineKeyboardButton(text=option, callback_data=option)
        markup.add(button)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Привет! Кто тут ко мне заглянул? Давай знакомиться. Я - бот Кузя. Как тебя зовут?')


@bot.message_handler(commands=["stop"])
def stop(message):
    bot.reply_to(message, "До встречи!")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Давай попробуем')
    btn2 = types.KeyboardButton('В другой раз')
    markup.add(btn1, btn2)
    if message.text == 'В другой раз':
        bot.reply_to(message, 'Буду ждать, приходи еще!')
    elif message.text == 'Давай попробуем':
        user_id = message.from_user.id
        user_state[user_id] = 0
        user_results[user_id] = 0
        question = get_quiz_question(user_id)
        markup = markup_creation(question)
        bot.send_message(message.chat.id, question["question"], reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Приятно познакомиться, ' + message.text)
        bot.send_message(message.from_user.id,
                         f"\nДавай сыграем в викторину? Если тебе надоест, ты можешь сказать мне об этом, "
                         f"просто напиши /stop",
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    user_id = call.from_user.id
    question = get_quiz_question(user_id)
    if call.data == question["answer"]:
        bot.reply_to(call.message, "Верно!")
        user_state[user_id] += 1
        user_results[user_id] += 1
        question = get_quiz_question(user_id)
        if question is None:
            bot.send_message(call.message.chat.id,
                                  f"Викторина закончилась. Вы ответили верно на {user_results[user_id]} вопросов")
            bot.send_photo(call.message.chat.id, img)
            return
        else:
            markup = markup_creation(question)
            bot.send_message(call.message.chat.id, question["question"], reply_markup=markup)
    elif call.data != question["answer"]:
        bot.reply_to(call.message, "Неверно! Правильный ответ " + question["answer"])
        user_state[user_id] += 1
        question = get_quiz_question(user_id)
        if question is None:
            bot.send_message(call.message.chat.id,
                                  f"Викторина закончилась. Вы ответили верно на {user_results[user_id]} вопросов")
            bot.send_photo(call.message.chat.id, img)
            return
        else:
            markup = markup_creation(question)
            bot.send_message(call.message.chat.id, question["question"], reply_markup=markup)


def get_quiz_question(user_id):
    question_index = user_state.get(user_id, 0)
    if question_index < len(QUIZ):
        return QUIZ[question_index]
    else:
        return None

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)