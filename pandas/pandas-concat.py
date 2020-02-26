import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])


frames = [df1, df2, df3]

# simple concat

result1 = pd.concat(frames)

print(result1)

# outer

#print(pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None,
#          levels=None, names=None, verify_integrity=False, copy=True))

#

result2 = pd.concat(frames, keys=['x', 'y', 'z'])

print(result2)

print(result2.loc['y'])

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])


result = pd.concat([df1, df4], axis=1, sort=False)
print(result)

result = pd.concat([df1, df4], axis=1, join='inner')

print(result)

result = df1.append(df2)

print(result)

result = df1.append(df4, sort=False)

print(result)

result = df1.append([df2, df3])

print(result)

result = pd.concat([df1, df4], ignore_index=True, sort=False)

print(result)

result = df1.append(df4, ignore_index=True, sort=False)

print(result)

s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name='X')

result = pd.concat([df1, s1], axis=1)

print(result)

s2 = pd.Series(['_0', '_1', '_2', '_3'])

result = pd.concat([df1, s2, s2, s2], axis=1)

print(result)

result = pd.concat([df1, s1], axis=1, ignore_index=True)

print(result)

s3 = pd.Series([0, 1, 2, 3], name='foo')

s4 = pd.Series([0, 1, 2, 3])

s5 = pd.Series([0, 1, 4, 5])

print(pd.concat([s3, s4, s5], axis=1))

print(pd.concat([s3, s4, s5], axis=1, keys=['red', 'blue', 'yellow']))

result = pd.concat(frames, keys=['x', 'y', 'z'])

print(result)

pieces = {'x': df1, 'y': df2, 'z': df3}

result = pd.concat(pieces)

print(result)

result = pd.concat(pieces, keys=['z', 'y'])

print(result.index.levels)

result = pd.concat(pieces, keys=['x', 'y', 'z'],
                   levels=[['z', 'y', 'x', 'w']],
                   names=['group_key'])

print(result)
print(result.index.levels)

s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])

result = df1.append(s2, ignore_index=True)

print(result)

dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4},
        {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]

result = df1.append(dicts, ignore_index=True, sort=False)

print(result)
