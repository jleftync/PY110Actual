def is_balanced(i_string):
    a = i_string.count("(")
    b = i_string.count(")")

    for x in range(len(i_string)):
        if i_string[x] == ")" and "(" not in i_string[0:x+1]:
            return False
        elif i_string[x] == "(" and ")" not in i_string[x+1:]:
            return False
        elif i_string[x] == "(":
            a -= 1
            b -= 1
    if a == 0 and b == 0:
        return True
    else:
        return False



print("What (is) this?".count("("))



print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)    