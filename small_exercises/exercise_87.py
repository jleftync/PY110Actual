from fractions import Fraction

"""
1. first a function to create an Egyptian function
an egyption fraction is a method by which you represent a numer as a sum of fractions
to this end we will 
2. generate a list of numbers beginning with 1 and moving up
we will divide 1 by the first digit, 
3. check to see if that number is less than the 
fraction represented.  
4. If yes, we will add the dominator to the list.  
5. We will then continue incrementing the number, likely with a while loop and adding 1/n to the previous total and checkign
if the sum total is equal the the target number
6.  If equal return the list
7. if less than increment and add denonminator to the list
8.  if greater than do not augment and check again check again
1
"""
def egyptian(i_Fraction):
    out_lst = [1]
    counter = 1
    while True:
        egypt_value = sum([1/x for x in out_lst])
        if egypt_value == i_Fraction:
            return out_lst
        if egypt_value > i_Fraction:
            out_lst.pop()
            counter += 1
            out_lst.append(counter)
        if egypt_value < i_Fraction:
            counter += 1
            out_lst.append(counter)
def unegyptian(e_fraction):
    return sum([1/x for x in e_fraction])
        
# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))