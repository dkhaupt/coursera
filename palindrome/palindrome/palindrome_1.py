def reverse(s):
    """ (str) -> str
    return a reversed version of s
    """
    rev = ''
    for char in s:
        rev = char + rev

    return rev