# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:05:27 2018

@author: 612436112
"""

import sys

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
         print('yum')
         
class Dog(Animal):
    def bark(self):
        print('Woof!')
        
class Robot():
    def move(self):
            print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        
class SuperRobot():
    
    def __init__(self,name,age):
        #This class contains 3 objects'
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog(name,age)
        self.o3 = CleanRobot()
        
        
        
    def playGame(self):
        print('alphago game')
        
    def move(self):
        return self.o1.move() #using robot class method
    
    def bark(self):
        return self.o2.bark() #using dog class method
    
    def eat(self):
        return self.o2.eat() #using dog class method
    
    def clean(self):
        return self.o3.clean() #using cleanrobot method
    

#name = sys.argv[0] #input('pet\'s name: ')
#age = sys.argv[1] #int(input('pet\'s age: '))

machineDog = SuperRobot('snoopy',7)
machineDog.move()
machineDog.bark()
machineDog.eat()