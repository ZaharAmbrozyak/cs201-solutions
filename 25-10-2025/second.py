def check_card(card: str) -> bool:
    """
    4441 1144 6436 2878
    """
    num_list = [int(i) for i in card if i != " "]
    if len(num_list) < 16:
        return False

    s = 0
    for i in range(16):
        if i%2 == 0:
            if num_list[i]*2 >= 10:
                s += (num_list[i]*2-9)
            else:
                s += (num_list[i]*2)
        else:
            s += num_list[i]
    return s%10 == 0

serafym_card_number = "4441 1144 6436 2878"

print(check_card(serafym_card_number))

