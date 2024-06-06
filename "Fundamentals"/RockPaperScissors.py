def rps(p1, p2):
    """
    Determine the winner of a rock-paper-scissors game.

    Args:
        p1 (str): The choice of player 1, one of "rock", "paper", or "scissors".
        p2 (str): The choice of player 2, one of "rock", "paper", or "scissors".

    Returns:
        str: A message indicating the result of the game:
             - "Draw!" if both players chose the same
             - "Player 1 won!" if player 1 wins
             - "Player 2 won!" if player 2 wins

    Examples:
        >>> rps("rock", "scissors")
        "Player 1 won!"
        >>> rps("rock", "paper")
        "Player 2 won!"
        >>> rps("paper", "paper")
        "Draw!"
    """

      if p1 == p2:
        return "Draw!"
      if p1 == "rock" and p2 != "rock":
            if p2 == "scissors":
                return "Player 1 won!"
            else: return "Player 2 won!"
      elif p1 == "scissors" and p2 != "scissors":
            if p2 == "paper":
                return "Player 1 won!"
            else: return "Player 2 won!"
      elif p1 == "paper" and p2 != "paper":
            if p2 == "rock":
                return "Player 1 won!"
            else: return "Player 2 won!"
     

      elif p2 == "rock" and p1 != "rock":
            if p2 == "scissors":
                return "Player 1 won!"
            else: return "Player 1 won!"
      elif p2 == "scissors" and p1 != "scissors":
            if p1 == "paper":
                return "Player 2 won!"
            else: return "Player 1 won!"
      elif p2 == "paper" and p1 != "paper":
            if p1 == "rock":
                return "Player 2 won!"
            else: return "Player 1 won!"
