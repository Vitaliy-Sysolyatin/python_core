class ATM:
    def __init__(self, bills_20, bills_50, bills_100):
        self.bills_20 = bills_20
        self.bills_50 = bills_50
        self.bills_100 = bills_100

    def add_money(self, bills_20, bills_50, bills_100):
        self.bills_20 += bills_20
        self.bills_50 += bills_50
        self.bills_100 += bills_100

    def withdraw(self, amount):
        for count_100 in range(self.bills_100 + 1):
            for count_50 in range(self.bills_50 + 1):
                for count_20 in range(self.bills_20 + 1):
                    total = (count_100 * 100 + count_50 * 50 + count_20 * 20)

                    if total == amount:
                        self.bills_100 -= count_100
                        self.bills_50 -= count_50
                        self.bills_20 -= count_20

                        print("Выдано купюр:")
                        print("100:", count_100)
                        print("50:", count_50)
                        print("20:", count_20)

                        return True
        return False


atm = ATM(5, 2, 1)

atm.add_money(2, 1, 1)

print("Снятие 160:")
print(atm.withdraw(160))

print("Снятие 70:")
print(atm.withdraw(70))

print("Снятие 1000:")
print(atm.withdraw(1000))
