def basic_op(operator, value1, value2):
    """
    Args:         
        operator (str): A character representing the operation to be performed. 
                        Should be one of '+', '-', '*', or '/'.
        value1 (int or float): The first operand.
        value2 (int or float): The second operand.
    
    Returns: 
          float: The result of the mathematical operation based on the operator 

    Examples:
        >>> basic_op('+', 5, 3)
        8
        
        >>> basic_op('-', 10, 4)
        6
        
        >>> basic_op('*', 2.5, 3)
        7.5
        
        >>> basic_op('/', 10, 2)
        5.0
    """


#your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
