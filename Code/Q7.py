#!/usr/bin/env python
# coding: utf-8

# **Loading Libraries**

# In[1]:


import numpy as np
import pandas as pd
import datetime
import json
import csv


# **District**

# Data Loading and Preprocessing

# In[2]:


data=pd.read_csv('../Data/vaccination_data_district_wise.csv',low_memory=False)


# In[3]:


data=data[['District_Key','14/08/2021.8','14/08/2021.9']].iloc[1:]


# In[4]:


data['14/08/2021.9']=pd.to_numeric(data['14/08/2021.9'])


# In[5]:


data['14/08/2021.8']=pd.to_numeric(data['14/08/2021.8'])


# Finding Ratio

# In[6]:


data['ratio']=data['14/08/2021.9']/data['14/08/2021.8']


# Sorting and Converting to CSV

# In[7]:


data[['District_Key','ratio']].sort_values(['ratio','District_Key'])[['District_Key','ratio']].to_csv('../Generated/7/vaccine-district-ratio.csv',index=False)


# **For State**

# Data Loading And Preprocessing

# In[8]:


data=pd.read_csv('../Data/vaccination_data_state_wise.csv',low_memory=False)


# In[9]:


data=data[(data['State']!='India')&(data['Updated On']=='14/08/2021')]


# In[10]:


data=data[['State','Covaxin (Doses Administered)','CoviShield (Doses Administered)']]


# Finding Ratio

# In[11]:


data['ratio']=data['CoviShield (Doses Administered)']/data['Covaxin (Doses Administered)']


# In[12]:


data.sort_values(['ratio','State'])[['State','ratio']].to_csv('../Generated/7/vaccine-state-ratio.csv',index=False)


# **For Overall**

# Data Loading and Preprocessing

# In[13]:


data=pd.read_csv('../Data/vaccination_data_state_wise.csv',low_memory=False)


# In[14]:


data=data[(data['State']=='India')&(data['Updated On']=='14/08/2021')]


# In[15]:


data=data[['State','Covaxin (Doses Administered)','CoviShield (Doses Administered)']]


# Finding Ratio

# In[16]:


data['ratio']=data['CoviShield (Doses Administered)']/data['Covaxin (Doses Administered)']


# In[17]:


data.sort_values(['ratio','State'])[['State','ratio']].to_csv('../Generated/7/vaccine-overall-ratio.csv',index=False)

