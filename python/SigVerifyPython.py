from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64decode


# Public Key
key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB"

# Base64 Encoded payload
payload = "your-payload"

signature = "your-signature"

signature_algorithm = "SHA512withRSA" #change if required
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
