def check_range(num: int, low: int, upper: int) -> str:
    """
    Check if Number Falls Within a Given Range
    Example:
    check_range(5, 1, 10) → True
    check_range(15, 1, 10) → False
    check_range(5, 10, 1) → False, wrong range
    """
    if low <= upper:
        if num in range(low, upper):
            return "True"
        return "False"
    return "False, wrong range"

def unique_list(list_to_change: list) -> list:
    """
    Returns a New List with Distinct Elements
    returns a new list with only unique elements (removing duplicates).

    Example:
    Input : [1,2,3,3,3,3,4,5]
    Output: [1, 2, 3, 4, 5]
    """
    return list(set(list_to_change))

def if_a_palindrome(text: str) -> bool:
    """
    Checks if a String is a Palindrome

    Examples:

    "madam" → True
    "nurses run" → True
    "python" → False
    """
    text = text.replace(' ','')
    return text[::-1] == text

def bold_tag(text: str) -> str:
    """
    wraps text in <b>...</b>
    """
    return f"<b>{text}</b>"

def italic_tag(text: str) -> str:
    """
    wraps text in <i>...</i>
    """
    return f"<i>{text}</i>"

def underline(text: str) -> str:
    """
    wraps text in <u>...</u>
    """
    return f"<u>{text}</u>"

task_1 = "Введіть ціле число, ліве число діапазону та \nправе число діапазону через пробіл: "
number, left, right = map(int, input(task_1).split())
print(check_range(number, left, right))

task_2 = "Введіть довільний список чисел через кому: "
my_list = [int(i) for i in input(task_2).split(sep=',')]
print(unique_list(my_list))

task_3 = "Введіть довільний текст на перевірку паліндрому"
my_text = ''.join([i for i in input(task_3) if i != " "])
print(if_a_palindrome(my_text))

task_4 = "Введіть довільний текст:"
my_text = input(task_4)
print(bold_tag(my_text))
print(italic_tag(my_text))
print(underline(my_text))