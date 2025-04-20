def unscramble(f_string, s_string):
    
    eq_list = [c for c in s_string if s_string.count(c) <= f_string.count(c)]
    return len(s_string) == len(eq_list)

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)