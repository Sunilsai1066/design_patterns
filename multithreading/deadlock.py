import threading
import time


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {self.name}: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {self.name}: {self.balance}")
        else:
            print(f"Withdraw failed for {self.name}: Not enough balance ({self.balance})")

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name


class BankTransfer:
    def __init__(self, from_account, to_account):
        self.from_account = from_account
        self.to_account = to_account

    def transfer(self, amount):
        print(f"{self.from_account.getName()} acquiring lock...")
        with self.from_account.lock:
            print(f"{self.from_account.getName()} acquired lock.")
            time.sleep(1)
            print(f"Trying to deposit {self.to_account.getName()}")
            with self.to_account.lock:
                self.from_account.withdraw(amount)
                self.to_account.deposit(amount)
                print(f"Transfer {self.from_account.getName()} to {self.to_account.getName()}: {amount}")


U1 = BankAccount("U1", 100)
U2 = BankAccount("U2", 200)
Transfer1 = BankTransfer(U1, U2)
Transfer2 = BankTransfer(U2, U1)

t1 = threading.Thread(target=Transfer1.transfer, args=(10,))
t2 = threading.Thread(target=Transfer2.transfer, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"U1 Balance: {U1.getBalance()}")
print(f"U2 Balance: {U2.getBalance()}")
