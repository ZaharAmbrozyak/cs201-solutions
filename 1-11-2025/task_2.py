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