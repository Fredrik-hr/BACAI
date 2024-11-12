from bank_module import Bank_Account
   
accounts = { "F123": Bank_Account("Fredrik", 3000000), "P456" : Bank_Account("Pedro", 50)}
print("Welcome to Engebret Bank, how can i help you good sir or madam?")
account_login = input("Log in with your code: ")
logged_in = True
while account_login in accounts and logged_in:
    account1 = accounts[account_login]
    print("These are our options:")
    print("B: Your Bank Balance")
    print("D: Deposit Money")
    print("W: Withdraw Money")
    print("T: Transfer Money")
    print("Q: Quit")
    while True:
        select = input("What would you like to do?: ").lower()
        if select == "q":
            print("Bye Bye, Now.")
            logged_in = False
            break
        elif select == "b":
            account1.display_balance()
        elif select == "d":
            account1.deposit()
        elif select == "w":
            account1.withdraw()
        elif select == "t":
            recipient_code = input("Enter code of the recipient: ")
            if recipient_code in accounts:
                recipient = accounts[recipient_code]
                amount = int(input("How much do you want to transfer: "))
                account1.transfer(recipient, amount)
            else:
                ("ERROR")
        else:
            print("Error, Try Again")
else:
    if not logged_in:
        pass
    else:
        print("Error, Try again")
