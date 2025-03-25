def is_palindrome(inpt):
    """
    if the length of the string is even
    divide length of string by 2
    "".join first half
    "".join second half
    use slicing to compare first and second half reversed
    else
    subtract 1
    "".join first half
    "".join second half
    use slicing to compare first and second half reversed
    """
    comp_str = input[::-1]
    if len(inpt) % 2 == 0:
        for x in range((len(inpt))/2):
            output_str = ''.append(inpt[x])
            compare = ''.append(comp_str[x])
            if output_str == compare:
                return True
            return False
    else:
        for x in range((len(inpt) - 1)/2):
            output_str = ''.append(inpt[x])
            compare = ''.append(comp_str[x])
            if output_str == compare:
                return True
            return False
        