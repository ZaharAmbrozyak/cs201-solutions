from datetime import datetime

filename = 'search_log.csv'

def log_attempt(attempt, value_at_index, hint):
    with open(filename, 'a') as f:
        cur_date = datetime.now()
        csv_text = f"{cur_date},attempt:{attempt},value:{value_at_index},result:{hint}\n"
        f.write(csv_text)

def display_summary():
    with open(filename, 'r') as f:
        data = f.readlines()
    incorrect = 0
    for line in data:
        if 'Invalid input' in line:
            incorrect += 1
    print(f"Загальна кількість спроб: {len(data)}")
    print("Кількість 'Invalid input': " + str(incorrect))
