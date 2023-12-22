import telebot
from telebot import types
import webbrowser

TOKEN = "6843288637:AAHPkqDs-Fs62mGYnqLtSy61A-3x-0x9HBA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
     bot.send_message(message.chat.id, 'Извини, но пока я не могу тебе помочь 😓')


bot.message_handler(commands=['ya'])
def site(message):
     bot.send_message(message.chat.id, 'https://ya.ru/')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
     markup = types.InlineKeyboardMarkup()
     btn1 = types.InlineKeyboardButton('git', url = 'https://github.com/')
     markup.row(btn1)
     
     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data= 'delete')
     btn3 = types.InlineKeyboardButton('Изменить', callback_data= 'edit')
     markup.row(btn2, btn3)
     bot.reply_to(message, 'Пора заливать на гит', reply_markup = markup)


@bot.message_handler()
def info(message):
     if message.text.lower() == 'привет':
          bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
     elif message.text.lower() == 'id':
          bot.reply_to(message, f'Твой ID: {message.from_user.id}')
     elif message.text.lower() == 'git':
          bot.send_message(message.chat.id, 'https://github.com/')



bot.polling(none_stop=True)