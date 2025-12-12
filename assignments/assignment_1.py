# Zahar Ambrozyak property

def task_1(number: int) -> int:
    """
    Як вхідні дані візьмемо ціле число; Це буде ціле число від 101 до 999, а
    його остання цифра не дорівнює нулю
    Виводить число, що складається з чисел першого у зворотному порядку.

    Наприклад: 256 → 652.
    """
    return int(str(number)[::-1])

def task_2(password: str) -> bool:
    """
    Перевірка пароля. Введіть ваш пароль. Код має повернути вам перевірку(TRUE FALSE) для наступних умов:
    a. чи має ваш пароль цифри,
    b. чи має великі літери,
    c. чи його довжина не менша за 9.
    """
    numbers = [str(i) for i in range(10)]
    letters = [chr(i) for i in range(65, 91)]
    has_numbers = True in [i in password for i in numbers]
    has_letters = True in [i in password for i in letters]
    has_len_9 = len(password) >= 9
    output = has_numbers and has_letters and has_len_9
    return output

def task_3(name: str, salary: str) -> str:
    """
    Бере на вхід ім'я користувача та місячну зарплату в доларах
    Повертає текст його річної зарплати в тисячах доларів.

    Наприклад:
    «Мішель», «12345» → «Річна зарплата Мішель складає 148 тис. доларів»
    """
    return f"Річна зарплата {name} складає {float(salary)*12/1000} тис. доларів"

def task_4(number_1: str, number_2: str) -> list:
    """
    Бере на вхід два цілих числа
    Повертає список з текстом:
    a. Їхньої суми
    b. Їхньої різниці
    c. Їхнього множення
    d. Результату поділу першого на друге
    e. Залишку від поділу першого на друге
    f. True, якщо перше число більше або дорівнює другому, інакше False.
    """
    operations = ("+", "-", "*", "/", "%", ">=")
    text_operations = ("Сума", "Різниця", "Множення", "Ділення", "Залишок від ділення", "Порівняння (>=)")
    output_4 = [f"{text_operations[i]} чисел {number_1} і {number_2} дорівнює {eval(number_1 + operations[i] + number_2)}" for i in range(6)]
    return output_4

input_1 = int(input("Введіть ціле число від 101 до 999: "))
print(task_1(input_1))

input_2 = input("\nТепер введіть пароль\nВін мусить містити цифри, великі літери та довжину хоча-б з 9 символів: ")
print(task_2(input_2))

my_name, my_salary = input("\nТепер введіть ім'я та ЗП через пробіл: ").split(" ")
print(task_3(my_name, my_salary))

a, b = input("\nТепер введіть два числа через пробіл: ").split(" ")
for text in task_4(a, b):
    print(text)