import json
import user
import bankOperations
import report

while True:
    choice=input("Please Login or Create an account\n1. Create Account\n2. Login\n")
    if choice==1:
        user.newAccount(
            newUsername=input("Enter Username: "),
            newPassword=input("Enter Password: ").strip(),
            newFullname=input("Enter Full Name: ").strip().title(),
            newQuestion=input("Enter Security Question: ").capitalize(),
            newAnswer=input("Enter Security Answer: ")
        )
    elif choice==2:
        print("todo")
    else:
        print("Invalid Choice")