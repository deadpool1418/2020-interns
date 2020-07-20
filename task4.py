#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 08:09:08 2020

@author: vijay
"""
import requests
import json
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
sym=input("Enter symbol 1")
sym2=input("Enter symbol 2")
print("Enter start date (YYYY-MM-DD)")
y,m,d=map(int,input().split("-"))
start_date = date(y,m,d)
print("Enter End date (YYYY-MM-DD)")
y,m,d=map(int,input().split("-"))
end_date = date(y,m,d)
url='https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols=INR,GBP'.format(start_date,end_date)
response = requests.get(url)
f = response.json()
rates=f['rates']

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

f.write('''<svg width="1500" height="1500" xmlns="http://www.w3.org/2000/svg">\n''')
f.write('''<rect width="100%" height="100%" fill="white" />\n''')
f.write("<text x=\"100\" y=\"15\" fill=\"red\">"+sym+"Exchange rates (Base EUR)"+"</text>\n")
f.write("<text x=\"100\" y=\"30\" fill=\"green\">"+"Start Date: "+str(start_date)+"</text>\n")
f.write("<text x=\"100\" y=\"45\" fill=\"green\">"+"End Date: "+str(end_date)+"</text>\n")
f.write("<text x=\"100\" y=\"60\" fill=\"green\">"+"Max Rate: "+str(mx)+"</text>\n")
f.write("<text x=\"100\" y=\"75\" fill=\"green\">"+"Min Rate: "+str(mn)+"</text>\n")
x,y=[],[]
for i in range(len(l1)):
    a=350-150*(l1[i]-mn)/(mx-mn)
    b=100+i*15
    x.append(b)
    y.append(a)    
    f.write('''<circle cx='''+'''"'''+str(b)+'''"'''+''' cy='''+'''"'''+str(a)+'''"'''+''' r="3"/> \n''')
    f.write("<text x=\"" + str(b-5) + "\" y=\"400\" fill=\"red\" style=\"font: 12px sans-serif;\" transform=\"rotate(90,"+str(b-5)+",400)\">"+date[i]+"</text>")
for i in range(len(x)-1):
    f.write("<line x1=\"" + str(x[i]) + "\" y1=\"" + str(y[i]) +"\" x2=\"" + str(x[i+1]) + "\" y2=\"" + str(y[i+1]) + "\" stroke=\"" + str("black") + "\" />")
f.write("</svg>")    
f=open("graph1.svg","w")
f.write('''<svg width="1500" height="1500" xmlns="http://www.w3.org/2000/svg">\n''')
f.write('''<rect width="100%" height="100%" fill="white" />\n''')
f.write("<text x=\"100\" y=\"15\" fill=\"red\">"+sym2+"Exchange rates (Base EUR)"+"</text>\n")
f.write("<text x=\"100\" y=\"30\" fill=\"green\">"+"Start Date: "+str(start_date)+"</text>\n")
f.write("<text x=\"100\" y=\"45\" fill=\"green\">"+"End Date: "+str(end_date)+"</text>\n")
f.write("<text x=\"100\" y=\"60\" fill=\"green\">"+"Max Rate: "+str(mx1)+"</text>\n")
f.write("<text x=\"100\" y=\"75\" fill=\"green\">"+"Min Rate: "+str(mn1)+"</text>\n")
x,y=[],[]
for i in range(len(l2)):
    a=350-150*(l2[i]-mn1)/(mx1-mn1)
    b=100+i*15
    x.append(b)
    y.append(a)
    f.write('''<circle cx='''+'''"'''+str(b)+'''"'''+''' cy='''+'''"'''+str(a)+'''"'''+''' r="3"/> \n''')
    f.write("<text x=\"" + str(b-5) + "\" y=\"400\" fill=\"red\" style=\"font: 12px sans-serif;\" transform=\"rotate(90,"+str(b-5)+",400)\">"+date[i]+"</text>")
for i in range(len(x)-1):
    f.write("<line x1=\"" + str(x[i]) + "\" y1=\"" + str(y[i]) +"\" x2=\"" + str(x[i+1]) + "\" y2=\"" + str(y[i+1]) + "\" stroke=\"" + str("black") + "\" />")

f.write("</svg>")    
