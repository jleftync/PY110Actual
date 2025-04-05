import sys

sys.set_int_max_str_digits(50_000)

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

def find_fibonacci_index_by_length(inpt):
    a = 0
    while len(str(fibonacci(a))) < inpt:
        a += 1
    return a

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)