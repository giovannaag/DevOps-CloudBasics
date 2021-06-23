import csv
from collections import deque
import elasticsearch
from elasticsearch import helpers

def readTweets():
    csvfile = open('tweets/tweetsTop10Actors.csv', 'r')

    reader = csv.DictReader(csvfile)

    for line in reader:
        tweets = {}
        tweets['actor'] = line['actor']
        tweets['created_at'] = line['created_at'][:10]
        tweets['id'] = int(line['id'])
        tweets['id_str'] = int(line['id_str'])
        tweets['text'] = line['text']
        tweets['truncated'] = bool(line['truncated'])
        tweets['entities'] = line['entities']
        tweets['metadata'] = line['metadata']
        tweets['source'] = line['source']
        tweets['in_reply_to_status_id'] = line['in_reply_to_status_id']
        tweets['in_reply_to_status_id_str'] = line['in_reply_to_status_id_str']
        tweets['in_reply_to_user_id'] = line['in_reply_to_user_id']
        tweets['in_reply_to_user_id_str'] = line['in_reply_to_user_id_str']
        tweets['in_reply_to_screen_name'] = line['in_reply_to_screen_name']
        tweets['user'] = line['user']
        tweets['geo'] = line['geo']
        tweets['coordinates'] = line['coordinates']
        tweets['place'] = line['place']
        tweets['contributors'] = line['contributors']
        tweets['is_quote_status'] = bool(line['is_quote_status'])
        tweets['retweet_count'] = int(line['retweet_count'])
        tweets['favorite_count'] = int(line['favorite_count'])
        tweets['favorited'] = bool(line['favorited'])
        tweets['retweeted'] = bool(line['retweeted'])
        tweets['location'] = line['location']
        yield tweets

def indexTweets():
    es = elasticsearch.Elasticsearch()

    es.indices.delete(index="tweets", ignore=404)
    deque(helpers.parallel_bulk(es, readTweets(), index="tweets"), maxlen=0)
    es.indices.refresh()