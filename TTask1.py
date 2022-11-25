#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from urllib.request import Request,urlopen
import re

hdr = {'user-Agent': 'Mozilla/5.0'}
Name = []
Price = []
Original_Price = []
Discounted_Price = []
Image = []

for i in range(1,12):
    site = "https://yoshops.com/products?page=" +str(i)
    req = Request(site , headers = hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    name = soup.find_all('span' , class_="product-title")
    for i in range(len(name)):
        Name.append(name[i].text)
    price = soup.find_all('div' , class_="product-price")
    for j in range(len(price)):
        Price.append(price[j].text)
    for k in Price:
        Original_Price.append(k.split("₹")[1])
        Discounted_Price.append(k.split("₹")[2])
    image = soup.find_all('div', class_="product-thumb-inner")
    for im in image:
        print(im.find("img")["src"])
        Image.append(im.find("img")["src"])
        
    hdr = {'User-Agent': 'Mozila/5.0'}
    Link = []
    for i in range(1,12):
        site = "https://yoshops.com/products?page=" +str(i)
        req = Request(site , headers = hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)
        link = soup.find_all('a' , class_='product-Link')
    for l in link:
        Link.append("https://yoshops.com/"+l["href"])
        
    j1 =0
    NoImage = []
    for i1 in Image:
        if i1 == "//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png": 
            NoImage.append(j1)
        
    j1+=1
        


# In[ ]:


from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.DataFrame({'Name':[Name[162],Name[393],Name[394],Name[395],Name[397],Name[398],Name[399],Name[400],Name[401],Name[415],Name[417],Name[418]],
                   'Original_Price':[Original_Price[162],Original_Price[393],Original_Price[394],Original_Price[395],Original_Price[397],Original_Price[398],Original_Price[399],Original_Price[400],Original_Price[401],Original_Price[415],Original_Price[417],Original_Price[418]],
                   'Discounted_Price':[Discounted_Price[162],Discounted_Price[393],Discounted_Price[394],Discounted_Price[395],Discounted_Price[397],Discounted_Price[398],Discounted_Price[399],Discounted_Price[400],Discounted_Price[401],Discounted_Price[415],Discounted_Price[417],Discounted_Price[418]],
                   'URL':[Link[162],Link[393],Link[394],Link[395],Link[397],Link[398],Link[399],Link[400],Link[401],Link[415],Link[417],Link[418]],
                   'Contact_No.' : ['+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858','+91-9080749858'],
                   'Address' : ['34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015','34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015']
                  })
                      
writer = ExcelWriter(No_Image2.xlsx)
df.to_excel(writer,'sheet1', index=False)
writer.save()


# In[ ]:




