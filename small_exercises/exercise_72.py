'''
Return 3 percentages as strings in dictionary form, the percentage of characters in the string uppercase,
percent lowercase, and percent neither

strings should include 2 places past the decimal
we do not need to cover the case of empty string


'''
def letter_percentages(str_chars):
    list_of_keys = ['lowercase', 'uppercase', 'neither']
    lower_count = sum(1 for char in str_chars if char.islower())
    upper_count = sum(1 for char in str_chars if char.isupper())
    neither_count = len(str_chars) - (upper_count + lower_count)
    count_list = [lower_count, upper_count, neither_count]
    value_list = [f"{round((x / len(str_chars) * 100), 2):.2f}" for x in count_list]
    return dict(zip(list_of_keys, value_list))




expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)