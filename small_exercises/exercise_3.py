def is_palindrome(s):
    return s.casefold() == s[::-1].casefold()