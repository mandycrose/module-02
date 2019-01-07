#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:02:50 2019

@author: mandyrose
"""

from Shapes import *
from pylab import random as r 


class MovingShape:
    def __init__(self,frame,shape,diameter): 
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        self.x = 0 
        self.y = 0

    # random velocities and movement
        self.dx = 5 + 10 * r() 
        if r() < 0.5:
            self.dx = 5 + 10 * r()
        else:
            self.dx = -5 + -10 * r()
            
        self.dy =  5 + 10 * r()
        if r() < 0.5:
            self.dy = 5 + 10 * r()
        else:
            self.dy = -5 + -10 * r()
            
        self.goto(self.x, self.y)

    # start position of x and y

        self.minx = diameter / 2
        self.maxx = frame.width - (diameter / 2)
        self.miny = diameter / 2
        self.maxy = frame.height -(diameter / 2)
        
    # adding random start
    
        self.x = self.minx + r () * (self.maxx - self.minx)
        self.y = self.miny + r () * (self.maxy - self.miny)
        
    #hit- wall   
          
    def moveTick(self): 
        if self.x <= self.minx or self.x >= self.maxx:
            self.dx = (self.dx) * -1
        if self.y <= self.miny or self.y >= self.maxy:
            self.dy =- self.dy
        self.x += self.dx
        self.y += self.dy
        self.figure.goto(self.x, self.y)
        
    def goto(self,x,y):
        self.figure.goto(x,y)

    
#################################################### 

class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
#################################################### 
        
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        
#################################################### 
        
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
