from pandas import *
from twitter_collect.tweet_stockage import transform_to_dataframe
from twitter_collect.twitter_connection_setup import twitter_setup
from tweepy import *
from numpy import *
import matplotlib.pyplot as plt

#tweets = twitter_setup().user_timeline("@EmmanuelMacron")
#frame = transform_to_dataframe(tweets)
#print(frame)

def max_retweet(dataframe,candidat):
    """entrée : dataframe renvoie le tweet avec le plus de retweet"""
    max_rt = max(dataframe['nb_RT'])
    id_du_tweet  = dataframe[dataframe.nb_RT == max_rt].index[0]

    print("The tweet from " + candidat + " with more retweets is: \n{}".format(dataframe['tweet_textual_content'][id_du_tweet])) #on imprime des trucs
    print("Number of retweets: {}".format(max_rt))
    print("{} characters.\n".format(dataframe['len_tweet'][id_du_tweet]))

    return id_du_tweet



def max_like(dataframe,candidat):
    """entrée : dataframe renvoie le tweet avec le plus de like"""
    max_like = max(dataframe['nb_like'])
    id_du_tweet  = dataframe[dataframe.nb_like == max_like].index[0]

    print("The tweet from " + candidat + " with more like is: \n{}".format(dataframe['tweet_textual_content'][id_du_tweet]))
    print("Number of likes: {}".format(max_like))
    print("{} characters.\n".format(dataframe['len_tweet'][id_du_tweet]))
    return id_du_tweet

def plus_long(dataframe):
    """entrée :dataframe etc... """

def like_retweet_f_temps(data):
    """trace les like et RT en fonction du temps"""
    tfav = Series(data=data['nb_like'].values, index=data['Date'])
    tret = Series(data=data['nb_RT'].values, index=data['Date'])

# Likes vs retweets visualization
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)
    plt.show()


#a=like_retweet_f_temps(frame)
#print (max_like(frame))

