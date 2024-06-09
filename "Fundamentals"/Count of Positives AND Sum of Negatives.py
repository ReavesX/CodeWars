def count_positives_sum_negatives(arr):
    """
    Given an array of integers, return an array where the first element is the count of positive numbers 
    and the second element is the sum of negative numbers. 0 is considered neither positive nor negative.

    Parameters:
    arr (list): A list of integers. Can be empty or None.

    Returns:
    list: A list containing two elements:
          - The first element is an integer representing the count of positive numbers in the input array.
          - The second element is an integer representing the sum of the negative numbers in the input array.
          - Returns an empty list if the input array is empty or None.

    Example:
    >>> count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
    [10, -65]
    >>> count_positives_sum_negatives([0, -1, -2, -3, -4, 1])
    [1, -10]
    >>> count_positives_sum_negatives([])
    []
    >>> count_positives_sum_negatives(None)
    []
    """

    posCount = 0
    negSum = 0
    if arr is None or len(arr) == 0:
        return arr
    for i in range(len(arr)):
        if arr[i] < 0:
            negSum+=arr[i]
        elif arr[i] == 0:
            pass
        elif arr[i] > 0: 
            posCount+=1
    else:
        return [posCount,negSum]
