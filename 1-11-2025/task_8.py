def _task_8_1(num: int) -> float:
    return num*0.5*1.1
def _task_8_2(num: int) -> float:
    return (100*0.5 + (num-100)*0.75)*1.1
def _task_8_3(num: int) -> float:
    return (100*1.25+ (num-200)*1.2)*1.1
def task_8(num: int) -> None:
    if num > 200:
        print(_task_8_3(num))
    elif num > 100:
        print(_task_8_2(num))
    else:
        print(_task_8_1(num))
