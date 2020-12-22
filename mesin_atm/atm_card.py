
class ATMCard:
    
    def __init__(self, defaultPin=1234, defaultBalance=10000):
       self.pin = defaultPin
       self.balance = defaultBalance

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance

    def set_pin(self, new_pin):
        self.pin = new_pin
