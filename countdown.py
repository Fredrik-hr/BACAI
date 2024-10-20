# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:28:57 2024

@author: Mathi
"""

import time

import sys

my_time=int(input("Enter the time in seconds:"))


#0 = end and -1 is how much it goes down
for x in range(my_time, -1, -1):
    #i think this is more clean as it's goes from the input to 1 insted of input -1 to 0
    seconds=x%60
    minutes=int(x/60) %60
    hours= int(x/3600)
    #print(f"{hours:02}:{minutes:02}:{seconds:02}")
    sys.stdout.write(f"\r{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("\nTIME'S UP!")

