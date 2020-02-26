#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])


right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])


result = left.join(right)

print(result)

result = left.join(right, how='outer')

print(result)

result = left.join(right, how='inner')

print(result)

result = pd.merge(left, right, left_index=True, right_index=True, how='outer')

print(result)

result = pd.merge(left, right, left_index=True, right_index=True, how='inner')

left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key': ['K0', 'K1', 'K0', 'K1']})

right = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                      index=['K0', 'K1'])

result = left.join(right, on='key')

print(result)

result = pd.merge(left, right, left_on='key', right_index=True,
                   how='left', sort=False);

print(result)

left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3'],
                      'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1']})


index = pd.MultiIndex.from_tuples([('K0', 'K0'), ('K1', 'K0'),
                                   ('K2', 'K0'), ('K2', 'K1')])


right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=index)

result = left.join(right, on=['key1', 'key2'])

print(result)

result = left.join(right, on=['key1', 'key2'], how='inner')

print(result)

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                      index=pd.Index(['K0', 'K1', 'K2'], name='key'))


index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                    names=['key', 'Y'])


right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=index)

result = left.join(right, how='inner')

print(result)

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})


result = pd.merge(left, right, on='key')

print(result)

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})


result = pd.merge(left, right, on=['key1', 'key2'])

print(result)

result = pd.merge(left, right, how='left', on=['key1', 'key2'])

print(result)

result = pd.merge(left, right, how='right', on=['key1', 'key2'])

print(result)

result = pd.merge(left, right, how='outer', on=['key1', 'key2'])

print(result)

result = pd.merge(left, right, how='inner', on=['key1', 'key2'])

left = pd.DataFrame({'A': [1, 2], 'B': [2, 2]})

right = pd.DataFrame({'A': [4, 5, 6], 'B': [2, 2, 2]})

result = pd.merge(left, right, on='B', how='outer')

print(result)

df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})

df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})

print(pd.merge(df1, df2, on='col1', how='outer', indicator=True))

print(pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column'))

left = pd.DataFrame({'key': [1], 'v1': [10]})

print(left)

right = pd.DataFrame({'key': [1, 2], 'v1': [20, 30]})

print(right)

print(pd.merge(left, right, how='outer'))

print(pd.merge(left, right, how='outer').dtypes)

print(pd.merge(left, right, how='outer', on='key'))
