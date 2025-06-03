class Atm:
    def __init__(self, initialbal):
        self.balance = initialbal

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")


# Example usage:
if __name__ == "__main__":
    AtmS = Atm(initialbal=99)  # Create ATM instance with initial balance

    AtmS.check_balance()       # Show balance
    AtmS.deposit(50)           # Deposit $50
    AtmS.withdraw(30)          # Withdraw $30
    AtmS.check_balance()       # Show balance again
