def remove_every_other(my_list):
    """
    Return a new list containing every other element from the input list, starting with the first element.

    Parameters:
    my_list (list): A list from which to remove every other element. The list can contain any type of elements.

    Returns:
    list: A new list containing every other element from the original list, starting from the first element.

    Raises:
    ValueError: If the input list is None.

    Example:
    >>> remove_every_other([1, 2, 3, 4, 5, 6])
    [1, 3, 5]
    >>> remove_every_other(["a", "b", "c", "d", "e"])
    ["a", "c", "e"]
    >>> remove_every_other([10])
    [10]
    >>> remove_every_other([])
    []
    >>> remove_every_other(None)
    Traceback (most recent call last):
        ...
    ValueError: The List Has No Contents
    """
    if my_list is None:
        raise ValueError("The List Has No Contents")
    
    # Return a new list containing every other element
    return my_list[::2]
