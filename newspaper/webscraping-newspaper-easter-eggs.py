import newspaper
# hot() returns a list of the top trending terms on Google using a public api
print(newspaper.hot())
# popular_urls() returns a list of popular news source urls
print(newspaper.popular_urls())
newspaper.languages()
