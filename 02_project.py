''' Simple ATM Simulation (Easy)
What to build
Options like check balance, deposit, withdraw.
Balance updates after each operation.
Concepts used
Variables for balance
match-case for menu selection
if or else for validation
Loop to keep ATM running
Functions for deposit and withdraw
Strings for menu and messages'''
def deposit(balance):
        amount=int(input("Enter the amount to deposit:"))
        balance+=amount
        print(f"Amount Deposited successful! New Balance={balance}")
        return balance
def withdraw(balance):
        amount=int(input("Enter the amount to withdraw:"))
        if amount>balance:
            print("Insufficient Funds")
        else:
            balance-=amount
            print(f"Withdrawl Successful! Remaining Balance={balance}")
        return balance
balance=int(input("Enter your current balance:"))
while True:
    print("\n1.Deposit\n2. withdraw\n3. Check Balance\n4. Exit")
    choose=int(input("Enter your choice(1-4):"))
    if choose==1:
        balance=deposit(balance)
    elif choose==2:
        balance=withdraw(balance)
    elif choose==3:
        print(f"Current Balance:{balance}")
    elif choose==4:
         print("Thank you for using our ATM")
         break
    else:
         print("Something went wrong")
result=deposit(45)
result2=withdraw(23)
print(result)
print(result2)