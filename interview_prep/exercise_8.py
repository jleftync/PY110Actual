
def longest_vowel_substring(in_string):
    vowel_string = 'aeiou'
    vowel_list = [c for c in in_string if c in vowel_string]
    if len(vowel_list) == 0:
        return 0
    if len(vowel_list) == 1:
        return 1
    consec_vowel_list = []
    counter = 0
    for idx, char in enumerate(in_string):
        if idx == len(in_string) - 1 and char in vowel_string:
            counter += 1
            consec_vowel_list.append(counter)
        elif char not in vowel_string:
            consec_vowel_list.append(counter)
            counter = 0
        else:
            counter += 1


    return max(consec_vowel_list)

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)