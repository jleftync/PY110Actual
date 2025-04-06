def next_featured(inpt):
    if inpt > 9876543200:
        return "There is no number that fulfills those requirements"
    
    x = ((inpt // 7) + 1) * 7
    while True:
        
        if len(set(list(str(x)))) == len(list(str(x))):
            if x % 2 == 1:
                print(x)
                return x
        x += 7

                
        
        
    

        
    

    
    # feat_lst = []
    # counter = 0

    # for num in range(1, 1410934743):
    #     num = num * 7
    #     for idx, char in enumerate(list(str(num))):
    #         if char in list(str(num))[idx+1:]:
    #             counter += 1
    #             break
    #     if counter == 0:
    #         feat_lst.append(num)
    #     counter = 0
    # for idx, x in enumerate(feat_lst):
    #     if inpt >= x:
    #         continue
    #     else:
    #         return x
    
                




print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)