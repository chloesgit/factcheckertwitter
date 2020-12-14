from  tweet_analysis.Analysis import * 
from tweet_analysis.opinion_analysis import * 
from twitter_collect.tweet_stockage import * 
from Candidatedata.Candidatequeries import * 
from twitter_collect.collect_entity_tweet_activity import * 

candidat = input ("Entrez EmmanuelMacron ou EdouardPhilippe : ")
filepathdesfichiers = input("Rentrez le filepath où sont stockés les fichiers hashtag_candidate et keyword_candidate : ")

mots_clés_candidat = get_candidate_queries(candidat, filepathdesfichiers)

tweets = get_tweets_from_candidates_search_queries(mots_clés_candidat,twitter_api) 
dataframe = transform_to_dataframe(tweets)
print(dataframe)
tweets2 = tweets = twitter_setup().user_timeline("@"+candidat)
dataframe2 = transform_to_dataframe(tweets2)
print(max_retweet(dataframe2,candidat))
print(max_like(dataframe2,candidat))
print(like_retweet_f_temps(dataframe2))






