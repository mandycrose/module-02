## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""

#### debugging #####
userInput = input('please give a number ')
print(type(userInput))

userInput = input('please give a number ')
def simpleOperation(userInput):
intInput = int(userInput)
result = intInput - 2
return result
def nestedOperation(result):
result = simpleOperation(userInput)
result2 = result * 2
return result2
result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)



##### run debugging on task ### 
#class Relationship():
# def __init__ (self, name, score=0, months=0, number_friends=0, do_brunch=0):
#      self.name = name
#      self.score = score
#      self.months = months
#      self.number_friends = number_friends
#      self.do_brunch = do_brunch
#
# def how_long(self,months):
#      if self.months >= 5:
#          #print('month', self.months)
#          self.score += 10
#      #print('score', self.score)
#      return self.score
#
# def how_friends(self, number_friends):
#      if self.number_friends >= 3:
#          self.score += 5
#      elif number_friends >= 5:
#          self.score += 10
#      #print('score', self.score)
#      return self.score
# def brunch_test(self, do_brunch):
#       if self.do_brunch == str("yes"):
#           self.score += 10
#       #print('score', self.score)
#       return self.score
# def big_move (self,score):
#      if self.score >= 10:
#          print ("move in!")
#      elif self.score <= 5:
#          print ("move on!")
#
#     # return self.score
#
#
#
#score = 0
#name=input("What is your partner's name? ")
#months=int(input("How many months have you been together? "))
#friends=int(input("How many friends have you met? "))
#brunch = input("Do you brunch on the weekends? (yes or no) ")
#
#
#mike_relationship= Relationship(name, score, months,friends,brunch)
#mike_relationship.how_long(months)
#mike_relationship.how_friends(friends)
#mike_relationship.brunch_test(brunch)
#mike_relationship.big_move(score)


#orders=["1", "2", "3"]
#print(orders)
#orders.append("4","5")
#print(orders)

list1 = range(5, 15, 3)
print(list1)

