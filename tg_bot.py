import telebot
import random

BOT_TOKEN = "HAHAHA_THERE_IS_NO_MY_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)


def create_keyboard_choice():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    rand_num = telebot.types.KeyboardButton("Угадай число 🎲")
    re_name_file = telebot.types.KeyboardButton("Переименовать файл 📁")
    another_func = telebot.types.KeyboardButton("Другие функции ⚙️")
    keyboard.add(rand_num, re_name_file)
    keyboard.add(another_func)

    return keyboard


def create_another_function():
    keyboard = telebot.types.InlineKeyboardMarkup()
    how_many_word = telebot.types.InlineKeyboardButton(text="Посчитать слова 🔢", callback_data="how_many_word")
    keyboard.add(how_many_word)
    return keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет я могу выполнять разные команды нажми /commands чтобы открыть меню вкладок!"
    )


@bot.message_handler(commands=['commands'])
def send_command(message):
    bot.send_message(
        message.chat.id,
        "Нажмите на любую из команд: ",
        reply_markup=create_keyboard_choice()
    )


@bot.message_handler(func=lambda message: message.text == "Угадай число 🎲")
def random_number(message):
    bot.send_message(
        message.chat.id,
        "Задано число от 1 до 10, попробуйте отгадать 😊"
    )
    num = random.randint(1, 10)

    def check_num(msg):
        try:
            num_input = int(msg.text)
        except ValueError:
            bot.send_message(
                message.chat.id,
                "Введите число, а не текст!",
            )
            bot.register_next_step_handler(msg, check_num)
            return

        if num_input != num:
            bot.send_message(message.chat.id, "Не угадали попробуйте еще раз 😢")
            bot.register_next_step_handler(msg, check_num)
        else:
            bot.send_message(message.chat.id, "Вы угадали! 🎉")

    bot.register_next_step_handler(message, check_num)


@bot.message_handler(func=lambda message: message.text == "Переименовать файл 📁")
def set_rename_file(message):
    bot.send_message(
        message.chat.id,
        "Пришлите файл: "
    )
    bot.register_next_step_handler(message, wait_file)


def wait_file(message):
    if message.document:
        bot.send_message(
            message.chat.id,
            "Введите название файла: "
        )
        bot.register_next_step_handler(message, rename_file, message.document)
    else:
        bot.send_message(
            message.chat.id,
            "Это не файл! Попробуйте снова: ",
        )
        bot.register_next_step_handler(message, wait_file)


def rename_file(message, document):
    struct = document.file_name.split(".")[-1]
    file_name = f"{message.text}.{struct}"
    file_info = bot.get_file(document.file_id)
    file_bytes = bot.download_file(file_info.file_path)
    bot.send_document(
        message.chat.id,
        (file_name, file_bytes),
    )


def count_word(message):
    if message.text:
        words = message.text.split()
        bot.send_message(
            message.chat.id,
            f"Количество слов: {len(words)}"
        )
    else:
        bot.send_message(
            message.chat.id,
            "Вы ввели не число!"
        )
        bot.register_next_step_handler(message, count_word)


@bot.message_handler(func=lambda message: message.text == "Другие функции ⚙️")
def another_func(message):
    bot.send_message(
        message.chat.id,
        "Выбери пункт: ⬇️⬇️⬇️",
        reply_markup=create_another_function(),
    )


@bot.callback_query_handler(func=lambda call: True)
def another_function(call):
    if call.data == "how_many_word":
        bot.send_message(
            call.message.chat.id,
            "Введите текст в котором надо посчитать слова: "
        )
        bot.register_next_step_handler(call.message, count_word)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(
        message.chat.id,
        "Я вас не понял, нажмите /commands для того чтобы открыть меню вкладок!"
    )


bot.infinity_polling()
