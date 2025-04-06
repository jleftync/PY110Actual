import  datetime

def friday_the_13ths(x):
    y = 1
    lst = []
    
    for y in range(1, 12):
        date = datetime.date(x, y, 13)
        if date.weekday() == 4:
            lst.append(date)
    return(len(lst))
    
    print(lst)


# # Check the weekday
# # Monday is 0 and Sunday is 6
#     if date.weekday() == 5:  # 5 = Saturday
#         print("March 15, 2025 is a Saturday.")
#     else:
#         print("March 15, 2025 is not a Saturday.")


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      