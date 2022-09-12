#!/usr/bin/env python
# coding: utf-8

# **Loading Libraries, Dataset and Preprocessing**

# In[1]:


import numpy as np
import pandas as pd
import datetime
import json
import csv


# In[2]:


data=pd.read_csv('../Data/districts-modified.csv')


# In[3]:


data=data[data['District_Id']!='Unknown']


# **For Weekly Data**

# Making Dates Range

# In[4]:


dates=list(set(data['Date'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
dates=dates[:476]


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


for i in range(0,68):
    start_day=7*i
    subtract_date=start_day-1 
    end_day=start_day+6
    week_count={}
    district_data=data[data['Date']==dates[end_day]]
    if subtract_date>=0:
      sub_data=data[data['Date']==dates[subtract_date]] 
      old_district_ids=sub_data['District_Id'].values
    district_ids=district_data['District_Id'].values
    
    for k in district_ids:
      if k not in week_count.keys():
        week_count[k]=0
      x=district_data[district_data['District_Id']==k]['Confirmed']
      if subtract_date>=0:
        if k in old_district_ids: 
          week_count[k]=x.values[0]-sub_data[sub_data['District_Id']==k]['Confirmed'].values[0]
        else:
          week_count[k]=x.values[0]

      else:
        week_count[k]=x.values[0]
      w1.append((k,'week'+str(c),week_count[k]))
    
    c+=1


# In[7]:


w1.insert(0,('District Id','Week Id','Cases Per Week'))


# In[8]:


file = open('../Generated/3/cases-week.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(w1)


# **For Month Wise**

# In[9]:


dates=list(set(data['Date'].values))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
dates=dates[:480]


# In[10]:


m=[]
c=1


# In[11]:


for i in range(0,16):
    start_day=30*i
    subtract_date=start_day-1
    end_day=start_day+29
    month_count={}
    district_data=data[data['Date']==dates[end_day]]
    if subtract_date>=0:
      sub_data=data[data['Date']==dates[subtract_date]]
      old_district_ids=sub_data['District_Id'].values
    district_ids=district_data['District_Id'].values
    
    for k in district_ids:
      if k not in month_count.keys():
        month_count[k]=0
      x=district_data[district_data['District_Id']==k]['Confirmed']
      if subtract_date>=0:
        if k in old_district_ids: 
          month_count[k]=x.values[0]-sub_data[sub_data['District_Id']==k]['Confirmed'].values[0]
        else:
          month_count[k]=x.values[0]

      else:
        month_count[k]=x.values[0]
      m.append((k,'month'+str(c),month_count[k]))
    
    c+=1


# In[12]:


m.insert(0,('District Id','Month Id','Cases Per Month'))


# In[13]:


file = open('../Generated/3/cases-month.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(m)


# **For Overall**

# In[14]:


district_data=data[data['Date']=='2021-08-14']


# In[15]:


overall_count=[]

for i in district_data['District_Id']:
  overall_count.append((i,'Overall',district_data[district_data['District_Id']==i]['Confirmed'].values[0]))


# In[16]:


overall_count.insert(0,('District Id','Overall','Cases'))


# In[17]:


file = open('../Generated/3/cases-overall.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(overall_count)

