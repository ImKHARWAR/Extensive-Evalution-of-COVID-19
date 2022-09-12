#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# **For District**

# In[2]:


data=pd.read_csv('../Data/vaccination_data_district_wise.csv',low_memory=False)


# In[3]:


data=data[['District_Key','District','14/08/2021.5','14/08/2021.6']]


# In[4]:


census=pd.read_excel('../Data/census.xlsx')


# In[5]:


census=census[(census['Level']=='DISTRICT')&(census['TRU']=='Total')][['Name','TOT_P','TOT_M','TOT_F']]


# In[6]:


census.columns=['District','Population','Male Population','Female Population']


# In[7]:


district_data=pd.merge(data,census,on=['District'])


# In[8]:


district_data['14/08/2021.5']=pd.to_numeric(district_data['14/08/2021.5'])


# In[9]:


district_data['14/08/2021.6']=pd.to_numeric(district_data['14/08/2021.6'])


# In[10]:


district_data['Vaccination Ratio (F/M)']=district_data['14/08/2021.6']/district_data['14/08/2021.5']


# In[11]:


district_data['Population Ratio (F/M)']=district_data['Female Population']/district_data['Male Population']


# In[12]:


district_data['Ratio Of Ratio']=district_data['Vaccination Ratio (F/M)']/district_data['Population Ratio (F/M)']


# In[13]:


district_data=district_data[['District_Key','Vaccination Ratio (F/M)','Population Ratio (F/M)','Ratio Of Ratio']]


# In[14]:


district_data.sort_values(['Ratio Of Ratio']).to_csv('../Generated/6/district-vaccination-population-ratio.csv',index=False)


# **State**

# In[15]:


data=pd.read_csv('../Data/vaccination_data_state_wise.csv',low_memory=False)


# In[16]:


data=data[data['Updated On']=='14/08/2021']


# In[17]:


data=data[['State','Male (Doses Administered)','Female (Doses Administered)']]


# In[18]:


state_vaccination=data[data['State']!='India']


# In[19]:


census=pd.read_excel('../Data/census.xlsx')


# In[20]:


census=census[(census['Level']=='STATE')&(census['TRU']=='Total')][['Name','TOT_M','TOT_F']]


# In[21]:


state_vaccination=state_vaccination[state_vaccination['State'].str.upper().isin(census['Name'].values)]
state_vaccination=state_vaccination[['State','Male (Doses Administered)','Female (Doses Administered)']].reset_index().drop('index',axis=1)


# In[22]:


census=census[census['Name'].isin(state_vaccination['State'].str.upper())]


# In[23]:


census=census.sort_values('Name').reset_index().drop('index',axis=1)


# In[24]:


state_vaccination['Vaccination Ratio (F/M)']=state_vaccination['Male (Doses Administered)']/state_vaccination['Female (Doses Administered)']


# In[25]:


state_vaccination['Population Ratio (F/M)']=census['TOT_F']/census['TOT_M']


# In[26]:


state_vaccination['Ratio Of Ratio']=state_vaccination['Vaccination Ratio (F/M)']/state_vaccination['Population Ratio (F/M)']


# In[27]:


state_vaccination=state_vaccination.sort_values(['Ratio Of Ratio'])


# In[28]:


state_vaccination[['State','Vaccination Ratio (F/M)','Population Ratio (F/M)','Ratio Of Ratio']].to_csv('../Generated/6/state-vaccination-population-ratio.csv',index=False)


# **Overall**

# In[29]:


overall_data=data[data['State']=='India'].reset_index().drop('index',axis=1)


# In[30]:


census=pd.read_excel('../Data/census.xlsx')
census=census[(census['Level']=='India')&(census['TRU']=='Total')][['Name','TOT_M','TOT_F']]


# In[31]:


overall_data['Vaccination Ratio (F/M)']=overall_data['Female (Doses Administered)']/overall_data['Male (Doses Administered)']


# In[32]:


overall_data['Population Ratio (F/M)']=census['TOT_F']/census['TOT_M']


# In[33]:


overall_data['Ratio Of Ratio']=overall_data['Vaccination Ratio (F/M)']/overall_data['Population Ratio (F/M)']


# In[34]:


overall_data[['State','Vaccination Ratio (F/M)','Population Ratio (F/M)','Ratio Of Ratio']].to_csv('../Generated/6/overall-vaccination-population-ratio.csv',index=False)

