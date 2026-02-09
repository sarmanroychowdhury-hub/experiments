class BankAccount:
    def _init_(self,acc_no,bal):
        self.acc_no = acc_no
        self.balance = bal
        
    def Deposit(self):
        amt = float(input("Entr amount to deposit"))
        self.balance = self.balance + amt
        print("Deposited:", amt)
        
    def withdraw(self):
        amt = float(input("Entr amount to deposit"))
        if amt <= self.balance:
            self.balance = self.balance - amt
            print("withdraw", amt)
        else:
            print("Not enough balance")
            
    def check_balance(self):
        print("Current balance", self.balance)
        
acc = input("enter account number")
bal = float(input("enter initial balance"))
obj = BankAccount(acc,bal)

while True:
    print("\n1 Deposit")
    print("2 withdraw")
    print("3 Check Balalance")
    print("4 Exit")
    
    ch = input("Enter Choice:")
    
if ch == "1":
        obj.Deposit()
elif ch == "2":
        obj.withdraw()
elif ch == "3":
        obj.check_balance
elif ch == "4":
    print("Thank You")
    break
else:
    print("Wrong Choice")