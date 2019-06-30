#!/usr/bin/env python
# coding: utf-8

# ### 1. Propose how you would calculate total time spent in ICU during hospitalization. Be specific what fields to use. Show example code using MIMIC III data.

# #### Total time spent in ICU during hospitalization can be calculated using ICUSTAYS tables INTIME and OUTTIME features. A difference between these features can give us the full length of time in days or secs or mins.

# In[1]:


import sqlite3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


conn = sqlite3.connect('/Users/Merin/Desktop/HAP880/HAP_880_Project/mimic.db/mimic.db')


# In[3]:


ICU = pd.read_sql('select * from icustays where hadm_id = 124064;', conn)


# In[5]:


ICU


# In[6]:


ICU['INTIME'] = pd.to_datetime(ICU['INTIME'])
ICU['OUTTIME'] = pd.to_datetime(ICU['OUTTIME'])

ICU['TOTAL_TIME_SPENT'] = (ICU['OUTTIME']-ICU['INTIME']).dt.total_seconds()/86400


# In[7]:


ICU


# ### 2. Suppose you want to build a model that predicts patient mortality anytime during hospital stay. You have access to ICD codes in the data (MIMIC III). Is it reasonable to use them in prediction? Explain why?

# #### Yes, it is very reasonable to use ICD codes as ICD codes have a clear bearing to a persons diagnosis or health condition.

# ### 3. You are given a set of LOINC codes and need to extract corresponding data during one ICU stay. Describe the process. Provide all needed details, including field names, etc

# #### LOINC codes are present in D_labitems, extracting ITEM_IDs from D_labitems and joining on ITEM_ID to LABEVENTS. LABEVENTS has HADM_ID for each admission events. Joining HADM_ID to ICUSTAYS table would help us in extracting corresponding data fro LOINC code suirng one ICU stay.

# In[8]:


d_labitems = pd.read_sql('select * from D_labitems limit 5;', conn)


# In[9]:


d_labitems


# In[10]:


labevents = pd.read_sql('select * from labevents limit 5;', conn)


# In[11]:


labevents


# In[12]:


ICU_Stay = pd.read_sql('select * from icustays limit 5;', conn)


# In[13]:


ICU_Stay


# In[ ]:




