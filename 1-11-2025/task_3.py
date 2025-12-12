def task_3(n: int = 4) -> None:
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*i + '*'*(i-1) + ' '*(n-i))

task_3(4)