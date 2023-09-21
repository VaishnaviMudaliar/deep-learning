#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas_datareader as pdr
import numpy as np
import pandas as pd
import datetime as datetime
import matplotlib.pyplot as plt


# In[66]:


df_tesla = pd.read_csv('Downloads/archive/TSLA.csv',index_col= 0)
df_tesla


# In[56]:


df_tesla['High'].plot(figsize = (12,4))


# In[57]:


# xlimit and ylimit
df_tesla['High'].plot(figsize = (12,4))


# In[68]:


df_tesla['High'].plot(xlim=['2010-06-29','2020-01-29'],figsize = (12,4),ls = '--',c = 'green')


# In[75]:


index = df_tesla.loc['2010-06-29':'2020-01-29'].index
share_open = df_tesla.loc['2010-06-29':'2020-01-29']['Open']
share_open


# In[72]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[77]:


figure,axis = plt.subplots()
figure.autofmt_xdate()
axis.plot(index,share_open)


# In[79]:


# Datetime Index
df_tesla = df_tesla.reset_index()
df_tesla.info()


# In[80]:


pd.to_datetime(df_tesla['Date'])


# In[85]:


df_tesla.set_index('Date')


# In[88]:


df_tesla.set_index('Date',drop = True)


# In[94]:


from datetime import datetime

datetime(2020,11,21)
datetime.now()


# In[102]:


date = datetime(2021,11,21)
date.date()
date.day
date.weekday()
date.year
date.month


# **Time Resampling**

# In[107]:


df_tesla['Date'] = pd.to_datetime(df_tesla['Date'])


# In[117]:


df_tesla.set_index('Date')


# In[119]:


df_tesla.info()


# In[124]:


## year end frequency
df_tesla.set_index('Date').resample(rule = 'A').max()['Open'].plot()


# In[126]:


## quarterly start frequency

df_tesla.set_index('Date').resample(rule = 'QS').max()['High'].plot()


# In[128]:


## buiness end freueancy

df_tesla.set_index('Date').resample(rule = 'BA').max()['High'].plot()


# In[129]:


#business quarterly year freuency

df_tesla.set_index('Date').resample(rule = 'BQS').max()['High'].plot()


# In[132]:


## plotting
df_tesla.set_index('Date')['Open'].resample(rule = 'A').mean().plot(kind = 'bar')


# In[133]:


## plotting
df_tesla.set_index('Date')['Open'].resample(rule = 'M').max().plot(kind = 'bar',figsize = (20,8))


# In[139]:


# example for rolling mean

df_tesla['High'].rolling(10).mean().plot()


# In[141]:


df_tesla['Open : 30 days rolling'] = df_tesla['Open'].rolling(30).mean()


# In[142]:


df_tesla[['Open','Open : 30 days rolling']].plot(figsize = (12,5))


# In[ ]:




