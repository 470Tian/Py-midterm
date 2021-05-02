# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:26:43 2020

@author: user
"""

n=input("請輸入第一組數字")
m=input("請輸入第二組數字")
A=0
B=0
for i in range(0,len(m)):
    a=n.count(m[i])
    if a>0:
        m_fi=m.find(m[i])
        n_fi=n.find(m[i])
        if m_fi==n_fi:
            A+=1
        else:
            B+=1
if A==len(m):
    print(str(A)+"A"+str(B)+"B全對")
else:
    print(str(A)+"A"+str(B)+"B加油")


