from case_OOP import Item

# Run the program / Console presentation ---
if __name__ == '__main__':
    print('\nValid commands:')
    print("* Show inventory amount: 'L'")
    print("* Add amount to inventory: I followed by amount e.g 'I20'")
    print("* Remove amount from inventory: S followed by amount e.g 'S7'")
    print("* 'Ctrl + C' to exit program\n")

    inventory = Item(0) # The example inventory we want to change

    active = True
    while active:
        user_input = input("Command: ")
        managed = inventory.manage(user_input)
       
        if user_input == "L":
            print('Inventory: ' + str(managed))
        elif managed == 'Invalid':
            print('Invalid Command')