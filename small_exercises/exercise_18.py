


def add_to(a, b, c):
    c.append(a*b)
    return c

def multiply_list(inpt_1, inpt_2):
    output = []
    for x in range(len(inpt_1)):
        add_to(inpt_1[x], inpt_2[x], output)
    
    return output

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])