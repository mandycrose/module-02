### -*- coding: utf-8 -*-
##"""
##Created on Thu Dec 13 09:45:32 2018
##
##@author: 612436112
##"""
################################################################
#lists and tuples
################################################################

#### task 1 ########

#my_favourite_fruits = ["apple", "orange", "banana"]
##
#x = ["this", 55, "that", my_favourite_fruits] #list can contain mix type of data!
#
#x = ["this", 55, "that", my_favourite_fruits]
#
#x[3][0]

##### task 2 ########

#x.remove(my_favourite_fruits)
#print(x)
#
#x[1] = "and"   #update list item value by using index of the item in the current list
#
#x.append("again")
#
#print(x)
#
#y = x.append("hello")
#
#print(x)
#print(y)
#
#y=x
#
#x.append("test 1")
#x.append("test 2")
#
#print (y)
#
#y.append("test 3")
#print(x)
#print(y)
#
#x = ["the", "cat", "sat"]
#y = ["on", "the", "hat"]
#z= x+y
#print (z)
#
#print(list(zip(x,y)))
#print(z*3)
#

############## task 3 - slicing #####################

#a=["the", "cat", "sat","on", "the", "hat"]
#print(a[:3])
#
#print(a[2:4])
#print(a[-1:])
#print(a[-1])
#print(a[-3:-1])

####### task 4 - sorting ###############
#x = [7,11,3,9,2]
#y= sorted(x,reverse=True) #this does not change x, need to assign to variable 
#print(y)
#
#x.sort(reverse= True) #changes x 
#print(x)
#
#toppings = ["pepperoni","pinapple","cheese","sausage","olives","anchovies","mushrooms"]
#toppings.sort()
#print (toppings)
#new_toppings = sorted(toppings, reverse= True)
#print(new_toppings)
###### task 5 - tuples #######
#list
##
#a = [0,1,2,3,4,5,6,7,8,9]
#del a [-1]
##
#print(a)
##
##tuple
##b = (0,1,2,3,4,5,6,7,8,9)
###del b [-1]
##print(b) # error message that tuple does not support deletion 
##
#a[2]= "hello"
#print(a)
#
###b[2]= "hello" # again, tuple can not be changed 
##
#a.append("this is an appendment")
#print(a)
#
##b.append("this is an appendment") # can't append tuple 
#print(b)

#### task 6 - lambda function ######

b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple","3","orange", "banana"]
x = ["afsf", "1", "csdf", "dsdf","fsdf", "sdfe"]
z = ["gsdf", "2", "isdb", "jsdf", "lsdf","ksfs" ]


x2= [("a",3,z),("c", 1, x),("b",5,myFavF)]
#print(sorted(x2))

print(sorted(x2, key=lambda s:s[2][2][-1])) 



