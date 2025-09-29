def display_menu():
    """Display the shopping list menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
   
    if not shopping_list:
        print("Your shopping list is empty. Nothing to remove.")
        return
    
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def view_list(shopping_list):

    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                add_item(shopping_list)
            elif choice == '2':
                remove_item(shopping_list)
            elif choice == '3':
                view_list(shopping_list)
            elif choice == '4':
                print("Thank you for using the Shopping List Manager! Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
                
        except KeyboardInterrupt:
            print("\n\nExiting Shopping List Manager. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
