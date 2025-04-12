def generate_hashtag(i_string):
    x = i_string.split()
    if not x or len(x) > 140:
        print(False)
        return False
    else:

        print(f"#{"".join([y.capitalize() for y in x])}")


generate_hashtag("")                       # should return `False`
generate_hashtag(" " * 200)                # should return `False`
generate_hashtag("Do We have A Hashtag")   # should return "#DoWeHaveAHashtag"
generate_hashtag("Nice To Meet You")       # should return "#NiceToMeetYou"
generate_hashtag("this is a test")         # should return "#ThisIsATest"
generate_hashtag("this is a very long string" + " " * 140 + "end")  # should return "#ThisIsAVeryLongStringEnd"
generate_hashtag("a" * 139)                # should return "#A" + "a" * 138
generate_hashtag("a" * 140)          