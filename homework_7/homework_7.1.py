class CreditCard:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_info(self):
        print(f"Счёт: {self.account_number}, баланс: {self.balance}")


card_1 = CreditCard("1001", 1000)
card_2 = CreditCard("1002", 2000)
card_3 = CreditCard("1003", 3000)

card_1.deposit(500)
card_2.deposit(1000)
card_3.withdraw(700)

card_1.show_info()
card_2.show_info()
card_3.show_info()
