class BankAccount:
  """
  A class representing a bank account with deposit, withdraw, and display balance functionalities.
  """
  def __init__(self, initial_balance=0.0):
    """
    Initializes a BankAccount object with an optional starting balance.

    Args:
      initial_balance (float, optional): The starting balance of the account. Defaults to 0.0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits a specified amount into the account balance.

    Args:
      amount (float): The amount to be deposited.
    """
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Attempts to withdraw a specified amount from the account balance.

    Returns:
      bool: True if withdrawal is successful, False otherwise.
    """
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      return False

  def display_balance(self):
    """
    Prints the current account balance in a user-friendly format.
    """
    print(f"Current Balance: ${self.account_balance:.2f}")