
# Uppgiften består av att skriva en konsolapplikation för att hantera lagersaldon.
# Användargränssnittet ska innehålla tre funktioner:
#   1) Att sälja x antal. Görs genom att man skriver “S” och så antalet + enter, t.ex. ”S5”.
#   2) Att inleverera x antal. Görs genom att man skriver “I” (stort i) och så antalet + enter, t.ex. ”I5”.
#   3) Visa aktuellt lager. Görs genom att man skriver ”L” + enter.
# När en försäljning eller inleverans görs ska lagersaldot räknas ner eller upp med angivet antal. När programmet startar är saldot alltid 0 och data behöver inte lagras på något annat sätt än i primärminnet.


# Logic ---

def add(n, data):
    data += n
    return data


def remove(n, data):
    data -= n
    return data


# Main function takes in data as an input as well so that it may be reused to work on any inventory item.
def manage(user_input, data):
    """
    The function updates and returns data based on input, returns 'Invalid' string if input is invalid.

    Parameters:
        user_input: String, 'L' to display data, 'I' followed by a number to add, 'S' followed by a number in str format to remove.
        data: The data which the user is concerned with.

    Returns:
        Integer or 'Invalid' string if input or data is invalid.
    """

    try:
        command = user_input[0]
        if command == 'L' and len(user_input) == 1:
            return data
        n = int(user_input[1:]) # Gets all characters in the String except for the first and converts to Int. If convertion to Int is not possible it triggers the exception.
        if command == 'S':
            return remove(n, data)
        elif command == 'I':
            return add(n, data)
        else:
            return 'Invalid'
    except:
        return 'Invalid'



# Run the program / Console presentation ---
if __name__ == '__main__':
    # Introduces the functionality of the program in console
    print('\nValid commands:')
    print("* Show inventory amount: 'L'")
    print("* Add amount to inventory: I followed by amount e.g 'I20'")
    print("* Remove amount from inventory: S followed by amount e.g 'S7'")
    print("* 'Q' to exit program\n")

    active = True
    inventory = 0 # The example inventory we want to change

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
