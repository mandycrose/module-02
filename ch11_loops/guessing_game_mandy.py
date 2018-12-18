# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:58:16 2018

@author: 612436112
"""

from random import randint
#def guess(attempts,range):
#    player_attempts = 0
#    number = randint(1,range)
#    print ("Welcome! Can you guess my secret number?")
#    while player_attempts < attempts:
#        player_guess= int(input("what is your guess?  "))
#        if player_guess == number:
#            return (print("wow! You guessed it!"))
#        else:
#            player_attempts += 1
#            attemtpts_left = attempts - player_attempts 
#            if player_guess > number:
#                print("too bad! your guess is too high. you have made {} guesses and you have {} guesses left".format(player_attempts,attemtpts_left))
#            else:
#                 print("too bad! your guess is too low. you have made {} guesses and you have {} guesses left".format(player_attempts,attemtpts_left))
#    while player_attempts > attempts:
#        print ("nice try but you are all out of guesses")
#        break
#    print ("END-OF-GAME: thanks for playing!")
#
#guess(3,10)

def dice_game():
    player_choice = ""
    while type(player_choice) == str:
        first_dice = randint(1,6)
        second_dice = randint(1,6)
        final_dice = first_dice + second_dice
        player_choice = input("would you like to guess: \n1:odd \n2:even \n3:quit \n ")
        if player_choice == "1" and final_dice %2 > 0:
            print ("You win!")
        elif player_choice == "2" and final_dice %2 == 0:
            print ("You win!")
        elif player_choice == "3":
            break
        else:
            print("you lose!")

dice_game()