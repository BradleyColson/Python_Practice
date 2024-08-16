#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Call pandas a python data analysis library
import pandas as pd


# In[10]:


#Read in file to analyse
df = pd.read_csv(r"C:\Users\Bradl\downloads\vgsales.csv")


# In[11]:


df


# In[12]:


#Get the basic headers on the file
df.head()


# In[13]:


#Understand the size of the file and object types
df.info()


# In[14]:


#See basic stats on the data
df.describe()


# In[15]:


#Which video game had the highest sales in 2010?
#Calling the year and specifically year 2010

df[df["Year"] == 2010]


# In[17]:


#Make a copy of the dataframe
#Which video game had the highest sales in 2010?

#Answer = Kinect Adventures!

twenty_ten_df = df[df["Year"] == 2010]

twenty_ten_df[twenty_ten_df["Global_Sales"] == twenty_ten_df["Global_Sales"].max()] 


# In[22]:


#What game genre is most popular for each year

df[["Year", "Global_Sales"]].groupby(by="Year").max()


# In[25]:


#Merge or join max sales with the associated name of the game

max_sales_by_year_df = df[["Year", "Global_Sales"]].groupby(by="Year").max()
max_sales_by_year_df.merge(df[["Year", "Global_Sales", "Name"]], on=["Year", "Global_Sales"], how="left")


# In[28]:


#What are the global sales per year?

df[["Year", "Global_Sales"]].groupby("Year").sum()


# In[40]:


#Store the result

global_sales_per_year_df = df[["Year", "Global_Sales"]].groupby("Year", as_index=False).sum()


# In[42]:


import matplotlib.pyplot as plt


# In[43]:


global_sales_per_year_df.plot(kind="bar", x="Year", y="Global_Sales")


# In[46]:


#The years were scrunched too close together

global_sales_per_year_df.plot(kind="bar", x="Year", y="Global_Sales", figsize=(15,5), ylabel="Sales (Millions $)", title="Global Video Games Sales Over the Years")


# In[ ]:


#This is the answer to global sales per year


# In[ ]:


#What are the sales trends per region over time


# In[47]:


df.head()


# In[50]:


df[["Year", "EU_Sales", "JP_Sales", "NA_Sales", "Other_Sales", "Global_Sales"]].groupby(by="Year").sum().plot(figsize=(15,5))

