import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
print(df.head())

# Row wise Operation
def hypotenuse(row):
    return round(row[1]**2 + row[2]**2, 2)**0.5

with mp.Pool(4) as pool:
    result = pool.imap(hypotenuse, df.itertuples(name=False), chunksize=10)
    output = [round(x, 2) for x in result]

print(output)

# # Column wise Operation
# def sum_of_squares(column):
#     return sum([i**2 for i in column[1]])

# with mp.Pool(2) as pool:
#     result = pool.imap(sum_of_squares, df.iteritems(), chunksize=10)
#     output = [x for x in result]

# print(output)

# import numpy as np
# import pandas as pd
# import multiprocessing as mp
# from multiprocessing import ProcessingPool as Pool

# df = pd.DataFrame(np.random.randint(3, 10, size=[500, 2]))

# def func(df):
#     return df.shape

# cores=mp.cpu_count()

# df_split = np.array_split(df, cores, axis=0)

# # create the multiprocessing pool
# pool = Pool(cores)

# # process the DataFrame by mapping function to each df across the pool
# df_out = np.vstack(pool.map(func, df_split))

# close down the pool and join
pool.close()
pool.join()

#pool.clear()
