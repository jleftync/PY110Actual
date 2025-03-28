def multiplicative_average(inpt):
    z = inpt[0]
    
    for x, y in enumerate(inpt[1:]):
        z *= y
        
    a = "{:.3f}".format(z/len(inpt))
    return a

    



print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")