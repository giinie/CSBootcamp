def search4vowels(phrase: str) -> set:
    # """Display any vowels found in an asked-for word."""
    # """Display any vowels found in a supplied word."""
    # """Return a boolean based on any vowels found."""
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    # word = input('Provide a word to search for vowels: ')
    # found = vowels.intersection(set(word))
    # for vowel in found:
    #     print(vowel)
    # return bool(found)
    # return found
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
