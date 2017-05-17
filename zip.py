v = [1, 2, 3]
w = [1, 2, 3]
z = []
for v_i, w_i in zip(v,w):
    z = z + [v_i + w_i]
print z
