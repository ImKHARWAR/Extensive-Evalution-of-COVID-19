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


data=pd.read_csv('../Data/vaccination_data_district_wise.csv',low_memory=False).fillna(0)


# **Weekly Data**

# Setting Dates Range 

# In[22]:


dates=[]
for i in data.columns[6:]:
  dates.append(i.split('.')[0])
dates=list(set(dates))
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

# In[4]:


w1=[]
c=1


# In[5]:


for i in range(31):
  start_day=7*i
  subtract_date=start_day-1 
  end_day=start_day+6
  list_column=['S No', 'State_Code', 'State', 'District_Key', 'Cowin Key', 'District',dates[end_day]+'.3',dates[end_day]+'.4']
  week_count={}
  district_data=data[list_column].iloc[1:,:]
  if subtract_date>=0:
      list_old_column=['S No', 'State_Code', 'State', 'District_Key', 'Cowin Key', 'District',dates[subtract_date]+'.3',dates[subtract_date]+'.4']
      sub_data=data[list_old_column].iloc[1:,:] 
      old_district_ids=sub_data['District_Key'].values
  district_ids=district_data['District_Key'].values
  for k in district_ids:
      if k not in week_count.keys():
        week_count[k]=[0,0]
      x=district_data[district_data['District_Key']==k]
      if subtract_date>=0:
        if k in old_district_ids: 
          week_count[k][0]=int(x[dates[end_day]+'.3'].values[0])-int(sub_data[sub_data['District_Key']==k][dates[subtract_date]+'.3'].values[0])
          week_count[k][1]=int(x[dates[end_day]+'.4'].values[0])-int(sub_data[sub_data['District_Key']==k][dates[subtract_date]+'.4'].values[0])
        else:
          week_count[k][0]=int(x[dates[end_day]+'.3'].values[0])
          week_count[k][1]=int(x[dates[end_day]+'.4'].values[0])

      else:
        week_count[k][0]=int(x[dates[end_day]+'.3'].values[0])
        week_count[k][1]=int(x[dates[end_day]+'.4'].values[0])
      w1.append((k,'week'+str(c),week_count[k][0],week_count[k][1]))
    
  c+=1


# In[6]:


w1=sorted(w1, key = lambda x: x[0])


# In[7]:


w1.insert(0,('District','Time Id','Dose 1','Dose 2',))


# In[8]:


file = open('../Generated/5/district-vaccinated-count-week.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(w1)


# **Monthly Data**

# In[9]:


dates=[]
for i in data.columns[6:]:
  dates.append(i.split('.')[0])
dates=list(set(dates))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
dates=dates[:210]


# In[10]:


m=[]
c=1


# In[11]:


for i in range(7):
  start_day=30*i
  subtract_date=start_day-1 
  end_day=start_day+29
  list_column=['S No', 'State_Code', 'State', 'District_Key', 'Cowin Key', 'District',dates[end_day]+'.3',dates[end_day]+'.4']
  month_count={}
  district_data=data[list_column].iloc[1:,:]
  if subtract_date>=0:
      list_old_column=['S No', 'State_Code', 'State', 'District_Key', 'Cowin Key', 'District',dates[subtract_date]+'.3',dates[subtract_date]+'.4']
      sub_data=data[list_old_column].iloc[1:,:] 
      old_district_ids=sub_data['District_Key'].values
  district_ids=district_data['District_Key'].values
  for k in district_ids:
      if k not in month_count.keys():
        month_count[k]=[0,0]
      x=district_data[district_data['District_Key']==k]
      if subtract_date>=0:
        if k in old_district_ids: 
          month_count[k][0]=int(x[dates[end_day]+'.3'].values[0])-int(sub_data[sub_data['District_Key']==k][dates[subtract_date]+'.3'].values[0])
          month_count[k][1]=int(x[dates[end_day]+'.4'].values[0])-int(sub_data[sub_data['District_Key']==k][dates[subtract_date]+'.4'].values[0])
        else:
          month_count[k][0]=int(x[dates[end_day]+'.3'].values[0])
          month_count[k][1]=int(x[dates[end_day]+'.4'].values[0])

      else:
        month_count[k][0]=int(x[dates[end_day]+'.3'].values[0])
        month_count[k][1]=int(x[dates[end_day]+'.4'].values[0])
      m.append((k,'month'+str(c),month_count[k][0],month_count[k][1]))
    
  c+=1


# In[12]:


m=sorted(m, key = lambda x: x[0])


# In[13]:


m.insert(0,('District Id','Time Id','Dose 1','Dose 2',))


# In[14]:


file = open('../Generated/5/district-vaccinated-count-month.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(m)


# **For Overall**

# In[15]:


dates=[]
for i in data.columns[6:]:
  dates.append(i.split('.')[0])
dates=list(set(dates))
dates=sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
dates=dates[:220]


# In[16]:


list_column=['S No', 'State_Code', 'State', 'District_Key', 'Cowin Key', 'District',dates[-1]+'.3',dates[-1]+'.4']


# In[17]:


district_data=data[list_column].iloc[1:,:]
overall=[]


# In[18]:


for i in district_data['District_Key'].values:
    x1=district_data[district_data['District_Key']==i][dates[-1]+'.3'].values[0]
    x2=district_data[district_data['District_Key']==i][dates[-1]+'.4'].values[0]
    overall.append((i,'Overall',x1,x2))


# In[19]:


overall=sorted(overall, key = lambda x: x[0])


# In[20]:


overall.insert(0,('District Id','Time Id','Dose 1','Dose 2',))


# In[21]:


file = open('../Generated/5/district-vaccinated-count-overall.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(overall)

