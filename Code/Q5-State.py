#!/usr/bin/env python
# coding: utf-8

# **Loading Libraries**

# In[1]:


import numpy as np
import pandas as pd
import csv
import datetime


# **Loading Data and Preprocessing**

# In[2]:


data=pd.read_csv('../Data/vaccination_data_state_wise.csv',low_memory=False).fillna(0)


# In[3]:


data=data[data['State']!='India']


# **Weekly**

# Making Dates Range 

# In[4]:


dates=list(set(data['Updated On'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
dates=dates[1:][:217]


# Data in Vaccination dataset is cumulative. We need to find the absolute data per week. So we have taken two index per week denoting start and end date of week and we subtract data[endweek] with data[start-1] (Which is data of previous week to get absolute value)
# 
# Similar Approach for
# 
# 1) Week
# 
# 2) Month
# 
# 3) Overall

# In[5]:


w1=[]
c=1


# In[6]:


for i in range(31):
  start_day=7*i
  subtract_date=start_day-1 
  end_day=start_day+6
  week_count={}
  state_data=data[data['Updated On']==dates[end_day]]
  if subtract_date>=0:
      
      sub_data=data[data['Updated On']==dates[subtract_date]]
      old_state_ids=sub_data['State'].values
  state_ids=state_data['State'].values
  for k in state_ids:
      if k not in week_count.keys():
        week_count[k]=[0,0]
      x=state_data[state_data['State']==k]
      if subtract_date>=0:
        if k in old_state_ids: 
          week_count[k][0]=int(x['First Dose Administered'].values[0])-int(sub_data[sub_data['State']==k]['First Dose Administered'].values[0])
          week_count[k][1]=int(x['Second Dose Administered'].values[0])-int(sub_data[sub_data['State']==k]['Second Dose Administered'].values[0])
        else:
          week_count[k][0]=int(x['First Dose Administered'].values[0])
          week_count[k][1]=int(x['Second Dose Administered'].values[0])

      else:
        week_count[k][0]=int(x['First Dose Administered'].values[0])
        week_count[k][1]=int(x['Second Dose Administered'].values[0])
      w1.append((k,'week'+str(c),week_count[k][0],week_count[k][1]))
    
  c+=1


# In[7]:


w1=sorted(w1, key = lambda x: x[0])


# In[8]:


w1.insert(0,('State','Time Id','Dose 1','Dose 2',))


# In[9]:


file = open('../Generated/5/state-vaccinated-count-week.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(w1)


# **For Monthly Data**

# In[10]:


dates=list(set(data['Updated On'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
dates=dates[:230]


# In[11]:


m=[]
c=1


# In[12]:


for i in range(7):
  start_day=30*i
  subtract_date=start_day-1 
  end_day=start_day+29
  month_count={}
  state_data=data[data['Updated On']==dates[end_day]]
  if subtract_date>=0:
      
      sub_data=data[data['Updated On']==dates[subtract_date]]
      old_state_ids=sub_data['State'].values
  state_ids=state_data['State'].values
  for k in state_ids:
      if k not in month_count.keys():
        month_count[k]=[0,0]
      x=state_data[state_data['State']==k]
      if subtract_date>=0:
        if k in old_state_ids: 
          month_count[k][0]=int(x['First Dose Administered'].values[0])-int(sub_data[sub_data['State']==k]['First Dose Administered'].values[0])
          month_count[k][1]=int(x['Second Dose Administered'].values[0])-int(sub_data[sub_data['State']==k]['Second Dose Administered'].values[0])
        else:
          month_count[k][0]=int(x['First Dose Administered'].values[0])
          month_count[k][1]=int(x['Second Dose Administered'].values[0])

      else:
        month_count[k][0]=int(x['First Dose Administered'].values[0])
        month_count[k][1]=int(x['Second Dose Administered'].values[0])
      m.append((k,'month'+str(c),month_count[k][0],month_count[k][1]))
    
  c+=1


# In[13]:


m=sorted(m, key = lambda x: x[0])


# In[14]:


m.insert(0,('State','Time Id','Dose 1','Dose 2',))


# In[15]:


file = open('../Generated/5/state-vaccinated-count-month.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(m)


# **For Overall Data**

# In[16]:


dates=list(set(data['Updated On'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
dates=dates[:217]


# In[17]:


overall=[]
state_data=data[data['Updated On']==dates[-1]]


# In[18]:


for i in state_data['State']:
    x1=state_data[state_data['State']==i]['First Dose Administered'].values[0]
    x2=state_data[state_data['State']==i]['Second Dose Administered'].values[0]
    overall.append((i,'Overall',x1,x2))


# In[19]:


overall.insert(0,('State','Time Id','Dose 1','Dose 2',))


# In[20]:


file = open('../Generated/5/state-vaccinated-count-overall.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(overall)

