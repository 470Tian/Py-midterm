# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 02:14:06 2021

@author: user
"""

data=input().split(" ")
card="A 2 3 4 5 6 7 8 9 10 J Q K".split(" ")
sum1=0
for i in data:
    sum1 += card.index(i)+1
print(sum1)
