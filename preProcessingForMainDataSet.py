
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


# In[18]:

primaryData = pd.read_csv("movie_metadata.csv")
#primaryData.head()


# ## Replace all NaN(null) values with 0 in director_facebook_likes,  actor_1_facebook_likes, actor_2_facebook_likes, actor_3_facebook_likes, movie_facebook_likes

# In[17]:

primaryData['director_facebook_likes'].fillna(0, inplace = True)
primaryData['actor_1_facebook_likes'].fillna(0, inplace = True)
primaryData['actor_2_facebook_likes'].fillna(0, inplace = True)
primaryData['actor_3_facebook_likes'].fillna(0, inplace = True)
primaryData['movie_facebook_likes'].fillna(0, inplace = True)
#primaryData.head()


# ## Now, calculate total likes' weightage and place it in new column

# In[19]:

primaryData['totalLikes'] = (0.9 * primaryData['director_facebook_likes']) + primaryData['actor_1_facebook_likes'] + primaryData['actor_2_facebook_likes'] + primaryData['actor_3_facebook_likes'] + primaryData['movie_facebook_likes']
#del primaryData['temp']
io.StringIO(primaryData.to_csv("movie_metadata_primary.csv",index=False,sep=","))
#primaryData.head()


# In[ ]:



