# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:50:54 2024

@author: Mathi
"""

import time

import sys

def countdown_timer(seconds):
    while seconds >= 0:
        #print(f"Time remaining:{seconds} seconds")
        sys.stdout.write(f"\rTime remaining:{seconds} seconds")
        time.sleep(1)
        seconds -=1
    
    print("\nTime's up!")
    
if __name__ == "__main__":
    seconds = int(input("Enter the number of seconds:"))
    countdown_timer(seconds)