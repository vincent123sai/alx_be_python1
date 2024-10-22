def safe_divide(numerator, denominator):
  """
  Divides two numbers, handling division by zero and non-numeric input errors.

  Args:
    numerator (str): The numerator value (to be converted to float).
    denominator (str): The denominator value (to be converted to float).

  Returns:
    str: A message indicating the result or the encountered error.
  """
  try:
    # Attempt conversion to floats
    numerator = float(numerator)
    denominator = float(denominator)
    # Perform division
    result = numerator / denominator
    return f"The result of the division is {result:.2f}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Please enter numeric values only."


import sys
from robust_division_calculator import safe_divide

def main():
  """
  Handles user input and calls the safe_divide function for division with error handling.
  """
  if len(sys.argv) != 3:
    print("Usage: python main.py <numerator> <denominator>")
    sys.exit(1)

  numerator = sys.argv[1]
  denominator = sys.argv[2]

  result = safe_divide(numerator, denominator)
  print(result)

if __name__ == "__main__":
  main()
  