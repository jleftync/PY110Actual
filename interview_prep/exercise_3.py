
def to_weird_case(input_string):
    word_list = input_string.split()
    change_word_list = word_list[2::3]
    updated_words = []
    for word in change_word_list:
        updated_words.append("".join(c.upper() if idx % 2 == 1 else c for idx, c in enumerate(word)))
    
    for i, newval in zip(range(2, len(word_list), 3), updated_words):
        word_list[i] = newval
    return " ".join(word_list)
    # changed_words = [list(word) for word in change_word_list]
    # for letter in changed_words:
    #     for chara in letter[1:0:2]:
    #         chara.upper()
    # altered_words = ["".join(letra) for items in changed_words for letra in items]
    # print(altered_words)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)
