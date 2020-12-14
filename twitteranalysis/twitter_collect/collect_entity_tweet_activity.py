import tweepy
import pep8
from Candidatedata.Candidatequeries import get_candidate_queries
from twitter_collect.twitter_connection_setup import twitter_setup

twitter_api = twitter_setup() #creation de la cle de connection
def get_tweets_from_candidates_search_queries(queries, twitter_api):
    """effectue les recherches correspondant aux listes de mots clés entrés"""
    try : 
        tweets=[]
        for word in queries : #word est un des mots clés
            for tweet in twitter_api.search(word,rpp=100):
                tweets.append(tweet) #on remplit la liste avec les tweets
        return(tweets)
    except TweepError: #toutes les erreurs de tweepy sont repertoriées sous TweepError
        return(TweepError.response.text)

#queries = get_candidate_queries("Clarence","C:/Users/Chloé Salomé/Documents/Codingweeks/twitteranalysis/Candidatedata")
#print(get_tweets_from_candidates_search_queries(queries,twitter_api))

#recherche = [ x.text for x in twitter_api.user_timeline ("@EmmanuelMacron")]
#print(recherche)
def get_replies_to_candidate(anum_candidate) :
    """cherche les réponses aux tweets les plus récents d'un candidat, anum_candidate est "@candidate" """ 
    twitter_api = twitter_setup()
    tweets = twitter_api.user_timeline (anum_candidate)
    reponse_candidat = "to:"+anum_candidate
    replies = twitter_api.search(reponse_candidat, rpp = 400) #plein de réponses au compte 
    reponses_triees={} # clé du dico = id tweet. Valeur du dico = liste contenant l'ensemble des tweets en réponse à idtweet
    for tweet in tweets : 
        idtweet = tweet.id
        reponses_triees[idtweet] = [] #on crée le dico 
    for replie in replies:
        for cle in reponses_triees : 
            if replie.in_reply_to_status_id == cle:
                reponses_triees[cle].append(replie.text)
    #probleme : pas assez de reponse, bcp de tweets n'ont pas de reponse
    #solution : faire plein de recherche de reponses, chronologiquement, decroissant
    return(reponses_triees)

#print(get_replies_to_candidate("@EmmanuelMacron"))

def get_retweets_of_candidate(anum_candidate) : 
    twitter_api=twitter_setup()
    tweets = twitter_api.user_timeline (anum_candidate)
    Dretweets={}
    for tweet in tweets :
        tweetid = tweet.id
        Dretweets[tweetid]=[ [x.text for x in twitter_api.retweets(tweetid)]]
    return(Dretweets)

#print(get_retweets_of_candidate("@EmmanuelMacron"))

from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_error(self, status): #ferme la connection avant que twitter ne sanctionne
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

    def on_status(self, status):
        print(status.text)  #imprime le texte des tweets recuperes
        #print(get_replies_to_candidate("@EmmanuelMacron")[status.id])

def collect_by_streaming(anum_candidate):
    connexion = twitter_setup()  #connecte a twitter
    listener = StdOutListener()  
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    #x = "to:"+anum_candidate
    stream.filter(track= [anum_candidate])

#print(collect_by_streaming("@EmmanuelMacron"))




    

    


