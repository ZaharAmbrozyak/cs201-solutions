class Calculator:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b
    def sum(self) -> float:
        return self.a + self.b
    def sub(self) -> float:
        return self.a - self.b
    def div(self) -> float:
        try:
            return self.a/self.b
        except ZeroDivisionError:
            raise ZeroDivisionError("Не можна ділити на нуль")
    def mul(self) -> float:
        return self.a*self.b
    def __str__(self):
        return "a = " + str(self.a) + ', ' + "b = " + str(self.b)
my_calculator = Calculator(5, 10)

print(my_calculator.sum())
print(my_calculator.sub())
print(my_calculator.div())
print(my_calculator.mul())
print(my_calculator)