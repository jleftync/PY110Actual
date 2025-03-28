def helper(chr, lst):
    chr = int(chr)
    lst.append(chr)
    return lst

def digit_list(inpt):
    output = []
    inpt = str(inpt)
    print(inpt)
    while inpt:
        a = inpt[-1]
        inpt = inpt[:-1]
        helper(a, output)
    output = output[::-1]
    return output



print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])         