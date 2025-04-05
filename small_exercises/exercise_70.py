
def fibonacci(n):
    a = []
    if n - 1 <= 1:
        
        return 1
    for x in range(n):
        if x == 0 or x == 1:
            a.append(1)
        else:
            a.append(a[x - 2] + a[x-1])
    return a[-1]

memo = {}
def fibonacci(n):
    
    if n - 1 <= 1:
        
        return 1
    elif n in memo.keys():
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]
        

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True