import hashlib
#import random

"""
Hashes the user string to create IDs of sockets and fiels.
"""
def hash_key(key: str) -> int:
    hash_object = hashlib.sha1(key.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) % 65536


"""
TESTING

print(hash_key(input("Enter a key: ")))

for i in range(1000):
    print(hash_key(str(random.randint(0, 10000))))
"""
