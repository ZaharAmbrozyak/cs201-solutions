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