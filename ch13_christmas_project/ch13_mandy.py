# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:25:25 2019

@author: 612436112
"""

### task 1 #### 

class Person:
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        if gender == "m":
            self.isMale = True
        elif gender == "f":
            self.isMale = False
        else:
            print("gender not recognised")
            
### task 2 ###
            
    def greetingInformal(self):
        print("hi {}! How are you?".format(self.name))
        
    def greetingFormal(self):
        if self.isMale:
            return"Hello Mr. {}! How are you?".format(self.name) 
        else:
            return"Hello Miss {}! How are you?".format(self.name) 
            
### task 3 #### 
            
    def greetingAgeBased(self):
        if self.age < 18:
            return "Welcome, young {}".format(self.name)
        elif self.age > 60:
            return "Welcome, venerable {}".format(self.name)
        else:
            return self.greetingFormal() 
        
## task 4/5/6 ### 
class Wizard(Person):   
    
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,"m")

    def greetingFormal(self):
        
       return "Welcome, Mr {}. You’re a fine wizard!".format( self.name)
        
    def spell(self):
        return "Expelliarmus!"


person1 = Person("Mindy", 14, "f")
person2 = Person("Jimmy", 15,"m")
person3= Wizard("Jim", 55,"m")

print(person1.name)
print(person1.greetingFormal())
print(person1.greetingAgeBased())
print(person3.greetingFormal())

