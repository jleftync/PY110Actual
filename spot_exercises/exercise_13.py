def kebabize(i_string):
    f_list = list(i_string)
    s_list = [x for x in f_list if x.isalpha()]
    for idx, char in enumerate(s_list):
        if char.isupper():
            s_list[idx] = s_list[idx].replace(char, char.lower())
            s_list.insert(idx, "-")
    print("".join(s_list))
    return "".join(s_list)
            
    



kebabize('camelsHaveThreeHumps') # should return 'camels-have-three-humps'
kebabize('myCamelHas3Humps') # should return 'my-camel-has-humps'