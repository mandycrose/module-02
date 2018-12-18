# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:17:28 2018

@author: 612436112
"""
############ while loops #####################################################
x = 33
while x >= 2: # runs the loop while x is > 2 
    print(x, ": ", end='' ) #end = '' connects by space and not new line
    x = x / 2                     #remember , gives a space and + gives no space 
#print(x)


def triangular(n):
    trinum = 0 
    while n > 0:
        trinum= trinum + n
        n= n - 1
    return trinum 

#print(triangular(3))

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
#grades()

################################## breaks in loop ############################

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

#greeting()

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
#################################################################################            
