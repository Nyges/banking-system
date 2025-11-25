import json
accounts={"admin":{"password":"secretadminpassword"}}

while True:
    choice=int(input("Please Login or Create an account\n1. Create Account\n2. Login\n"))
    if choice==1:
        newUsername=input("Enter Username: ")
        newPassword=input("Enter Password: ")
        accounts.update({newUsername:{"password":newPassword,"balance":0}})
        print(f"Account '{newUsername}' successfully created, please log in again")
    elif choice==2:
        print(":)") #todo
    else:
        print("No such option")