def solution(string):
    """
    Reverse the input string and return the reversed version.

    Parameters:
    string (str): The string to be reversed.

    Returns:
    str: The reversed string.

    Example:
    >>> solution("hello")
    'olleh'
    >>> solution("world")
    'dlrow'
    >>> solution("")
    ''
    >>> solution("Python")
    'nohtyP'
    """

    return string[::-1]
