# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:50:27 2024

@author: 1119f
"""

def babbit():
    a, b = 0, 1
    while b <= 50:
        print(b)
        a, b = b, a+b
    return b

babbit()
