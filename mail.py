def mailcreate(nickname, mailtype=""):
    mailadresi = "@".join([nickname, mailtype])
    return mailadresi


nickname = input("Please enter your username: ")
mail = input("Please enter the mail type: ")
if mail:
    print("Mail adresi:", mailcreate(nickname, mail))
else:
    print("Mail adresi:", mailcreate(nickname))

response = input("Would you like to modify the email address? (Y/N): ")
if response.lower() == "y":
    new_mail = input("Please enter the new mail type: ")
    print("Modified mail adresi:", mailcreate(nickname, new_mail))

check_mail = input("Please enter an email address to check: ")
if check_mail == mailcreate(nickname, mail):
    print("This email address is already in use.")
    print("Your email address has been created.")