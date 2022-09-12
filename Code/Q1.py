#!/usr/bin/env python
# coding: utf-8

# **Importing Necessary Library**

# In[1]:


import numpy as np
import pandas as pd


# ***Loading Dataset***

# In[2]:


district_vaccine=pd.read_csv('../Data/vaccination_data_district_wise.csv',encoding='utf-8', low_memory=False)


# In[3]:


district_covid=pd.read_csv('../Data/district_wise.csv')


# In[4]:


import json
d=open('../Data/neighbor-districts.json')
data=json.load(d)


# ***Finding Common District between Covid Dataset and Vaccine Dataset***

# In[5]:


a=set(district_vaccine['District_Key'])
b=set(district_covid['District_Key'])
common_distict=list(a.intersection(b))


# **Dictionary to store the Distict_id and its corresponding District_Key**

# In[6]:


def preprocessing(s):
    s1=s.split("/")[0]
    s1=s1.replace('_'," ").replace('-'," ")
    s1=s1.title()
    s1=s1.replace("District","").strip()

    return s1


# In[7]:


dcodemapper={}
absent=[]
for i in data.keys():
    x=preprocessing(i)
    if len(district_vaccine[district_vaccine['District']==x])==1:
        if district_vaccine[district_vaccine['District']==x]['District_Key'].values[0] in common_distict:
            dcodemapper[i]=district_vaccine[district_vaccine['District']==x]['District_Key'].values[0]
    else:
        absent.append(i)


# **Handling Same name Districts**

# In[8]:


same_district=['hamirpur/Q2086180','hamirpur/Q2019757','pratapgarh/Q1585433','pratapgarh/Q1473962','balrampur/Q1948380','balrampur/Q16056268','bilaspur/Q1478939','bilaspur/Q100157','aurangabad/Q43086','aurangabad/Q592942']


# In[9]:


dcodemapper['hamirpur/Q2086180']='HP_Hamirpur' 
dcodemapper['hamirpur/Q2019757']='UP_Hamirpur'
dcodemapper['pratapgarh/Q1585433']='RJ_Pratapgarh' 
dcodemapper['pratapgarh/Q1473962']='UP_Pratapgarh' 
dcodemapper['balrampur/Q1948380']='UP_Balrampur'
dcodemapper['balrampur/Q16056268']='CT_Balrampur'
dcodemapper['bilaspur/Q1478939']='HP_Bilaspur'
dcodemapper['bilaspur/Q100157']='CT_Bilaspur' 
dcodemapper['aurangabad/Q43086']='BR_Aurangabad'
dcodemapper['aurangabad/Q592942']='MH_Aurangabad'


# In[10]:


for i in same_district:
    absent.remove(i)


# **Handling Multi-entry District**

# In[11]:


for i in absent:
  x=preprocessing(i)
  if len(district_vaccine[district_vaccine['District']==x])>1:
    if district_vaccine[district_vaccine['District']==x]['District_Key'].values[0] in common_distict:
      dcodemapper[i]=district_vaccine[district_vaccine['District']==x]['District_Key'].values[0]


# **Handling Spelling Error District**

# In[12]:


dcodemapper['aizwal/Q1947322']='MZ_Aizawl'
dcodemapper['anugul/Q1772807']='OR_Angul'
dcodemapper['ashok_nagar/Q2246416']='MP_Ashoknagar'
dcodemapper['badgam/Q2594218']='JK_Budgam'
dcodemapper['baleshwar/Q2022279']='OR_Balasore'
dcodemapper['banas_kantha_district/Q806125']='GJ_Banaskantha'
dcodemapper['bangalore_rural/Q806464']='KA_Bengaluru Rural'
dcodemapper['bangalore_urban/Q806463']='KA_Bengaluru Urban'
dcodemapper['baramula/Q1912057']='JK_Baramulla'
dcodemapper['baudh/Q2363639']='OR_Boudh'
dcodemapper['belgaum_district/Q815464']='KA_Belagavi'
dcodemapper['bellary_district/Q1791926']='KA_Ballari'
dcodemapper['bemetara/Q16254159']='CT_Bametara'
dcodemapper['bid/Q814037']='MH_Beed'
dcodemapper['bishwanath/Q28110722']='AS_Biswanath'
dcodemapper['chamarajanagar_district/Q862912']='KA_Chamarajanagara'
dcodemapper['dantewada/Q100211']='CT_Dakshin Bastar Dantewada'
dcodemapper['debagarh/Q2269639']='OR_Deogarh'
dcodemapper['devbhumi_dwaraka_district/Q14594717']='GJ_Devbhumi Dwarka'
dcodemapper['dhaulpur/Q1207709']='RJ_Dholpur'
dcodemapper['east_karbi_anglong/Q42558']='AS_Karbi Anglong'
dcodemapper['faizabad/Q1814132']='UP_Ayodhya'
dcodemapper['fategarh_sahib/Q172485']='PB_Fatehgarh Sahib'
dcodemapper['firozpur/Q172385']='PB_Ferozepur'
dcodemapper['gondiya/Q1917227']='MH_Gondia'
dcodemapper['hugli/Q548518']='WB_Hooghly'
dcodemapper['jagatsinghapur/Q971581']='OR_Jagatsinghpur'
dcodemapper['jajapur/Q2087771']='OR_Jajpur'
dcodemapper['jalor/Q1460832']='RJ_Jalore'
dcodemapper['jhunjhunun/Q1471427']='RJ_Jhunjhunu'
dcodemapper['jyotiba_phule_nagar/Q1891677']='UP_Amroha'
dcodemapper['kabirdham/Q2450255']='CT_Kabeerdham'
dcodemapper['kaimur_(bhabua)/Q77367']='BR_Kaimur'
dcodemapper['kanchipuram_district/Q15157']='TN_Kancheepuram'
dcodemapper['kheri/Q1755447']='UP_Lakhimpur Kheri'
dcodemapper['kochbihar/Q2728658']='WB_Cooch Behar'
dcodemapper['kodarma/Q2085480']='JH_Koderma'
dcodemapper['komram_bheem/Q28170184']='TG_Komaram Bheem'
dcodemapper['lahul_and_spiti/Q837595']='HP_Lahaul and Spiti'
dcodemapper['mahesana_district/Q2019694']='GJ_Mehsana'
dcodemapper['mahrajganj/Q1356139']='UP_Maharajganj'
dcodemapper['maldah/Q2049820']='WB_Malda'
dcodemapper['marigaon/Q42737']='AS_Morigaon'
dcodemapper['muktsar/Q1947359']='PB_Sri Muktsar Sahib'
dcodemapper['mumbai_city/Q2341660']='MH_Mumbai'
dcodemapper['nandubar/Q1623525']='MH_Nandurbar'
dcodemapper['narsimhapur/Q2341616']='MP_Narsinghpur'
dcodemapper['nav_sari_district/Q1797349']='GJ_Navsari'
dcodemapper['pakaur/Q2295930']='JH_Pakur'
dcodemapper['palghat/Q1535742']='KL_Palakkad'
dcodemapper['panch_mahal_district/Q1781463']='GJ_Panchmahal'
dcodemapper['pashchim_champaran/Q100124']='BR_West Champaran'
dcodemapper['pashchimi_singhbhum/Q1950527']='JH_West Singhbhum'
dcodemapper['pattanamtitta/Q634935']='KL_Pathanamthitta'
dcodemapper['purba_champaran/Q49159']='BR_East Champaran'
dcodemapper['purbi_singhbhum/Q2452921']='JH_East Singhbhum'
dcodemapper['puruliya/Q307474']='WB_Purulia'
dcodemapper['rae_bareilly/Q1321157']='UP_Rae Bareli'
dcodemapper['rajauri/Q544279']='JK_Rajouri'
dcodemapper['rangareddy/Q15388']='TG_Ranga Reddy'
dcodemapper['ri-bhoi/Q1884672']='ML_Ribhoi'
dcodemapper['sabar_kantha_district/Q1772856']='GJ_Sabarkantha'
dcodemapper['sahibzada_ajit_singh_nagar/Q2037672']='PB_S.A.S. Nagar'
dcodemapper['sait_kibir_nagar/Q1945445']='UP_Sant Kabir Nagar'
dcodemapper['sant_ravidas_nagar/Q127533']='UP_Bhadohi'
dcodemapper['sepahijala/Q16086076']='TR_Sipahijala'
dcodemapper['seraikela_kharsawan/Q2362658']='JH_Saraikela-Kharsawan'
dcodemapper['shaheed_bhagat_singh_nagar/Q202710']='PB_Shahid Bhagat Singh Nagar'
dcodemapper['sharawasti/Q1945458']='UP_Shrawasti'
dcodemapper['shimoga_district/Q2981389']='KA_Shivamogga'
dcodemapper['shopian/Q2073646']='JK_Shopiyan'
dcodemapper['siddharth_nagar/Q1815339']='UP_Siddharthnagar'
dcodemapper['sivagangai_district/Q15195']='TN_Sivaganga'
dcodemapper['sonapur/Q1473957']='OR_Subarnapur'
dcodemapper['sri_ganganagar/Q1419696']='RJ_Ganganagar'
dcodemapper['sri_potti_sriramulu_nellore/Q15383']='AP_S.P.S. Nellore'
dcodemapper['the_dangs/Q1135616']='GJ_Dang'
dcodemapper['the_nilgiris_district/Q15188']='TN_Nilgiris'
dcodemapper['thoothukudi_district/Q15198']='TN_Thoothukkudi'
dcodemapper['tiruchchirappalli_district/Q15201']='TN_Tiruchirappalli'
dcodemapper['tirunelveli_kattabo/Q15200']='TN_Tirunelveli'
dcodemapper['tiruvanamalai_district/Q15207']='TN_Tiruvannamalai'
dcodemapper['tumkur_district/Q1301635']='KA_Tumakuru'
dcodemapper['yadagiri_district/Q1786949']='KA_Yadgir'
dcodemapper['bijapur_district/Q1727570']='KA_Vijayapura'
dcodemapper['ysr/Q15342']='AP_Y.S.R. Kadapa'


# **Converting To Json**

# In[13]:


d_json={}
c=0
for i in data.keys():
    if i in dcodemapper.keys():
        d_json[dcodemapper[i]]=[dcodemapper[j] for j in data[i] if j in dcodemapper.keys()]
        


# In[14]:


for i in d_json:
    d_json[i].sort()


# In[15]:


with open("../Generated/1/neighbor-districts-modified.json", "w") as outfile:
    json.dump(d_json, outfile,sort_keys=True)

