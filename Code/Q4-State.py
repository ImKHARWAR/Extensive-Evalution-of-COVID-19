#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks
import datetime


# In[2]:


data=pd.read_csv('../Data/states.csv')


# In[3]:


state_data=data[data['State']!='India'].iloc[121:,:].reset_index().drop('index',axis=1)


# In[4]:


state_data=state_data[state_data['State']!='State Unassigned']


# # State

# **Week Wise**

# In[5]:


dates=list(set(state_data['Date'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
dates=dates[:518]


# In[6]:


w1=[]
c=1


# In[7]:


for i in range(0,74):
    start_day=7*i
    subtract_date=start_day-1
    end_day=start_day+6
    week_count={}
    week_data=state_data[state_data['Date']==dates[end_day]]
    if subtract_date>=0:
      sub_data=state_data[state_data['Date']==dates[subtract_date]]
      old_state_ids=sub_data['State'].values
    state_ids=week_data['State'].values
    
    for k in state_ids:
      if k not in week_count.keys():
        week_count[k]=0
      x=week_data[week_data['State']==k]['Confirmed']
      if subtract_date>=0:
        if k in old_state_ids: 
          week_count[k]=x.values[0]-sub_data[sub_data['State']==k]['Confirmed'].values[0]
        else:
          week_count[k]=x.values[0]

      else:
        week_count[k]=x.values[0]
      w1.append((k,'week'+str(c),week_count[k]))
    
    c+=2


# In[8]:


dates=list(set(state_data['Date'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
dates=dates[4:][:518]


# In[9]:


c=2


# In[10]:


for i in range(0,74):
    start_day=7*i
    subtract_date=start_day-1
    end_day=start_day+6
    week_count={}
    week_data=state_data[state_data['Date']==dates[end_day]]
    if subtract_date>=0:
      sub_data=state_data[state_data['Date']==dates[subtract_date]]
      old_state_ids=sub_data['State'].values
    state_ids=week_data['State'].values
    
    for k in state_ids:
      if k not in week_count.keys():
        week_count[k]=0
      x=week_data[week_data['State']==k]['Confirmed']
      if subtract_date>=0:
        if k in old_state_ids: 
          week_count[k]=x.values[0]-sub_data[sub_data['State']==k]['Confirmed'].values[0]
        else:
          week_count[k]=x.values[0]

      else:
        week_count[k]=x.values[0]
      w1.append((k,'week'+str(c),week_count[k]))
    
    c+=2


# In[11]:


def Sort_Tuple(tup): 
    return(sorted(tup, key = lambda x: int(x[1].replace('week',''))))


# In[12]:


w1=Sort_Tuple(w1)


# **Month**

# In[13]:


dates=list(set(state_data['Date'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
dates=dates[:510]


# In[14]:


m=[]
c=1


# In[15]:


for i in range(0,17):
    start_day=30*i
    subtract_date=start_day-1
    end_day=start_day+29
    month_count={}
    month_data=state_data[state_data['Date']==dates[end_day]]
    if subtract_date>=0:
      sub_data=state_data[state_data['Date']==dates[subtract_date]]
      old_state_ids=sub_data['State'].values
    state_ids=month_data['State'].values
    
    for k in state_ids:
      if k not in month_count.keys():
        month_count[k]=0
      x=month_data[month_data['State']==k]['Confirmed']
      if subtract_date>=0:
        if k in old_state_ids: 
          month_count[k]=x.values[0]-sub_data[sub_data['State']==k]['Confirmed'].values[0]
        else:
          month_count[k]=x.values[0]

      else:
        month_count[k]=x.values[0]
      m.append((k,'month'+str(c),month_count[k]))
    
    c+=1


# In[16]:


k=list(set(state_data['State'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
k.remove('Lakshadweep')


# In[17]:


state_dict=[]
for d_id in k:
    cases_week=[(h[1],h[2]) for h in w1 if h[0]==d_id]
    cases_month=[(h[1],h[2]) for h in m if h[0]==d_id]
    #Week
    x1=[int(i[0].replace('week',"")) for i in cases_week]
    y1=[i[1] for i in cases_week]
    z1=find_peaks(y1)
    wave1=[i for i in z1[0] if i<80]
    wave2=[i for i in z1[0] if i>80]
    i_w1=0
    for i in wave1:
        if y1[i_w1]<y1[i]:
            i_w1=i
    #print(d_id," week ",x1[i_w1],' value ',y1[i_w1])
    i_w2=80
    for i in wave2:
        if y1[i_w2]<y1[i]:
            i_w2=i
    #print(d_id," week ",x1[i_w2],' value ',y1[i_w2])
    #Month
    
    x2=[int(i[0].replace('month',"")) for i in cases_month]
    y2=[i[1] for i in cases_month]
    z2=find_peaks(y2)
    wave1=[i for i in z2[0] if i<10]
    wave2=[i for i in z2[0] if i>10]
    i_m1=0
    for i in wave1:
        if y2[i_m1]<y2[i]:
            i_m1=i
    #print(d_id," month ",x2[i_m1],' value ',y2[i_m1])
    i_m2=10
    for i in wave2:
        if y2[i_m2]<y2[i]:
            i_m2=i
    #print(d_id," month ",x2[i_m2],' value ',y2[i_m2])
    state_dict.append((d_id,'week'+str(x1[i_w1]),'week'+str(x1[i_w2]),'month'+str(x2[i_m1]),'month'+str(x2[i_m2])))
    


# In[18]:


state_dict.insert(0,('State','Wave 1 Week Id','Wave 2 Week Id','Wave 1 Month Id','Wave 2 Month Id'))


# In[19]:


file = open('../Generated/4/state-peak.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(state_dict)

