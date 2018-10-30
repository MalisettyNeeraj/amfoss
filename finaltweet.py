import tweepy 
consumer_key ="bIwwiAA8OgHaXvWHkzkR7EHTa"
consumer_secret ="2MlvQSObKujrBIXo6MfFm2Uzo8lfuBLmbHQFCdDy9AxoIakBZQ"
access_token ="1053149916434849793-4CidNkFt4OFwZ3ZBZM5hVY7pTKY13c"
access_token_secret ="qjpCZ1CxvylmhHmDuDOJJfnnMxyTsmiedL2CLDkfIOc2o"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
api.update_status(status ="hello")