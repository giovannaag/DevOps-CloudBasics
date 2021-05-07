from movies_analysis import top10_actors
from tweets_analysis import select_tweets

actorsList = top10_actors()

select_tweets(actorsList)