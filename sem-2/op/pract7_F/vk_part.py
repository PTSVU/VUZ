import datetime
import json
import math
import random
import re

import PIL.Image as Image
import requests
from vk_api import vk_api, VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id

from config import token, check_group_format, weather_api_key, check_proffesor_pattern
from parsing_links import week_number
from schedule import professors

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
upload = VkUpload(vk_session)
longpoll = VkLongPoll(vk_session)

weather_s = "{description}, температура: {temp_min}-{temp_max}\u00b0С\n" \
            "Давление: {pressure} мм рт.ст., влажность: {humidity}%\n" \
            "Ветер: {wind_character}, {wind_speed} м/с, {wind_direction}\n"

eng_to_rus = {"Thunderstorm": "гроза", "Drizzle": "морось", "Rain": "дождь", "Snow": "снег",
              "Mist": "туман", "Smoke": "смог", "Haze": "дымка", "Fog": "туман",
              "Dust": "пыль", "Sand": "песчаная буря", "Ash": "пепел",
              "Squall": "шквалистый ветер", "Tornado": "ураган",
              "Clouds": "облачно", "Clear": "ясно"}


def wind_degrees_to_name(degree):
    if 0 <= degree < 45 or degree == 360:
        return "северный"
    elif 45 <= degree < 90:
        return "северо-восточный"
    elif 90 <= degree < 135:
        return "восточный"
    elif 135 <= degree < 180:
        return "юго-восточный"
    elif 180 <= degree < 225:
        return "южный"
    elif 225 <= degree < 270:
        return "юго-западный"
    elif 270 <= degree < 315:
        return "западный"
    elif 315 <= degree < 360:
        return "северо-западный"


def wind_speed_to_desc(speed):
    if 0 <= speed < 0.3:
        return "штиль"
    elif 0.3 <= speed < 3.3:
        return "легкий"
    elif 3.4 <= speed < 5.5:
        return "слабый"
    elif 5.5 <= speed < 10.8:
        return "умеренный"
    elif 10.8 <= speed < 20.8:
        return "сильный"
    elif 20.8 <= speed < 32.7:
        return "шторм"
    elif speed >= 32.7:
        return "ураган"


def pressure_in_mm(pressure):
    return math.floor(pressure * 100 / 133)


def current_weather(vk_event):
    weather_site = "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=" + weather_api_key + "&units=metric&lang=ru"
    weather_response = requests.get(weather_site)
    weather_info = weather_response.json()

    new_s = weather_s.format(description=weather_info["weather"][0]["description"].capitalize(),
                             temp_min=round(weather_info["main"]["temp_min"]),
                             temp_max=round(weather_info["main"]["temp_max"]),
                             pressure=pressure_in_mm(weather_info["main"]["pressure"]),
                             humidity=weather_info["main"]["humidity"],
                             wind_character=wind_speed_to_desc(weather_info["wind"]["speed"]),
                             wind_speed=round(weather_info["wind"]["speed"]),
                             wind_direction=wind_degrees_to_name(weather_info["wind"]["deg"]))

    image = requests.get("http://openweathermap.org/img/w/" + weather_info["weather"][0]["icon"] + ".png", stream=True)

    with open("single.png", "wb") as f:
        f.write(image.content)

    weather_pic = upload.photo_messages(photos='single.png')[0]
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Погода в Москве: {main}\n".format(main=eng_to_rus[weather_info["weather"][0]["main"]]),
        attachment="photo{}_{}".format(weather_pic["owner_id"], weather_pic["id"])
    )
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=new_s
    )
    weather_keyboard(vk_event)


def day_weather(vk_event, next_day=False):
    weath = ""
    weather_site = "http://api.openweathermap.org/data/2.5/forecast?q=moscow&appid=" + weather_api_key + "&units=metric&lang=ru"
    weather_response = requests.get(weather_site)
    weather_info = weather_response.json()
    start_index = 0
    img = Image.new('RGB', (200, 50))
    pic_x = 0

    if next_day:
        for i in range(9):
            if int(weather_info["list"][i]["dt_txt"].split()[1].split(':')[0]) == 0 and i != 0:
                start_index = i

    for daytime in range(start_index, start_index + 7, 2):
        hour = int(weather_info["list"][daytime]["dt_txt"].split()[1].split(':')[0])
        if 0 <= hour < 6:
            weath += "------------------НОЧЬ------------------\n"
        elif 6 <= hour < 12:
            weath += "------------------УТРО------------------\n"
        elif 12 <= hour < 18:
            weath += "------------------ДЕНЬ------------------\n"
        elif 18 <= hour < 24:
            weath += "------------------ВЕЧЕР------------------\n"

        image = requests.get(
            "http://openweathermap.org/img/w/" + weather_info["list"][daytime]["weather"][0]["icon"] + ".png",
            stream=True)
        with open("file_.png", "wb") as f:
            f.write(image.content)
        img_pt = Image.open("file_.png")
        img.paste(img_pt, (pic_x, 0))
        pic_x += 50

        weath += weather_s.format(
            description=weather_info["list"][daytime]["weather"][0]["description"].capitalize(),
            temp_min=round(weather_info["list"][daytime]["main"]["temp_min"]),
            temp_max=round(weather_info["list"][daytime]["main"]["temp_max"]),
            pressure=pressure_in_mm(weather_info["list"][daytime]["main"]["pressure"]),
            humidity=weather_info["list"][daytime]["main"]["humidity"],
            wind_character=wind_speed_to_desc(weather_info["list"][daytime]["wind"]["speed"]),
            wind_speed=round(weather_info["list"][daytime]["wind"]["speed"]),
            wind_direction=wind_degrees_to_name(weather_info["list"][daytime]["wind"]["deg"]))
        weath += "\n"

        # print(weather_info)

    img.save("day_weather.png")
    weather_pic = upload.photo_messages(photos='day_weather.png')[0]

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Погода в Москве на {day}".format(day="завтра" if next_day else "сегодня"),
        attachment="photo{}_{}".format(weather_pic["owner_id"], weather_pic["id"])

    )

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=weath,

    )
    weather_keyboard(vk_event)


def week_weather(vk_event):
    weather = ""
    weather_site = "http://api.openweathermap.org/data/2.5/forecast?q=moscow&appid=" + weather_api_key + "&units=metric&lang=ru"
    weather_response = requests.get(weather_site)
    weather_info = weather_response.json()
    # pprint(weather_info)
    night_start_index = 0
    day_start_index = 0
    start_pic_x = 0

    img = Image.new('RGB', (250, 50))

    for i in range(9):
        if int(weather_info["list"][i]["dt_txt"].split()[1].split(':')[0]) == 0:
            night_start_index = i
        if int(weather_info["list"][i]["dt_txt"].split()[1].split(':')[0]) == 12:
            day_start_index = i

    for day in range(day_start_index, len(weather_info["list"]), 8):
        weather += "/ " + str(round(weather_info["list"][day]["main"]["temp"])) + "\u00b0С /"

        image = requests.get(
            "http://openweathermap.org/img/w/" + weather_info["list"][day]["weather"][0]["icon"] + ".png",
            stream=True)
        with open("file.png", "wb") as f:
            f.write(image.content)
        img_part = Image.open("file.png")
        img.paste(img_part, (start_pic_x, 0))
        start_pic_x += 50

    img.save("week_weather.png")
    weather_pic = upload.photo_messages(photos='week_weather.png')[0]

    weather += " ДЕНЬ\n"

    for night in range(night_start_index, len(weather_info["list"]), 8):
        weather += "/  " + str(round(weather_info["list"][night]["main"]["temp"])) + "\u00b0С /"

    weather += " НОЧЬ"

    period_end = todays_date + datetime.timedelta(days=5)

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Погода в Москве c {start_day} до {end_day}".format(start_day=todays_date.strftime("%d.%m"),
                                                                    end_day=period_end.strftime("%d.%m")),
        attachment="photo{}_{}".format(weather_pic["owner_id"], weather_pic["id"])
    )

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=weather
    )
    weather_keyboard(vk_event)


def weather_keyboard(vk_event):
    temp_keyboard = VkKeyboard(one_time=True)
    temp_keyboard.add_button(label='сейчас', color=VkKeyboardColor.PRIMARY)
    temp_keyboard.add_button(label='сегодня', color=VkKeyboardColor.POSITIVE)
    temp_keyboard.add_button(label='завтра', color=VkKeyboardColor.POSITIVE)
    temp_keyboard.add_line()
    temp_keyboard.add_button(label='на 5 дней', color=VkKeyboardColor.POSITIVE)
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Показать погоду в Москве",
        keyboard=temp_keyboard.get_keyboard()
    )


def schedule_keyboard(vk_event, name_of_proffesor):
    global pass_prof
    temp_keyboard = VkKeyboard(one_time=True)
    temp_keyboard.add_button(label='Расписание на сегодня', color=VkKeyboardColor.POSITIVE)
    temp_keyboard.add_button(label='Расписание на завтра', color=VkKeyboardColor.NEGATIVE)
    temp_keyboard.add_line()  # Добавляем новую строку
    temp_keyboard.add_button(label='На эту неделю', color=VkKeyboardColor.PRIMARY)
    temp_keyboard.add_button(label='На следующую неделю', color=VkKeyboardColor.PRIMARY)
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Показать расписание преподавателя " + name_of_proffesor[0],  # todo имя препода
        keyboard=temp_keyboard.get_keyboard()
    )
    pass_prof = True


# todo присылать расписание преподов
def professor_schedule(vk_event, professor):
    msg = ""
    professors = proffesors_schedule
    msg += "Schedule for " + professor + ":\n"
    curr_sched = professors[professor]

    for weekday, schedule in curr_sched.items():
        msg += weekday.capitalize() + ":\n"
        for i, lesson in enumerate(schedule):
            lesson = i + 1
            lesson_info = ", ".join(lesson.values())
            # msg += str(lesson_num) + ") " + lesson_info + "\n"

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=msg
    )


def proffesors_keyboard(professors_list, vk_event):
    # Create a dictionary to group professors with the same surname
    temp_keyboard = VkKeyboard(one_time=True)
    for prof_name in professors_list:
        temp_keyboard.add_button(label=prof_name, color=VkKeyboardColor.PRIMARY)

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Выберите преподавателя",
        keyboard=temp_keyboard.get_keyboard()
    )


# images
attachments = []
photo = upload.photo_messages(photos='src/ikbo-23-22.jpg')[0]
attachments.append("photo{}_{}".format(photo["owner_id"], photo["id"]))
photoes = ['src/ikbo-23-22.jpg', 'src/ikbo-23-22(2).jpg', 'src/ikbo-23-22(3).jpg', 'src/ikbo-23-22(4).jpg',
           'src/ikbo-23-22(5).jpg',
           'src/ikbo-23-22(6).jpg', 'src/ikbo-23-22(7).jpg', 'src/ikbo-23-22(8).jpg', 'src/ikbo-23-22(9).jpg',
           'src/ikbo-23-22(10).jpg']
doggo = upload.photo_messages(photos='src/ikbo-23-22.jpg')[0]

# MIREA schedule
weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
todays_date = datetime.date.today()
group_regex = r"И[АВКНМ]{1}БО-[0-9]{2}-1[7-9]{1}"
current_group = ""
current_proffesor = ''
base_schedule_str = "Расписание на {weekday}, {date}:\n"
pass_gr = False
pass_prof = False
# schedule for each course
with open("course1_sch.json", "r") as read_file:
    first_course_schedule = json.load(read_file)
with open("course2_sch.json", "r") as read_file:
    second_course_schedule = json.load(read_file)
with open("course2_sch.json", "r") as read_file:
    third_course_schedule = json.load(read_file)
with open("professors.json", "r") as read_file:
    proffesors_schedule = json.load(read_file)
oddity = 1 if int(week_number) % 2 == 0 else 0


def choose_random_photo():
    photo = upload.photo_messages(photos=random.choice(photoes))[0]
    return "photo{}_{}".format(photo["owner_id"], photo["id"])


def greeting(vk_event):
    # print('New from {}, text = {}'.format(vk_event.user_id, vk_event.text))
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message='Привет, ' + vk.users.get(user_id=vk_event.user_id)[0]['first_name'],
        keyboard=keyboard.get_keyboard(),
        attachment="photo{}_{}".format(doggo["owner_id"], doggo["id"])
    )


def instructions(vk_event):
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message='Инструкция по работе с ботом:\n'
                'Этот бот умеет выдавать расписание студентов ИИТ РТУ МИРЭА и сообщать о погоде. '
                'Для каждого раздела есть свои команды. Чтобы увидеть список доступных команд (кнопки) в любое время, отправьте сообщение "бот".\n\n'
                'Список команд бота:\n\n'
                'Название группы в формате "ИКБО-XX-XX" - основная группа, по которой будет выдаваться расписание\n\n'
                '"Какая группа?" - основная группа на данный момент,\n\n'
                '"Какая неделя?" - номер текущей недели, \n\n'
                '"Расписание на сегодня", "Расписание на завтра", "Расписание на эту неделю", "Расписание на следующую неделю" - подробное расписание занятий на соответствующий период,\n\n'
                '"Бот <группа>" - изменить основную группу и показать ее расписание на выбранный период,\n\n'
                '"Бот <день недели>" - расписание для нечетной и четной недели в соответствующий день у основной группы,\n\n'
                '"Бот <день недели> <группа>" - расписание для нечетной и четной недели в соответствующий день у указанной группы,\n\n'
                '"Погода" - погода в Москве на выбранный период времени.\n\n'
                '"Найти <фамилия преподавателя>" - расписание выбраного преподавателя\n\n'
                'Если команда не будет совпадать со списком перечисленных, бот кинет обидку. Удачи!'
    )


def show_functions(vk_event):
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Показать...",
        keyboard=keyboard.get_keyboard()
    )


def unknown(vk_event):
    vk.messages.send(
        user_id=vk_event.user_id,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message='Неизвестная команда. Чтобы посмотреть список допустимых команд, отправьте "инструкция" или "бот"'
    )


def set_current_group(vk_event, group):
    global current_group
    save_group(str(vk_event.user_id), group)
    current_group = load_group(str(vk_event.user_id))
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Я запомнил, что ты из группы " + current_group,
        keyboard=keyboard.get_keyboard()
    )


def print_current_group(vk_event):
    if load_group(str(vk_event.user_id)) == None:
        s = "Сначала введите номер группы"
    else:
        s = "Показываю расписание группы " + current_group

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=s,
        keyboard=keyboard.get_keyboard()
    )


def print_current_week(vk_event):
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message='Идёт ' + str(week_number) + ' неделя',
        keyboard=keyboard.get_keyboard()
    )


def choose_schedule(group):
    str(group)
    if group.endswith("22"):
        return first_course_schedule
    elif group.endswith("21"):
        return second_course_schedule
    elif group.endswith("20"):
        return third_course_schedule
    elif check_proffesor_pattern(group):
        print("ПОБЕДА")
        return proffesors_schedule


def day_schedule(group, day=todays_date, for_next_week=False):
    # Определение дня недели (weekday) и форматирование даты и дня недели
    current_weekday = day.weekday()
    current_weekday_s = weekdays[current_weekday]
    inner_oddity = oddity

    # Если указано расписание на следующую неделю, то меняем значене внутренней переменной "oddity"
    # (которая используется для выбора пар в текущей неделе) на противоположное
    if for_next_week:
        inner_oddity = 1 if oddity == 0 else 0

    # Формируем строку с данными о дате и дне недели
    s = base_schedule_str.format(
        weekday=current_weekday_s.replace("а", "у") if current_weekday_s.endswith("а") else current_weekday_s,
        date=day.strftime('%d.%m.%Y'))

    # Если не было указаноазвания группы, возвращаем сообщение об ошибке
    if group == "":
        s = "Сначала введите номер группы"
    else:
        # Получим расписание выбранной группы, используя функцию choose_schedule
        curr_schedule = choose_schedule(group)
        if curr_schedule is not None:
            print("Победа 3")
        lesson_num = 0

        try:
            # Проверяем, что не воскресенье (т.к. воскресенье - отдельный случай)
            if current_weekday != 6:
                # Проходимся по каждой паре в текущий день и добавляем в строку s
                for i in range(7):
                    lesson_num += 1
                    day_info = list(curr_schedule[group.upper()][current_weekday_s][i][inner_oddity].values())
                    s += str(lesson_num) + ") " + ', '.join(day_info) + '\n'
            else:
                # Если воскресенье, добавляем только информацию для этого дня из расписания текущей группы
                s += str(curr_schedule[group.upper()][current_weekday_s])
        except KeyError:
            # В случае, если название группы указано неверно, возвращаем сообщение об ошибке
            s = "Группы не существует или для нее отсутствует расписание. " \
                "Пожалуйста, отправьте корректное название группы"

    # Возвращаем сформированную строку
    return s


def print_day_schedule(vk_event, group, day=todays_date, next_week=False):
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=day_schedule(group, day, for_next_week=next_week),
        keyboard=keyboard.get_keyboard()
    )
    global current_group, pass_gr, pass_prof
    current_group = load_group(str(vk_event.user_id))
    pass_gr = False
    pass_prof = False


def print_week_schedule(vk_event, group, next_week=False):
    msg = ""
    if next_week:
        dates = [todays_date + datetime.timedelta(days=i) for i in
                 range(7 - todays_date.weekday(), 14 - todays_date.weekday())]
    else:
        dates = [todays_date + datetime.timedelta(days=i) for i in
                 range(0 - todays_date.weekday(), 7 - todays_date.weekday())]

    for day in dates:
        if msg != "Сначала введите номер группы\n":
            msg += day_schedule(group, day=day, for_next_week=next_week) + '\n'

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=msg,
        keyboard=keyboard.get_keyboard()
    )
    global current_group, pass_gr, pass_prof
    current_group = load_group(str(vk_event.user_id))
    pass_gr = False
    pass_prof = False


def weekday_schedule(vk_event, weekday, group):
    msg = ""
    if load_group(str(vk_event.user_id)) == None:
        msg += "Сначала введите номер группы"
    else:
        msg += weekday.capitalize() + ", нечетная неделя:\n"
        curr_sch = choose_schedule(group)
        if curr_sch is not None:
            print("ПОБЕДЕДА 2")
        lesson_num = 0
        try:
            if weekday != "воскресенье":
                for i in range(6):  # amount of lessons
                    lesson_num += 1
                    day_info = list(curr_sch[group][weekday][i][0].values())
                    msg += str(lesson_num) + ") " + ', '.join(day_info) + '\n'
            else:
                msg += curr_sch[group][weekday]

            msg += "\n" + weekday.capitalize() + ", четная неделя:\n"
            lesson_num = 0

            if weekday != "воскресенье":
                for i in range(6):  # amount of lessons
                    lesson_num += 1
                    day_info = list(curr_sch[group][weekday][i][1].values())
                    msg += str(lesson_num) + ") " + ', '.join(day_info) + '\n'
            else:
                msg += curr_sch[group][weekday]
        except TypeError:
            msg = "Группы не существует или для нее отсутствует расписание. " \
                  "Пожалуйста, отправьте корректное название группы"

    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message=msg
    )
    global current_group, pass_gr, pass_prof
    current_group = load_group(str(vk_event.user_id))
    pass_gr = False
    pass_prof = False


def change_group(vk_event, group):
    global current_group
    current_group = group.upper()
    vk.messages.send(
        user_id=vk_event.user_id,
        random_id=get_random_id(),
        message="Показать расписание группы " + group.upper(),
        keyboard=keyboard.get_keyboard()
    )
    global pass_gr
    pass_gr = True


professor_names = list(professors.keys())


def search_professor_by_surname(surname: str, professor_names_clear: list) -> list:
    result = []
    for professor in professor_names_clear:
        if surname == professor.split()[0].lower():
            result.append(professor)
    return result


# разделить имена преподавателей по запятой
professor_names = [name.strip() for name in ','.join(professor_names).split(',')]

# убрать дубликаты
professor_names = list(set(professor_names))
pattern_for_proffesors = r'\d+\s+[п|П]/[г|Г]'
professor_names_clear = [i for i in professor_names if i not in ['', '--'] and not re.search(pattern_for_proffesors, i)]
print(professor_names_clear)


# BOT APPEARANCE AND BEHAVIOUR
def save_group(id, group):
    with open("users_group.json", "r") as file:
        data = json.load(file)
    data[str(id)] = str(group).upper().replace("[", "").replace("]", "").replace("'", "")
    with open("users_group.json", "w") as file:
        json.dump(data, file)


def load_group(id):
    try:
        with open("users_group.json", "r") as file:
            data = json.load(file)
        return data[str(id)]
    except KeyError:
        return None


# Buttons
keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Расписание на сегодня', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()  # Добавляем новую строку
keyboard.add_button('На эту неделю', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('На следующую неделю', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()  # Добавляем новую строку
keyboard.add_button('Какая неделя?', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Какая группа?', color=VkKeyboardColor.SECONDARY)

# Mainloop
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg_words = event.text.lower().split()
        print('id{}: "{}"'.format(event.user_id, event.text), end='\n')
        if current_group == "" or current_group == None:
            current_group = load_group(str(event.user_id))

        # if pass_prof == True and event.text.lower() == "расписание на сегодня":
        #     temp = str(search_professor_by_surname(current_proffesor, professor_names_clear)[0])
        #     print(temp)
        #     print_day_schedule(event, temp)

        elif event.text.lower() == "начать":
            greeting(event)
            instructions(event)
        elif event.text.lower() == "привет":
            greeting(event)
        elif event.text.lower() == "инструкция":
            instructions(event)
        elif event.text.lower() == "расписание на сегодня":
            print_day_schedule(event, current_group)
        elif event.text.lower() == "на эту неделю":
            print_week_schedule(event, current_group)
        elif event.text.lower() == "на следующую неделю":
            print_week_schedule(event, current_group, next_week=True)
        elif event.text.lower() == "расписание на завтра":
            if todays_date.weekday() != 6:
                print_day_schedule(event, current_group, todays_date + datetime.timedelta(days=1))
            else:
                print_day_schedule(event, current_group, todays_date + datetime.timedelta(days=1), next_week=True)
        elif event.text.lower() == "какая группа?":
            print_current_group(event)
        elif event.text.lower() == "какая неделя?":
            print_current_week(event)
        elif len(msg_words) == 1 and check_group_format(msg_words[0]):
            set_current_group(event, event.text)
        elif msg_words[0] == "бот":
            if len(msg_words) == 1:
                show_functions(event)
            if len(msg_words) == 2:
                if msg_words[1] in weekdays:
                    weekday_schedule(event, msg_words[1], current_group)
                elif check_group_format(msg_words[1]):
                    change_group(event, msg_words[1])
            elif len(msg_words) == 3:
                if msg_words[1] in weekdays and check_group_format(msg_words[2]):
                    weekday_schedule(event, msg_words[1], msg_words[2].upper())
        elif len(msg_words) == 2 and msg_words[0] == "найти":
            if (len(search_professor_by_surname(msg_words[1], professor_names_clear))) > 1:
                proffesors_keyboard(search_professor_by_surname(msg_words[1], professor_names_clear), event)
            else:
                schedule_keyboard(event, (search_professor_by_surname(msg_words[1], professor_names_clear)))
                current_proffesor = msg_words[1]

        # elif check_proffesor_pattern(event.text.lower):
        #     print_day_schedule(event, str(event.text.lower.capitalize()))

        elif event.text.lower() == "погода" or event.text.lower() == "погоду":
            weather_keyboard(event)
        elif event.text.lower() == "сейчас":
            current_weather(event)
        elif event.text.lower() == "сегодня":
            day_weather(event)
        elif event.text.lower() == "завтра":
            day_weather(event, next_day=True)
        elif event.text.lower() == "на 5 дней":
            week_weather(event)
        elif event.text.lower() == "спасибо" or event.text.lower() == "спс" or event.text.lower() == "молодец":
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                attachment=choose_random_photo()
            )
        else:
            unknown(event)
        if current_group != load_group(str(event.user_id)) and pass_gr == False:
            current_group = load_group(str(event.user_id))
