
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


# ## Remove all those tuples having total likes < 500 !!!

# In[2]:

secondaryData = pd.read_csv("movie_metadata_primary.csv")
secondaryData = secondaryData[secondaryData['totalLikes'] >= 500]
#secondaryData


# ## Replacing director_facebook_likes containing '0' value

# In[3]:

for index, row in secondaryData.iterrows():
    if row['director_facebook_likes'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #print(temp_df)
        temp_median = temp_df['director_facebook_likes'].median()
        if temp_median == 0:
            temp_median = temp_df['totalLikes'].median()
        #print(temp_median)
        secondaryData.loc[index, 'director_facebook_likes'] = temp_median
        
            
secondaryData.head()


# ## Replacing actor_1_facebook_likes containing '0' value 

# In[4]:

for index, row in secondaryData.iterrows():
    if row['actor_1_facebook_likes'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #temp_df
        temp_median = temp_df['actor_1_facebook_likes'].median()
        if temp_median == 0:
            temp_median = temp_df['totalLikes'].median()
        #print(temp_df)
        #print(type(temp_median))
        secondaryData.loc[index, 'actor_1_facebook_likes'] = temp_median
        
            
#secondaryData


# ## Replacing actor_2_facebook_likes containing '0' value

# In[5]:

for index, row in secondaryData.iterrows():
    if row['actor_2_facebook_likes'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #temp_df
        temp_median = temp_df['actor_2_facebook_likes'].median()
        if temp_median == 0:
            temp_median = temp_df['totalLikes'].median()
        
        #print(type(temp_median))
        secondaryData.loc[index, 'actor_2_facebook_likes'] = temp_median
        
            
#secondaryData


# ## Replacing actor_3_facebook_likes containing '0' value

# In[6]:

for index, row in secondaryData.iterrows():
    if row['actor_3_facebook_likes'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #temp_df
        temp_median = temp_df['actor_3_facebook_likes'].median()
        #print(type(temp_median))
        if temp_median == 0:
            temp_median = temp_df['totalLikes'].median()
        secondaryData.loc[index, 'actor_3_facebook_likes'] = temp_median
        
            
#secondaryData


# ## Replacing movie_facebook_likes containing '0' value

# In[7]:

for index, row in secondaryData.iterrows():
    if row['movie_facebook_likes'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #temp_df
        temp_median = temp_df['movie_facebook_likes'].median()
        #print(type(temp_median))
        if temp_median == 0:
            temp_median = temp_df['totalLikes'].median()
        secondaryData.loc[index, 'movie_facebook_likes'] = temp_median
        
            
#secondaryData


# ## Replacing budget containing '0' or NaN value

# In[8]:

secondaryData['budget'].fillna(0, inplace = True)
for index, row in secondaryData.iterrows():
    if row['budget'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #temp_df
        temp_median = temp_df['budget'].median()
        #print(type(temp_median))
        if temp_median == 0:
            temp_median = temp_df['budget'].mean() 
            if temp_median == 0:
                temp_median = secondaryData['budget'].median()
        secondaryData.loc[index, 'budget'] = temp_median
        
            
#secondaryData


# ## Replacing gross containing '0' or NaN value

# In[9]:

secondaryData['gross'].fillna(0, inplace = True)
for index, row in secondaryData.iterrows():
    if row['gross'] == 0:
        genre = row['genres']
        #print(genre)
        #myList = []
        temp_df = secondaryData[secondaryData.genres == genre]
        #temp_df
        temp_median = temp_df['gross'].median()
        temp_totalLikes = row['totalLikes']
        if temp_median == 0:
            temp_median = temp_df['gross'].mean() 
            if temp_median == 0:
                temp_median = secondaryData['gross'].median()
        #print(type(temp_median))
        secondaryData.loc[index, 'gross'] = temp_median
        
            
#secondaryData


# In[10]:

secondaryData['title_year'].fillna(2010, inplace = True)


# In[11]:

#del secondaryData['color']
#del secondaryData['num_critic_for_reviews']
#del secondaryData['num_voted_users']
#del secondaryData['facenumber_in_poster']
#del secondaryData['movie_imdb_link']
#del secondaryData['num_user_for_reviews']
secondaryData.head()
io.StringIO(secondaryData.to_csv("movie_metadata_secondary.csv",index=False,sep=","))


# In[12]:

secondaryData['Norm_Gross'] = secondaryData['gross'] / secondaryData['budget']
secondaryData.head()


# In[24]:

secondaryData['colorID'] = 0
secondaryData.loc[secondaryData['color'] == 'Color', 'colorID'] = 1
#secondaryData['colorID']


# In[25]:

secondaryData.head()


# In[50]:

secondaryData.head()
actor_1_list = []

for value in secondaryData['actor_1_name']:
    if value not in actor_1_list:
        actor_1_list.append(value)        
secondaryData.head()

io.StringIO(secondaryData.to_csv("movie_metadata_secondary.csv",index=False,sep=","))


# In[51]:

secondaryData.head()


# 

# In[96]:

secondaryData = pd.read_csv("movie_metadata_secondary.csv")
count = 0
for index, row in secondaryData.iterrows():
    if row['Norm_Gross'] >= 0 and row['Norm_Gross'] < 0.5:
        secondaryData.set_value(index, 'Norm_Gross', 0)
    elif row['Norm_Gross'] >= 0.5 and row['Norm_Gross'] < 1:
        secondaryData.set_value(index, 'Norm_Gross', 1)
    elif row['Norm_Gross'] >= 1 and row['Norm_Gross'] < 1.5:
        secondaryData.set_value(index, 'Norm_Gross', 2)
    elif row['Norm_Gross'] >= 1.5 and row['Norm_Gross'] < 2:
        secondaryData.set_value(index, 'Norm_Gross', 3)
    elif row['Norm_Gross'] >= 2 and row['Norm_Gross'] < 2.5:
        secondaryData.set_value(index, 'Norm_Gross', 4)
    elif row['Norm_Gross'] >= 2.5 and row['Norm_Gross'] < 3:
        secondaryData.set_value(index, 'Norm_Gross', 5)
    elif row['Norm_Gross'] >= 3 and row['Norm_Gross'] < 3.5:
        secondaryData.set_value(index, 'Norm_Gross', 6)
    elif row['Norm_Gross'] >= 5 and row['Norm_Gross'] < 10:
        secondaryData.set_value(index, 'Norm_Gross', 7)
    else :
        secondaryData.set_value(index, 'Norm_Gross', 8)

secondaryData


# In[98]:

io.StringIO(secondaryData.to_csv("movie_metadata_secondary.csv",index=False,sep=","))


# In[ ]:



