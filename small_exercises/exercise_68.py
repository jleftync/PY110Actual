def fibonacci(i_int):
    lst = []
    if i_int == 1:
            return 1
    if i_int == 2:
         return 1
    for x in range(i_int + 1):
        
        if x == 0:
            continue
        if x == 1:
             lst.append(1)
        if x == 2:
            lst.append(1)
        if x > 2:
             lst.append(lst[x-3] + lst[x-2])
            
        
        
    print(lst)
    return lst[-1]
        
    
        

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True