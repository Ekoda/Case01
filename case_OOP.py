class Item:
    def __init__(self, amount):
        self.amount = amount
    
    def manage(self, user_input):
        try:
            command = user_input[0]
            if command == 'L' and len(user_input) == 1:
                return self.amount
            n = int(user_input[1:])
            if command == 'S':
                self.amount -= n
                return n
            elif command == 'I':
                self.amount += n
                return n
            else:
                return 'Invalid'
        except:
            return 'Invalid'


# Initialize inventory: inventory = Item(0)
