# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:24:58 2017

@author: Stefano
"""
import numpy as np
import matplotlib.pyplot as plt

print "Make a 3 row x 4 column array of random numbers"
x = np.random.random((3,4))
print x

print "Add 1 to every element"
x = x + 1
print x
print

print "Get the element at row 1, column 2"
print x[1, 2]
print

# The colon syntax is called "slicing" the array. 
print "Get the first row"
print x[0, :]
print

print "Get every 2nd column of the first row"
print x[0, ::2]
print

print "Max is ", x.max()
print "Min is  ", x.min()
print "Mean is ", x.mean()

print "Max for line is ", x.max(axis=1)

x = np.random.binomial(500, .5) # 500 launches with probability 1/2
print "number of heads:", x

# 3 ways to run the simulations

# loop
heads = []
for i in range(500):
    heads.append(np.random.binomial(500, .5))
histogram1 = plt.hist(heads, bins=10)

# "list comprehension"
heads = [np.random.binomial(500, .5) for i in range(500)]
histogram2 = plt.hist(heads, bins=10)

# pure numpy
heads = np.random.binomial(500, .5, size=500)
histogram3 = plt.hist(heads, bins=10)

heads.shape