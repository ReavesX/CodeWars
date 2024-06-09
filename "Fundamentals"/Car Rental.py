def rental_car_cost(d):
    """
    Calculate the total cost of renting a car based on the number of days rented,
    applying discounts for longer rentals.

    Parameters:
    d (int): The number of days the car is rented. Must be a non-negative integer.

    Returns:
    float: The total rental cost after applying any applicable discounts.

    Pricing:
    - The base cost is $40 per day.
    - A discount of $50 is applied if the car is rented for 7 or more days.
    - A discount of $20 is applied if the car is rented for 3 to 6 days (inclusive).
    - No discount is applied for rentals less than 3 days.

    Examples:
    >>> rental_car_cost(1)
    40
    >>> rental_car_cost(4)
    140
    >>> rental_car_cost(7)
    230
    >>> rental_car_cost(10)
    350
    """


    car = 40
    total = 0  
    if d >= 7:
        total = (d * car) - 50
        return total
    elif d >= 3 and d < 7:
        total = (d * car) - 20
        return total
    else:
        total = d * car
        return total
