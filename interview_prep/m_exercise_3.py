
def to_weird_case(inp_string):
    word_list = inp_string.split()
    words_to_change = word_list[2::3]
    updated_words = []
    for word in words_to_change:
        updated_words.append("".join(c.upper() if idx % 2 == 1 else c for idx, c in enumerate(word)))
    
    for x, y in zip(range(2, len(word), 3), updated_words):
        word_list[x] = y
    



original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
to_weird_case(original)