#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[56]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")


# In[57]:


from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd
from urllib.request import Request,urlopen


# In[58]:


import pyautogui
import time


# In[72]:


from selenium.webdriver.chrome.service import Service
s=Service("C:\\Users\\Pandi\\chromedriver.exe")
browser = webdriver.Chrome(service=s)
url="https://yoshops.com/products?page=3" 
browser.get(url)
time.sleep(5)


# In[13]:


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


# In[18]:


ReviewStar = []
ReviewStar1 = []
Link1 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe")
for i in Link:
    driver.get(i)
    driver.implicitly_wait(100)
    ReviewStar = driver.find_element_by_class_name("yotpo-stars")
    if ReviewStar.text == '0.0 star rating':
        continue
        
    else:
        ReviewStar1.append(ReviewStar.text)
        Link1.append(i)
            
        
    
ReviewStar1 = list(filter(None,ReviewStar1))
print(len(ReviewStar1))
print(ReviewStar1)


# In[94]:


print(Link1)


# In[95]:


print(len(Link1))


# In[96]:


Name = []
driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe",encoding="utf-8")
for i in Link1:
    driver.get(i)
    driver.implicitly_wait(100)
    name = driver.find_element_by_class_name("single-product-title")
    Name.append(name.text)
            
        
    
Name = list(filter(None,Name))
print(len(Name))
print(Name)


# In[53]:


Customer_Name = []
Customer_Name1 = []
Customer_Name_Final = []
driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe",encoding="utf-8")
for i in range(len(Link1)):
    driver.get(Link1[i])
    driver.implicitly_wait(100)
    Customer_Name = driver.find_elements_by_xpath("//span[@class='y-label yotpo-user-name yotpo-font-bold pull-left']")
    for j in Customer_Name:
        Customer_Name1.append(j.text)
    
    Customer_Name1 = list(filter(None,Customer_Name1))
    Customer_Name_Final.append(Customer_Name1)
    Customer_Name1 = []

print(Customer_Name_Final)


# In[89]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\Pandi\\chromedriver.exe",encoding="utf-8")
driver.get(Link1[5])
driver.implicitly_wait(100)
    
reviewButton=driver.find_element_by_xpath("//span[@class='yotpo-icon-button-text']")

driver.execute_script("arguments[0].click();", reviewButton)

titleField = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "review_title")))
reviewField = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "review_content")))
userIDField = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "display_name")))
emailIDField = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "email")))
    
titleField.send_keys('Great Product')
reviewField.send_keys('Dear Customer, Thank you for your amazing feedback!')
userIDField.send_keys('Yoshops')
emailIDField.send_keys('sabitalangkam.yoshops@gmail.com')
 
starRating = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@class='yotpo-icon pull-left review-star yotpo-icon-empty-star']")))
starRating = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[3]/div[2]/div/div/form/div/div/div[1]/div[3]/span/span[5]")
driver.execute_script("arguments[0].click();", starRating)
    
time.sleep(5)
    
postButton=driver.find_element_by_xpath("//input[@class='yotpo-default-button primary-color-btn yotpo-submit']")
driver.execute_script("arguments[0].click();", postButton)


# In[97]:


from pandas import ExcelWriter
from pandas import ExcelFile
    
Final_List = []

Final_List = [Name,Link1,Customer_Name_Final,ReviewStar1]

print(Final_List)

df = pd.DataFrame (Final_List).transpose() 
df.columns = ['Product_name','Product_URL','Customer_Name','Product_Rating']
    

writer = ExcelWriter('Task_3.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()


# In[98]:


pd.read_excel('Task_3.xlsx')

print("products list")
# In[ ]:





# In[ ]:


get_ipython().system('pip install webdriver')


# In[ ]:


get_ipython().system('pip install chromedrivermanager')


# In[ ]:


get_ipython().system('pip install ChromeDriverManager')


# In[ ]:


get_ipython().system('pip install selenium')


# In[ ]:


get_ipython().system('pip install webdriver')


# In[ ]:


get_ipython().system('pip install random')


# In[ ]:


get_ipython().system('pip install warnings')


# In[ ]:


get_ipython().system('pip install webdrivermanger')


# In[ ]:


get_ipython().system('pip install webdriver-manager')


# In[ ]:


get_ipython().system('pip install chromedrivermanager')


# In[ ]:


get_ipython().system('pip install pyautogui')


# In[ ]:


get_ipython().system('pip install time')


# In[ ]:


get_ipython().system('brew cask upgrade chromedriver')


# In[ ]:


get_ipython().system('pip install webdriverexception')


# In[ ]:


get_ipython().system('pip install webdriver')


# In[ ]:


get_ipython().system('pip install driver')


# In[ ]:


get_ipython().system('pip install reviewstar')


# In[ ]:




