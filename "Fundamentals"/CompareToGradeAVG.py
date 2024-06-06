import numpy as np

def better_than_average(class_points, your_points):
    """
    Determine if your points are better than the class average.

    Args:
        class_points (list): A list of integers representing the points of all students in the class.
        your_points (int): Your points.

    Returns:
        bool: True if your points are better than the class average, False otherwise.

    Examples:
        >>> better_than_average([70, 80, 90], 85)
        True
        >>> better_than_average([60, 50, 40], 55)
        True
        >>> better_than_average([80, 75, 70], 65)
        False
    """

    
    if np.mean(class_points) < your_points:
        return True
    else:
        return False
