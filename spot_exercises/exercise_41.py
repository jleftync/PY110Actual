def duplicate_count(i_string):
    f_set = set(list(i_string.lower()))
    
    counter = 0
    if not i_string:
        print(0)
        return 0
    for x in f_set:
        if i_string.lower().count(x) > 1:
            counter += 1
    print(counter)
    return counter





duplicate_count("") == 0
duplicate_count("abcde") == 0
duplicate_count("abcdeaa") == 1
duplicate_count("abcdeaB") == 2
duplicate_count("Indivisibilities") == 2