# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:47:18 2020

@author: shara
"""

import requests
from bs4 import BeautifulSoup as bs  
import re 
sigma_reviews=[]

for i in range(1,20):
  ip=[]  
  url="https://www.amazon.in/Sigma-DC-DN-Contemporary-Black/product-reviews/B077BWD2BB/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html") 
  reviews = soup.findAll("span",attrs={"Class", "review-text-content"})  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  sigma_reviews=sigma_reviews+ip  


with open("sigma.txt","w",encoding='utf8') as output:
    output.write(str(sigma_reviews))
    
import pandas as pd

sigma = pd.DataFrame(columns = ["reviews"])
sigma["reviews"] = sigma_reviews

review_text = []

for i in  range(0, (len(sigma.reviews)), 1):
    review_text.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", str(sigma.reviews[i])).lower().split()))

with open("G:\DS Assignments\Text Mining\stop.txt","r") as st:
    stop_words = st.read()

review_stop = []    
for i in  range(0, (len(review_text)), 1):
    review_stop.append(' '.join(w for w in str(review_text[i]).split(" ") if not w in stop_words))

review_text[1].split(" ")
nltk.download('words')
words = set(nltk.corpus.words.words())


review_english = []

for i in  range(0, (len(review_stop)), 1):
    review_english.append(' '.join(w for w in str(review_stop[i]).split(" ") if w in words))
    
review_english = [i for i in review_english if len(i) > 2 ]

from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 
nltk.download('wordnet')
review_lem = []

for i in  range(0, (len(review_english)), 1):
    review_lem.append(' '.join(lemmatizer.lemmatize(w) for w in str(review_english[i]).split(" ")))
    
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

po = "Positive"
ne = "Negative"
nu = "Neutral"


Emotion = []
for i in review_lem:
    analysis = sia.polarity_scores(i)
    if analysis["compound"] > 0: 
        Emotion.append(po)
    elif analysis["compound"] == 0: 
        Emotion.append(nu)
    else: 
        Emotion.append(ne)




Compund = []
for i in review_lem:
    analysis = sia.polarity_scores(i)
    Compund.append(analysis["compound"])
    
import matplotlib.pyplot as plt    
    
plt.plot(Compund)
sigma = pd.DataFrame(columns = ["Reviews","Emotion", "Compound"])
sigma["Reviews"] = review_lem
sigma["Emotion"] = Emotion
sigma["Compound"] = Compund
sigma
