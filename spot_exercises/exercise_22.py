def scramble(f_str, s_str):
    a = list(f_str)
    b = list(s_str)
    for x in b:
        if a.count(x) < b.count(x):
            print(False)
            return False
    
    print(True)
    return True
            

    



scramble('rkqodlw', 'world') # should return True
scramble('cedewaraarossoqqyt', 'carrot') # should return True
scramble('katas', 'steak') # should return False
scramble('scriptjava', 'javascript') # should return True
scramble('scriptingjava', 'javascript') # should 