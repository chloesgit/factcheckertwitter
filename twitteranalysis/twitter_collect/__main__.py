from twitter_collect.collect_entity_tweet_activity import get_tweets_from_candidates_search_queries
from twitter_collect.collect_entity_tweet_activity import get_replies_to_candidate
from twitter_collect.collect_entity_tweet_activity import get_retweets_of_candidate
from twitter_collect.twitter_connection_setup  import twitter_setup
from Candidatedata.Candidatequeries import get_candidate_queries

num_candidate = input("Entrez le nom du candidat a suivre,de la forme PrenomNom : ")
anum_candidate = "@"+num_candidate

"""print(get_tweets_from_candidates_search_queries(get_candidate_queries(num_candidate, "C:/Users/Chloé Salomé/Documents/Codingweeks/twitteranalysis/Candidatedata"),twitter_setup()))
print (get_replies_to_candidate(anum_candidate))
print (get_retweets_of_candidate(anum_candidate))"""

"""def collect (num_candidate):
    return (get_tweets_from_candidates_search_queries(get_candidate_queries(num_candidate, "C:/Users/Chloé Salomé/Documents/Codingweeks/twitteranalysis/Candidatedata"),twitter_setup()))"""

