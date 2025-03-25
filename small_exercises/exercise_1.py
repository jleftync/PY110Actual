lst = []
lst.append(input("Enter the 1st number: "))
lst.append(input("Enter the 2nd number: "))
lst.append(input("Enter the 3rd number:")) 
lst.append(input("Enter the 4th number: "))
lst.append(input("Enter the 5th number: "))
lst.append(input("Enter the last number: "))

if lst[-1] in lst[0:-2]:
    print(f"{lst[-1]} is in{[",".join(i) for i in lst[0:-1]]}.")
else:
    print(f"{lst[-1]} is not in{[",".join(i) for i in lst[0:-1]]}.")