def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]


print(repr(palindrome.__doc__))
