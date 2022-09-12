#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# **For District**

# In[2]:


data=pd.read_csv('../Data/vaccination_data_district_wise.csv',low_memory=False)


# In[3]:


data=data[['District_Key','District','14/08/2021.3','14/08/2021.4']].iloc[1:]


# In[4]:


census=pd.read_excel('../Data/census.xlsx')


# In[5]:


census=census[(census['Level']=='DISTRICT')&(census['TRU']=='Total')][['Name','TOT_P']]


# In[6]:


census.columns=['District','Population']


# In[7]:


district_data=pd.merge(data,census,on=['District'])


# In[8]:


district_data['14/08/2021.3']=pd.to_numeric(district_data['14/08/2021.3'])


# In[9]:


district_data['14/08/2021.4']=pd.to_numeric(district_data['14/08/2021.4'])


# In[10]:


district_data['Dose 1 Ratio']=district_data['14/08/2021.3']/district_data['Population']


# In[11]:


district_data['Dose 2 Ratio']=district_data['14/08/2021.4']/district_data['Population']


# In[12]:


district_data[['District_Key','Dose 1 Ratio','Dose 2 Ratio']].sort_values(['Dose 1 Ratio']).to_csv('../Generated/8/district-vaccinated-dose-ratio.csv',index=False)


# **For State**

# In[13]:


data=pd.read_csv('../Data/vaccination_data_state_wise.csv',low_memory=False)


# In[14]:


data=data[data['Updated On']=='14/08/2021']


# In[15]:


data=data[['State','First Dose Administered','Second Dose Administered']]


# In[16]:


state_vaccination=data[data['State']!='India']


# In[17]:


census=pd.read_excel('../Data/census.xlsx')


# In[18]:


census=census[(census['Level']=='STATE')&(census['TRU']=='Total')][['Name','TOT_P']]


# In[19]:


state_vaccination=state_vaccination[state_vaccination['State'].str.upper().isin(census['Name'].values)]
state_vaccination=state_vaccination[['State','First Dose Administered','Second Dose Administered']].reset_index().drop('index',axis=1)


# In[20]:


census=census[census['Name'].isin(state_vaccination['State'].str.upper())]


# In[21]:


census=census.sort_values('Name').reset_index().drop('index',axis=1)


# In[22]:


state_vaccination['Dose 1 Ratio']=state_vaccination['First Dose Administered']/census['TOT_P']


# In[23]:


state_vaccination['Dose 2 Ratio']=state_vaccination['Second Dose Administered']/census['TOT_P']


# In[24]:


state_vaccination[['State','Dose 1 Ratio','Dose 2 Ratio']].sort_values(['Dose 1 Ratio']).to_csv('../Generated/8/state-vaccinated-dose-ratio.csv',index=False)


# **For Overall**

# In[25]:


overall_data=data[data['State']=='India'].reset_index().drop('index',axis=1)


# In[26]:


census=pd.read_excel('../Data/census.xlsx')
census=census[(census['Level']=='India')&(census['TRU']=='Total')][['Name','TOT_P']]


# In[27]:


overall_data['Dose 1 Ratio']=overall_data['First Dose Administered']/census['TOT_P']


# In[28]:


overall_data['Dose 2 Ratio']=overall_data['Second Dose Administered']/census['TOT_P']


# In[29]:


overall_data[['State','Dose 1 Ratio','Dose 2 Ratio']].sort_values(['Dose 1 Ratio']).to_csv('../Generated/8/overall-vaccinated-dose-ratio.csv',index=False)

