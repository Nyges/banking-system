import json
import bankOperations

accounts={"admin":{"password":"secretadminpassword"}}
def newAccount(newUsername,newPassword,newFullname,newQuestion,newAnswer):
    if newUsername in accounts:
        print("Username Taken, Please Try Again")
    else:
        accounts.update({newUsername:{"password":newPassword,"fullname":newFullname,"securityquestion":newQuestion,"answer":newAnswer,"balance":0}})
        print("Account Successfully Created!")
    with open("user.json","w") as userJson:
        json.dump(accounts,userJson,ensure_ascii=False)

def login(enteredUsername,enteredPassword):
    if enteredUsername in accounts:
        if accounts[enteredUsername]["password"]==enteredPassword:
            if accounts[enteredUsername]==accounts["admin"]:
                bankOperations.adminMenu()
            else:
                bankOperations.menu(loggedUser=enteredUsername)
        else:
            print("Incorrect Password")
    else:
        print("User not found")

def passwordRecovery(enteredUsername):
    if enteredUsername in accounts:
        if enteredUsername=="admin":
            print("ADMIN PASSWORD CANNOT BE RECOVERED")
        else:
            enteredAnswer=str(input(f"Security Question: {accounts[enteredUsername]["securityquestion"]}\n"))
            if enteredAnswer==accounts[enteredUsername]["answer"]:
                print(f"Correct Answer, Your account password is '{accounts[enteredUsername]["password"]}'")
            else:
                print("Wrong Answer!")
    else:
        print("User not found")