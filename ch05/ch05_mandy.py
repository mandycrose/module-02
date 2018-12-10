# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:37:43 2018

@author: 612436112
"""
import sys

#if 5>8:
#    print("hello")
#print("it worked")

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
    def __init__(self ,name, surname,balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.surname = surname
        self.balance = balance
    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        else:
            self.balance -= int(withdraw_amount)
        return self.balance
    def deposit (self,amount):
        """Return the balance remaining after depositing *amount* dollars"""
        self.balance += amount
        return self.balance
#jason = Customer('Jason Taylor',1000.0) 
#mandy= Customer("mandy","rose", 1.0)
#
#print(mandy.balance)
#print(mandy.deposit(500.0))
#print(mandy.withdraw (5.0))
#print(mandy.withdraw (50.0))
#print(mandy.balance)
#print(mandy.name, mandy.surname) 
    
#mandy= Customer("mandy","rose", 1.0)
#mandy.name() = 
#mandy.balance() = sys.argv[0]
#mandy.deposit() = sys.argv[1]

name= sys.argv [1]
surname= sys.argv [2]
balance= sys.argv [3]
amount_1= sys.argv [4]
amount_2= sys.argv [5]
mandy = Customer(name,surname, balance)
deposit= mandy.deposit(amount_1)
withdrawl= mandy.withdraw(amount_2)
#print (Customer(name,surname,balance))

print(mandy.balance)
print(deposit)
print(withdrawl)
#print(mandy.withdraw ())
print(mandy.balance)
#print(mandy.name, mandy.surname)

#name= "mindy"
#surname= "oaks"
#balance= 100
#amount_1= 10
#amount_2= 50
#mandy = Customer(name,surname, balance)
#deposit= mandy.deposit(amount_1)
#withdrawl= mandy.withdraw(amount_2)
#
#print(mandy.balance)
#print(deposit)
#print(withdrawl)
#print(mandy.balance)


#class Animal():
#    def eat(self):
#        print("yum")
#class dog(Animal):
#    def bark(self, age):
#        self.age = age
#        print("woof")
#        if age <= 5:
#            print ("you are a young dog")
#        else:
#            print ("you are an old dog")
#class cat(Animal):
#    def meow(self):
#        print("meow")
#        
##Snoopy= dog()
##Snoopy.bark(8)
##Snoopy.eat()
##
#class robot():
#    def move(self):
#        print("move move move")
#class cleanRobot(robot):
#    def clean (self):
#        print("look at me! I can clean!")
#class cookRobot(robot):
#    def cook(self):
#        print ("Maybe you can clean, but I can cook! nom nom")
#        
##joey=cleanRobot()
##joey.clean()
#
#class superRobot():
#    def __init__(self):
#        self.o1 = cleanRobot()
#        self.o2 = Animal()
#    def clean (self):
#        return self.o1.move()
#    def eat(self):
#        return self.o2.eat()
#machineDog= superRobot()
#machineDog.clean()
#machineDog.eat()


#
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
    