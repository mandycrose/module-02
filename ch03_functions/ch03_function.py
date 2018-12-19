# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:49:19 2018

@author: 612436112
"""
def add_two_numbers(a,b):
    answer= a+b
    print ("{} plus {} is {}".format(a, b, answer))

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)

    
def cent_to_fahrenheit(cent):
    fahrenheit= (cent* 9.0) / 5.0 + 32
    print ("Converting centigrade to fahrenheit:")
    print (cent, "degrees centigrade is equal to" , fahrenheit , "degrees farenheit")



def cent_to_fahrenheit(cent):
    fahrenheit= (cent* 9.0) / 5.0 + 32
    print ("Converting centigrade to fahrenheit:")
    print (str(cent) + " degrees centigrade is equal to " + str(fahrenheit) + " degrees farenheit")

def temperature_conversion(centigrade):
    fahrenheit=((centigrade*9.0)/5.0)+32
    kelvin=(centigrade+273.15)
    return(fahrenheit, kelvin)

############### functions with return ########################################
    
def temperature_conversion(centigrade):
    fahrenheit=((centigrade*9.0)/5.0)+32
    kelvin=(centigrade+273.15)
    return(fahrenheit, kelvin)

fahrenheit1, kelvin1 = temperature_conversion(31)
new_var= fahrenheit1, kelvin1
print(new_var)

fahrenheit2, kelvin2 = temperature_conversion(45)
new_var_2= fahrenheit2, kelvin2
print(new_var_2)

