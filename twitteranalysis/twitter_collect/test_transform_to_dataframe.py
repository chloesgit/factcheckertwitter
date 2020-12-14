from tweepy import *
from pytest import *
from twitter_connection_setup import twitter_setup
from tweet_stockage import transform_to_dataframe
#ce truc est un pytest qui test la fonction transform to dataframe
#pour le faire tourner tu te place dans twitter collect et tu tapes python -m pytest
#j'ai change les imports dans plusieurs fichiers sinon le test marche pas faudra remedier a ca
api = twitter_setup()

def test_transform_to_dataframe():
    tweets = api.search("aleatoire",rpp=100) #on recupere des tweets au pif
    data =  transform_to_dataframe(tweets) #la fonction tourne
    assert 'tweet_textual_content' in data.columns #CA MARCHE !!!!!!!!!!!!!!!!      
#y a bcp de changements par rapport au code de l'enonce 
#mais je vois pas le rapport entre le code de l'enonce et le projet
#y a aucune correspondance entre le nom des fichiers, la fonction collect() je sais pas ce que c'est etc...


print("il se passe qq chose si si")