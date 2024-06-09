def min_max(lst):
    """
    Calculate the minimum and maximum values in the input list and return them as a list.
    
    Parameters:
    lst (list): A list of numerical values. The list should not be empty or None.

    Returns:
    list: A list containing two elements:
          - The first element is the minimum value in the input list.
          - The second element is the maximum value in the input list.
          - If the input list is None or empty, the function returns the string "Null".

    Example:
    >>> min_max([1, 2, 3, 4, 5])
    [1, 5]
    >>> min_max([-10, 0, 10, 20])
    [-10, 20]
    >>> min_max([7])
    [7, 7]
    >>> min_max([])
    'Null'
    >>> min_max(None)
    'Null'
    """
    if lst is None or len(lst) == 0:
        return "Null"
    
    minmax = [min(lst), max(lst)]
    return minmax
