class Item:
    def __init__(self, amount: int ):
        self.amount = amount
    
    def manage(self, user_input: str ) -> str:
        try:
            command = user_input[0]
            if command == 'L' and len(user_input) == 1:
                return str(self.amount)
            n = int(user_input[1:])
            if command == 'S':
                self.amount -= n
                return str(n)
            elif command == 'I':
                self.amount += n
                return str(n)
            else:
                return 'Invalid'
        except:
            return 'Invalid'