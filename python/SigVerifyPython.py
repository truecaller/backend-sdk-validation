from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64decode


# Public Key
key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB"

# Base64 Encoded payload
payload = b"eyJyZXF1ZXN0Tm9uY2UiOiJkNDg3ZmJkMi03YmIwLTRhMzMtYTA3OS05OTg1NTdjOWZiMjUiLCJyZXF1ZXN0VGltZSI6MTYyMTgzMzMzMCwicGhvbmVOdW1iZXIiOiIrOTE2MjA0NTc3MDYyIiwiZmlyc3ROYW1lIjoiQWRoaXNoIiwibGFzdE5hbWUiOiJMYWwiLCJnZW5kZXIiOiJOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzQnVzaW5lc3MiOmZhbHNlLCJ0cnVlTmFtZSI6dHJ1ZSwiYW1iYXNzYWRvciI6ZmFsc2V9"

signature = "u8sKIx5iwMpBmqouY6qe2/DJgm0hJLkm1XZicqUdRz6PxhMKHYfPo9U0pxwMQud3sTTtjg9Q157xcQs7KLCGvqmws3bW2zbccxC2Nmk7i4cLWC3NOfxOtp2XP4XxkWVkj0Rc6hSTddp3NXt2T3FHMkxruQH72SwgI8ljWELvnK0\u003d"

signature_algorithm = "SHA512withRSA"
keytype = "RSA"

# Creating hash for the payload object
msg_hash = SHA512.new()
msg_hash.update(payload)

# Signature object based on Truecaller's public key
keyDER = b64decode(key)
rsakey = RSA.importKey(keyDER)
signer = PKCS1_v1_5.new(rsakey)

if signer.verify(msg_hash, b64decode(signature)):
    print ("Verified")
else:
    print ("Not Verified")
