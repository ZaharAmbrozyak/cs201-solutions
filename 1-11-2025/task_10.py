def task_10(*numbers) -> list:
    output = []
    for number in numbers:
        if number%2 == 0:
            output.append(number**2)
    return output

task_10(1, 2, 3, 4, 5, 6)