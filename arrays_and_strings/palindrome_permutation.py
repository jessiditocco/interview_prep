def is_palindrome_permutation(str):
    """Given a string, check whether the stirng is a permutation of a palindrome
    >>> is_palindrome_permutation("Tact Coa")
    True

    >>> is_palindrome_permutation("eheh")
    True

    >>> is_palindrome_permutation("ehehh")
    True

    >>> is_palindrome_permutation("abcdefab")
    False

    >>> is_palindrome_permutation("ehhheh")
    True

    >>> is_palindrome_permutation("taco cat")
    True

    >>> is_palindrome_permutation("atco aaadfcta")
    False
    """

    char_count = {}

    odd_num_chars = 0

    lowercase_str = str.lower()

    for char in lowercase_str:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    for char in char_count:
        if char_count[char] % 2 != 0:
            odd_num_chars += 1

        if odd_num_chars > 1:
            return False

    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "All tests passed!!!"