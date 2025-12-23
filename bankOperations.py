import json
import user
def withdrawal(loggedUser,amount):
    if amount<0:
        print("Invalid Amount")
    elif user.accounts[loggedUser]["balance"]<amount:
        print("Insufficient Balance")
    else:
        user.accounts[loggedUser]["balance"]-=amount
        print(f"Withdrawal Success, Your remaining Balance is {user.accounts[loggedUser]["balance"]}")
        with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def menu(loggedUser):
    while True:
        choice=input(f"Current Balance: {user.accounts[loggedUser]["balance"]}\n1. Withdrawal\n2. Deposit\n3. Logout\n")
        if choice=="1":
            withdrawal(loggedUser,amount=int(input("Please enter amount to Withdraw: ")))
        elif choice=="2":
            print("todo")
        elif choice=="3":
            break
        else:
            print("Invalid Choice")