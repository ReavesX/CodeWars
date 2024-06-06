def feast(beast, dish):
    """
    Determine if the first and last letters of the beast and dish match.

    Args:
        beast (str): The name of the beast.
        dish (str): The name of the dish.

    Returns:
        bool: True if the first and last letters of the beast and dish match, False otherwise.

    Examples:
        >>> feast("great blue heron", "garlic naan")
        True
        >>> feast("lazy brown bear", "apple pie")
        False
        >>> feast("python", "pasta")
        True
    """
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False
