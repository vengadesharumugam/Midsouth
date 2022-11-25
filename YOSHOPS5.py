#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[225]:


import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QInputDialog,QApplication

app = QApplication(sys.argv)


# In[2]:


df = pd.read_csv('orders_2016-2020_Dataset.csv')
#print(df)


# # Que-2

# In[138]:


df2 = pd.DataFrame()
df2['Payment Method'] = ''
df2['Payment Method'] = df['Payment Method'].values
#df2


# In[139]:


df2.dropna(inplace=True)
df2.reset_index(drop=True, inplace=True)
#df2


# In[ ]:





# In[ ]:





# In[140]:


for i in range(240):
    df2['Payment Method'][i] = df2['Payment Method'][i].split(' ')


# In[141]:


#df2['Payment Method']


# In[142]:


for i in range(240):
    df2['Payment Method'][i] = df2['Payment Method'][i][0]
    
#df2['Payment Method']


# In[143]:


df2


# In[ ]:





# In[ ]:





# In[145]:


#df['Shipping State'].unique()


# In[146]:


#df['Shipping State'].value_counts(dropna=True)


# # Que-3

# In[147]:


df3 = pd.DataFrame()

df3['Shipping State'] = df['Shipping State'].values

#print(df3)


# In[148]:


#df3.info()


# In[149]:


df3.dropna(inplace=True)
df3.reset_index(drop=True, inplace=True)
#df3.info()


# In[150]:


for i in range(2276):
    x = df3['Shipping State'][i].split('-')
    df3['Shipping State'][i] = x
    
#print(x)


# In[151]:


#df3['Shipping State']


# In[152]:


df3 = df3.drop(index=879)
df3.reset_index(drop=True, inplace=True)
#df3.info()


# In[159]:


for i in range(2275):
    if df3['Shipping State'][i][0] == 'IN':
        df3['Shipping State'][i] = df3['Shipping State'][i][1]
    
#df3['Shipping State']


# In[163]:


df3 = df3.drop(index=[1411,1508,1583,2248,2250])
df3.reset_index(drop=True, inplace=True)
#df3.info()
#df3


# In[164]:


#df3['Shipping State'].unique()


# In[165]:


#df3['Shipping State'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Que-4

# In[174]:


df4 = pd.DataFrame()

df4['Shipping City'] = df['Shipping City'].values

#print(df4)


# In[175]:


#df4.info()
df4.dropna(inplace=True)
df4.reset_index(drop=True, inplace=True)
#df4.info()


# In[28]:


#df4.info()


# In[171]:


df4.loc[df4['Shipping City'] == '$%^&']


# In[172]:


df4 = df4.drop(index=2263)
df4.reset_index(drop=True, inplace=True)
#df4.info()
#df4


# In[ ]:





# In[176]:


df4['Shipping City'].value_counts().head(10)


# In[68]:


pd.set_option('display.max_rows', None)


# In[ ]:





# # Que-5

# In[180]:


df5 = pd.DataFrame()

df5['LineItem Name'] = df['LineItem Name'].values

#print(df5)


# In[ ]:





# In[ ]:





# In[ ]:





# # Que-7

# In[183]:


df6 = pd.DataFrame()

df6['Order Date and Time Stamp'] = df['Order Date and Time Stamp'].values

#print(df6)


# In[184]:


#df6.info()
df6.dropna(inplace=True)
df6.reset_index(drop=True, inplace=True)
#df6.info()


# In[185]:


for i in range(2297):
    df6['Order Date and Time Stamp'][i] = df6['Order Date and Time Stamp'][i].split(' ')
    
#df6['Order Date and Time Stamp']


# In[186]:


df6['Date'] = ''
for i in range(2297):
    df6['Date'][i] = df6['Order Date and Time Stamp'][i][0]
    
#df6['Date']


# In[187]:


for i in range(2297):
    df6['Date'][i] = df6['Date'][i].split('-')
    
#df6['Date']


# In[188]:


df6['Month'] = ''
for i in range(2297):
    df6['Month'][i] = df6['Date'][i][1]
    
#df6['Month']


# In[189]:


df6['Year'] = ''
for i in range(2297):
    df6['Year'][i] = df6['Date'][i][2]
    
#df6['Year']    


# In[190]:


#df6


# In[191]:


df6['LineItem Qty'] = df['LineItem Qty'].values

#print(df6)


# In[ ]:





# # Que-9

# In[196]:


df6['Day'] = ''
for i in range(2297):
    df6['Day'][i] = df6['Date'][i][0]
    
#df6['Day']


# In[197]:


df6['Time'] = ''
for i in range(2297):
    df6['Time'][i] = df6['Order Date and Time Stamp'][i][1]
    
#df6['Time'] 


# In[198]:


for i in range(2297):
    df6['Time'][i] = df6['Time'][i].split(':')
    
#df6['Time']


# In[199]:


df6['Hours'] = ''
for i in range(2297):
    df6['Hours'][i] = df6['Time'][i][0]
    
#df6['Hours'] 


# In[200]:


df6['Hours'] = df6['Hours'].astype(int)
#df6['Hours']


# In[201]:


df6['Time of Day'] = ''
for i in range(2297):
    if df6['Hours'][i] <= 11: 
        df6['Time of Day'][i] = 'Morning'
    
    elif df6['Hours'][i] <= 16:
        df6['Time of Day'][i] = 'Afternoon'
        
    elif df6['Hours'][i] <= 20:
        df6['Time of Day'][i] = 'Evening'
        
    elif df6['Hours'][i] >= 21:
        df6['Time of Day'][i] = 'Night'
        
    else:
        df6['Time of Day'][i] = 'None'
        
#df6['Time of Day'] 


# In[ ]:





# In[203]:


df1 = pd.DataFrame()
df1 = pd.read_csv('review_dataset.csv')
#print(df1)


# # Que-1

# In[204]:


df7 = pd.DataFrame()

df7['Review_Stars'] = df1['stars'].values

#print(df7)


# In[205]:


df7['Feedback'] = ''
for i in range(1861):
    if pd.isnull(df7['Review_Stars'][i]) == True:
        df7['Feedback'][i] = 'No Reviews'
    else:
        df7['Review_Stars'][i] = df7['Review_Stars'][i].split(' ')
        df7['Review_Stars'][i] = df7['Review_Stars'][i][0]
    
#df7


# In[206]:


#df7['Review_Stars']


# In[207]:


df7['Review_Stars'] = df7['Review_Stars'].astype(float)
#df7['Review_Stars']


# In[208]:


for i in range(1861):
    if pd.isnull(df7['Review_Stars'][i]) == True:
        continue
    else:
        if df7['Review_Stars'][i] >= 2.0:
            df7['Feedback'][i] = 'Positive'
            
        else:
            df7['Feedback'][i] = 'Negative'
            
    
#df7


# In[209]:


#df7['Feedback'].unique()


# In[210]:


#df7['Feedback'].value_counts()


# In[211]:


for i in range(1861):
    if pd.isnull(df7['Review_Stars'][i]) == True:
        df7['Review_Stars'][i] = 'No Reviews'
    else:
        df7['Review_Stars'][i] = round(df7['Review_Stars'][i])
        
#df7['Review_Stars']


# In[212]:


#df7


# In[112]:


#df7['Review_Stars'].unique()


# In[113]:


#df7['Review_Stars'].value_counts()


# In[ ]:





# # Que-6

# In[214]:


df8 = pd.DataFrame()

df8['category'] = df1['category'].values

#print(df8)


# In[ ]:





# # Que-8

# In[216]:


df9 = pd.DataFrame()

df9['status'] = df1['status'].values

#print(df9)


# In[217]:


for i in range(1861):
    if pd.isnull(df9['status'][i]) == True:
        df9['status'][i] = 'Not Reviewed'


# In[218]:


#df9['status'].unique()


# In[219]:


#df9['status'].value_counts()


# In[ ]:





# In[223]:


Choice = QInputDialog.getText(None,'Input', "Enter 1 to see the analysis of Reviews given by Customers \n Enter 2 to see the analysis of different payment methods used by the Customers\n Enter 3 to see the analysis of Top Consumer States of India\n Enter 4 to see the analysis of Top Consumer Cities of India\n Enter 5 to see the analysis of Top Selling Product Categories\n Enter 6 to see the analysis of Reviews for All Product Categories\n Enter 7 to see the analysis of Number of Orders Per Month Per Year\n Enter 8 to see the analysis of Reviews for Number of Orders Per Month Per Year\n Enter 9 to see the analysis of Number of Orders Across Parts of a Day\n Enter 10 to see the Full Report \n Enter your Choice :")


# In[ ]:


print(Choice)


# In[ ]:


if Choice[0] == '1':
    with PdfPages(r'C:\Users\Pandi\Que_1.pdf') as export_pdf:
        ig = plt.figure(figsize = (10, 5))
        Reviews = ['No Reviews' , '5.0' , '4.0' , '3.0' ,'2.0']
        plt.bar(Reviews, df7['Review_Stars'].value_counts() , color ='green', width = 0.4)
        plt.xlabel("Reviews")
        plt.ylabel('No. of Customers')
        plt.title("Analysis of reviews given by the Customers")
        export_pdf.savefig()
        plt.close()

        fig = plt.figure(figsize =(10, 7))
        values = df7['Feedback'].value_counts()
        Reviews = ['No Reviews','Positive']
        mycolors = ["red", "c"]
        plt.title("Pie Chart of analysis of reviews given by the Customers")
        plt.pie(values, labels = Reviews , colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close() 
    
    
elif Choice[0] == '2':
    with PdfPages(r'C:\Users\Pandi\Que_2.pdf') as export_pdf:
        counts = [45 , 195]
        ig = plt.figure(figsize = (10, 5))
        plt.bar(df2['Payment Method'].unique(),counts , color ='green', width = 0.4)
        plt.xlabel("Payment Methods")
        plt.ylabel("No. of Customers")
        plt.title("Different Payment Methods used by the Customers")
        export_pdf.savefig()
        plt.close()

        fig = plt.figure(figsize =(10, 7))
        values = df2['Payment Method'].value_counts()
        Payment_Type = ['CCAvenue' , 'Offline']
        mycolors = ["red", "c"]
        plt.title("Pie Chart of Different Payment Methods used by the Customers")
        plt.pie(counts, labels = Payment_Type , colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close() 
    
    
elif Choice[0] == '3':
    with PdfPages(r'C:\Users\Pandi\Que_3.pdf') as export_pdf:
        ig = plt.figure(figsize = (15, 15))
        df3.groupby(['Shipping State'])['Shipping State'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=7)
        plt.xlabel("Shipping State")
        plt.ylabel("No. of Customers")
        plt.title("The analysis of Top Consumer States of India")
        export_pdf.savefig()
        plt.close()
    
    
elif Choice[0] == '4':
    with PdfPages(r'C:\Users\Pandi\Que_4.pdf') as export_pdf:
        fig = plt.figure(figsize =(10, 7))
        plt.title("Top 10 Consumer Cities")
        df4.groupby(['Shipping City'])['Shipping City'].count().sort_values(ascending=False).head(10).plot.pie(shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close() 
    
    
elif Choice[0] == '5':
    with PdfPages(r'C:\Users\Pandi\Que_5.pdf') as export_pdf:
        ig = plt.figure(figsize = (15, 15))
        df5.groupby(['LineItem Name'])['LineItem Name'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=7)
        plt.xlabel("Consumer Products")
        plt.ylabel("No. of Purchases")
        plt.title("Top Consumer Products")
        export_pdf.savefig()
        plt.close()
    
    
elif Choice[0] == '6':
    with PdfPages(r'C:\Users\Pandi\Que_6.pdf') as export_pdf:
        ig = plt.figure(figsize = (15, 15))
        df8.groupby(['category'])['category'].count().sort_values(ascending=False).plot.bar(fontsize=7)
        plt.xlabel("Product Categories")
        plt.ylabel("No. of Reviews")
        plt.title("The analysis of Reviews for All Product Categories")
        export_pdf.savefig()
        plt.close()
    
    
elif Choice[0] == '7':
    with PdfPages(r'C:\Users\Pandi\Que_7.pdf') as export_pdf:
        ig = plt.figure(figsize = (15, 15))
        df6.groupby(['Month','Year'])['LineItem Qty'].sum().plot.bar()
        plt.ylabel("No. of Purchases")
        plt.title('Number of Orders Per Month Per Year',fontsize=25)
        export_pdf.savefig()
        plt.close()
    
    
elif Choice[0] == '8':
    with PdfPages(r'C:\Users\Pandi\Que_8.pdf') as export_pdf:
        fig = plt.figure(figsize =(10, 7))
        values = df9['status'].value_counts()
        Reviewes = ['Not Reviewed', 'Reviewed']
        mycolors = ["green", "yellow"]
        plt.title("Pie Chart of analysis of reviewed Products")
        plt.pie(values, labels = Reviewes , colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close() 
    
    
elif Choice[0] == '9':
    with PdfPages(r'C:\Users\Pandi\Que_9.pdf') as export_pdf:
        ig = plt.figure(figsize = (30, 15))
        mycolors = ['red', 'green' , 'black' , 'cyan']
        df6.groupby(['Time of Day'])['LineItem Qty'].sum().plot.bar(color = mycolors ,width = 0.4)
        plt.xlabel("Time of Day")
        plt.ylabel("Total Orders")
        plt.title('Analysis of Number of Orders Across Parts of a Day',fontsize=25)
        export_pdf.savefig()
        plt.close()
    
    
        fig = plt.figure(figsize =(30, 15))
        df6.groupby(['Time of Day'])['LineItem Qty'].sum().plot.pie(colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100))
        plt.title('Analysis of Number of Orders Across Parts of a Day',fontsize=25)
        export_pdf.savefig()
        plt.close()
    
    
elif Choice[0] == '10':
    #Que-10
    with PdfPages(r'C:\Users\Pandi\Full_Report.pdf') as export_pdf:
        ig = plt.figure(figsize = (10, 5))
        Reviews = ['No Reviews' , '5.0' , '4.0' , '3.0' ,'2.0']
        plt.bar(Reviews, df7['Review_Stars'].value_counts() , color ='green', width = 0.4)
        plt.xlabel("Reviews")
        plt.ylabel('No. of Customers')
        plt.title("Analysis of reviews given by the Customers")
        export_pdf.savefig()
        plt.close()

        fig = plt.figure(figsize =(10, 7))
        values = df7['Feedback'].value_counts()
        Reviews = ['No Reviews','Positive']
        mycolors = ["red", "c"]
        plt.title("Pie Chart of analysis of reviews given by the Customers")
        plt.pie(values, labels = Reviews , colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close()

        #Que-2
        counts = [45 , 195]
        ig = plt.figure(figsize = (10, 5))
        plt.bar(df2['Payment Method'].unique(),counts , color ='green', width = 0.4)
        plt.xlabel("Payment Methods")
        plt.ylabel("No. of Customers")
        plt.title("Different Payment Methods used by the Customers")
        export_pdf.savefig()
        plt.close()

        fig = plt.figure(figsize =(10, 7))
        values = df2['Payment Method'].value_counts()
        Payment_Type = ['CCAvenue' , 'Offline']
        mycolors = ["red", "c"]
        plt.title("Pie Chart of Different Payment Methods used by the Customers")
        plt.pie(counts, labels = Payment_Type , colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close()

        #Que-3
        ig = plt.figure(figsize = (15, 15))
        df3.groupby(['Shipping State'])['Shipping State'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=7)
        plt.xlabel("Shipping State")
        plt.ylabel("No. of Customers")
        plt.title("The analysis of Top Consumer States of India")
        export_pdf.savefig()
        plt.close()

        #Que-4
        fig = plt.figure(figsize =(10, 7))
        plt.title("Top 10 Consumer Cities")
        df4.groupby(['Shipping City'])['Shipping City'].count().sort_values(ascending=False).head(10).plot.pie(shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close()

        #Que-5
        ig = plt.figure(figsize = (15, 15))
        df5.groupby(['LineItem Name'])['LineItem Name'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=7)
        plt.xlabel("Consumer Products")
        plt.ylabel("No. of Purchases")
        plt.title("Top Consumer Products")
        export_pdf.savefig()
        plt.close()

        #Que-6
        ig = plt.figure(figsize = (15, 15))
        df8.groupby(['category'])['category'].count().sort_values(ascending=False).plot.bar(fontsize=7)
        plt.xlabel("Product Categories")
        plt.ylabel("No. of Reviews")
        plt.title("The analysis of Reviews for All Product Categories")
        export_pdf.savefig()
        plt.close()

        #Que-7
        ig = plt.figure(figsize = (15, 15))
        df6.groupby(['Month','Year'])['LineItem Qty'].sum().plot.bar()
        plt.ylabel("No. of Purchases")
        plt.title('Number of Orders Per Month Per Year',fontsize=25)
        export_pdf.savefig()
        plt.close()

        #Que-8
        fig = plt.figure(figsize =(10, 7))
        values = df9['status'].value_counts()
        Reviewes = ['Not Reviewed', 'Reviewed']
        mycolors = ["green", "yellow"]
        plt.title("Pie Chart of analysis of reviewed Products")
        plt.pie(values, labels = Reviewes , colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , startangle=90)
        export_pdf.savefig()
        plt.close()

        #Que-9
        ig = plt.figure(figsize = (30, 15))
        mycolors = ['red', 'green' , 'black' , 'cyan']
        df6.groupby(['Time of Day'])['LineItem Qty'].sum().plot.bar(color = mycolors ,width = 0.4)
        plt.xlabel("Time of Day")
        plt.ylabel("Total Orders")
        plt.title('Analysis of Number of Orders Across Parts of a Day',fontsize=25)
        export_pdf.savefig()
        plt.close()
    
        fig = plt.figure(figsize =(30, 15))
        df6.groupby(['Time of Day'])['LineItem Qty'].sum().plot.pie(colors = mycolors ,shadow=True , autopct= lambda x: '{:.0f}'.format(x*values.sum()/100))
        plt.title('Analysis of Number of Orders Across Parts of a Day',fontsize=25)
        export_pdf.savefig()
        plt.close()
    
else:
    sys.exit()
    
    
    
    


# In[ ]:




