import json
import user
import bankOperations

with open("user.json","r") as userJson:
    user.accounts=json.load(userJson)
print("Please Login or Create an Account")
while True:
    choice=(input("1. Create Account\n2. Login\n3. Forgot Password\n").strip())
    if choice=="1":
        user.newAccount(
            newUsername=input("Enter Username: "),
            newPassword=input("Enter Password: ").strip(),
            newFullname=input("Enter Full Name: ").strip().title(),
            newQuestion=input("Enter Security Question: ").capitalize(),
            newAnswer=input("Enter Security Answer: ")
        )
    elif choice=="2":
        user.login(
            enteredUsername=input("Please enter your username: "),
            enteredPassword=input("Please enter your password: ")
        )
    elif choice=="3":
        user.passwordRecovery(enteredUsername=input("Please enter your username: "))
    else:
        print("Invalid Choice")