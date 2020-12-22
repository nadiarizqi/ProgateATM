
class Customer:

    def __init__(self, id, card):
        self.id = id
        self.card = card
    
    def get_id(self):
        return self.id

    def get_card(self):
        return self.card
    
    def get_custPin(self):
        card = self.get_card()
        return card.get_pin()
    
    def get_custBalance(self):
        card = self.get_card()
        return card.get_balance()
    
    def withdraw_balance(self, nominal):
        updated_balance = self.get_custBalance() - nominal
        self.get_card().set_balance(updated_balance)
    
    def deposit_balance(self, nominal):
        updated_balance = self.get_custBalance() + nominal
        self.get_card().set_balance(updated_balance)

    def set_custPin(self, new_pin):
        card = self.get_card()
        card.set_pin(new_pin)
    
