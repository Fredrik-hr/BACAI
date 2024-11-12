# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:46:41 2024

@author: engeb
"""

class Bank_Account():
    def __init__(self, n, b):
        self.ac_name = n
        self.ac_balance = b
    
    def display_balance(self):
        print(f"This is your bank balance: \n {self.ac_balance}")
        
    def deposit(self):
        new_deposit = int(input("How much would you like to deposit:"))
        while new_deposit > 0:
            self.ac_balance += new_deposit
            print(f"Your balance is now {self.ac_balance}")
            break
        else:
            print("Error, Try again")
        
    def withdraw(self):
        new_withdrawn = int(input("How much would you like to withdraw:"))
        while new_withdrawn <= self.ac_balance:
            self.ac_balance -= new_withdrawn
            print(f"Your balance is now {self.ac_balance}")
            break
        else:
            print("Error try again")

                  
    def transfer(self, recipient):
        transfer = int(input("How much do you want to transfer: "))
        if transfer <= self.ac_balance:
            self.ac_balance -= transfer
            recipient.ac_balance += transfer
            print(recipient.ac_balance)
        else:
            ("Error, Try again")