# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:46:48 2020

@author: takuya5715
"""

with open("input.txt") as f:
    lines = f.readlines()
    m = int(lines[-1])
    data = lines[:-1]
    isList = []
    for line in data:
        l = list(line.split(":"))
        l[0] = int(l[0])
        isList.append(l)
    isList.sort(key=lambda x:x[0])
    
    cnt = 0
    for l in isList:
        if(m % l[0] == 0):
            print(l[1][:-1],end='')
            cnt += 1
    if(cnt == 0):
        print(m)