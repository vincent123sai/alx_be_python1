def display_menu():
    """
    Prints the menu options for the shopping list manager.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
  """
  Main function that manages the shopping list.
  """
  shopping_list = []  # Initialize an empty list for the shopping list
  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
      # Add item
      item = input("Enter the item name: ")
      shopping_list.append(item)
      print(f"{item} added to the list.")
    elif choice == '2':
      # Remove item
      item = input("Enter the item name to remove: ")
      if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
      else:
        print(f"{item} not found in the list.")
    elif choice == '3':
      # View list
      if shopping_list:
        print("Your shopping list:")
        for item in shopping_list:
          print(f"- {item}")
      else:
        print("The list is empty.")
    elif choice == '4':
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()