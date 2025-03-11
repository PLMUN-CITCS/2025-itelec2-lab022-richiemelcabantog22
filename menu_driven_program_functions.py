def display_menu():
    print("Menu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    print("Hello! Welcome!")

def even_odd_checker_action():
    user_input = int(input("Enter an integer: "))
    if user_input % 2 == 0:
        print(f"{user_input} is an Even number.")
    else:
        print(f"{user_input} is an Odd number.")

def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please select a valid option.")
        return False

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()