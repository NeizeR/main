import telebot

VeryUsefulBot = telebot.TeleBot("685991048:AAEZAwIaFglAKDzKTHBnTJgoTUYt8Y8kMsc")


@VeryUsefulBot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        VeryUsefulBot.send_message(message.from_user.id, "Hi! I'm new and I'm useless so far, but it will change soon.")
    elif message.text == "How are you?" or message.text == "How are u?":
        VeryUsefulBot.send_message(message.from_user.id, "I'm fine.")
    else:
        VeryUsefulBot.send_message(message.from_user.id, "Sorry, I didn't catch what you've said.")


VeryUsefulBot.polling(none_stop=True, interval=0)
