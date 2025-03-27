
def integer_to_string(inpt):
    if inpt == 0:
        return "0"
    def_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',

    }
    capture = []
    output = ""
    while inpt > 0:
        a = inpt % 10
        capture.append(a)
        inpt -= a
        inpt //= 10 
    print(capture)
    capture = capture[::-1]
    for x in capture:
        output += def_dict[x]
    print(output)
    return output
   
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")