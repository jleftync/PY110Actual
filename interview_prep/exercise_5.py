def most_common_char(in_string):
    lower_string = in_string.lower()
    lower_set = frozenset(list(lower_string))
    values_list = [(lower_string.count(letr), letr) for letr in lower_set]
    values_list =sorted(values_list, reverse=True)
    max_list = [valu for valu in values_list if valu[0] == max(values_list)[0]]
    if len(max_list) == 1:
        return(max_list[0][1])
    else:
        max_index = [(lower_string.index(c[1]), c) for c in max_list]
        return min(max_index)[1][1]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

