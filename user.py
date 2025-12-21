import json
accounts={"admin":{"password":"secretadminpassword"}}
def newAccount(newUsername,newPassword,newFullname,newQuestion,newAnswer):
    if newUsername in accounts:
        print("Username Taken, Please Try Again")
    else:
        accounts.update({newUsername:{"password":newPassword,"fullname":newFullname,"securityquestion":newQuestion,"answer":newAnswer,"balance":0}})
        print("Account Successfully Created!")
    with open("user.json","w") as userJson:
        json.dump(accounts,userJson,ensure_ascii=False)