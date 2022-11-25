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
from urllib.request import build_opener, HTTPCookieProcessor
import readline
from PyQt5.QtWidgets import QInputDialog,QApplication
import sys
import time

# In[8]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[86]:
app = QApplication(sys.argv)


Get_Category = QInputDialog.getText(None, 'Input', "Select Any Category :\n 1. Toys & Games \n 2. Mobiles \n 3. Laptops \n 4. Accessories \n 5. Electronics \n 6. Home & Kitchen \n 7. Fashion \n 8. Foods \n 9. Services \n :")


# In[69]:


if Get_Category[0] == '1':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. PlayStation \n 2. Drones \n 3. RC Toys \n 4. Soft Toys \n 5. Gaming Accessories \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/playstation"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/drones"
        
    if Get_Subcategory[0] == '3':
        url = "https://yoshops.com/t/rc-helicopter"
        
    if Get_Subcategory[0] == '4':
        url = "https://yoshops.com/t/soft-toys"
        
    if Get_Subcategory[0] == '5':
        url = "https://yoshops.com/t/gaming-accessories"


# In[70]:


if Get_Category[0] == '2':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Smartphones \n 2. Headphones \n 3. Mobile Accessories \n 4. Feature Keypad Mobiles \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/smartphones"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/headphones"
        
    if Get_Subcategory[0] == '3':
        url = "https://yoshops.com/t/mobiles-accessories"
        
    if Get_Subcategory[0] == '4':
        url = "https://yoshops.com/t/basic-keypad-phone"


# In[87]:


if Get_Category[0] == '3':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Gaming Laptops \n 2. Personal Laptops \n 3. Tablets \n 4. Laptop Accessories \n 5. Computer Accessories \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/gaming-laptops"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/personal-laptops"
        
    if Get_Subcategory[0] == '3':
        url = "https://yoshops.com/t/tablets"
        
    if Get_Subcategory[0] == '4':
        url = "https://yoshops.com/t/laptop-accessories"
        
    if Get_Subcategory[0] == '5':
        url = "https://yoshops.com/t/computers-accessories"


# In[72]:


if Get_Category[0] == '4':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Books \n 2. Stationary \n 3. Bags \n 4. Spare Parts \n 5. More \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/books"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/stationery"
        
    if Get_Subcategory[0] == '3':
        url = "https://yoshops.com/t/books--bags"
    
    if Get_Subcategory[0] == '4':
        Get_input = QInputDialog.getText(None, 'Input',"Select Specific Parts:\n 1. Auto Spare Parts \n 2. Mobile Spare Parts \n 3. Laptop Spare Parts \n :")
        
        if Get_input[0] == '1':
            url = "https://yoshops.com/t/bike"
        
        if Get_input[0] == '2':
            url = "https://yoshops.com/t/Mobile-Parts"
            
        if Get_input[0] == '3':
            url = "https://yoshops.com/t/Laptop-spare-parts"
            
    if Get_Subcategory[0] == '5':
        url = "https://yoshops.com/t/more"


# In[73]:


if Get_Category[0] == '5':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. LED TV \n 2. Others \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/led-tv"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/jewelry--watches"


# In[79]:


if Get_Category == '6':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Irons \n 2. Mixer Grinder Juicer \n :")
    
    if Get_Subcategory == '1':
        url = "https://yoshops.com/t/irons"
        
    if Get_Subcategory == '2':
        url = "https://yoshops.com/t/mixer-grinder-juicer"


# In[75]:


if Get_Category[0] == '7':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Men \n 2. Women \n 3. Kids \n :")
    
    if Get_Subcategory[0] == '1':
        Get_input = QInputDialog.getText(None, 'Input',"Select Specific Parts:\n 1. Men Clothing \n 2. Sunglasses \n 3. Watches \n 4. Men's Footwear \n :")
        
        if Get_input[0] == '1':
            url = "https://yoshops.com/t/men-clothing"
        
        if Get_input[0] == '2':
            url = "https://yoshops.com/t/sunglasses"
            
        if Get_input[0] == '3':
            url = "https://yoshops.com/t/watches"
            
        if Get_input[0] == '4':
            url = "https://yoshops.com/t/mens-footwear"
        
    if Get_Subcategory[0] == '2':
        Get_input = QInputDialog.getText(None, 'Input',"Select Specific Parts:\n 1. Women Clothing \n 2. Face Makeup \n 3. Personal Care \n :")
        
        if Get_input[0] == '1':
            url = "https://yoshops.com/t/women-clothing"
        
        if Get_input[0] == '2':
            url = "https://yoshops.com/t/face-makeup"
            
        if Get_input[0] == '3':
            url = "https://yoshops.com/t/personal-care"
        
    if Get_Subcategory[0] == '3':
        Get_input = QInputDialog.getText(None, 'Input',"Select Specific Parts:\n 1. Kids Clothing \n 2. Shoes \n :")
        
        if Get_input[0] == '1':
            url = "https://yoshops.com/t/kids-clothing"
        
        if Get_input[0] == '2':
            url = "https://yoshops.com/t/shoes"
    
    


# In[76]:


if Get_Category[0] == '8':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Organic Foods \n 2. Vegetable \n 3. Non Veg \n 4. Seafood \n 5. Biryani \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/organic"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/vegetable"
        
    if Get_Subcategory[0] == '3':
        url = "https://yoshops.com/t/non-veg"
        
    if Get_Subcategory[0] == '4':
        url = "https://yoshops.com/t/seafood"
        
    if Get_Subcategory[0] == '5':
        url = "https://yoshops.com/t/biryani"


# In[77]:


if Get_Category[0] == '9':
    Get_Subcategory = QInputDialog.getText(None, 'Input',"Select Sub-Category :\n 1. Online Live Tuition \n 2. Training Internship Work From Home \n 3. PCD Pharma Franchise \n 4. Sponsership Marketing \n :")
    
    if Get_Subcategory[0] == '1':
        url = "https://yoshops.com/t/tuition"
        
    if Get_Subcategory[0] == '2':
        url = "https://yoshops.com/t/internship"
        
    if Get_Subcategory[0] == '3':
        url = "https://yoshops.com/t/pcd-pharma-distributor"
        
    if Get_Subcategory[0] == '4':
        Get_input = QInputDialog.getText(None, 'Input',"Select Specific Parts:\n 1. Blog Sponsorship \n 2. Instagram Sponsorship \n 3. Youtube Sponsorship \n :")
        
        if Get_input[0] == '1':
            url = "https://yoshops.com/t/blog-sponsorship"
        
        if Get_input[0] == '2':
            url = "https://yoshops.com/t/instagram-sponsorship"
            
        if Get_input[0] == '3':
            url = "https://yoshops.com/t/youtuber-sponsorship"


# In[95]:


print(url)


# In[89]:


hdr = {'User-Agent': 'Mozilla/5.0'}
Link = []
site = url
req = Request(site , headers = hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
link = soup.find_all('a' , class_="product-link")
for l in link:
    Link.append("https://yoshops.com"+l["href"])
        
        
print(Link)


# In[97]:


Name = []
hdr = {'User-Agent': 'Mozilla/5.0'}
site = url
req = Request(site , headers = hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
name = soup.find_all('span' , class_="product-title")
for i in range(len(name)):
    Name.append(name[i].text)
    
print(Name)


# In[92]:


Comments = []
comments = []
Comments_Final = []
j = 0
driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe")
for i in Link:
    driver.get(i)
    driver.implicitly_wait(100)
    while True:
        reviews = driver.find_element_by_class_name("yotpo-reviews")
        comments = reviews.find_elements_by_class_name("content-title")
        for c in comments:
            Comments.append(c.text)
        buttons = driver.find_elements_by_class_name("yotpo-page-element.yotpo-icon.yotpo-icon-right-arrow.yotpo_next")
        if len(buttons) == 0:
            break
        if buttons[0].get_attribute('href') == None:
            break
        driver.get(buttons[0].get_attribute('href'))
    
    Comments_Final.append(Comments) 
    j+=1
    Comments = []

driver.close()


# In[93]:


Comments_Final


# In[106]:


ReviewStarCount = []
ReviewStarCount1 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe")
for i in Link:
    driver.get(i)
    driver.implicitly_wait(100)
    try:
        if len(driver.find_elements_by_class_name("yotpo-sum-reviews")) == 0:
            ReviewStarCount1.append('No Reviews')
            continue
        else :
            ReviewStarCount = driver.find_element_by_class_name("yotpo-sum-reviews")
            ReviewStarCount1.append(ReviewStarCount.text)
            
    except:
        continue
        
    
    
print(len(ReviewStarCount1))
driver.close()


# In[107]:


ReviewStarCount1


# In[110]:


ReviewStar = []
ReviewStar1 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe")
for i in Link:
    driver.get(i)
    driver.implicitly_wait(100)
    ReviewStar = driver.find_element_by_class_name("yotpo-stars")
    ReviewStar1.append(ReviewStar.text)
            
        
    
ReviewStar1 = list(filter(None,ReviewStar1))
print(len(ReviewStar1))
print(ReviewStar1)
driver.close()


# In[111]:


from pandas import ExcelWriter
from pandas import ExcelFile
    
Final_List = []

Final_List = [Name,Link,Comments_Final,ReviewStarCount1,ReviewStar1]

print(Final_List)

df = pd.DataFrame (Final_List).transpose() 
df.columns = ['Product_name','Product_URL','Product_Comments','Review_Star_Count','Product_Rating']
    

writer = ExcelWriter('Comments.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
print('Excel File is Generated')
time.sleep(50)

# In[112]:




# In[ ]:





# In[ ]:




