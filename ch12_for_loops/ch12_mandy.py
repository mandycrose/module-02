## -*- coding: utf-8 -*-
#"""
#Created on Thu Dec 20 09:28:24 2018
#
#@author: 612436112
#"""
##### chapter 12 - FOR loop ######

#### task 1 ### 
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print (item)
    
###### task 2 ##### 
values = [875, 23, 451]

for v in values:
    print('hello '+str(v))
    
for v in values:
    print('---> '+str(v+50))
    
#while v in values: ### would go forever
    #print('hello '+str(v))
    

### task 3 ### 

list1 = ["this", "and", 55, "different", "things"]

for i in list1:
    print("***", i)
    
### task 4 - loop str ###

for letter in "yes":
    print(letter)

var1 = "hello! it is nice to meet you!"
for i in var1: ## prints every letter/character 
    print(i)

var2 = var1.split() ## how to make a string into a list -- .split() ## 
for i in var2:
    print(i) ## now will print each word out ## 
    
## task 5 - loop in tuple ## 

tuple1 = ("hello", "how", "are", "you")
for a in tuple1:
        print(a)
        
# task 6/7  loop in dictonary ##
        
densities = {"iron":7.8, "gold":19.3, "zinc":7.13, "lead":11.4}
metals = list(densities.keys())
price= list(densities.values())
print(metals)

metals.sort(reverse = True, key=lambda m:densities[m])
print(metals)

for metal in metals:
    print (metal, densities [metal]) ## calling the key so you get the value in dict ## 

print(densities.items()) ## print key and value in list format ## 

for item in densities.items(): ## loop for printing key/value in dict ##
    print (item)
    
for item in sorted(densities.items()): ## loop for printing key/value in dict sorted ##
    print (item)    
    
products = {'iron' : (7.8, 0.93, 6000), 'gold': (19.3, 1.58, 26000), 'zinc': (7.13, 0.42, 15800), 'lead': (11.4, 0.75, 7300)}
metals = list(products.keys())
metals.sort()
print(metals)
sort_value = sorted(products.items(), key=lambda kv:kv[1][1], reverse= True)

for metal, metalValue in sort_value: ## taking the key and value ## 
    print ("metal:", metal, "price is", metalValue [1]) ## this is pulling the 1 index from the tuple

for metal in metals:
    print(metal, "share price:", products[metal][1]) ## calling 1 index of values 
for metal in metals:
    print(metal, "avail shares:", products[metal][2])  ## to call dic value - dict[key] ##
    
 ### formatting ###    
#for metal in metals:
#    print("{0:>8} = {1:5.1f}".format(metal,densities[metal])) # .1f is float 
 
    
##### task 8 #####
 
for metal in metals:
    if products[metal][0] <8:
        print(metal,"is under 8 with a value of", products[metal][0])
    else:
        print (metal,"is above 8 with a value of", products[metal][0])

#### task 9 #### 

values = [2,4,6,8,10]
total = 0 
for val in values:
    total += val
print("total:", total) 
print("total:" + str(total)) ## reminder: if use + , you need to change to str

def add_values(num):
    sumV = 0
    for val in num:
        sumV += val
    return sumV
print("sumV total:",add_values([4,6,3,5]))

## task 10 -- index loops ## 

for i in range(len(values)): ## for is calling the index when using range(len())
    values[i] = values[i] + 1
print  (values)

## taske 11 -- range loops ## 
for i in range(4):
    print(i)

for i in range(4,14,2): ## start, finish, skip ## 
    print(i)

## task 12 -- break in loops ## 
nums = [ 2, 45, 6667, 23, 5, 6, 800]

for n in nums: 
    if n > 50:
        print ("found a number over 50:", n)
        break
    

#### counting colors ###### 
colours= ["red", "red", "red", "red", "blue", "yellow", "blue", "brown"]
new_d= {}
for item in colours: 
     if item not in new_d:
         new_d[item] = 1 
     else: 
         new_d[item] += 1
print (new_d)

## task 13 nested loops ## 
  
outer_vals = [1, 2, 3]
inner_vals = ["A", "B", "C"]
dict = {}
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)
        dict[oval] = ival

### task 14 -- multiplication table ### 

for i in range(1,7): 
    for j in range (1,11): 
        print("{0:>3}".format(i*j), end ='')
    print("\n")
