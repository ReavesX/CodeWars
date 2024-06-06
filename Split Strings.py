def SplitByTwoChars(s):
    """
    Splits a given string into pairs of two characters. If the string contains an odd number 
    of characters, it appends an underscore '_' to the last pair to make it complete.

    Args:
        s (str): The input string to be split into pairs. For example, "Day Night Cycle".

    Returns:
        list: A list of strings, each containing a pair of characters from the input string.

    Example:
        >>> solution("abcdefgh")
        ['ab', 'cd', 'ef', 'gh']
        >>> solution("abcde")
        ['ab', 'cd', 'e_']
        
    """
    arr = [x for x in s]
    arr2 = [] 
  
    if len(arr) % 2 != 0:
        oddchar = "_"
        arr.append(oddchar)
        
    for i in range(0, len(arr), 2):
        arr2.append(arr[i] + arr[i+1])
    return arr2
