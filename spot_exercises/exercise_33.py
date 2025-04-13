def alphabet_position(i_str):
    x = [y.lower() for y in i_str if y.isalpha()]
    if not x:
        return ""
    z = [str(ord(a) - 65) for a in x]
    print(" ".join(z))


alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
alphabet_position("-.-'") == ""