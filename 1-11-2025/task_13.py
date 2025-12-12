def task_13():

    def inner(first, last, middle=''):
        if middle:
            return f"{last}, {first} {middle}"
        return f"{last} {first}"

    return inner

format_name = task_13()
print(format_name('John', 'Smith'))
print(format_name('John', 'Smith', 'M.'))
