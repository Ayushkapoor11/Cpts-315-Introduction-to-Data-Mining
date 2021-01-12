import ROCR
import(xgboost)
import(textmining)
import(str)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import findspark
import nltk


lyrics = pd.read_csv("C:/music.csv")
lyrics.shape 
lyrics.head() 
X = lyrics.drop('Class', axis=1)
y = lyrics['Class']


#Determine the count ofeach of the words
    top_ten_wordcount = count_of_each_words.takeOrdered(10, key=lambda x: -x[1])
    #after_removed=remove_Stop_words(set_of_words)
    #print("skdbv jk",after_removed)
    stopwords_removed_top_ten = set_of_words.filter(lambda x: x not in stopwords).map(lambda x: (x, 1)).reduceByKey(\
        add).takeOrdered(12, key=lambda x: -x[1])
