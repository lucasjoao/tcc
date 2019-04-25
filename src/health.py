#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd

# path changes if you run this inside src directory
data = pd.read_csv('datasets/OSMI_Mental_Health_in_Tech_Survey_2018.csv')
data.head()
