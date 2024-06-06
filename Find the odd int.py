def find_it(seq):
    """
    Finds the element that occurs an odd number of times in the given sequence.

    Args:
        seq (list): The input sequence.

    Returns:
        int: The element that occurs an odd number of times.
    
    Example:
        [7]
        [0] s
        [1,1,2]
        [0,1,0,1,0]
        [1,2,2,3,3,3,4,3,3,3,2,2,1]
    """
    
    # First attempt / Brute force
   
    occurrences = {}
    for item in seq:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    
    for key, value in occurrences.items():
        if value % 2 != 0:
            return key
