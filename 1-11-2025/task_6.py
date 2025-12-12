def task_6(year: int) -> None:
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print('Leap year')
    else:
        print("Not a leap year")

task_6(2000)
task_6(1900)