# Initialize an empty shopping list
shopping_list = []

# Define a function to display menu
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()