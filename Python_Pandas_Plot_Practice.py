#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


df = pd.read_csv(r"C:\Users\Bradl\Downloads\ice cream ratings.csv")
df = df.set_index('Date')
df


# In[30]:


print(plt.style.available)
plt.style.use('fivethirtyeight')


# In[31]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[12]:


df.plot(kind = 'bar', stacked = True)


# In[15]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, c= 'Yellow')


# In[17]:


df.plot.hist(bins = 20)


# In[18]:


df.boxplot()


# In[19]:


df.plot.area()


# In[23]:


df.plot.pie(y = 'Flavor Rating', figsize =(10,6))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




