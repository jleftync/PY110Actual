def only_alnum(inpt):
    new_str = "" 
    # for char in inpt:
    #     if char.isalnum():
    #         new_str += char
    new_str = "".join(char for char in inpt if char.isalnum())
    print(new_str)
    return new_str

def word_sizes(words):
    words_list = words.split()
    counts = {}
    for word in words_list:
        word = only_alnum(word)
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0
        
        counts[word_size] += 1
    
    return counts
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})