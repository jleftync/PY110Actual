def transactions_for(inpt_1, in_lst):
    return [in_lst[x] for x in range(len(in_lst)) if inpt_1 in in_lst[x].values()]

def is_item_available(i_int, tranctn):
    x = transactions_for(i_int, tranctn)
    y = 0
    for z in range(len(x)):
        if x[z]["movement"] == 'in':
            y += x[z]['quantity']
        else:
            y -= x[z]['quantity']
    
    if y > 0:
        return True
    else:
        return False


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True