# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:16:27 2020

@author: shara
"""

import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import tweepy as twt
consumer_key = "coXS7WiEBAn92bEX3Vc0kldbs"
consumer_secret = "vnP92eztcT9P4i5XUY0R7DAjmsF3GToJSYXP5C4E76DUEIlHOb"
access_key = "1327915081745588225-Dl7ggfgcYuNUga1HAyWCvoR6mjb12h"
access_secret = "9TE6Ac6s311RSqXFycjUngSIX6cjHJqsvieyjV1by95xN"
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem import WordNetLemmatizer

alltweets = []

def get_all_tweets(screen_name):
    auth = twt.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = twt.API(auth)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    while len(new_tweets)>0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
       
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print ("...%s tweets downloaded so far" % (len(alltweets)))                
 
    outtweets = [[tweet.created_at,tweet.entities["hashtags"],tweet.entities["user_mentions"],tweet.favorite_count,
                  tweet.geo,tweet.id_str,tweet.lang,tweet.place,tweet.retweet_count,tweet.retweeted,tweet.source,tweet.text,
                  tweet._json["user"]["location"],tweet._json["user"]["name"],tweet._json["user"]["time_zone"],
                  tweet._json["user"]["utc_offset"]] for tweet in alltweets]
    
    import pandas as pd
    tweets_df = pd.DataFrame(columns = ["time","hashtags","user_mentions","favorite_count",
                                    "geo","id_str","lang","place","retweet_count","retweeted","source",
                                    "text","location","name","time_zone","utc_offset"])
    tweets_df["time"]  = pd.Series([str(i[0]) for i in outtweets])
    tweets_df["hashtags"] = pd.Series([str(i[1]) for i in outtweets])
    tweets_df["user_mentions"] = pd.Series([str(i[2]) for i in outtweets])
    tweets_df["favorite_count"] = pd.Series([str(i[3]) for i in outtweets])
    tweets_df["geo"] = pd.Series([str(i[4]) for i in outtweets])
    tweets_df["id_str"] = pd.Series([str(i[5]) for i in outtweets])
    tweets_df["lang"] = pd.Series([str(i[6]) for i in outtweets])
    tweets_df["place"] = pd.Series([str(i[7]) for i in outtweets])
    tweets_df["retweet_count"] = pd.Series([str(i[8]) for i in outtweets])
    tweets_df["retweeted"] = pd.Series([str(i[9]) for i in outtweets])
    tweets_df["source"] = pd.Series([str(i[10]) for i in outtweets])
    tweets_df["text"] = pd.Series([str(i[11]) for i in outtweets])
    tweets_df["location"] = pd.Series([str(i[12]) for i in outtweets])
    tweets_df["name"] = pd.Series([str(i[13]) for i in outtweets])
    tweets_df["time_zone"] = pd.Series([str(i[14]) for i in outtweets])
    tweets_df["utc_offset"] = pd.Series([str(i[15]) for i in outtweets])
    tweets_df.to_csv(screen_name+"_tweets.csv")
    return tweets_df
trump = get_all_tweets("realDonaldTrump")
trump.dtypes
print(range(100, 1))
tweets = trump['text']

tweets_text = []

import re

for i in  range(0, (len(tweets)), 1):
    tweets_text.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", str(tweets[i])).lower().split()))
    
tweets_text = [i for i in tweets_text if len(i) > 3 ]

tweets_text_join = " ".join(tweets_text)
tweets_text_join.split(" ")
z= []
x = tweets_text_join.split(" ")
   
for i in x:
    if len(i) > 3:
        z.append(i)
        
z = " ".join(z)

z = re.sub(r'\w*\d\w*', '', z).strip()

with open("G:\DS Assignments\Text Mining\stop.txt","r") as st:
    stop_words = st.read()

z = " ".join ([w for w in z.split(" ") if not w in stop_words])

wordcloud_z1 = WordCloud(background_color='black', width=1800, height=1400).generate(z)
plt.imshow(wordcloud_z1)
with open("G:\DS Assignments\Text Mining\positive-words.txt","r") as pos:
  poswords = pos.read()
poswords = poswords.split("\n") 
poswords = poswords[36:]
with open("G:\\DS Assignments\\Text Mining\\negative-words.txt","r") as neg:
  negwords = neg.read()
negwords = negwords.split("\n") 
negwords = negwords[36:]

tweets_neg = " ".join ([w for w in z.split(" ") if w in negwords])

wordcloud_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(tweets_neg)

plt.imshow(wordcloud_neg)
tweets_pos = " ".join ([w for w in z.split(" ") if w in poswords])
wordcloud_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(tweets_pos)

plt.imshow(wordcloud_pos)



pip install textblob
from textblob import TextBlob
-m textblob.download_corpora
TextBlob.download_corpora
analysis = []
def get_senti(z):
    analysis = TextBlob(z)
    if analysis.sentiment.polarity > 0: 
            return 'positive'
    elif analysis.sentiment.polarity == 0: 
            return 'neutral'
    else: 
            return 'negative'
get_senti(str(tweets[0]))

test = re.sub(r'\w*\d\w*', '', str(tweets[1])).strip()
range(0, 10, 2)

test1 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", str(tweets[1])).split())
for number in range(0, 10, 1):
    print (number)

Tweets_by_tweet = []

for number in  range(0, (len(tweets)), 1):
    Tweets_by_tweet.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", str(tweets[number])).split()))
    
po = "Positive"
ne = "Negative"
nu = "Neutral"

Tweets_by_tweet = [i for i in Tweets_by_tweet if len(i) > 7 ]
Sentiments = []
for i in Tweets_by_tweet:
    analysis = TextBlob(i)
    if analysis.sentiment.polarity > 0: 
        Sentiments.append(po)
    elif analysis.sentiment.polarity == 0: 
        Sentiments.append(nu)
    else: 
        Sentiments.append(ne)

Emotion_by_tweets = {"Tweet" : [Tweets_by_tweet], "Emotion" : [Sentiments]}
Emotion = pd.DataFrame(Emotion_by_tweets, columns = ["Tweet", "Emotion"])
Emotion = pd.DataFrame(Tweets_by_tweet, Sentiments)
Emotion = Emotion.reset_index()
Emotion = Emotion.rename(columns={Emotion.index[1]: "Tweet"})
Emotion.columns = ["Sentiments", "Tweets"]
