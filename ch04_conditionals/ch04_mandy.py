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
################# IF/ELSE statements Task 3/4 ###############
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

######## task 5 #####################
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



########## shipping weight project #######

#def ground_shipping(weight):
#  if weight <= 2.0:
#    return (1.50 * weight)
#  elif weight >2.0 and weight <= 6.0:
#    return (3.00 * weight)
#  elif weight >6.0 and weight <= 10.0:
#    return (4.0 * weight)
#  else:
#    return (weight * 4.75) 
#
#print (ground_shipping(11))
#
#def ground_shipping(weight):
#  if weight <= 2.0:
#    return (4.50 * weight)
#  elif weight >2.0 and weight <= 6.0:
#    return (9.00 * weight)
#  elif weight >6.0 and weight <= 10.0:
#    return (12.0 * weight)
#  else:
#    return (weight * 14.25) 

#def best_shipping(weight):
#    if weight <= 2.0 and ((1.50 * weight) + 20.00) < ((4.50 * weight) or 125):
#        print ("your best shipping is ground")
#    elif weight weight >2.0 and weight <= 6.0 and ((3.00 * weight) + 20.00) < ((9.00 * weight)or 125) :
#        print("your best shipping is ground")
        
#def best_shipping(weight):
#    if weight <= 2.0 and ((1.50 * weight) + 20) < ((4.50 * weight) or 125):
#        return ("your best shipping is ground")
#    elif weight <= 2.0 and ((4.50 * weight) < ((1.50 * weight) + 20) or < 125):
#        return ("your best shipping is drone")
#    elif weight <= 2.0 and ((1.50 * weight) + 20) and (4.50 * weight) > 125:
#        return ("your best shipping is flat rate ground")
#    else:
#        print("hold on")
        
#def best_shipping(weight):
#    if weight <= 2.0 and ((1.50 * weight) + 20) < ((4.50 * weight) or 125):
#        return ("your best shipping is ground")
#    elif weight <= 2.0 and ((1.50 * weight) + 20) > ((4.50 * weight) or 125):
#        return ("your best shipping is drone") 
#    elif weight <= 2.0 and (((4.50 * weight) + 20) or (1.50 * weight)) > 125:
#        return ("your best shipping is flat rate")
#    
#    elif weight >2.0 and weight <= 6.0 and ((3.00 * weight) + 20) < ((9.00 * weight) or 125):
#        return ("your best shipping is ground")
#    elif weight >2.0 and weight <= 6.0 and ((3.00 * weight) + 20) > ((9.00 * weight) or 125):
#        return ("your best shipping is drone") 
#    elif weight >2.0 and weight <= 6.0 and (((3.00 * weight) + 20) or (9.00 * weight)) > 125:
#        return ("your best shipping is flat rate")
#    
#    elif weight >6.0 and weight <= 10.0 and ((4.00 * weight) + 20) < ((12.00 * weight) or 125):
#        return ("your best shipping is ground")
#    elif weight >6.0 and weight <= 10.0 and ((4.00 * weight) + 20) > ((12.00 * weight) or 125):
#        return ("your best shipping is drone") 
#    elif weight >6.0 and weight <= 10.0 and (((4.00 * weight) + 20) or (12.00 * weight)) > 125:
#        return ("your best shipping is flat rate")
#    
#    elif weight > 10.0 and  (125 or (14.25 * weight)) > ((4.75 * weight) + 20):
#        return ("your best shipping is ground")
#    elif weight > 10.0 and ((4.75 * weight) + 20) > ((14.25 * weight) or 125):
#        return ("your best shipping is drone") 
#    elif weight > 10.0 and (125 < (((4.75 * weight) + 20) or (14.25 * weight))):
#        return ("your best shipping is flat rate")
#print(best_shipping(400))
#    
