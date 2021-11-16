import twitter
api = twitter.Api()
consumer_key = input("Enter consumer key: ")
consumer_secret = input("Enter consumer secret: ")
access_token_key = input("Enter access token key: ")
access_token_secret = input("Enter access token secret: ")

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
statuses = api.GetUserTimeline(screen_name='davidam9')
print([s.text for s in statuses])
