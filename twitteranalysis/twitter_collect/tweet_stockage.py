from pandas import DataFrame
from pandas import Categorical
from twitter_collect.twitter_connection_setup import twitter_setup
from tweepy import *



def transform_to_dataframe(tweets):
    """prend en entrée une liste de tweet, renvoie une dataframe panda"""
    D_tweets = {}  #je crée un dico pour que e soit plus facile pour le dataframer apres ( je sais pas faire autrement)
    for tweet in tweets:
        D_tweets[tweet.id] = Categorical([tweet.text,len(tweet.text),tweet.in_reply_to_status_id,tweet.in_reply_to_user_id,tweet.user.id,tweet.created_at,\
        tweet.retweet_count,tweet.favorite_count,tweet.place])
#je remplis le dico avec le texte des tweets, plus d'autres trucs sous la clé -id du tweet-
# le com dessous ne sert a rien
##,tweet.in_reply_to_status_id,tweet.in_reply_to_user_id,tweet.user.id
    data_frame = DataFrame(D_tweets, index = ['tweet_textual_content','len_tweet','reply_tweet','reply_user','user_id','Date','nb_RT','nb_like','country'])
    data_frame = data_frame.transpose()
#on cree un dataframe, les noms des colonnes sont les id des tweets, le contenu des colonnes le texte etc..
#je sais pas changer le nom des lignes si tu y arrive ca peut etre tres beau
    return data_frame

#liste = twitter_setup().search("aleatoire", rpp=100)
#print(transform_to_dataframe(liste))
