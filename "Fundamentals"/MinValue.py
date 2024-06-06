def find_smallest_int(arr):
    """
    Find the smallest integer in a list.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The smallest integer in the list.

    Examples:
        >>> find_smallest_int([4, 7, 2, 9, 1])
        1
        >>> find_smallest_int([-3, -8, -2, -5])
        -8
        >>> find_smallest_int([0, 5, 3, 2, 1])
        0
    """
    for x in range(0, len(arr)):
        return min(arr)
