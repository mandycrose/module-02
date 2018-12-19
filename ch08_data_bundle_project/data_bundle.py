# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:40 2018

@author: 612436112
"""
#new version -- 

def DataBundlePurchase(truePassword,balance):
    if checkPassword(truePassword):
        if whatDoyouWant (balance):
            if checkPhonenumber():
                return buyData(balance)
            else: 
                return "error!"
        else:
            return ("Your balance is {}".format(balance))
    else:
        return "Wrong password"
    
    
def checkPassword (truePassword):
    attempt = input("Please enter your password ")
    if truePassword == attempt:
        return True
    else: 
        return False 
def whatDoyouWant (balance):
    transactionType = input ("What would you like to do? Please enter 1 to check balance and 2 to buy data ")
    if transactionType == "1":
        return False
    elif transactionType == "2":
        return True
    
def checkPhonenumber ():
    phoneNumber1= input ("Please enter your phone number ")
    phoneNumber2= input("Please enter your phone number again so we can be really sure ")
    if phoneNumber1 == phoneNumber2:
        return True
    else:
        return False 
    
def buyData (balance):
    amount = int(input ("Got your number! Now - you can buy data in increments of 5 and you can buy no more that 100 How much data would you like to buy?"))
    new_balance = (balance - amount)
    if balance >= amount and (amount % 5 == 0):
        return ("Great! You have sufficent balance and your account has been credited with {} and your new balance is {}".format(amount, new_balance))
    elif balance >= amount and (amount % 5 != 0):
        return ("That is not a correct amount of data. It needs to be increment of 5")
    elif balance < amount:
        return ("Your balance is not sufficient. Your balance is {}".format(balance))

########## older code ####################
#def DataBundlePurchase(truePassword,balance):
#    if checkPassword(truePassword): 
#        if whatDoyouWant (balance):
#            return buyData(balance)
#        else:
#            return ("Your balance is {}".format(balance))
#    else:
#        return "Wrong password"
#    
#    
#def checkPassword (truePassword):
#    attempt = input("Please enter your password ")
#    if truePassword == attempt:
#        return True
#    else: 
#        return False 
#def whatDoyouWant (balance):
#    transactionType = input ("What would you like to do? Please enter 1 to check balance and 2 to buy data ")
#    if transactionType == "1":
#        return False
#    elif transactionType == "2":
#        return True
#def buyData (balance):
#    phoneNumer1= input ("Please enter your phone number ")
#    phoneNumber2= input("Please enter your phone number again so we can be really sure ")
#    amount = int(input ("Got your number! Now - you can buy data in increments of 5 and you can buy no more that 100 How much data would you like to buy?"))
#    valid_amount = range(0,101,5)
#    new_balance = (balance - amount)
#    if balance >= amount and amount :
##        return True
#        return ("Great! You have sufficent balance and your account has been credited with {} and your new balance is {}".format(amount, new_balance)) 
##    elif amount != range(0,101,5) and balance >= amount:
##        return "That is not a valid amount"
#    elif balance < amount:
##        return False
#        return ("Your balance is not sufficient. Your balance is {}".format(balance))
#     # if amount == (range(0,101,5)) and balance >= amount:    
##       print("not yet created")
#     
#     
#     
#     
#     #            if (buyData(balance)):
##                    return "your account is upated"
##            else:
##                    return "fail"
##        else:
##            return ("Your balance is {}".format(balance))
##                
#                
##        if buyData(balance): 
##                    return (checkBalance(balance))
##        else:
##                    return "That is not a valid amount"
#                
##           
##        else:
##            return
#        #computer understands that it is really "if checkPassword(truePassword)== True:"
##        if checkBalance(balance):
##            return ("Your balance is {}".format(balance))
##        else:
##            return ("Your balance is not sufficient. Your balance is {}".format(balance))
##    else: