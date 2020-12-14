import tweepy 
from twitter_connection_setup import twitter_setup

def collect():
    connexion =twitter_setup()
    tweets = connexion.search("Chocolate OR Cake -Cake",language="english",rpp=10)
    #return(tweets)
    for tweet in tweets:
            print(tweet.text)

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 100,since_id =1193970218206412801)
    for status in statuses:
        print(status.text)
    return statuses


from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])
def init_stream(id):
    global listener
    global poster
    # ll_wikia 2734031000
    # mkydyrea 3299062544
    # LLupdates 4423137133
    # ll_extra 739117766100189184
    # lovelive_staff 347849994
    # lovelive_sif 1346933186
    # ischyrb 357915189

    listener = TweetListener(id)
    poster = tweepy.Stream(auth=auth, listener=listener)
    poster.filter(follow=id, track=['#??????????????'], async=True)

init_stream(2734031000)