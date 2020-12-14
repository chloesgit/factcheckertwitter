import tweepy

import os

def get_candidate_queries(num_candidate, file_path): # file_path : chemin entre guillemets
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag 
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    os.chdir(file_path) #se déplace à la bonne direction
    try : 
        keywords_candidate = "keyword_"+ str(num_candidate)+".txt"
        hashtag_candidate = "hashtag_"+str(num_candidate)+".txt"
        keywords_candidate_n = open(keywords_candidate, "r")
        hashtag_candidate_n = open (hashtag_candidate,"r")
        return(keywords_candidate_n.read().splitlines()+hashtag_candidate_n.read().splitlines())
        #renvoie le tuple constitué des lignes du fichier keywords_candidate_n et de celles du fichier hashtag_candidate
        # splitlines() enlève le \n à la fin de chaque élément de la liste
        
    except IOError :
        print("ERROR, il manque un fichier")
    
#print(get_candidate_queries("Clarence","C:/Users/Chloé Salomé/Documents/Codingweeks/twitteranalysis/Candidatedata"))


