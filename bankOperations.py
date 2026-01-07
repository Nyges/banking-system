import json
import user
def withdrawal(loggedUser,amount):
    if amount<=0:
        print("Invalid Amount")
    elif user.accounts[loggedUser]["balance"]<amount:
        print("Insufficient Balance")
    else:
        user.accounts[loggedUser]["balance"]-=amount
        print("Withdrawal Success")
        with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def deposit(loggedUser,amount):
    if amount<=0:
        print("Invalid Amount")
    else:
        user.accounts[loggedUser]["balance"]+=amount
        print("Deposit Success")
        with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def transferFunds(sendingUser,receivingUser,amount):
    if receivingUser in user.accounts:
        if receivingUser=="admin":
            print("CANNOT SEND FUNDS TO ADMIN")
        elif receivingUser==sendingUser:
            print("Cannot send Funds to yourself")
        elif amount<=0:
            print("Invalid Amount")
        elif amount>user.accounts[sendingUser]["balance"]:
            print("Insufficient Balance")
        else:
            withdrawal(loggedUser=sendingUser,amount=amount)
            deposit(loggedUser=receivingUser,amount=amount)
            print("Funds Transfer Success")
            with open("user.json","w") as userJson:
                json.dump(user.accounts,userJson,ensure_ascii=False)
    else:
        print("User not found")

def menu(loggedUser):
    while True:
        choice=input(f"Current Balance: {user.accounts[loggedUser]["balance"]}\n1. Withdrawal\n2. Deposit\n3. Transfer Funds\n4. Logout\n")
        if choice=="1":
            withdrawal(loggedUser,amount=int(input("Please enter amount to Withdraw: ")))
        elif choice=="2":
            deposit(loggedUser,amount=int(input("Please enter amount to Deposit: ")))
        elif choice=="3":
            transferFunds(
                sendingUser=loggedUser,
                receivingUser=str(input("Please Choose recipient by Username: ")),
                amount=int(input("Please enter amount to Send: "))
            )
        elif choice=="4":
            break
        else:
            print("Invalid Choice")

def adminWithdrawal(chosenUser):
    amount=int(input("ENTER AMOUNT TO WITHDRAW: "))
    if amount<=0:
        print("INVALID AMOUNT")
    elif amount>user.accounts[chosenUser]["balance"]:
        print("ACCOUNT BALANCE INSUFFICIENT")
    else:
        user.accounts[chosenUser]["balance"]-=amount
        print("WITHDRAWAL SUCCESS")
        with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def adminDeposit(chosenUser):
    amount=int(input("ENTER AMOUNT TO DEPOSIT: "))
    if amount<=0:
        print("INVALID AMOUNT")
    else:
        user.accounts[chosenUser]["balance"]+=amount
        print("DEPOSIT SUCCESS")
        with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def adminDetailChange(chosenUser):
    choice=input("CHOOSE DETAIL TO CHANGE\n1. PASSWORD\n2. FULL NAME\n3. SECURITY QUESTION\n4. QUESTION ANSWER\n")
    if choice=="1":
        user.accounts[chosenUser]["password"]=str(input("ENTER NEW PASSWORD: "))
        print("PASSWORD CHANGED")
    elif choice=="2":
        user.accounts[chosenUser]["fullname"]=str(input("ENTER NEW FULL NAME: ")).strip().title()
        print("FULL NAME CHANGED")
    elif choice=="3":
        user.accounts[chosenUser]["securityquestion"]=str(input("ENTER NEW SECURITY QUESTION: ")).capitalize()
        print("SECURITY QUESTION CHANGED")
    elif choice=="4":
        user.accounts[chosenUser]["answer"]=str(input("ENTER NEW QUESTION ANSWER: "))
        print("ANSWER CHANGED")
    with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def adminDeletion(chosenUser):
    choice=str(input("ARE YOU SURE YOU WANT TO DELETE THIS ACCOUNT? ('YES' TO CONFIRM)\n")).casefold()
    if choice=="yes":
        user.accounts.pop(chosenUser)
        print("ACCOUNT DELETED")
    with open("user.json","w") as userJson:
            json.dump(user.accounts,userJson,ensure_ascii=False)

def adminMenu():
    print("--ADMIN MENU--")
    while True:
        choice=input("1. MANAGE AN ACCOUNT\n2. PRINT ALL ACCOUNTS\n3. LOGOUT\n")
        if choice=="1":
            userChoice=input("CHOOSE ACCOUNT BY USERNAME: ")
            if userChoice in user.accounts:
                if userChoice=="admin":
                    print("THE ADMIN ACCOUNT CANNOT BE MANAGED")
                else:
                    while True:
                        print(f"ACCOUNT BALANCE: {user.accounts[userChoice]["balance"]}")
                        choice2=input("1. WITHDRAW\n2. DEPOSIT\n3. CHANGE DETAIL\n4. DELETE ACCOUNT\n5. BACK\n")
                        if choice2=="1":
                            adminWithdrawal(chosenUser=userChoice)
                        elif choice2=="2":
                            adminDeposit(chosenUser=userChoice)
                        elif choice2=="3":
                            adminDetailChange(chosenUser=userChoice)
                        elif choice2=="4":
                            adminDeletion(chosenUser=userChoice)
                            break
                        elif choice2=="5":
                            break
                        else:
                            print("INVALID CHOICE")
            else:
                print("USER NOT FOUND")
        elif choice=="2":
            with open("user.json","w") as userJson:
                json.dump(user.accounts,userJson,ensure_ascii=False)
            print(user.accounts)
        elif choice=="3":
            break
        else:
            print("INVALID CHOICE")