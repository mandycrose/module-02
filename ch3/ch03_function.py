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
