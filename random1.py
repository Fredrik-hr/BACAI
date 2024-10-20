# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:01:08 2024

@author: Mathi
"""

import random

random.seed(10) #this make it so the random dont swap

numbers = list(range(1,11))
print(numbers)
print("----------------")

random.shuffle(numbers)
print(numbers)
print("----------------")

num =random.choice(numbers)
print(num)
print("----------------")

nums4 = random.sample(numbers, 4)
print(nums4)
print("----------------")


a_random_int = random.randint(1,10)
print(a_random_int)
print("----------------")