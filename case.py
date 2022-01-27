# Main function takes in data as an input as well so that it may be reused to work on any inventory item.
def manage(user_input, inventory):
    """
    The function updates and returns data based on input, returns 'Invalid' string if input is invalid.

    Parameters:
        user_input: String, 'L' to display data, 'I' followed by a number to add amount, 'S' followed by a number in str format to remove amount.
        inventory: Integer of the amount of stock items.

    Returns:
        Integer or 'Invalid' string if input or data is invalid.
    """

    try:
        command = user_input[0]
        if command == 'L' and len(user_input) == 1:
            return inventory
        n = int(user_input[1:])
        if command == 'S':
            inventory -= n
            return inventory
        elif command == 'I':
            inventory += n
            return inventory
        else:
            return 'Invalid'
    except:
        return 'Invalid'
