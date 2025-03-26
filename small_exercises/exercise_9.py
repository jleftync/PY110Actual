def string_to_signed_integer(inpt):
    h = 0
    def_dict = {
        "+": "+",
        "-": "-",
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,

    }
    output = []
    inpt = inpt[::-1]
    if inpt[-1] not in ["+", "-"]:
        for x in range(len(inpt)):
            output.append(def_dict[inpt[x]])
        print(output)
    elif inpt[-1] == "+":
        for x in range(len(inpt) - 1):
            output.append(def_dict[inpt[x]])
        print(output)
    else:
        for x in range(len(inpt) - 1):
            output.append(def_dict[inpt[x]])
        print(output)
        h += 1

    z = 0
    if h == 1:
        for a, b in enumerate(output):
            z += b * (10 ** a)
        z *= -1
        print(z)
        return z

    for a, b in enumerate(output):
        z += b * (10 ** a)
        
    print(z)
    return z




print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)  