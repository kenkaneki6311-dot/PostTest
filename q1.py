class BankAccount:
    def __init__(self):
        self.__balance = 10000 

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}. Remaining Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient!")
        else:
            self.__balance -= amount
            print(f"Deducted: {amount}. Remaining Balance: {self.__balance}")

    def get_balance(self):
        print(f"Current Balance: {self.__balance}")


print("--- Person 1 Account ---")
account1 = BankAccount()
account1.get_balance()
account1.deposit(5000)
account1.withdraw(3000)


print("\n--- Person 2 Account ---")
account2 = BankAccount()
account2.get_balance()
account2.withdraw(15000)  # Testing insufficient funds
account2.deposit(2000)