def is_anagram(f_string, s_string):
    a = f_string.lower()
    b = s_string.lower()
    if sorted(a) == sorted(b):
        print(True)
        return True
    print(False)
    return(False)
                                  

is_anagram('Creative', 'Reactive')
is_anagram("foefet", "toffee")
is_anagram("Buckethead", "DeathCubeK")
is_anagram("Twoo", "WooT")
is_anagram("dumble", "bumble")