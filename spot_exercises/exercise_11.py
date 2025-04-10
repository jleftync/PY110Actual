ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def panagram(i_string):
    f_list = list(i_string)
    s_list = list(ALPHA)
    for x in f_list:
        if x in s_list:
            s_list.remove(x)
    if s_list:
        print(False)
        return False
    else:
        print(True)
        return True





panagram("The quick brown fox jumps over the lazy dog.") # should return True
panagram("This is not a pangram.") # should return False
