# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:56:32 2024

@author: engeb
"""

#List of games people can add it to

game = input("Hva er det spillet du spiller mest (Som har multiplayer): ").lower()

with open("games.txt", "rt") as file1:
    games_file = file1.read()
    if game in games_file:
        print("Dette spillet spiller noen andre.")
    else:
        with open("games.txt", "a") as file2:
            file2.write(f"{game}, \n")
            