class bankaccount:
    def _init_(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount>0:
            self.__balance += amount
            print(f"Deposited: {amount}")
            print(f"New balance: {self.__balance}")
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.__balance-=amount
            print(f"withdrawn_amount:{amount}")
            print(f"New balance:{self.__balance}")
        else:
            print("insufficient balance")
            
