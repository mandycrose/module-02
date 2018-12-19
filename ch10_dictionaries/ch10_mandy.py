### -*- coding: utf-8 -*-
##"""
##Created on Thu Dec 13 15:07:18 2018
##
##@author: 612436112
##"""
#################### chapter 10 dict ####################################

######### task 1 & 2 #############

salary = {} # you create a dictonary with the {}
salary["mandy"]= 500
salary["chen"]=1000
salary["mystery"]= 5000

salary[7]= ("person1", "person2","person3")
print(salary)

print(salary["mandy"])

####### task 3 #######
tel = {"mandy": 1111, "cem": 2222, "handan": 3333, "cemal":4444} #add string and int with : and comma
print (tel)

print( tel["mandy"])
tel["mandy"]= 555 # you can overwrite old values
print (tel)

tel["mandy"] += 100 #you can add to vaules

print(tel)
print (tel["cem"])

del tel["cemal"] #delete items from dict

print(tel)
#### task 4 ##### 
print(tel.keys()) # to get the keys (str)
print(tel.values()) #to get values (int)

test_list = {"mandy":"rose", "bob":"jones", "sally": "nobody"}
#test_list = {"mandy":1, "bob": 2 , "sally": 3}

print(test_list.keys())
print(test_list.values())

##### task 5 #####

list(tel.keys())[0]

##### task 6 ##### 

k = 'eric'
if k in tel:
    print(k, ':', tel[k])
else:
    print(k, 'not found!')

#########***check on page 103**************
#print(test_list[0]) #how do you check placement?
#
##################Sorting a dictionary#####################
##### task 7 & 8 ###################
#
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k])
#labels.sort() --- if you want to just sort the keys 
print(labels)

salary_by_name= list(salary.keys())
print(salary_by_name)
#salary_by_name.sort()
#salary_by_name.sort(key=lambda k:salary[k]) #lambda sorts the value. If you wanted to just sort the key, you could do a normal .sort
print(salary_by_name)

print(sorted(counts.items(), key=lambda kv:kv[1]))


############################### metals ############################
densities = {'iron' : 7.8, 'gold': 19.3, 'zinc': 7.13, 'lead': 11.4}
metals= list(densities.keys())
print(metals)

metals.sort(reverse= True, key=lambda m:densities[m]) # "m" could be anything 
print(metals) # returns the highest density first because reverse 

print(sorted(densities.items(), key= lambda kv: kv[0], reverse= True))

products = {'iron' : (7.8, 0.93, 6000), 'gold': (19.3, 1.58, 26000), 'zinc': (7.13, 0.42, 15800), 'lead': (11.4, 0.75, 7300)}
metals = list(products.keys())
print(metals)
sort_key = sorted(products.items(), key=lambda kv:kv[0], reverse= True)
#print(sort_key) ## printing just the key
sort_density = sorted(products.items(), key=lambda kv:kv[1][0], reverse= True)
print(sort_density) # printing index 1 of key/value and 0 index of value 
sort_share = sorted(products.items(), key=lambda kv:kv[1][1], reverse= True)
print(sort_share) # index 1 of kv and index 1 of value 
sort_avail = sorted(products.items(), key=lambda kv:kv[1][2], reverse= True)
print(sort_avail) # index 1 of kv and index 2 of value 



############################# Pam Notes #############################################
#print('\nCheck if a key exists in a dictionary:')

#    
#    
#print('\nSorting a dictionary:')
#counts = {'a': 3, 'c': 1, 'b': 5}
#labels = list(counts.keys())
#labels.sort(key=lambda k:counts[k])
#print(labels)
#
#
#print('\nSorting exercise with sort():')
#students = {'kate' : (3, 14), 'pam': (5, 7), 'amina' : (2, 4), 'leanne': (9, 26)}
#
#studentsList = list(students.keys())
#
#studentsList.sort(key = lambda m:students[m][0])
#print('\nSort by month:')
#print(studentsList)
#
#studentsList.sort(key = lambda l:students[l][1])
#print('\nSort by lucky number:')
#print(studentsList)
#
#print('\nSorting exercise with sorted():')
#
#byMonth = sorted(studentsList, key = lambda m:students[m][0])
#print('\nSort by month:')
#print(byMonth)
#
#byLuckyNumber = sorted(studentsList, key = lambda l:students[l][1])
#print('\nSort by lucky number:')
#print(byLuckyNumber)
#
#
#byMonthPair = sorted(students.items(), key = lambda kv:kv[1][0])
#print(byMonthPair)
#
#byLuckyNumberPair = sorted(students.items(), key = lambda kv:kv[1][1])
#print(byLuckyNumberPair)
#




