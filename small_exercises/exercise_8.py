
def string_to_integer(inpt):
    def_dict = {
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
    for x in range(len(inpt)):
        output.append(def_dict[inpt[x]])
    print(output)
   
    z = 0
    for a, b in enumerate(output):
        z += b * (10 ** a)
    print(z)
    return z






print(string_to_integer("4321") == 4321) 