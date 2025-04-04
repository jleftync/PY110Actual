def word_to_digit(words):
    out_list = []
    for token in words.split():
        match token:
            case "one":
                out_list.append("1")
            case "two":
                out_list.append("2")
            case "three":
                out_list.append("3")
            case "four":
                out_list.append("4")
            case "five":
                out_list.append("5")
            case _:
                out_list.append(token)
    out_str = " ".join(out_list)
    print(out_str)
    return out_str


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True