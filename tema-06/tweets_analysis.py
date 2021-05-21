import pandas as pd
import tweepy as tw
import os .path


def authentication():
    with open('twitter-tokens.txt', 'r') as tfile:
        consumer_key = tfile.readline().strip('\n')
        consumer_secret = tfile.readline().strip('\n')
        access_token = tfile.readline().strip('\n')
        access_token_secret = tfile.readline().strip('\n')

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tw.API(auth)


def select_tweets(top10_actors):
    api = authentication()

    tweets_dict = {}
    tweets_dict = tweets_dict.fromkeys(['actor', 'created_at', 'id', 'id_str', 'text', 'truncated', 'entities',
                                        'metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str',
                                        'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name',
                                        'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status',
                                        'retweet_count', 'favorite_count', 'favorited', 'retweeted'])

    for actor in top10_actors:
        search_query = actor + "-filter:retweets"
        tweets = tw.Cursor(api.search, q=search_query).items(10)

        for tweet in tweets:
            for key in tweets_dict.keys():
                try:
                    if key == 'actor':
                        twkey = actor
                        tweets_dict[key].append(twkey)
                    else:
                        twkey = tweet._json[key]
                        tweets_dict[key].append(twkey)
                except KeyError:
                    twkey = ""
                    if tweets_dict[key] is None:
                        tweets_dict[key] = [twkey]
                    else:
                        tweets_dict[key].append(twkey)
                except:
                    tweets_dict[key] = [twkey]

    tweets_dataframe = pd.DataFrame.from_dict(tweets_dict)

    if not os.path.isdir("tweets/"):
        os.mkdir("tweets/")

    tweets_dataframe.to_csv("tweets/tweetsTop10Actors.csv", index=False)

