def square_sum(numbers):
    """
    Calculate the sum of the squares of the elements in the input list.

    Parameters:
    numbers (list of int/float): A list of numerical values whose squares will be summed.

    Returns:
    int/float: The sum of the squares of the elements in the input list.

    Example:
    >>> square_sum([1, 2, 3])
    14
    >>> square_sum([-1, -2, -3])
    14
    >>> square_sum([0, 4, 5])
    41
    >>> square_sum([0])
    0
    >>> square_sum([])
    0
    """
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i] ** 2)
    return sum(nums)
