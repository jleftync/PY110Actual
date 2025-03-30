def double_char(char):
    z = char + char
    return z


def repeater(strng):
    y = ""
    for x in range(len(strng)):
        y += double_char(strng[x])
    return y

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")    