def task_5(n=5) -> None:
    print(' '.join([' '] + [str(i) for i in range(1, n+1)]))
    for i in range(1, n+1):
        print(str(i), end=' ')
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()

task_5(5)
