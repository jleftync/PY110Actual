def longest(i_str):
    o_str = ""
    counter = 1
    f_list = list(i_str)
    if len(f_list) == 1:
        print(f_list[0])
        return f_list[0]
    for idx, x in enumerate(f_list):
        # 
        hold_str = ""
        for z in range(len(f_list[idx:])):
            if sorted(f_list[idx:idx+z-1]) == f_list[idx:idx+z-1]:
                hold_str = "".join(f_list[idx:idx+z-1])
                if len(hold_str) > len(o_str):
                    o_str = hold_str
                
        if len(o_str) > len(f_list[idx:])/2:
            print(o_str)
            return o_str
    print(o_str)
    return o_str

longest('asd')                  # should return 'as'
longest('nab')                  # should return 'ab'
longest('abcdeapbcdef')         # should return 'abcde'
longest('asdfaaaabbbbcttavvfffffdf') # should return 'aaaabbbbctt'
longest('asdfbyfgiklag')        # should return 'fgikl'
longest('z')                    # should return 'z'
longest('zyba')                 # should return 'z'