# bank accounts ( from OOPS concept)

class SahilBankAccount:
    '''
    this class stores all the accounts
    '''
    sahil_accounts_dict = {}

    def __init__(self, account_number, name, initial_balance):
        self.account_number = account_number
        self.name = name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("insufficient balance.")
            return
        self.__balance -= amount
        print(f"{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"current Balance: {self.__balance}")


    def get_balance(self):  # Used internally for transfer
        return self.__balance

    def receive_transfer(self, amount):
        self.__balance += amount

    @classmethod
    def create_account(cls):
        try:
            acc_no = int(input("enter account number: "))
            if acc_no in cls.sahil_accounts_dict:
                print("account already exists.")
                return

            name = input("enter account holder name: ")
            balance = float(input("enter initial balance: "))

            if balance < 0:
                print("initial balance cannot be negative.")
                return

            account_obj = SahilBankAccount(acc_no, name, balance)
            cls.sahil_accounts_dict[acc_no] = account_obj
            print("account created successfully.")

        except:
            print("invalid input.")

    @classmethod
    def get_account(cls, acc_no):
        return cls.sahil_accounts_dict.get(acc_no)

    @classmethod
    def transfer_money(cls):
        try:
            from_acc = int(input("from account number: "))
            to_acc = int(input("to account number: "))
            amount = float(input("enter amount to transfer: "))

            sender = cls.get_account(from_acc)
            receiver = cls.get_account(to_acc)

            if not sender or not receiver:
                print("one or both accounts do not exist.")
                return

            if amount <= 0:
                print("transfer amount must be positive.")
                return

            if sender.get_balance() < amount:
                print("insufficient balance in sender account.")
                return

            sender.withdraw(amount)
            receiver.receive_transfer(amount)

            print("transfer successful.")

        except:
            print("invalid input.")



def sahil_bank_menu():
    while True:
        print("1. create account")
        print("2. deposit")
        print("3. withdraw")
        print("4. check balance")
        print("5. transfer money")
        print("6. exit")

        choice = input("enter your choice: ")

        if choice == "1":
            SahilBankAccount.create_account()

        elif choice == "2":
            acc_no = int(input("enter account number: "))
            account = SahilBankAccount.get_account(acc_no)
            if account:
                amount = float(input("enter deposit amount: "))
                account.deposit(amount)
            else:
                print(" account not found")

        elif choice == "3":
            acc_no = int(input("Enter Account Number: "))
            account = SahilBankAccount.get_account(acc_no)
            if account:
                amount = float(input("Enter Withdrawal Amount: "))
                account.withdraw(amount)
            else:
                print(" Account not found.")

        elif choice == "4":
            acc_no = int(input("Enter Account Number: "))
            account = SahilBankAccount.get_account(acc_no)
            if account:
                account.check_balance()
            else:
                print(" Account not found.")

        elif choice == "5":
            SahilBankAccount.transfer_money()

        elif choice == "6":
            print("Thank you for using Sahil Bank.")
            break

        else:
            print(" Invalid choice.")


sahil_bank_menu()


