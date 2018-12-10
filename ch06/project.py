# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:29:28 2018

@author: 612436112
"""

#class Relationship():
#    def __init__ (self, name, score=0 , months=10 , number_friends=0, do_brunch=0):
#        self.name=name
#        self.score=score
#        self.months=months
#        self.number_friends=number_friends
#        self.do_brunch = do_brunch
#
#
#class Length(Relationship):
#
#   def __init__ (self, name, score=0, months=0):
#        Relationship.__init__ (self, name, score=0)
#        self.months=months
#
#   def how_long(self):
#        if self.months >= 5:
#            print('month', self.months)
#            self.score += 10
#        print('score', self.score)
#        return self.score
#
#class Friends(Relationship):
#
#   def __init__ (self, name, score=0,number_friends=0):
#         Relationship.__init__ (self, name, score=0)
#         self.number_friends=number_friends
#
#   def how_friends(self):
#        if number_friends >= 3:
#            self.score += 5
#        elif number_friends >= 5:
#            self.score += 10
#            
#        return self.score
#
#class Brunch(Relationship):
#
#   def __init__ (self, name, score=0,do_brunch=0):
#         Relationship.__init__ (self, name, score=0)
#         self.do_brunch = do_brunch
#
#   def brunch_test(self):
#        if do_brunch == "yes":
#            self.score += 10  
#        print('score', self.score)
#        return self.score
#    
#    
##class Move_in(Relationship):
##    def __init__ (self, name, score=0,)
##         Relationship.__init__ (self, name, score=0)
##         self.score = score
##         
##    def big_move (self):
##        if number_friends >= 3:
##            self.score += 5
##        elif number_friends >= 5:
##            self.score += 10
##            
##        return self.score
#            
#            
#
#score=0
#name=input("What is your partner's name? ")
#months=int(input("How many months have you been together? "))
#friends=int(input("How many friends have you met? "))
#brunch = input("Do you brunch on the weekends? (yes or no) ")
#
#
#mike_relationship= Relationship(name, score, months,friends,brunch)
#mike_relationship.how_long()
#mike_relationship.how_friends()
#mike_relationship.brunch_test()
#print(mike_relationship.score)

#try 2 ----
class Relationship():
 def __init__ (self, name, score=0, months=0, number_friends=0, do_brunch=0):
      self.name = name
      self.score = score
      self.months = months
      self.number_friends = number_friends
      self.do_brunch = do_brunch

 def how_long(self,months):
      if self.months >= 5:
          #print('month', self.months)
          self.score += 10
      #print('score', self.score)
      return self.score

 def how_friends(self, number_friends):
      if self.number_friends >= 3:
          self.score += 5
      elif number_friends >= 5:
          self.score += 10
      #print('score', self.score)
      return self.score
 def brunch_test(self, do_brunch):
       if self.do_brunch == str("yes"):
           self.score += 10
       #print('score', self.score)
       return self.score
 def big_move (self,score):
      if self.score >= 10:
          print ("move in!")
      elif self.score <= 5:
          print ("move on!")

     # return self.score



score = 0
name=input("What is your partner's name? ")
months=int(input("How many months have you been together? "))
friends=int(input("How many friends have you met? "))
brunch = input("Do you brunch on the weekends? (yes or no) ")


mike_relationship= Relationship(name, score, months,friends,brunch)
mike_relationship.how_long(months)
mike_relationship.how_friends(friends)
mike_relationship.brunch_test(brunch)
mike_relationship.big_move(score)

# not inh

class Relationship():
  def __init__ (self, name, score=0):
      self.name=name
      self.score=score


class Length(Relationship):

 def __init__ (self, name, score=0, months=0):
      Relationship.__init__ (self, name, score=0)
      self.months=months

 def how_long(self):
      if self.months >= 5:
          #print('month', self.months)
          self.score += 10
      #print('score', self.score)
      return score

class Friends(Relationship):

 def __init__ (self, name, score=0,number_friends=0):
       Relationship.__init__ (self, name, score=0)
       self.number_friends=number_friends

 def how_friends(self):
      if self.number_friends >= 3:
          self.score += 5
      elif number_friends >= 5:
          self.score += 10
      #print('score', self.score)
      return score

class Brunch(Relationship):

 def __init__ (self, name, score=0,do_brunch=0):
   Relationship.__init__ (self, name, score=0)
   self.do_brunch = do_brunch

 def brunch_test(self):
       if self.do_brunch == str("yes"):
           self.score += 10
       #print('score', self.score)
       return score


class Move_in(Relationship):
  def __init__ (self, name, score):
       Relationship.__init__ (self, name, score)
       self.score = score

  def big_move (self):
      if self.score >= 10:
          print ("move in!")
      elif self.score <= 5:
          print ("move on!")

     # return self.score



score = 0
name=input("What is your partner's name? ")
months=int(input("How many months have you been together? "))
friends=int(input("How many friends have you met? "))
brunch = input("Do you brunch on the weekends? (yes or no) ")


mike_length_relationship= Length(name, score, months)
mike_length_relationship.how_long()
score= score + mike_length_relationship.score
mike_friends= Friends(name,score,friends)
mike_friends.how_friends()
score= score + mike_friends.score
mike_brunch = Brunch(name,score,brunch)
mike_brunch.brunch_test()
score += mike_brunch.score
mike_move= Move_in(name,score)
mike_move.big_move()
