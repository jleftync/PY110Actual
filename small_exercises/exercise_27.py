def double_char(char):
    if char.isalpha() and char.lower() not in ('aeiou'):
        z = char + char
        return z
    return char


def double_consonants(strng):
    y = ""
    for x in range(len(strng)):
        y += double_char(strng[x])
    return y

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")