# Zahar Ambrozyak property

from random import randint, choice

def generate(bottom=60, top=100, count=6) -> tuple:
    """
    Напишіть програму, яка використовує модуль рандом та випадковим
    чином генерує оцінки кожного учня і те, чи здав він іспит.
    Потім програмі необхідно надрукувати дві речі:
    a. Чи був професор Грубл послідовним у проставленні позначки
    "Passed" для студентів.
    b. Якщо професор Грубл був послідовним, виведіть діапазон у
    якому знаходиться поріг для складання іспиту.
    """

    decisions = ("Passed", "Failed")
    grades = [randint(bottom, top) for _ in range(count)]
    validation = [choice(decisions) for _ in range(count)]
    print(grades)
    print(validation)
    if 'Passed' in validation:
        if 'Failed' in validation:
            max_grade_fail = bottom-1
            min_grade_pass = top+1
            for i in range(count):
                if max_grade_fail < grades[i] and validation[i] == "Failed":
                    max_grade_fail = grades[i]
                elif min_grade_pass > grades[i] and validation[i] == 'Passed':
                    min_grade_pass = grades[i]
            print('max_fail:', max_grade_fail)
            print('min_pass:', min_grade_pass)
            if max_grade_fail >= min_grade_pass:
                return "Не послідовний", (None, None)
            grades_sorted = sorted(grades)
            _range = grades_sorted[grades_sorted.index(max_grade_fail)+1], grades_sorted[-1]
            return "Послідовний", _range
        else:
            return 'Послідовний', (min(grades), max(grades))
    else:
        return 'Послідовний', ("Діапазон", 'невідомий')

my_decision, my_range = generate()
print(my_decision + (', ' + '-'.join([str(i) for i in my_range]) if my_range != (None, None) else ''))