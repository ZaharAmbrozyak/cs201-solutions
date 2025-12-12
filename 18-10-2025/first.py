from typing import Optional

def summ(number_1: int, number_2: int) -> int: return number_1 + number_2
def dif(number_1: int, number_2: int) -> int: return number_1 - number_2
def mul(number_1: int, number_2: int) -> int: return number_1 * number_2
def power(number_1: int, number_2: int) -> int: return number_1 ** number_2

def rem(number_1: int, number_2: int) -> Optional[int]:
    try:
        return number_1 % number_2
    except ZeroDivisionError:
        print("Zero division Error")
        return None

def div(number_1: int, number_2: int) -> Optional[float]:
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        print("Zero division error")
        return None

def calculations(number_1: int, number_2: int, operation: str):
    """My dumb calculator"""
    calculator = {"+": summ, "-": dif, "*": mul, "/": div, "%": rem, "^": power}
    return calculator[operation](number_1, number_2)

a, b = map(int, input("Введіть два числа через пробіл: ").split())
operator = input("А тепер введіть операцію між цими числами (+,-,/,%,^): ")

print(f"{a} {operator} {b} = {calculations(a, b, operator)}")