import pandas
data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")

data.shape    # 40 rows and 8 columns
data.columns  # It has columns   
print(data['Gender'])  # Columns can be addressed by name   

# Simpler selector
print(data[data['Gender'] == 'Female']['VIQ'].mean())

groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

groupby_gender.mean()
