def task_7(score: int) -> None:
    system={90: 'A', 80: 'B', 70: 'C', 60: 'D'}
    for i in system.keys():
        if score >= i:
            print(system[i] + ('⭐' if score >= 70 and score%2 == 0 else ''))
            return
    print('F' + ('⭐' if score%2 == 0 else ''))

task_7(82)
task_7(73)
task_7(59)