# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:02:26 2020

@author: user
"""
list1=[]
n=int(input("請輸入正整數n:"))
for i in range(1,n):
    if n%i==0:
       list1.append(i)

a=sum(list1)
if a==n:
    print("perfect")
elif a>n:
    print("abundant")
else:
    print("deficient")