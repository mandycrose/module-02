# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:53:42 2018

@author: 612436112
"""
#import math 
#print(math.pi)

#from math import*
#print(pi)

#from math import pi
#print(pi)
#
#import math as m 
#print(m.pi)

#print ("What’s your name?")
#name = input()
#print ("Hello {}!".format(name))
#
#name= input("what is your name?      ")
#location= input ("where are you from?  ")
#print ("Hello {}!That is cool you are from {}".format(name.upper(),location))
#
#name= input("what is your name?      ")
#input ("where are you from?")

#print ("Hello {}!".format(name.upper()) +)
#
#def hello_world():
#    print ("Hello World!")
#hello_world()
#
#def your_name ():
#    print("mandy")
#    print(2+2)
#your_name()

#def whereAreyouFrom ():
#    name= input("what is your name?  ")
#    print ("nice to meet you {}" .format(name)) 
#    city= input("where are you from?")
#    askTime= input ("wow {}! that is so cool! I have a friend from {}. How many years have you lived there? ".format (name, city))
#    longtime = int(askTime) + 10
#    print ("{} years is a long time! In 10 years you will have lived there for {} years".format(askTime, longtime))
#whereAreyouFrom ()
#
#def hello_world_2args (a,b,c,d):
#    print("{} {} I {} {}!".format(a,b,c,d))
#a1= "hello"
#b1= "world"
#a2= "love"
#b2= "coding"
#
##hello_world_2args(a1,b1)
##hello_world_2args(a2,b2)
#hello_world_2args(a1,b1,a2,b2)
#
#hello_world_2args("hello","world","love","coding")
#
#def add_two_numbers(a,b):
#    answer= a+b
#    print ("{} plus {} is {}".format(a, b, answer))
#add_two_numbers(2,2)
#
#def convert_distance(miles):
#    kilometers = (miles * 8.0) / 5.0
#    print ("Converting distance in miles to kilometers:")
#    print ("Distance in miles:", miles)
#    print ("Distance in kilometers:", kilometers)
#convert_distance(44)
#convert_distance(122.5)
#
#def cent_to_fahrenheit(cent):
#    fahrenheit= (cent* 9.0) / 5.0 + 32
#    print ("Converting centigrade to fahrenheit:")
#    print (cent, "degrees centigrade is equal to" , fahrenheit , "degrees farenheit")
#
#cent_to_fahrenheit(30)

#def cent_to_fahrenheit(cent):
#    fahrenheit= (cent* 9.0) / 5.0 + 32
#    print ("Converting centigrade to fahrenheit:")
#    print (str(cent) + " degrees centigrade is equal to " + str(fahrenheit) + " degrees farenheit")
#
#cent_to_fahrenheit(30)

#def convert_distance(miles):
#    kilometers = (miles * 8.0) / 5.0
#    print ("Converting distance in miles to kilometers:")
#    print ("Distance in miles:", miles)
#    print ("Distance in kilometers:", kilometers)
#    return (kilometers)
#convert_distance(44)
#convert_distance(122.5)
#
#London_ipswich = convert_distance(10)
#New_place = London_ipswich+30
#
#print(New_place)

def temperature_conversion(centigrade):
    fahrenheit=((centigrade*9.0)/5.0)+32
    kelvin=(centigrade+273.15)
    return(fahrenheit, kelvin)
#
#fahrenheit1, kelvin1 = temperature_conversion(31)
#new_var= fahrenheit1, kelvin1
#print(new_var)
#
#fahrenheit2, kelvin2 = temperature_conversion(45)
#new_var_2= fahrenheit2, kelvin2
#print(new_var_2)

#def temperature_conversion(centigrade):
#    fahrenheit=((centigrade*9.0)/5.0)+32
#    kelvin=(centigrade+273.15)
#    return("fahrenheit:", fahrenheit , "kelvin:",kelvin )
#
#temperature_conversion(30)
#
#  homework 
#print("I will now count my chickens:")
#print ("Hens", 25 + 30 / 6)
#print( "Roosters", 100 - 25 * 3 % 4)
#print( "Now I will count the eggs")
#print( 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 )
#print("Is it true that 3 + 2 < 5 - 7?")
#print(3 + 2 < 5 - 7)

#days= "Mon Tue Wed Thu Fri Sat Sun"
#months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#print ("Here are the days: ", days)
#print("Here are the months: ", months)

#bool_one = 5 != 7 
#print(bool_one)

#import ch2_mandy
