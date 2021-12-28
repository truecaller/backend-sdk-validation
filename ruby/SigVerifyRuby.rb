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
signedString = "<<SIGNATURE_STRING_FROM_TRUECALLER_SDK>>"
# Payload from SDK response
payload = "<<PAYLOAD_STRING_FROM_TRUECALLER_SDK>>"
# Public Key Fetched from 'https://api4.truecaller.com/v1/key'
publicKeyString = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB"
signatureAlgorithm = 'sha512'
keyType = "RSA"

puts VerifySignatureUtil.verify(keyType, publicKeyString, payload, signedString, signatureAlgorithm)
