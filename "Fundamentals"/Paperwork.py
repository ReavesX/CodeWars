def paperwork(n, m):
    """
    Calculate the product of two numbers if they are both greater than 0.

    Args:
        n (int): The first number.
        m (int): The second number.

    Returns:
        int: The product of n and m if both n and m are greater than 0, otherwise returns 0.
    """
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
