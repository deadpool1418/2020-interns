#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

2019-01-01
2019-01-31

Created on Sat Jul 18 10:04:49 2020

@author: vijay
"""

import json
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


with open('data.json') as f:
    perf = json.load(f)
rates=perf['rates']
print("Enter symbol 1")
sym=input()
sym2=input("Enter symbol 2")
print("Enter start date (YYYY-MM-DD)")
y,m,d=map(int,input().split("-"))
start_date = date(y,m,d)
print("Enter End date (YYYY-MM-DD)")
y,m,d=map(int,input().split("-"))
end_date = date(y,m,d)
date=[]
l1=[]
l2=[]
for single_date in daterange(start_date, end_date):
    try:
        l1.append(rates[single_date.strftime("%Y-%m-%d")][sym])
        l2.append(rates[single_date.strftime("%Y-%m-%d")][sym2])
        date.append(single_date.strftime("%Y-%m-%d"))
    except:
       None

mx,mn=max(l1),min(l1)
mx1,mn1=max(l2),min(l2)
f=open("graph.svg","w")
f.write('''<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">\n''')
f.write('''<rect width="100%" height="100%" fill="white" />\n''')
f.write("<text x=\"70\" y=\"15\" fill=\"red\">"+sym+"Exchange rates (Base EUR)"+"</text>\n")
for i in range(len(l1)):
    a=350-150*(l1[i]-mn)/(mx-mn)
    b=100+i*10
    f.write('''<circle cx='''+'''"'''+str(b)+'''"'''+''' cy='''+'''"'''+str(a)+'''"'''+''' r="3"/> \n''')
    f.write("<text x=\"" + str(b-5) + "\" y=\"400\" fill=\"red\" style=\"font: 12px sans-serif;\" transform=\"rotate(90,"+str(b-5)+",400)\">"+date[i]+"</text>")
f.write("</svg>")    
f=open("graph1.svg","w")
f.write('''<svg width="1000" height="1000" xmlns="http://www.w3.org/2000/svg">\n''')
f.write('''<rect width="100%" height="100%" fill="white" />\n''')
f.write("<text x=\"70\" y=\"15\" fill=\"red\">"+sym2+"Exchange rates (Base EUR)"+"</text>\n")
for i in range(len(l2)):
    a=350-150*(l2[i]-mn1)/(mx1-mn1)
    b=100+i*10
    f.write('''<circle cx='''+'''"'''+str(b)+'''"'''+''' cy='''+'''"'''+str(a)+'''"'''+''' r="3"/> \n''')
    f.write("<text x=\"" + str(b-5) + "\" y=\"400\" fill=\"red\" style=\"font: 12px sans-serif;\" transform=\"rotate(90,"+str(b-5)+",400)\">"+date[i]+"</text>")
f.write("</svg>")    
