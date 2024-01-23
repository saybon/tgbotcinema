import telebot
from icrawler.builtin import GoogleImageCrawler
from random import randint

bot = telebot.TeleBot('')
qq = False
admin_id = ''
link1 = '@testtesttesttest12332'


boevik = ['Код доступа «Кейптаун» 2012, ЮАР,Боевики', 'Семейный бизнес 2021 США Боевики', 'Охота 2020 США Боевики',
          'Месть земли 2021 Китай Боевики', 'Герой 2019 Россия Боевики', 'Выжить в игре 2021 США Боевики',
          'Плечом к плечу 2021 США Боевики', 'Мировой парень 1972 СССР Боевики', 'Обет молчания 2017 Болгария Боевики',
          'Апокалипсис: Зависшие в небе 2017 Германия Боевики', 'Падение Олимпа 2013 США Боевики',
          'Поймать свидетеля 2021 США Боевики', 'Наемник 2017 США Боевики', 'Марлен 2020 Автралия Боевики']
fantastic = ['Кольцо времени 2019, Канада, Фантастика', 'Приключения мышонка Переса 2 2008 Испания Фантастика',
             'Имплант 2021 США Фантастика', 'Эллипс 2019 США Фантастика',
             '[4k] Последний день Земли 2020 Франция Фантастика', 'Земля сыновей 2021 Италия Фантастика',
             'Порталы времени 2019 США Фантастика', 'Последние дни Земли 2017 ЮАр Фантастика',
             'Халк 2003 США Фантастика', 'Водный мир 1995 США Фантастика', 'Вторжение 202 Россия Фантастика',
             'Возвращение 2017 Канада Фантастика']
comedy = ['Вдребезги 2011 Россия Комедии', 'Тесть-драйв 2021 США Комедии', 'Изобретение лжи 2009 США Комедии',
          'Хищники 2021 Россия Комедии', 'День дурака 2014 Россия Комедии',
          'В винном отражении (с русскими субтитрами) 2021 Россия Комедии',
          'Любовь, свидания, Нью-Йорк 2021 США Комедии', 'Хищники 2021 Россия Комедии',
          'О, счастливчик! 2009 Россия Комедии', 'Формула любви для узников брака 2009 США Комедии',
          'Фантазии для взрослых 2021 США Комедии', 'Днюха! 2018 Россия Комедии',
          'Новогодний ремонт 2019 Россия Комедии', 'Клуб воров 2018 США Комедии']




@bot.message_handler(commands=['admin'])
def add_special_function(message):
    # Получение id пользователя
    user_id = message.from_user.id
    # Добавление специальной функции пользователю по его id
    if int(user_id) == int(admin_id):
        bot.send_message(message.chat.id, "Вы являетесь админо этого бота!\n"
                                          "Добавление рекламных постов: /advertising\n"
                                          "Только вам доступны эти функции.")


global user_id


@bot.message_handler(commands=['advertising'])
def advertising(message):
    user_id = message.from_user.id
    if int(user_id) == int(admin_id):
        sent = bot.send_message(message.chat.id, "Введите сообщение которое хотите отправить всем пользователям бота:")
        bot.register_next_step_handler(sent, ask)


def ask(message):
    user_id = message.from_user.id
    if int(user_id) == int(admin_id):
        message_to = message.text
        for i in open('users.txt', 'r').readlines():
            bot.send_message(i, f"{message_to}")

@bot.message_handler(commands=['start'])
def start(message):
    with open('users.txt', 'a+') as users:
        print(message.chat.id, file=users)
    # Отправляем приветственное сообщение и кнопку "Проверить"
    user = message.chat.first_name
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('Проверить'))
    markup.add(telebot.types.KeyboardButton('Боевики'))
    markup.add(telebot.types.KeyboardButton('Фантастика'))
    markup.add(telebot.types.KeyboardButton('Комедийные'))
    photo = open("start.jpg", "rb")
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, f"Приветствую,{user}! Для того, чтобы пользоваться ботом подпишись на каналы: \n"
                                      f"1) {link1}\n", reply_markup=markup)

@bot.message_handler(content_types=['text','photo'])
def text(message):
    global qq, film
    file = open("films.txt", encoding="utf-8")
    user = message.chat.first_name
    if message.chat.type == 'private':
        if message.text == "Проверить":
            status = ['creator', 'administrator', 'member']
            for stat in status:
                if stat == bot.get_chat_member(chat_id=link1, user_id=message.from_user.id).status:
                    bot.send_message(message.chat.id, f"{user}, спасибо за выполнение условий")
                    bot.send_message(message.chat.id, f"{user}, чтобы узнать название фильма введите его номер:")
                    qq = True
                    break
                else:
                    bot.send_message(message.chat.id, f"{user}, подпишитесь на все каналы!")
                    qq = False

        if message.text == "Боевики" and qq == True:
            random_number = randint(0, len(boevik))
            bot.send_message(message.chat.id, f"Фильм: {boevik[random_number - 1]}")
        if message.text == "Фантастика" and qq == True:
            random_number = randint(0, len(fantastic))
            bot.send_message(message.chat.id, f"Фильм: {fantastic[random_number - 1]}")
        if message.text == "Комедийные" and qq == True:
            random_number = randint(0, len(comedy))
            bot.send_message(message.chat.id, f"Фильм: {comedy[random_number - 1]}")

        while qq:
            film_list = file.readlines()  # прочитать все строки из файла и сохранить в список
            if message.text.isdigit():  # проверить, является ли введенный текст числом
                index = int(message.text)  # преобразовать текст в число
                if 0 <= index < len(film_list):  # проверить, что индекс находится в допустимых пределах
                    index -= 1
                    film = film_list[index]  # получить значение из списка по индексу
                    #
                    file = open("films.txt", encoding="utf-8")
                    google_crawler = GoogleImageCrawler(
                        storage={'root_dir': 'C:/Users/Богдан/Desktop/Новая папка/botcinema'})
                    q = 1
                    for line in file:
                        if index == 1:
                            google_crawler.crawl(keyword="Код доступа «Кейптаун» 2012, ЮАР,Боевики", max_num=1, overwrite=True)
                            photo = open("000001.jpg","rb")
                            bot.send_photo(message.chat.id, photo)

                        if q-1 == index:
                            google_crawler.crawl(keyword=line, max_num=1, overwrite=True)
                            photo = open("000001.jpg","rb")
                            bot.send_photo(message.chat.id, photo)
                            break
                        q+=1
                    #
                    bot.send_message(message.chat.id, f"Фильм: {film}")
                else:
                    bot.send_message(message.chat.id, "Неверный номер фильма")
            else:
                bot.send_message(message.chat.id, "Введите номер фильма в виде числа")
            break

bot.polling(non_stop=True)