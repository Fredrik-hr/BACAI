# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:45:53 2024

@author: Mathi
"""

#husk at alle filene må være i samme mappe

#filenavn = main_program.py
#    filename         (def) function name
import time 
from square_root import square_root_calc

def main():
    num = 4
    print(f"square root of {num} is {square_root_calc(num)}\n")
    


print("------------")
print(__name__) #__name__ will be printed as __main__ 
print("------------")

if __name__ == "__main__":
    starttime = time.time()
    print(starttime)
    main()
    time.sleep(1)
    endtime = time.time()
    differnce = endtime - starttime
    print(differnce)
    
    
