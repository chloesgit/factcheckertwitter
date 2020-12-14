from textblob import *
from stop_words import get_stop_words
from pandas import *
from twitter_collect.tweet_stockage import transform_to_dataframe
from twitter_collect.twitter_connection_setup import twitter_setup
from tweepy import *

stopwords = get_stop_words('french') ##liste des stop words francais
#print(stopwords)  deboguage
#tweets = twitter_setup().user_timeline("@EmmanuelMacron")
#frame = transform_to_dataframe(tweets)
#print([x for x in frame['tweet_textual_content']]) deboguage

def voc_extract (frame) : #extrateur de vocabulaire
    voc=[]
    for text in [x for x in frame['tweet_textual_content']] : 
        texte = TextBlob(text)
        voc = voc + texte.words
    for word in stopwords :
        try: 
            voc.remove(word)
        except ValueError:
            continue
     
    return(list(set(voc))) #enleve les doublons


#print(voc_extract(frame))






