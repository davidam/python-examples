import numpy as np

a = np.random.randn(9, 6)
q, r = np.linalg.qr(a)
print(np.allclose(a, np.dot(q, r)))  # a does equal qr

r2 = np.linalg.qr(a, mode='r')
r3 = np.linalg.qr(a, mode='economic')
print(np.allclose(r, r2))  # mode='r' returns the same r as mode='full'

# But only triu parts are guaranteed equal when mode='economic'
print(np.allclose(r, np.triu(r3[:6,:6], k=0)))
