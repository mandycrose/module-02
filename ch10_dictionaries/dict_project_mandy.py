# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:10:37 2018

@author: 612436112
"""

phonebook= {"mandy":(111,999,666, "London",21), 
            "cem":(222,888,555, "Oxford",31), 
            "handan":(333,777,444,"cambridge",41)}
def whatWant(phonebook):
    choice = input("what would you like to do? If you would like to add a contact to the phone book, enter 1. \nIf you would like to sort the phonebook, enter 2 /n If you would like to calculate the difference in age with the queen, enter 3 \n ")
    if choice == "1":
        return phonebook_add(phonebook)
    elif choice == "2":
        return sort_phonebook(phonebook)
    elif choice == "3":
        return queenAge(phonebook)
    else:
        return print("That is not a valid choice")
def phonebook_add (phonebook):
    name= input("what is the name you would like to enter?")
    number = input ("what are the last three digits of the phone number?")
    luckyN = int(input("what is the lucky number? "))
    postCode = input ("what is the post code? ")
    town = input ("what is the town? ")
    age= input("what is the age of the new contact ")
    phonebook[name]=[number,luckyN,postCode,town,age]
    want_sort = input ("would you now like to sort dict? y/n")
    if want_sort == "y":
        return sort_phonebook(phonebook)
    elif want_sort == "n":
        return phonebook

def sort_phonebook(phonebook):
  sort_by = input ("If you would like to sort the phonebook by name, enter 1 \nIf you would like to sort by town enter 2 \nEnter 3 to sort by lucky number \n ")
  if sort_by == "1":
      return print (sorted(phonebook.items(), key = lambda kv:kv [0], reverse = True))
  elif sort_by == "2":
      return print(sorted (phonebook.items(), key = lambda kv:kv [1][3],reverse =True))
  elif sort_by == "3":
      return  print(sorted(phonebook.items(), key = lambda kv:kv [1][1], reverse = True))
#  else:
#      return sort_phonebook(phonebook)

def queenAge(phonebook):
    classmate = input("what is the name of the classmate that you would like to compare age with?  ")
    if classmate in phonebook:
        queen_age = 92 - phonebook[classmate][4]
        return print("Your classmate {} is {} years younger than the Queen!".format(classmate,queen_age)) 
    else:
        return print("that is not a valid entry")   
def print_phonebook(newPhoneBook):
    file=open("Phonebook.txt", "w+")
    file.write(newPhoneBook)
    file.close()        
    
whatWant(phonebook)     
newPhoneBook = str(list(phonebook.items()))           
print_phonebook(newPhoneBook)                 


##### work in progress##############              
#  sorted(phonebook.items(), key = lambda kv:kv [0])
##sort_town = sorted (phonebook.items(), key = lambda kv:kv [1][3])    
#sort_luckyN = sorted(phonebook.items(), key = lambda kv:kv [1][1])
##print(sort_name)
##print(sort_town)
##print(sort_luckyN)

##sort_name = sorted(phonebook.items(), key = lambda kv:kv [0])
##sort_town = sorted (phonebook.items(), key = lambda kv:kv [1][3])    
##sort_luckyN = sorted(phonebook.items(), key = lambda kv:kv [1][1])
##print(sort_name)
##print(sort_town)
##print(sort_luckyN)
# def phoneBook():
#    name= input("what is the name you would like to enter?")
#    number = input ("what are the last three digits of the phone number?")
#    luckyN = input("what is the lucky number? ")
#    postCode = input ("what is the post code? ")
#    town = input ("what is the town? ")
#    phoneBook_dict = {name:number, luckyN, postCode,Town}
#    return phoneBook
    
    