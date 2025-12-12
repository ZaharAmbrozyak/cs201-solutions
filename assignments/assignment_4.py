# Zahar Ambrozyak property
def find_primes(a: int = 2, b: int = 100) -> list[int]:
    """
    Функція з назвою find_primes, яка приймає два цілі
    числа a і b і повертає список всіх простих чисел між a і b
    (включно).

    :param a:
    :param b:
    """
    numbers = [True for _ in range(b)]
    numbers[0] = False  # 0 - не просте число
    numbers[1] = False  # 1 - не просте число
    primes = []
    for i in range(2, b):
        if numbers[i]:
            if a <= i <= b:
                primes.append(i)
            for j in range(i * i, b, i):
                numbers[j] = False
    return primes


print(find_primes(1, 1000))  # -> [31, 37, 41, 43, 47]


def unique_characters(s: str = 'Serafym') -> bool:
    """
    Напишіть функцію з назвою unique_characters,
    яка приймає рядок s і повертає логічне значення, яке
    вказує, чи всі символи в рядку s унікальні.
    Наприклад:
    рядок "abcdefg" має унікальні символи (поверне True)
    але рядок "abcdeff" - ні (поверне False)
    :param s:
    """
    characters = []

    # Вважаємо, що S та s - це різні символи
    for i in s:
        if i in characters:
            return False
        characters.append(i)
    return True


print(unique_characters('abcdefg'))  # -> True
print(unique_characters('abcdeff'))  # -> False


def fibonachi(n: int = int(input("Введіть к-сть ітерацій: "))) -> str:
    """
    Функція, яка розраховує Послідовність Фібоначчі.
    Кількість ітерацій визначається користувачем,
    тобто аргумент функції - кількість ітерацій при розрахунку послідовності.
    :param n:
    """
    a, b = 0, 1
    output = ['1', ]
    for _ in range(0, n - 1):
        a, b = b, a + b
        output.append(str(b))
    return ', '.join(output) if n > 0 else ''


print(fibonachi())


def sw_case(s: str = 'Аль-Патов') -> str:
    """
    Функція, яка реалізує заміну регістру.
    Повертає той самий результат, що й метод swapcase().
    Функція має приймати один аргумент str і перетворювати всі
    значення нижнього регістру у верхній регістр і навпаки.
    Не можна використовувати метод swapcase()
    :param s:
    """
    # різниця між великим і малим символом = 32
    # малі символи лежать в діапазоні [97;122] (eng), або [1072;1103] (ukr)
    # великі символи лежать в діапазоні [65;90] (eng), або [1040;1071] (ukr)
    output = []
    for i in [ord(j) for j in s]:
        if 97 <= i <= 122 or 1072 <= i <= 1103:  # мала літера
            output.append(chr(i - 32))
        elif 65 <= i <= 90 or 1040 <= i <= 1071:  # велика літера
            output.append(chr(i + 32))
        else:
            output.append(chr(i))
    return ''.join(output)


print(sw_case('123__SeRaFyM__456'))  # -> 123__sErAfYm__456
print('123__SeRaFyM__456'.swapcase())  # -> 123__sErAfYm__456

symbol_cases = [(97, 122), (1072, 1103), (91, 96),
                (58, 64), (123, 126), (127, 191),
                (65, 90), (1040, 1071), (48, 57)]


def encrypt(text: str = 'Це ж було вже!', rng: int = 1) -> str:
    """
    Функція шифрування має приймати
    повідомлення та значення зсуву як аргументи
    :param text:
    :param rng:
    """

    output = []

    for i in [ord(j) for j in text]:
        bad = True
        for lower, upper in symbol_cases:
            # входить до якогось сімейства букв
            if lower <= i <= upper:
                output.append(chr(i + (rng % (upper - lower + 1)) if lower <= i + (
                            rng % (upper - lower + 1)) <= upper else lower + i + (
                            rng % (upper - lower + 1)) - upper - 1))
                bad = False
                break
        # якщо хтось вирішив закодувати китайські ієрогліфи, то ми їх залишаємо
        if bad:
            output.append(chr(i))

    return ''.join(output)


def decrypt(text: str = encrypt(), rng: int = 1) -> str:
    """
    Функція дешифрування має приймати зашифроване повідомлення
    та те саме значення зсуву як аргументи

    :param text:
    :param rng:
    """

    output = []

    for i in [ord(j) for j in text]:
        bad = True
        for lower, upper in symbol_cases:
            # входить до якогось сімейства букв
            if lower <= i <= upper:
                output.append(chr(i - (rng % (upper - lower + 1)) if lower <= i - (
                            rng % (upper - lower + 1)) <= upper else upper + 1 - (
                            lower - (i - (rng % (upper - lower + 1))))))
                bad = False
                break

        # якщо хтось вирішив закодувати китайські ієрогліфи, то ми їх залишаємо
        if bad:
            output.append(chr(i))

    return ''.join(output)


my_rng = 2
my_text = 'aZaAаБвВЯяЯ'
schypr = encrypt(text=my_text, rng=my_rng)
print(schypr)
print(decrypt(schypr, rng=my_rng))
