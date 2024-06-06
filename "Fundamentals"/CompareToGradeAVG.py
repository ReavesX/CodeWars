import numpy as np
def better_than_average(class_points, your_points):
    # Your code here
    if np.mean(class_points) < your_points:
        return True
    else: return False
