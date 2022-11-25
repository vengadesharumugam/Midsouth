#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd
from urllib.request import Request,urlopen
import re
import time

# In[2]:


Name = []
page=[]
Price = []


# In[3]:


hdr = {'User-Agent': 'Mozilla/5.0'}
for i in range(1,12):
    site = "https://yoshops.com/products?page="+str(i)
    req = Request(site , headers = hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    name = soup.find_all('span' , class_="product-title")
    for i in range(len(name)):
        Name.append(name[i].text)
        
        
print(len(Name))


# In[4]:


hdr = {'User-Agent': 'Mozilla/5.0'}
for i in range(1,12):
    site = "https://yoshops.com/products?page="+str(i)
    req = Request(site , headers = hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    price = soup.find_all('div' , class_="product-price")
    for i in range(len(price)):
        Price.append(price[i].text)
        
print(len(Price))


# In[5]:


Original_Price = []
Discounted_Price = []
for i in Price:
    
    Original_Price.append(i.split("₹")[1])
    Discounted_Price.append(i.split("₹")[2])
    
print(len(Original_Price))
print(len(Discounted_Price))


# In[6]:


print(len(Name))
print(len(Price))


# In[7]:


hdr = {'User-Agent': 'Mozilla/5.0'}
Image = []
for i in range(1,12):
    site = "https://yoshops.com/products?page="+str(i)
    req = Request(site , headers = hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    image = soup.find_all('div' , class_="product-thumb-inner")
    #print(image)
    for im in image:
        #print image source
        
        print(im.find("img")["src"])
        Image.append(im.find("img")["src"])


# In[8]:


len(Image)


# In[9]:


hdr = {'User-Agent': 'Mozilla/5.0'}
Link = []
for i in range(1,12):
    site = "https://yoshops.com/products?page="+str(i)
    req = Request(site , headers = hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    link = soup.find_all('a' , class_="product-link")
    for l in link:
        #print image source
        Link.append("https://yoshops.com/"+l["href"])
        
        
print(Link)
    


# In[10]:


len(Link)


# In[11]:


Image.count("//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png")


# In[12]:


Image.index('//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png')


# In[13]:


j =0
NoImage = []
for i in Image:
    if i == "//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png":
        NoImage.append(j)
        
    j+=1
    


# In[22]:


NoImage


# In[29]:


from pandas import ExcelWriter
from pandas import ExcelFile
Name1 = []
Original_Price1 = []
Discounted_Price1 = []
Contact_No1 = []
URL1 = []
Address1 = []


for i in NoImage:
    Name1.append(Name[i])
    Contact_No1.append('+91-9080749858')
    Original_Price1.append(Original_Price[i])
    Discounted_Price1.append(Discounted_Price[i])
    URL1.append(Link[i])
    Address1.append('34,Sundareswarar Koil Street, Saidapet, Chennai, Tamil Nadu, PIN -600015')
    
Final_List = []

Final_List = [Name1,Original_Price1,Discounted_Price1,URL1,Contact_No1,Address1]

print(Final_List)

df = pd.DataFrame (Final_List).transpose() 
df.columns = ['Product_name', 'Original-Price','Discounted-Price','Product_URL','Contact_Number','Address2']
    

writer = ExcelWriter('No_Image.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()


# In[30]:


pd.read_excel('No_Image.xlsx')
print("No Image File is created")
time.sleep(50)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




