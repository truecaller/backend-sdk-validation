require 'base64'
require 'openssl'

class VerifySignatureUtil

    def self.verify(key_type, public_key_string, payload, signed_string, signature_algorithm)
        public_key = OpenSSL::PKey.const_get(key_type).new(Base64.decode64(public_key_string))
        signature  = Base64.decode64(signed_string)
        digest     = OpenSSL::Digest.new(signature_algorithm)
        public_key.verify(digest, signature, payload) # returns true or false
    end
end

## Usage example

# Signature from SDK Response
signedString = "ULgM59pxFZRG+ziYXXi+ozUIRZ9JsIFZ3FmGm7sasVPx6avQrxCgJAuSRT1A5hdm7EJPTHykUJm6Z+UCebzTf+/q3vx6Zbnws4T/5P1yLZlt0dsZv+F31EmMmj4YMPJImElIH1va83cIw65OI0QRfl2aDwxpLG/+DtPsI3DGid8="
# Payload from SDK response
payload = "eyJyZXF1ZXN0Tm9uY2UiOiI4MGEwMWVkMS1hNGI2LTQ5MDgtODJkYy04ZjU2MDVjM2Q0OTEiLCJyZXF1ZXN0VGltZSI6MTUxMDgxNjE4NywicGhvbmVOdW1iZXIiOiIrOTE5OTExNDg2NTIyIiwiZmlyc3ROYW1lIjoicmF2aW5kZXIiLCJsYXN0TmFtZSI6IlNpbmdoIiwiZ2VuZGVyIjoiTSIsImNpdHkiOiJOb2lkYSwgSW5kaWEiLCJjb3VudHJ5Q29kZSI6ImluIiwiZmFjZWJvb2tJZCI6InJhbWluZGVyc2FoYW5pIiwiZW1haWwiOiJyYW1pbmRlcnNhaGFuaUBnbWFpbC5jb20iLCJpc1RydWVOYW1lIjpmYWxzZSwiaXNBbWJhc3NhZG9yIjpmYWxzZX0="
# Public Key Fetched from 'https://api4.truecaller.com/v1/key'
publicKeyString = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB"
signatureAlgorithm = 'sha512'
keyType = "RSA"

puts VerifySignatureUtil.verify(keyType, publicKeyString, payload, signedString, signatureAlgorithm)