def task_9(hour, minute, second) -> None:
    hour_con = 0 <= hour <= 23
    minute_con = 0 <= minute <= 59
    second_con = 0 <= second <= 59
    print('Valid' if hour_con and minute_con and second_con else 'Invalid')

task_9(14, 59, 60)
task_9(23, 45, 00)
