def task_14(inp='students.txt', output='honors.txt'):
    with open(inp, 'r') as f:
        text = f.readlines()
    data = {}
    for row in text:
        name, number = row.split()
        data[name] = int(number)
    print(data)

    data_filter = {name: number for name, number in data.items() if number >= 85}
    print(data_filter)
    with open(output, 'w') as f:
        f.write('\n'.join(data_filter.keys()))

task_14()