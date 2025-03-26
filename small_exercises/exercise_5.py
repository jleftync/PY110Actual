def word_sizes(inpt):
    if bool(inpt) == False:
        return {}
    outpt = {}
    inlst = inpt.split(" ")
    wrd_sz_set = []
    wrd_cnt_lst = []
    len_lst = []
    check_lst = []
    
    for y in inlst:    
        len_lst.append(len(y))
    
    for x in len_lst:
        if x not in check_lst: 
            wrd_cnt_lst.append(len_lst.count(x))
        check_lst.append(x)

    for w in inlst:
        if len(w) not in wrd_sz_set:
            wrd_sz_set.append(len(w))
    wrd_sz_set = list(wrd_sz_set)
    
    outpt = {wrd_sz_set[x]: wrd_cnt_lst[x] for x in range(len(wrd_sz_set))}
    print(outpt)
    return outpt




string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})