import configparser
import datetime

import tweepy

config = configparser.ConfigParser()
config.read('nuke.ini')


auth = tweepy.OAuthHandler(config['consumer']['key'], config['consumer']['secret'])
print('bl;;rps')
print(config['application']['key'])
auth.set_access_token(config['application']['key'], config['application']['secret'])

api = tweepy.API(auth)

public_tweets = api.user_timeline(count=5)
print(len(public_tweets))
for tweet in public_tweets:
    print(tweet.text)
    print(tweet.id)
    print((datetime.datetime.now() - tweet.created_at).days)
    print('-----')
#api.destroy_status('1048565642624950272')