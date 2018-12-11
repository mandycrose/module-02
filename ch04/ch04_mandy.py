# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import random
#import datetime
#import time
#print("hello")
#
##def luckyNumberRandom():
##    name= input ("please type your name here: ")
##    print ("hello", name.upper())
##    number= int(input("please give a number: "))
##    print ("your luck number is:" + str(random.randint(50,number)))
##    
##luckyNumberRandom()
#
#startTime= time.time()
#
#print("date and time", datetime.datetime.now())
#print ()
#print ("current time:", datetime.datetime.now().time())
#
#def luckyNumberRandom():
#    name= input ("please type your name here: ")
#    print ("hello", name.upper())
#    number= int(input("please give a number: "))
#    print ("your luck number is:" + str(random.randint(50,number)))
#    
#luckyNumberRandom()
#
#processTime= time.time()-startTime
#print ()
#print("program running time:", round(processTime,2), "seconds")

#print("this"=="this")
#
#age = 15
#isaTeen= age>=13 and age<=19
#print(isaTeen)
#
#age = 24 
#isaTeen= age>=13 and age<=19
#print (isaTeen)
#
#def checkTeen(age):
#    return age>=13 and age<=19
#
#age = 34
#print(checkTeen(age))

#def numberGame ():
#    number= input("Enter a number between 1 and 10: ")
#    number = int(number)
#    
#    if number > 10 :
#        print("Too high!")
#        number= input("try again! Enter a number between 1 and 10: ")
#        number = int(number)
#    if number <= 0 :
#        print("Too low")
#        number= input("try again! Enter a number between 1 and 10: ")
#        number = int(number)
#    else: 
#        print ("great number!")
#numberGame()

def ageGame():
    age= input("what is your age? ")
    age= int(age)
    
#    if age < 65:
#        print("you are an adult")
    if age < 13:
        print ("you are a child!")
    elif age < 18: 
        print ("you are a teen!")
    elif age < 65:
        print("you are an adult")
    else: 
        print ("you are a pensioner! Lucky you!")
ageGame()     
