def helper_functn(i_str):

    if i_str == i_str[::-1] and len(i_str) >= 2:
        return i_str

def palindromes(i_str):
    i_list = list(i_str)
    
    lst = []
    while i_list:
        lst.extend(["".join(i_list[:y+1]) for y in range(len(i_str))])
        i_list.pop(0)
        i_str = i_str[1:]
    
    return [x for x in lst if helper_functn(x)]
    
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True