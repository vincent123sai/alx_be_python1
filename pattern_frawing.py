def main():
  """
  This function prompts the user for a size and draws a square pattern with asterisks.
  """
  # Get user input for pattern size
  while True:
    try:
      size = int(input("Enter the size of the pattern (positive integer): "))
      if size <= 0:
        print("Please enter a positive integer.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Draw the pattern using nested loops
  for i in range(size):
    for j in range(size):
      print("*", end="")
    print()  # Move to the next line after each row

if __name__ == "__main__":
  main()