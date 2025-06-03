class ATM:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance
        
    def deposit(self):
        amount=int(input("enter your deposit amount"))
        self.balance +=amount
        print(f"rs{amount} deposited succesfully")
    def withdrawl(self):
        amount=int(input("enter your withdrawl amount"))
        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance -=amount
            print(f"rs{amount} withdrawn succesfully")
        
    def checkbalance(self):
        print(f"current balance: rs{self.balance}")
    def exit(self):
        print ("thanks for using atm.have a great day")

atm = ATM(initial_balance=500000)
while True:
    print("\n----ATM menu---")
    print("1.deposit")
    print("2.withdrawl")
    print("3.checkbalance")
    print("4.exit")
    choice = int(input("enter your choice"))

    if choice ==1:
        atm.deposit()
    if choice ==2:
        atm.withdrawl()
    if choice ==3:
        atm.checkbalance()
    if choice ==1:
        atm.exit()
        break
    else:
        print("invalid")
    
