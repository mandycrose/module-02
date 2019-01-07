#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:10:57 2019

@author: mandyrose
"""

from MovingShapes import *


frame = Frame()
shape1 = Square (frame,100) 

for i in range(100):
    shape1.moveTick()
