from case import manage

# Run the program / Console presentation ---
if __name__ == '__main__':
    print('\nValid commands:')
    print("* Show inventory amount: 'L'")
    print("* Add amount to inventory: I followed by amount e.g 'I20'")
    print("* Remove amount from inventory: S followed by amount e.g 'S7'")
    print("* 'Q' to exit program\n")

    inventory = 0 # The example inventory we want to change

    active = True
    while active:
        user_input = input("Command: ")
        if user_input == 'Q': 
            print('Program exited\n')
            break

        processed_input = manage(user_input, inventory)

        if processed_input == 'Invalid':
            print("\n\nInvalid command!\n\nValid commands:\n*Show inventory amount: L\n*Add amount to inventory: I followed by amount, e.g 'I20'\n*Remove amount from inventory: S followed by amount, e.g 'S5'\n")
        elif user_input[0] == 'L':
            print('There are ' + str(processed_input) + ' item(s) in inventory.\n')
        elif user_input[0] == 'S':
            inventory = processed_input # Updates inventory in accordance with principles of functional programming as each data entity is immutable.
            print('Removed ' + str(user_input[1:]) + ' item(s) from inventory.\n')
        elif user_input[0] == 'I':
            inventory = processed_input # Updates inventory in accordance with principles of functional programming as each data entity is immutable.
            print('Added ' + str(user_input[1:]) + ' item(s) to inventory.\n')