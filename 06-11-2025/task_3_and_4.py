import task_4

def my_game():
    from random import choice
    numbers = range(1, 1001)
    i = 0
    my_list = []
    while i < 50:
        my_choice = choice(numbers)
        if my_choice not in my_list:
            my_list.append(my_choice)
            i += 1

    my_list.sort()
    target = choice(range(0, 50))
    tries = 0
    win_con = True

    while win_con and tries < 6:
        try:
            my_choice = int(input("Індекс від 0 до 49: "))
        except ValueError:
            print("Це не число")
            tries += 1
            task_4.log_attempt(tries, None, 'Invalid input')
            continue
        try:
            my_number = my_list[my_choice]
        except IndexError:
            print("Ви вийшли за рамки індексів 0-49")
            tries += 1
            my_number = None
            task_4.log_attempt(tries, my_number, 'Invalid input')
            continue
        if my_choice == target:
            print("Перемога :)")
            tries += 1
            task_4.log_attempt(tries, my_number, 'Correct')
            win_con = False
        elif my_choice > target:
            print("Беріть менший індекс")
            tries += 1
            task_4.log_attempt(tries, my_number, 'Too high')
        else:
            print("Беріть більший індекс")
            tries += 1
            task_4.log_attempt(tries, my_number, 'Too low')

    if win_con:
        print("Зрада :(")

my_game()
task_4.display_summary()