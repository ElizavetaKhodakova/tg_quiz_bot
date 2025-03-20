# Telegram Quiz Bot

## Description
This project is a Telegram bot that allows users to participate in quizzes. The bot provides questions, accepts answers, and then displays the results. The questions are provided in the excel file, you can replace them with your own.

## Features
- Generation of random questions from various categories.
- Calculation and display of results after the quiz is completed.
- Ability to add new questions using excel file.

## Installation

### Requirements
- Python 3.x
- Libraries:
  - `pyTelegramBotAPI`
  - `pandas`
  - `openpyxl`

### Installing Dependencies
1. Clone the repository:
   bash
   git clone https://github.com/ElizavetaKhodakova/tg_quiz_bot.git
2. Navigate to the project folder:
   bash
   cd tg_quiz_bot

## Setup
1. Create a bot in Telegram via [BotFather](https://t.me/botfather) and get your token.
2. Create a `.env` file in the root of the project and add your token:
  bot = telebot.TeleBot('YOUR_TOKEN')

## Usage
Run the bot:
  bash
  python main.py

## References
  [Documentation](https://telegrambots.github.io/book/)


## Описание
Этот проект представляет собой Telegram бота, который позволяет пользователям участвовать в викторинах. Бот предоставляет вопросы и принимает ответы, а затем отображает результаты.
Вопросы указаны в excel-файле, вы можете заменить их на свой вариант.

## Функциональные возможности
- Вывод случайных вопросов из различных категорий.
- Подсчет и отображение результатов после завершения викторины.
- Возможность добавления новых вопросов через эксель-файл.

## Установка

### Требования
- Python 3.x
- Библиотеки:
  - `pyTelegramBotAPI`
  - `pandas`
  - `openpyxl`

### Установка зависимостей
1. Клонируйте репозиторий:
   bash
   git clone https://github.com/ElizavetaKhodakova/tg_quiz_bot.git
2. Перейдите в папку проекта:
   bash
   cd tg_quiz_bot
   
## Настройка
1. Создайте бота в Telegram через [BotFather](https://t.me/botfather) и получите токен.
2. Создайте файл `.env` в корне проекта и добавьте токен:
   bot = telebot.TeleBot('YOUR_TOKEN')

## Использование
Запустите бота:
  bash
  python main.py

## Ссылки
  [Документация](https://telegrambots.github.io/book/)
