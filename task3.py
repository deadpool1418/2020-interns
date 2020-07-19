#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:04:49 2020

@author: vijay
"""

import json
from datetime import timedelta, date
import matplotlib.pyplot as plt


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


with open('data.json') as f:
    perf = json.load(f)
rates=perf['rates']

with open('latest-rates.json') as f:
    perf = json.load(f)
lrates=perf['rates']
print("Enter currency symbol1 (eg: INR for Indian Rupees)")
sym1=input()
print("Enter currency symbol2 (eg: INR for Indian Rupees)")
sym2=input()
print("Enter start date (YYYY-MM-DD)")
y,m,d=map(int,input().split("-"))
start_date = date(y,m,d)
print("Enter end date (YYYY-MM-DD)")
y,m,d=map(int,input().split("-"))
end_date = date(y,m,d)

date=[]
l1=[]
l2=[]
for single_date in daterange(start_date, end_date):
    try:
        l1.append(rates[single_date.strftime("%Y-%m-%d")][sym1])
        l2.append(rates[single_date.strftime("%Y-%m-%d")][sym2])
        date.append(single_date.strftime("%Y-%m-%d"))
    except:
       None
plt.figure(figsize=(30,20)) 
plt.subplot(1,2,1)       
plt.plot(date,l1,label=sym1)
plt.xlabel("Dates in month of Jan 2019")
plt.xticks(rotation=90)
plt.ylabel(sym1+" exchange rates (Current Rate: "+str(lrates[sym1])+")" )
l=plt.legend(loc="upper left")
l.get_texts()[0].set_text(sym1+"(Current Rate: "+str(lrates[sym1])+")")
plt.subplot(1,2,2)
plt.plot(date,l2,label=sym2)
plt.xlabel("Dates in month of Jan 2019")
plt.xticks(rotation=90)
plt.ylabel(sym2+"exchange rates (Current Rate: "+str(lrates[sym2])+")" )
l=plt.legend(loc="upper left")
l.get_texts()[0].set_text(sym2+"(Current Rate: "+str(lrates[sym2])+")")
plt.show()  