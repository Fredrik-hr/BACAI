# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:48:54 2024

@author: engeb
"""

import random
import math
#1.1

list1 = []

#Function to make a random list to test the functions

def random_list():
    n = random.randint(10,20)
    for i in range(n):
        list1.append(random.randint(1,10))
        list1.sort()
    print(list1)

random_list()


#1.1

print()
print("----------------------- task 1.1 ------------------------------------")
print()

#Function for Mean
def mean(numbers):
    #if the list is empty, the entire function outputs zero
    if len(numbers) == 0:
        return 0
    #counts the elements of the list
    n = len(numbers)
    #adding together the elements of the list
    sum_of = sum(numbers)
    #divides the sum of the elements with the number of elements
    mean_value = sum_of / n
    return mean_value

#function for variance
def variance(numbers):
    n = len(numbers)
    #inputs the mean function
    var_mean = mean(numbers)
    
    sqrd_diff = sum((i - var_mean)**2 for i in numbers) 
    variance_val = sqrd_diff/(n-1)
    return variance_val

#function for standard Deviation
def standard_deviation(numbers):
    var = variance(numbers) #sample variance
    deviation = math.sqrt(var) #Square root of variance
    return deviation

def task1_1():
    print(mean(list1))
    print(variance(list1))
    print("standard dev is ",standard_deviation(list1))

task1_1()
#for safety, as to not mess up anything
list1.clear()

#1.2
print()
print("----------------------- task 1.2 ------------------------------------")
print()
def task1_2():
    with open("numbers_file.txt", "r") as file:
        numbers = file.read()
        numbers_list = numbers.split()
        numbers_amount = len(numbers_list)
        print(numbers_amount)
        for i in range (numbers_amount):
            print(numbers_list[i], end=" ") #so all the elements prints on the same line
    
    print() #to make it look cleaner

task1_2()

#1.3
print()
print("----------------------- task 1.3 ------------------------------------")
print()
def confidence_interval(numbers):
    n = len(numbers)
    mean_value = mean(numbers)
    standard_error = standard_deviation(numbers)/math.sqrt(n)
    Z_score = 1.96
    lower_bounds = mean_value - Z_score * standard_error
    upper_bounds = mean_value + Z_score * standard_error
    return lower_bounds, upper_bounds

def task1_3():
    #the text file in question is comprised of 50 randomly generated numbers
    with open("numbers.txt", "r") as file:
        numb = file.read()
        
    data = [float(num) for num in numb.split()]
        
    print("The mean of the numbers text is", mean(data))
    print(f"Variance is {variance(data)}")
    print("The Standard Deviation of the numbers file is", standard_deviation(data))
    print("And the confidence interval is", confidence_interval(data))

task1_3()

#2.1
print()
print("----------------------- task 2.1 ------------------------------------")
print()
#Function for bernulli trial
def bernoulli_trial(p):
    rand = random.random() #generate a numeber between 1 and 0
    if rand <= p:  # if its a success
        return 1
    else:          # if its a failure
        return 0

trial2_1 = bernoulli_trial(0.5)
print(f"The results of the trial is {'a success' if trial2_1 == 1 else 'a failure'}")

#2.2
print()
print("----------------------- task 2.2 ------------------------------------")
print()

def trial_success(p,n):
    successes = 0
    for _ in range (n):
        if bernoulli_trial(p) == 1:
            successes += 1
    return successes

#within the print i wrote the probability of success, as well as how many trials
#i picked these numbers because they were easy
print(f"The number of successes is {trial_success(0.5, 10)}")


#2.3
print()
print("----------------------- task 2.3 ------------------------------------")
print()
#function to calculate expectations and standard deviation of trials
def trials_functions(p, n):
    #to calculate expectations
    E = n*p
    #i couldnt find a way to properly use the function i had already made
    #instead i made a simplified one
    standard_dev = math.sqrt(n * p * (1 - p))
    return E, standard_dev


def simulate_theoretical_trials(p, n):
    E, standard_dev = trials_functions(p, n)
    #calculates the expectations and standard deviations of the theoretical trails
    print(f"For {n} trials")
    print(f"The theoretical expectations of the trials are {E}")
    print(f"while the theoretical standard deviation is {standard_dev}")
    sim_succ = trial_success(p, n) #to calculate the success of the theoretical trials
    #unfortunate naming conventions, i know, but its easier to write short
    print(f"The number of simulated successes is {sim_succ}")


#input for the probability and the number of trials
p = float(input("What is the probabilty? "))
if p < 0 or p > 1:
    #So the user doesn't go either over or under 1 and 0
    raise ValueError("Probability must be between 0 and 1.")
        
choose = input("Do you want to input trials yourself? (y/n): ")
if choose == "y":
    n = int(input("How many trials? "))
    trial2_3 = bernoulli_trial(p)
    simulate_theoretical_trials(p, n)
elif choose == "n":
    print("This is the theoretical results of 30 and 100 trials")
    #the theoretical trials in a list
    simulate_theoretical_trials(p, 30)
    #for spacing
    print()
    simulate_theoretical_trials(p, 100)
    
else:
    print("Thats not one of the choices, run again.")
