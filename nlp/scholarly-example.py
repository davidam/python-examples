import scholarly

s = scholarly.search_author("Steven A. Cholewiak")
print(next(s))

search_query = scholarly.search_keyword('Haptics')
print(next(search_query))

search_query = scholarly.search_pubs_query('Perception of physical stability and center of mass of 3D objects')
print(next(search_query))

