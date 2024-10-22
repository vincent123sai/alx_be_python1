def main():
  """
  This function prompts for a task, its priority, and time sensitivity and provides a reminder.
  """
  # Get user input for the task
  task = input("Enter your task: ")

  # Get user input for task priority
  while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
      break
    else:
      print("Invalid priority. Please enter high, medium, or low.")

  # Get user input for time sensitivity
  while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
      break
    else:
      print("Invalid input. Please enter yes or no.")

  # Create a reminder message
  reminder = f"Reminder: '{task}' is a {priority} priority task"

  # Add urgency message for time-bound tasks
  if time_bound == "yes":
    reminder += " that requires immediate attention today!"

  # Print the reminder
  print(reminder)

if __name__ == "__main__":
  main()