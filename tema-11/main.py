from movies_analysis import top10_actors
from tweets_analysis import select_tweets
from datasets_verification import folders_creation, data_verification, data_download
from elasticsearch_connection import indexTweets

print("-- Creating datasets folders --")
folders_creation()

print("-- Checking data --")
data_verification()

print("-- Downloading data --")
data_download()

print("-- Analyzing tweets --")
actorsList = top10_actors()
select_tweets(actorsList)

print("-- Sending to Elasticsearch --")
indexTweets()



