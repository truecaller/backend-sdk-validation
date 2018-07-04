
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64decode


# Public Key
key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB"

# Base64 Encoded payload
payload = "eyJyZXF1ZXN0Tm9uY2UiOiI0OTQ0NGYwZC1hN2M0LTQyYjUtYmUxOS1iYzEyNzg4NmFjNjEiLCJwaG9uZU51bWJlciI6Iis5MTgzNjg0Nzg1NzYiLCJmaXJzdE5hbWUiOiJZb2dlc2giLCJsYXN0TmFtZSI6IlNpbmdoYWwiLCJnZW5kZXIiOiJOIiwic3RyZWV0IjoiU2hhbGltYXIgQmFnaCIsImNpdHkiOiJOZXcgRGVsaGkiLCJ6aXBjb2RlIjoiMTEwMDg4IiwiY291bnRyeUNvZGUiOiJpbiIsImVtYWlsIjoieW9nZXNoLnNpbmdoYWxAdHJ1ZWNhbGxlci5jb20iLCJ1cmwiOiJkZXZlbG9wZXIudHJ1ZWNhbGxlci5jb20iLCJpc1RydWVOYW1lIjpmYWxzZSwiaXNBbWJhc3NhZG9yIjpmYWxzZSwiY29tcGFueU5hbWUiOiJUcnVlY2FsbGVyIiwiam9iVGl0bGUiOiJUZWNoIEV2YW5nZWxpc3QifQ=="

signature = "pnb0bt5fNC6R75H2/Ea8CeLxiDUJDb4NTfzAmuYG72VzNW4wXQ9ODvWaN2gF37IFSi4vV4Ozgzd9rBl12xZSDCv9bp1ZnsuySseX9uuRSlOxOxTVs3HQ7bazPxgjVjo6LV2E2ofbKTCd18VBltsI9qSOnBjSphrJyAXy1VZii04="

signature_algorithm = "SHA512withRSA"
keytype = "RSA"


# decoded_payload = b64decode(payload)
# print decoded_payload
msg_hash = SHA512.new()
msg_hash.update(payload)
# print msg_hash.digest()
# print msg_hash.hexdigest()


keyDER = b64decode(key)
# print keyDER
rsakey = RSA.importKey(keyDER)
# print rsakey.n
# print rsakey.e
# print rsakey.size()
signer = PKCS1_v1_5.new(rsakey)

if signer.verify(msg_hash, b64decode(signature)):
    print "Verified"
else:
    print "Not Verified"
