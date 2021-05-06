import tweepy as tw


def authentication():
    with open('twitter-tokens.txt', 'r') as tfile:
        consumer_key = tfile.readline().strip('\n')
        consumer_secret = tfile.readline().strip('\n')
        access_token = tfile.readline().strip('\n')
        access_token_secret = tfile.readline().strip('\n')

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tw.API(auth)

