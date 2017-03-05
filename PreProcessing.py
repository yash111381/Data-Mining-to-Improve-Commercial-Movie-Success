
# coding: utf-8

# In[1]:

from __future__ import print_function

import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
#import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import linear_model, pipeline
#import category_encoders as ce
import io

from sklearn import preprocessing
from collections import defaultdict


# ## This is the main data set with original values
# 

# In[72]:

main_df = pd.read_csv("movie_metadata.csv")
#main_df.count


# ## This is the data set with director's fb likes = 0 removed!!!

# In[64]:

director_fb_df = main_df[main_df.director_facebook_likes != 0]  
#director_fb_df


# ## This is actor 1 with fb likes <= 100 replaced with median

# In[67]:

actor1Median = director_fb_df['actor_1_facebook_likes'].median()
#print(actor1Median)
director_fb_df['actor_1_facebook_likes'].replace(range(0, 100), actor1Median)
director_fb_df = director_fb_df[director_fb_df.actor_1_facebook_likes != 0] 
#director_fb_df


# ## This is actor 2 with fb likes <= 100 replaced with median

# In[69]:

actor2Median = director_fb_df['actor_2_facebook_likes'].median()
#print(actor2Median)
director_fb_df['actor_2_facebook_likes'].replace(range(0, 100), actor2Median)
director_fb_df = director_fb_df[director_fb_df.actor_2_facebook_likes != 0] 
#director_fb_df


# ## This is actor 3 with fb likes <= 100 replaced with median

# In[73]:

actor3Median = director_fb_df['actor_3_facebook_likes'].median()
#print(actor3Median)
director_fb_df['actor_3_facebook_likes'].replace(range(0, 100), actor3Median)
director_fb_df = director_fb_df[director_fb_df.actor_3_facebook_likes != 0] 
#director_fb_df


# ## Gross null values are sent into test data set and then removed in original data set

# In[87]:

grossForTest_df = director_fb_df[director_fb_df['gross'].isnull()]
io.StringIO(grossForTest_df.to_csv("movie_metadata_test.csv",index=False,sep=","))

grossForTrain_df = director_fb_df[director_fb_df['gross'].notnull()]
#grossForTrain_df


# ## This is about cast-total fb likes < 100 removed!!!

# In[91]:

totalFbLikes_df = grossForTrain_df[grossForTrain_df.cast_total_facebook_likes >= 100]
#totalFbLikes_df


# In[ ]:



