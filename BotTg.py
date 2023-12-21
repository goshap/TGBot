import telebot
# import webbrowser

TOKEN = "6843288637:AAHPkqDs-Fs62mGYnqLtSy61A-3x-0x9HBA"

bot = telebot.TeleBot(TOKEN)


# bot.message_handler(commands=['ya'])
# def site(message):
#      bot.send_message(message.chat.id, 'https://ya.ru/')


@bot.message_handler(commands=['start'])
def main(message):
     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
     bot.send_message(message.chat.id, 'Извини, но пока я не могу тебе помочь 😓')


@bot.message_handler()
def info(message):
     if message.text.lower() == 'привет':
          bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
     elif message.text.lower() == 'id':
          bot.reply_to(message, f'Твой ID: {message.from_user.id}')




bot.polling(none_stop=True)