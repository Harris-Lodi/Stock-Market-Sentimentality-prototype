# region description

"""from 'Computer Science' youtube channel
https://www.youtube.com/watch?v=4OlvGGAsj8I

Description: This program predicts if the stock price
of a company will increase or decrease based on top
news headlines.

***This is a prototype, not intended to be a final project;
all code is not object oriented or re-usable, 
this script is meant for testing purposes only!***

Note to self: continue from 11:33, or just copy from jupyter version
              Actually just use jupyter version as reference for a new version here

"""
# endregion

# region imports, packages, and modules

import pandas as pd 
import numpy as np 
from textblob import TextBlob 
import re # regular expressions
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, classification_report 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
# import csv 

# endregion

# region code

# load the data sets:
df1 = pd.read_csv("Data/News_DJIA.csv")
df2 = pd.read_csv("Data/Value_DJIA.csv")

# show the first 3 rows of data, df1
# print(df1.head(3))

# get the number of rows and columns
# print(df1.shape)

# show the first 3 rows of data, df2
# print(df2.head(3))

# get the shape of df2
# print(df2.shape)

# merge the datasets on the date field
merge = df1.merge(df2, how = 'inner', on = 'Date', left_index = True)

# show the merged data set
print(merge.head(3))
print(merge.shape)

# endregion