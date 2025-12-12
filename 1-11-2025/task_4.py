def task_4(n: int) -> None:
    nums = [True for _ in range(n+1)]
    nums[0] = False
    nums[1] = False
    for i in range(2, n+1):
        if nums[i]:
            for j in range(i+i, n+1, i):
                nums[j] = False

    print(', '.join([str(i) for i in range(1, n+1) if nums[i]]))

task_4(10)
