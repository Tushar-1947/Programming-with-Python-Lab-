class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    def show_details(self):
        print("Account Holder:", self.name)
        print("Balance:", self.get_balance())
        print("Interest Rate:", self.interest, "%")


class CurrentAccount(BankAccount):
    def __init__(self, name, balance, limit):
        super().__init__(name, balance)
        self.limit = limit

    def show_details(self):
        print("Account Holder:", self.name)
        print("Balance:", self.get_balance())
        print("Overdraft Limit:", self.limit)


name = input("Enter account holder name: ")
amount = float(input("Enter initial balance: "))

account = SavingsAccount(name, amount, 5)

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = float(input("Enter deposit amount: "))
        account.deposit(value)

    elif choice == "2":
        value = float(input("Enter withdrawal amount: "))
        account.withdraw(value)

    elif choice == "3":
        print("Current Balance:", account.get_balance())

    elif choice == "4":
        account.show_details()

    elif choice == "5":
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid choice!")
