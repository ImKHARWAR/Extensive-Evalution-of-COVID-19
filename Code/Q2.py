#!/usr/bin/env python
# coding: utf-8

# **Importing Neccesary Files**

# In[1]:


import csv
import json
import pandas as pd
import numpy as np


# **Data Files Loading**

# In[3]:


d=open('../Generated/1/neighbor-districts-modified.json')
data=json.load(d)


# **Converting To Graph**

# In[4]:


l=[]
for i in data:
    l.extend([(i,x) for x in data[i] if (x,i) not in l])
l.insert(0,('District 1 id','District 2 id'))


# In[6]:


file = open('../Generated/2/edge-graph.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(l)

