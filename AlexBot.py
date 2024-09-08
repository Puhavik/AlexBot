import telebot # type: ignore
from telebot import types # type: ignore

# Токен твоего бота
TOKEN = ''

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения текущего состояния игры пользователя
user_state = {}

# Стартовое сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    # Кнопка для первой загадки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    first_clue_button = types.KeyboardButton("Первая загадка")
    markup.add(first_clue_button)
    
    bot.send_message(message.chat.id, 
                     "Привет! Я душный бот, создан чтобы помочь тебе найти свой подарок на день рождения. С наступающим, кстати… Я буду высылать тебе разного вида загадки, которые тебе нужно будет разгадать, чтобы получить свой подарок (тот самый, который ты просил не дарить тебе, но кто тебя слушает…).",
                     reply_markup=markup)
    bot.send_message(message.chat.id, 
                     "Если у тебя будут возникать трудности, то ты всегда сможешь попросить своих друзей о помощи. Только есть одно «но»: чтобы «разблокировать» их помощь, тебе прийдется по памяти назвать дату рождения того, у кого нужная тебе подсказка. Удачи!",
                     reply_markup=markup)
    bot.send_message(message.chat.id, 
                     "Жми на кнопку для того, чтобы получить первую подсказку.",
                     reply_markup=markup)
    user_state[message.chat.id] = {'step': 0, 'hints_used': 0}

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True, content_types=["voice", "text"])
def handle_message(message):
    user_id = message.chat.id
    state = user_state.get(user_id, {'step': 0, 'hints_used': 0})

    if state['step'] == 0 and message.text == "Первая загадка":
        # Удаляем клавиатуру после нажатия кнопки
        remove_markup = types.ReplyKeyboardRemove()
        bot.send_photo(user_id, open('puzzle1.jpg', 'rb'))  # Отправляем картинку-загадку
        bot.send_message(user_id, "Если ты не знаешь как разгадывать ребусы, можешь попросить Рустама тебе помочь. Только сначала тебе прийдется вспомнить дату его рождения.", reply_markup=remove_markup)
        state['step'] = 1

    elif state['step'] == 1:
        if message.text.lower() == "soso4ki":
            bot.send_message(user_id, "С ребусом ты справился, конечно, ты же дева… Теперь посмотрим на твои познания в астрологии. Ты должен рассчитать свою матрицу судьбы и найти свою визитную карточку.")
            bot.send_message(user_id, "Если тебе нужна помощь профессионала, можешь обратиться к Вике. Только не забудь задобрить ее тем, что помнишь когда она родилась!")
            state['step'] = 2
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 2:
        if message.text.lower() == "coding":
            bot.send_message(user_id, "А ты не пальцем деланный, я смотрю, выкрутился… Теперь тебе станет посложнее. Разгадай загадку и поймешь куда идти: Крути педали пока не дали.")
            bot.send_message(user_id, "Если тебе понадобится помощь, обратись к Вику, он тебе поможет. Его день рождения ты помнишь?")
            state['step'] = 3
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 3:
        if message.text.lower() == "richie":
            bot.send_message(user_id, "Чтобы получить следующую подсказку, тебе надо всего лишь продолжить песню. Запиши аудио, как ты поешь, и отправь мне. И да, я проверю, что ты пел!")
            bot.send_message(user_id, "Ведьмаку заплатите …")
            state['step'] = 4
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 4:
        if message.content_type == 'voice':
            bot.send_message(user_id, "Нет, ну я всегда говорил: «Лох не мамонт, не вымрет». Как же я проверю твое аудио? Я же всего лишь бот. Вот следующая загадка: На что самое постыдное ты писал по пьяне?")
            bot.send_message(user_id, "За помощью можешь обратиться к Сашуле, ей до сих пор стыдно, что она это видела.")
            state['step'] = 5
        else:
            bot.send_message(user_id, "Я же сказал, что надо петь!")

    elif state['step'] == 5:
        if message.text.lower() == "namak":
            bot.send_message(user_id, "Следующая подсказка находится там, куда мы любили ходить во время карантина.")
            bot.send_message(user_id, "В этот раз тебе поможет твоя бывшая соседка по общежитию Элис.")
            state['step'] = 6
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 6:
        if message.text.lower() == "kmpg":
            bot.send_message(user_id, "Следующее место зашифровано сканвордом. Из первых букв ответов на эти вопросы тебе надо будет составить название места где спрятана следующая подсказка.")
            bot.send_message(user_id, "С этим заданием ты можешь попросить помощи у любого из друзей и братьев.")
            bot.send_message(user_id, "Летит как гавно на __?")
            state['step'] = 7
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 7:
        if message.text.lower() == "муху":
            bot.send_message(user_id, "Слышь сучка, __ на беззвучку")
            state['step'] = 8
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 8:
        if message.text.lower() == "ебучку":
            bot.send_message(user_id, "____ заплывчиво, а дело забывчиво.")
            state['step'] = 9
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 9:
        if message.text.lower() == "тело":
            bot.send_message(user_id, "Не грусти, а то болт не будет _")
            state['step'] = 10
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 10:
        if message.text.lower() == "расти":
            bot.send_message(user_id, "Нет лучше влагалища чем _ товарища")
            state['step'] = 11
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 11:
        if message.text.lower() == "очко":
            bot.send_message(user_id, "Ты ответил на все вопросы! Теперь из первых букв этих ответов составь правильное слово и ты сразу поймешь куда тебе идти. Как дойдешь- найдешь конверт с кодовым словом, отправь его мне для следующей подсказки.")
            state['step'] = 12
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 12:
        if message.text.lower() == "loch":
            bot.send_message(user_id, "Чтобы получить следующее место, тебе прийдется вспомнить первый семестр в универе.")
            bot.send_message(user_id, "Если тебе нужна помощь, можешь обратиться к Владу сразу после того, как вспомнишь его дату рождения. Если совсем туго, обратись к брату-айтишнику, он всегда поможет.")
            bot.send_message(user_id, "VMRRFSIGOWXVEWWI 11100, 1010")
            state['step'] = 13
        else:
            bot.send_message(user_id, "Неправильно. Думай еще!")

    elif state['step'] == 13:
        # Создаем объект клавиатуры
        markup = types.ReplyKeyboardMarkup( resize_keyboard=True)
        
        # Создаем кнопки
        button_yes = types.KeyboardButton('Да')
        button_no = types.KeyboardButton('Нет')
        
        # Добавляем кнопки на клавиатуру
        markup.add(button_yes, button_no)
        
        # Отправляем сообщение с кнопками
        bot.send_message(user_id, "Это пасхалки, ответь на вопрос: \"Ты пидр?\"", reply_markup=markup)
        
        # Обновляем состояние, чтобы обработать ответ в следующем сообщении
        state['step'] = 14

    elif state['step'] == 14:
        # Обрабатываем выбор пользователя
        if message.text == "Нет":
            bot.send_message(user_id, "Тут ты неправ! Подумай еще!")
        elif message.text == "Да":
            bot.send_message(user_id, "Я так и знал!")
            bot.send_message(user_id, "Конец игры!")
        
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        
            # Создаем кнопки
            button_rewiev = types.KeyboardButton('Оставить Отзыв')
            markup.add(button_rewiev)
            bot.send_message(user_id, "Как тебе игра?", reply_markup=markup)
            state['step'] = 15

    elif state['step'] == 15:
        if message.content_type == 'text':
            bot.send_message(user_id, "Да мне похуй!")

    user_state[user_id] = state



# Запуск бота
bot.polling(none_stop=True)
