
def is_pangram(in_string):
    alpha_str = 'abcdefghijklmnopqrstuvwxyz'
    alpha_list = list(alpha_str)
    for chr in in_string:
        if chr in alpha_str:
            for x in alpha_list:
                if x == chr:
                    alpha_list.remove(x)
    if bool(alpha_list) == True:
        return False
    else:
        return True
            


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)