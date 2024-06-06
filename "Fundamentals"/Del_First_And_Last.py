def remove_char(str):
    """
    Remove the first and last characters from a string.

    Args:
        str (str): The input string.

    Returns:
        str: The input string with the first and last characters removed.

    Examples:
        >>> remove_char("hello")
        'ell'
        >>> remove_char("python")
        'ytho'
        >>> remove_char("abc")
        'b'
    """
    return str[1:-1]
