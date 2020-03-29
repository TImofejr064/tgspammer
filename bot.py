import telebot
from telebot import types
from Bomber import bombing

bot = telebot.TeleBot("923492737:AAHA-LNgf4np0kz4Iws6vteziocqg9fa0ns")

keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyStartBomb = types.KeyboardButton(text="💣Начать бомбежку")
keyHelp = types.KeyboardButton(text="🆘Помощь")
keyboard.add(keyStartBomb, keyHelp)

keyboardTime = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
key1time = types.KeyboardButton(text="1")
key5time = types.KeyboardButton(text="5")
key10time = types.KeyboardButton(text="10")
key15time = types.KeyboardButton(text="15")
key20time = types.KeyboardButton(text="20")
key30time = types.KeyboardButton(text="30")

keyboardTime.add(key1time, key5time, key10time, key15time, key20time, key30time)

@bot.message_handler(commands=["start"])
def start_messaging(message): 
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def get_message(message):
    if message.text[1::] == "Начать бомбежку":
        bot.send_message(message.chat.id, "Выберите кол-во кругов бомбежки", reply_markup=keyboardTime)
        bot.register_next_step_handler(message, getTime)

def getTime(message):
    time = message.text
    bot.send_message(message.chat.id, "Введите номер по формату 79xxxxxxxxx")
    bot.register_next_step_handler(message, getNumber, time)

def getNumber(message, time):
    number = message.text
    
    bombing(number, int(time), message.chat.id)
    



if __name__ == '__main__':
    bot.polling(none_stop=True)