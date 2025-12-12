def task_1(nu: int) -> None:
    neg = False
    if nu < 0:
        neg = True
    num = abs(nu)
    if neg:
        print('-',end='')
    while num > 0:
        n = num%10
        num = num//10
        print(n, end='')
    print()

task_1(12345)
