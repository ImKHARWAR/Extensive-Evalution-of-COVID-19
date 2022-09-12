#!/usr/bin/env python
# coding: utf-8

# **Loading Libraries**

# In[1]:


import numpy as np
import pandas as pd
import datetime


# **Loading Data**

# In[2]:


data=pd.read_csv('../Data/vaccination_data_state_wise.csv')


# In[3]:


dates=list(set(data['Updated On'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
dates=dates[:211]
total_vaccination_days=211


# In[4]:


census=pd.read_excel('../Data/census.xlsx')


# **Preprocessing**

# In[5]:


census=census[(census['Level']=='STATE')&(census['TRU']=='Total')][['Name','TOT_P']]


# In[6]:


last_week_start_data=data[(data['State']!='India')&(data['Updated On']==dates[-8])].reset_index().drop('index',axis=1)


# In[7]:


state_vaccination=data[(data['State']!='India')&(data['Updated On']==dates[-1])]


# In[8]:


state_vaccination=state_vaccination[state_vaccination['State'].str.upper().isin(census['Name'].values)]
state_vaccination=state_vaccination[['State','First Dose Administered']].reset_index().drop('index',axis=1)


# In[9]:


census=census[census['Name'].isin(state_vaccination['State'].str.upper())]


# In[10]:


census=census.sort_values('Name').reset_index().drop('index',axis=1)


# In[11]:


state_vaccination['Remaining Population']=census['TOT_P']-state_vaccination['First Dose Administered']


# In[12]:


last_week_start_data=last_week_start_data.merge(state_vaccination,on=['State'])


# In[13]:


state_vaccination['Rate']=(last_week_start_data['First Dose Administered_y']-last_week_start_data['First Dose Administered_x'])/7


# In[14]:


state_vaccination['Day To Complete Dose 1']=np.ceil(state_vaccination['Remaining Population']/state_vaccination['Rate'])


# In[15]:


state_vaccination['Date Of Complete']='14/08/2021'


# In[16]:


for i in range(state_vaccination.shape[0]):
    start_date=datetime.datetime.strptime('14/08/2021', "%d/%m/%Y")
    end_date=start_date+datetime.timedelta(days=int(state_vaccination['Day To Complete Dose 1'][i]))
    state_vaccination.loc[i,['Date Of Complete']]=end_date.strftime("%d/%m/%Y")


# **Converting To CSV**

# In[17]:


state_vaccination[['State','Remaining Population','Rate','Date Of Complete']].to_csv('../Generated/9/complete-vaccination.csv',index=False)

