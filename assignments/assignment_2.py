# Zahar Ambrozyak property

from typing import Optional

def task_1(number: int) -> Optional[str]:
    """
    Як вхідні дані бере ціле число.
    Якщо воно ділиться на 3, повертає "foo"; я
    Якщо воно ділиться на 5, повертає "bar";
    Якщо воно ділиться на обидва, повертає "ham".
    Інакше повертає None
    """
    if number%3 == 0 and number%5 == 0:
        return "ham"
    elif number%3 == 0:
        return "foo"
    elif number%5 == 0:
        return 'bar'
    return None

def task_2(number_1: float, number_2: float) -> str:
    """
    Як вхідні дані приймає два числа
    Повертає яке з них менше і яке більше.
    Якщо числа однакові - має бути помилка
    """
    if number_1 > number_2:
        return f"{number_1} > {number_2}"
    elif number_2 > number_1:
        return f"{number_2} > {number_1}"
    raise Exception("Ці числа рівні!")

def task_3(number_1: float, number_2: float, number_3: float) -> str:
    """
    Як вхідні дані приймає три числа
    Повертає текст з найменшим значенням, середнім та найбільшим.
    Припустимо, всі вони різні. Якщо числа однакові - має бути помилка
    """
    if number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
        raise Exception("Ці числа мають бути різними!")

    mini, midi, maxi = sorted((number_1, number_2, number_3))
    return f"Мінімальне = {mini}, середнє = {midi}, максимальне = {maxi}"

def task_4() -> tuple:
    """
    Велика закупка. Ви будуєте будинок, вам треба купити номера для
    квартир. У вашому будинку 127 квартир. Одна цифра коштує 20,79 грн.
    Якщо номер вашої квартири 102 - у вас 3 цифри. Підраховує вартість
    закупівлі та скільки яких цифр вам потрібно
    """
    k = 0
    price = 20.79
    numbers = [0 for _ in range(10)]
    for number in range(1, 128):
        for digit in str(number):
            numbers[int(digit)] += 1
            k += 1
    return k*price, numbers


a = int(input("Введіть ціле число: "))
print(task_1(a))

a,b = map(float, input("Введіть два цілих числа через пробіл: ").split())
print(task_2(a,b))

a,b,c = map(float, input("Введіть три цілих числа через пробіл: ").split())
print(task_3(a,b,c))

money, digits = task_4()
print(f"Велика закупка\n{money} грн потрібно")
for i in range(10):
    print(f"Цифра {i}: {digits[i]} штук")


