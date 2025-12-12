# Zahar Ambrozyak property

import requests

# Для ліпшої читабельності коду
from typing import Optional, Any

# Щоб додавати до логу час
from datetime import datetime, UTC

class OpenWeatherMap:
    """
    Побудувати клас OpenWeatherMap
    """
    def __init__(self, city: str = 'Kyiv') -> None:
        """
        Створюємо всі необхідні атрибути для роботи
        :param city: назва міста, якщо ми раптом хочемо одразу задати місто, за замовчуванням 'Kyiv'
        """
        self.key = '2ffda98bfbe8f5d17280fa7d817d1e2b'
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}"
        self.data = self.__set_data(self.url)
        self.code = int(self.data['cod'])

        # Текста та коди помилок
        self.KEY_ERROR = 'Такого ключа немає!'
        self.ERROR = 'Упс, вискочила помилка!'
        self.WRONG_DATA_TYPE = 'Неправильний тип даних!'
        self.NO_CITY_TEXT = 'Такого міста не існує!'
        self.NO_DATA = 'Немає даних!'
        self.WRONG_T_MEASURE = 'Такої одиниці вимірювання для температури немає!'
        self.NOT_ENOUGH_DATA = 'Недостатньо даних!'
        self.GOOD_CODE = 200
        self.NO_CITY_CODE = 404
        self.BAD_CODE = 400

        # Всі помилки разом зібрані
        self.errors = (self.KEY_ERROR, self.ERROR, self.WRONG_T_MEASURE,
                      self.NO_DATA, self.BAD_CODE, self.NOT_ENOUGH_DATA,
                      self.NO_CITY_CODE, self.NO_CITY_TEXT, self.WRONG_DATA_TYPE,
                        None)

        # Деякі константи
        self.T_CONST = 273.15
        self.filename = 'log.txt'

        # Хапаєм помилку, якщо місто, яке ми задали - не існує
        if self.code != self.GOOD_CODE:
            if self.code == self.NO_CITY_CODE:
                print(self.NO_CITY_TEXT)
            while True:
                another_city = input('Введіть назву міста: ')
                self.url = f"https://api.openweathermap.org/data/2.5/weather?q={another_city}&appid={self.key}"
                self.data = self.__set_data(self.url)
                self.code = int(self.data['cod'])
                print(self.code)
                if self.code == self.GOOD_CODE:
                    break
                print(self.NO_CITY_TEXT)

    @staticmethod
    def __set_data(url: str) -> dict:
        """
        Статичний метод, який повертає дані з API

        Приймає один аргумент:
        :param url: посилання на API
        """
        return eval(requests.get(url).text)

    def __add_origin(self, text: str, origin: str):
        """
        Метод, який додає джерело запиту

        Наприклад:
        get_temp -> show (get_temp йде від show)
        :param text: сам метод
        :param origin: звідки він походить

        Повертає модифікований текст
        """

        # Хапаєм помилку
        if isinstance(text, str) and isinstance(origin, str):
            if origin:
                output = text + ' -> ' + origin
                return output
            return text
        else:
            return self.WRONG_DATA_TYPE

    def __check_error(self, data: list[Any]) -> bool:
        """
        Перевіряє, чи немає помилки в списку з даними
        :param data: самі дані

        Повертає True (є хоча б одна помилка) або False (немає)
        """

        # Дивимось, чи є взагалі, що перевіряти
        if data:
            for error in self.errors:
                if error in data:
                    return True
        else:
            print(self.NO_DATA)
        return False

    def __wrap_text_if_errors(self, text: str, data: list[Any]) -> str:
        """
        Додає до тексту відповідні смайлики, якщо в даних є/немає помилок
        :param text: сам текст
        :param data: дані для перевірки
        """

        # Дивимось, чи правильні типи даних задані
        if isinstance(text, str) and isinstance(data, list):
            return '⛔️ ' + str(text) if self.__check_error(data) else '✅ ' + str(text)
        print(self.WRONG_DATA_TYPE)
        return 'None'

    def __log_data(self, data: list[Any]) -> None:
        """
        Метод, який логує виконані запити
        Приймає один аргумент:
        :param data: дані для логування
        """

        # Додаєм смайлик
        data[0] = self.__wrap_text_if_errors(data[0], data[1:])

        with open(self.filename, 'a') as f:
            f.write(', '.join([str(datetime.now(UTC))] + [str(i) for i in data]) + '\n')

    def get_temp(self, measure: str = 'K', t_type: str = 'temp', origin: str = '') -> Optional['str']:
        """
        Метод get_temp - повертає текст температури та її одиниці вимірювання

        Приймає два аргументи:
        :param measure: C (Цельсій), F (Фаренгейт), K (Кельвін - за замовчуванням)
        :param t_type: яку саме темпаратуру дістаєм: temp_min, temp_max, feels_like, temp (за замовчуванням)
        :param origin: звідки походить цей запит, опціонально
        """

        request_text = self.__add_origin('get_temp', origin)
        # Хапаєм помилку
        try:
            temp = self.data['main'][t_type]
        except KeyError:
            self.__log_data([request_text, measure, t_type, self.KEY_ERROR,])
            return self.KEY_ERROR
        except Exception as f:
            self.__log_data([request_text, measure, t_type, self.ERROR, f,])
            return self.ERROR
        match measure.upper():
            case 'C':
                value = round(float(temp - self.T_CONST), 1)
            case 'K':
                value = temp
            case 'F':
                value = round(float(temp - self.T_CONST), 1)*9/5 + 32
            case _:
                self.__log_data([request_text, measure, t_type, self.WRONG_T_MEASURE,])
                return self.WRONG_T_MEASURE

        output = f"{str(value)} °{measure}"

        self.__log_data([request_text, output, t_type])
        return output

    def get_weather(self, origin: str = '') -> str:
        """
        Метод get_weather - повертає поточну погоду в місті

        Приймає один аргумент:
        :param origin: звідки походить цей запит, опціонально
        """
        request_text = self.__add_origin('get_weather', origin)
        # Хапаєм помилку
        try:
            weather = self.data['weather'][0]['main']
        except KeyError:
            weather = self.KEY_ERROR
        except Exception as f:
            weather = self.ERROR, f
        self.__log_data([request_text, weather])
        return weather

    def get_speed(self, origin: str = '') -> str:
        """
        Метод get_speed - повертає швидкість вітру у м/с

        :param origin: звідки походить запит, опціонально
        """

        # Хапаєм помилку
        try:
            speed = self.data['wind']['speed']
        except KeyError:
            speed = self.KEY_ERROR
        except Exception as f:
            speed = self.ERROR, f

        request_text = self.__add_origin('get_speed', origin)
        self.__log_data([request_text, speed])
        return speed

    def get_wind(self, origin: str = '') -> str:
        """
        Метод get_wind - повертає напрямок вітру у вигляді "Північ, Південь, Захід, Схід"

        Приймає один аргумент:
        origin: звідки походить запит, опціонально
        """
        directions = ['Північ', "Захід", "Південь", "Схід"]

        # Хапаєм помилку
        try:
            deg = self.data['wind']['deg']
            direction = directions[int(round((deg / 90) % 4, 0))]
        except KeyError:
            direction = self.KEY_ERROR
        except Exception as f:
            direction = self.ERROR, f

        request_text = self.__add_origin('get_wind', origin)
        self.__log_data([request_text, direction])
        return direction

    def get_city(self, origin: str = '') -> Optional[str]:
        """
        Метод get_city - повертає назву міста.

        Приймає один аргумент:
        :param origin: звідки походить запит, опціонально
        """
        # Хапаєм помилку
        try:
            city_name = self.data['name']
        except KeyError:
            city_name = self.KEY_ERROR
        except Exception as f:
            city_name = self.ERROR, f

        request_text = self.__add_origin('get_city', origin)
        self.__log_data([request_text, city_name])
        return city_name

    def get_text(self, origin: str = '') -> str:
        """
        Метод get_text створює великий текст, у якому виводиться вся інформація,
        яку ми запитуємо з АPI у вигляді тексту з ключем та значенням

        Приймає один аргумент:
        :param origin: звідки походить цей метод, опціонально
        """

        # Дивимось, чи словник не пустий
        if self.data:
            text = []
            for key, value in self.data.items():
                text.append(f"{key}: {value}")
            output = ', \n'.join(text)
        else:
            output = self.NO_DATA

        request_text = self.__add_origin('get_text', origin)
        self.__log_data([request_text, output.replace('\n', '')])
        return output

    def show(self, measure: str = 'C', origin: str = '') -> None:
        """
        Метод show який показує інформацію про
        1. Назву міста,
        2. Температуру,
        3. Погоду,
        4. Напрямок вітру.

        Приймає два аргументи:
        :param measure: одиниця вимірювання температури, за замовчуванням 'C'
        :param origin: звідки походить метод, опціонально
        """

        city = self.get_city(origin='show')
        weather = self.get_weather(origin='show')
        temp = self.get_temp(measure=measure, origin='show')
        # Дивимось, чи всі дані обрахувало добре
        if self.__check_error([city, weather, temp, ]):
            output = self.WRONG_DATA_TYPE
        else:
            output = f"Сьогодні у {city} погода буде - {weather}. Температура за вікном - {temp}."

        request_text = self.__add_origin('show', origin)
        self.__log_data([request_text, output])
        print(output)

    def get_data(self, origin: str = '') -> dict:
        """
        Підготовлюємо всі дані для комфортної роботи зовні :)
        """
        request_text =  self.__add_origin('show', origin)
        temp_min = self.get_temp('C', 'temp_min', 'get_data')
        temp_max = self.get_temp('C', 'temp_max', 'get_data')
        feels_like = self.get_temp('C', 'feels_like', 'get_data')

        wind_direction = self.get_wind('get_data')
        wind_speed = self.get_speed('get_data')
        weather = self.get_weather('get_data')

        output = {
            'temp_min': temp_min,
            'temp_max': temp_max,
            'feels_like': feels_like,
            'wind_direction': wind_direction,
            'wind_speed': wind_speed,
            'weather': weather
        }

        self.__log_data([request_text, output])

        return output

def ai(data: dict) -> None:
    """
    Дістаємо всі потрібні дані з data, а потім виводимо відповіді аля AI
    :param data: дані для роботи
    """
    print("Штучний інтелект 'Брак' до ваших послуг! 🤖")
    print("Подивимось що тут... 👀")
    try:
        temp = data['temp_min']
        temp = float(temp[:temp.index('°')-1])
    except KeyError as f:
        print("Не знайшло дані! ⛔️", f)
    except Exception as f:
        print("Помилка! 🙅‍♂️", f)
    else:
        print("По температурі: 🌡️")
        if temp > 50:
            print("Надворі вибухнула атомна бомба. IT'S OVER 9000!!! ⚛️")
        elif 40 <= temp <= 50:
            print("Надворі дуже жарко, бережіть себе! 🔥")
        elif 30 <= temp < 40:
            print("Надворі досить тепло, саме гарний час на річку та шашлики! 🍖")
        elif 20 <= temp < 30:
            print("Надворі тепло, не забудьте взяти капелюх з собою! 🧢")
        elif 10 <= temp < 20:
            print("Надворі комфортна температура, можна взяти легку кофтину наверх 👔")
        elif 0 <= temp < 10:
            print("Надворі трохи прохолодно, вдягніть куртку! 🧥")
        elif -10 <= temp < 0:
            print("Надворі холодно! Вдягайтесь тепліше, і шапку візьміть! ❄️")
        elif -20 <= temp < -10:
            print("Надворі дуже холодно! Бережіть себе! 🥶")
        elif -30 <= temp < -20:
            print("Ліпше не виходьте з дому! 🧊")
        else:
            print("Надворі Гренландія! 🇬🇱")

    try:
        wind = data['wind_speed']
    except KeyError as f:
        print("Не знайшло дані! 🧐", f)
    except Exception as f:
        print("Помилка! 😩", f)
    else:
        print("По вітру: 💨")
        if wind < 1:
            print("Вітру немає! 😁")
        elif 1 <= wind <= 5:
            print("Легкий вітер! Потрібен легкий верхній шар для захисту 👔")
        elif 5 < wind <= 8:
            print("Середній вітер! Потрібен середній верхній шар для захисту 🧥")
        elif 8 < wind <= 12:
            print("Сильний вітер! Потрібен максимальний захист від вітру 🛡️")
        else:
            print("Тоооорнааадо!!! 🌪️")
    print("По погоді:")
    try:
        weather = data['weather']
    except KeyError as f:
        print("Не знайшло дані! 🧐", f)
    except Exception as f:
        print("Помилка! 😩", f)
    else:
        match weather:
            case 'Clouds':
                print("Хмарки! Є ризик дощу! ☁️")
            case 'Rain':
                print("Дощик! Візьміть парасольку! ☔️")
            case 'Clear':
                print('Погода чиста! Слідкуйте за сонцем! 🌞')
            case _:
                print("Погода невідома 🔬")

if __name__ == '__main__':
    origin = 'main'
    my_weather = OpenWeatherMap()
    # print(my_weather.get_text(origin=origin))
    my_weather.show(origin=origin)
    ai(my_weather.get_data(origin=origin))