def digitize(n):
    """
    Args:   
            n (int), any integer
    
    Returns: 
            arr (array), the integer reversed 
    
    Example:
        digitize(35231) => [1,3,2,5,3]

    """

  
    arr = [int(x) for x in str(n)]
    return arr[::-1]
