import twitter
api = twitter.Api()
api = twitter.Api(consumer_key='2SA5WCwn2C1BwjAeLPKlSDSyt', consumer_secret='Ic4MftMlT10kfFzZJkDpcMsBajbuWUP39X13LLSDC1ZwlO4Yby', access_token_key='37636497-zhFylZ3WPr7V8ZWYSYDlBuz6O3ptj5dqlld8lwZtA', access_token_secret='wszO8SeUnRgxz55Zt5Cw5G21pZw66QJbZG0Yf43lu4GPH')
statuses = api.GetUserTimeline(screen_name='davidam9')
print([s.text for s in statuses])
