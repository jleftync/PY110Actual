def max_rotation(inpt):
    x = list(str(inpt))
    
    for idx, y in enumerate(x): 
        z = x.pop(idx)
        x.append(z)
    return int("".join(x))



print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)