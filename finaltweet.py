import tweepy 
consumer_key ="rh71NOcPOKvIdij65A7RuDMD9"
consumer_secret ="0b7ONdEzAC7LX4V4vG6Mkw570SJnKPY5zVQULfRa8LJbvwOzRW"
access_token ="1053149916434849793-UqJ5DqQI2aOdAAmGDTSCGkulyWkxbE"
access_token_secret ="IVyOC36qdPe7R8ohApsyMegtnbBsuOjxU2p2QAPNV91xg"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
api.update_status(status ="hello")
