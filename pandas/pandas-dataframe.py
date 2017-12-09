import pandas as pd

data = {
    'Country': ['Belgium',  'India',  'Brazil'],
    'Capital': ['Brussels',  'New Delhi',  'Brasilia']
        }

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

print df
        
