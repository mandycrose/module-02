# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:17:28 2018

@author: 612436112
"""
############ while loops #####################################################

##### task 1 ### 
x = 33
while x >= 2: # runs the loop while x is > 2 
    print(x, ": ", end='' ) #end = '' connects by space and not new line
    x = x / 2                     #remember , gives a space and + gives no space 
#print(x)

#### task 2 #####

def triangular(n):
    trinum = 0 
    while n > 0:
        trinum= trinum + n
        n= n - 1
    return trinum 

print(triangular(3))
### task 3 #### 
def grades():
    did_you_pass = "yes"
    while did_you_pass == "yes":
            mark = input("what is the mark?")
            mark= int(mark)
            if mark >= 70:
                print("The mark is a first!")
            elif mark >= 40:
                print ("pass")
            else:
                print("fail") # if you did not do return it would keep asking the question/ running loop
            did_you_pass = input("did you pass?")
grades()

################################## task 4 - breaks in loop ############################

i = 55
while i > 10:
    print (i)
    i = i * 0.8
    if i == 35.2:
        break
    
def greeting ():
    what_name = " "
    while type(what_name) == str:
        what_name = input("enter name  ")
        if what_name == "done":
            break
        else:
            print ("hello {}".format(what_name))

greeting()

#################### phonebook with loop ##################################### 

phonebook= {"mandy":(111,999,666, "London",21), 
            "cem":(222,888,555, "Oxford",31), 
            "handan":(333,777,444,"cambridge",41)}
def phonebook_add (phonebook): 
    number_add = 0
    while number_add <= 4:
        name= input("what is the name you would like to enter?")
        number = input ("what are the last three digits of the phone number?")
        luckyN = int(input("what is the lucky number? "))
        postCode = input ("what is the post code? ")
        town = input ("what is the town? ")
        age= input("what is the age of the new contact ")
        phonebook[name]=[number,luckyN,postCode,town,age]
        number_add += 1
    while number_add > 4:
        add_another = input ("would you like to add another contact? y/n")
        if add_another == "y":
            name= input("what is the name you would like to enter?")
            number = input ("what are the last three digits of the phone number?")
            luckyN = int(input("what is the lucky number? "))
            postCode = input ("what is the post code? ")
            town = input ("what is the town? ")
            age= input("what is the age of the new contact ")
            phonebook[name]=[number,luckyN,postCode,town,age]
            are_done = input("would you like to add another contact? y/n ")
            if are_done == "n":
                return phonebook 
    return phonebook
phonebook_add(phonebook)
############################ games #####################################################  
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
