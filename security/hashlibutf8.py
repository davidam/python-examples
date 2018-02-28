import hashlib, random
print(hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())
