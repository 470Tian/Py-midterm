# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:03:21 2020

@author: user
"""

m=int(input("請輸入階層值:"))
num=i=1
while True:
    num*=i
    if num>m:
        break
    i+=1
print("超過M為",m,"的最小階層N值為:",i)



