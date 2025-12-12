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

def task_2(stri: str) -> None:
    import string

    let = 0
    dig = 0
    oth = 0
    for i in stri:
        if i.lower() in string.ascii_letters:
            let += 1
        elif i in string.digits:
            dig += (1 if i in string.digits else 0)
        else:
            oth += 1
    print('Letters: ' + str(let))
    print('Digits: ' + str(dig))
    print('Others: ' + str(oth))

task_2('Hello123!')

def task_3(n: int = 4) -> None:
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*i + '*'*(i-1) + ' '*(n-i))

task_3(4)

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

def task_5(n=5) -> None:
    print(' '.join([' '] + [str(i) for i in range(1, n+1)]))
    for i in range(1, n+1):
        print(str(i), end=' ')
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()

task_5(5)

def task_6(year: int) -> None:
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print('Leap year')
    else:
        print("Not a leap year")

task_6(2000)
task_6(1900)

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

def task_9(hour, minute, second) -> None:
    hour_con = 0 <= hour <= 23
    minute_con = 0 <= minute <= 59
    second_con = 0 <= second <= 59
    print('Valid' if hour_con and minute_con and second_con else 'Invalid')

task_9(14, 59, 60)
task_9(23, 45, 00)

def task_10(*numbers) -> list:
    output = []
    for number in numbers:
        if number%2 == 0:
            output.append(number**2)
    return output

task_10(1, 2, 3, 4, 5, 6)

def task_11(sentence: str) -> None:
    text = sentence.split()
    output = {word: len(word) for word in text if len(word)}
    print(output)
    print(', '.join([word for word, leng in output.items() if leng > 3]))

task_11('I love Python very much')

def task_12(inp='input.txt', output='summary.txt') -> None:
    with open(inp, 'r') as f:
        data = f.read()

    characters = f"Characters: {len(data)}"
    lines = f"Lines: {data.count('\n') + 1}"
    words = f"Words: {data.count(' ')}"
    out = '\n'.join((characters, lines, words))

    with open(output, 'w') as f:
        f.write(out)

task_12()

def task_13():

    def inner(first, last, middle=''):
        if middle:
            return f"{last}, {first} {middle}"
        return f"{last} {first}"

    return inner

format_name = task_13()
print(format_name('John', 'Smith'))
print(format_name('John', 'Smith', 'M.'))

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

def task_15():
    inventory = {
        'fruits': {
            'apple': 10,
            'banana': 5,
            'orange': 8
        },
        'drinks': {
            'water': 20,
            'juice': 10,
            'soda': 6
        }
    }
    inputs = []
    while True:
        name = input("Product name: ")
        quantity = float(input("Quantity: "))
        if name and quantity:
            inputs.append((name, quantity))
        else:
            break
    purchases = []
    i = 1
    for name, quantity in inputs:
        for category in inventory.keys():
            if name in inventory[category].keys() and \
                inventory[category][name] <= quantity:
                purchases.append((name, i, quantity))
                inventory[category][name] -= quantity
            else:
                print("Sorry, we don't have in in stock")
        i += 1

task_15()

def task_16():

    def calc(operation: str, *args, precision: int = 2, **options) -> float:
        match operation:
            case 'add':
                output = 0
                for arg in args:
                    output += arg
            case 'mul':
                output = 1
                for arg in args:
                    output *= arg
            case 'avg':
                output = 0
                for arg in args:
                    output += arg
                output /= len(args)
            case _:
                raise ValueError('Unknown operation')
        match options:
            case {'negative': True}:
                return round(output*(-1), precision)
            case {'negative': False} | {}:
                return round(output, precision)
            case _:
                raise ValueError('Unknown operation')
    return calc

calculate = task_16()

print(calculate('add', 2, 3, 5, prec=1))
print(calculate('mul', 2, 3, negative=True))
print(calculate('avg', 4, 8, 10, precision=3))
