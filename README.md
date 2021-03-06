#  Steps for Server Side Validation of Payload : -

In the response for TrueProfile we return -

- Payload, which is a Base64 encoding of the json object containing all profile info
- Signature, which contains the payload's signature . Signature is generated by applying signing algorithm with our private key
- Signature Algorithm in the response header

To verify the payload, our public key for a given algorithm can be fetched using this API:

https://api4.truecaller.com/v1/key.

Using the payload, the signature and the public key, you can verify that the content sent is authentic through the following flow:

Apply verification, which means apply our public key to the signature (with given algorithm) and comparing result with payload 

If verified, you would know that response comes from truecaller's backend and is authentic. The profile can then be used as base64 decoding of the payload.

NOTE : Truecaller already verifies the authenticity of the response before forwarding it to the caller app, therefore it is not a required step, but we provide these data for allowing the developers to verify the payload as a second level of security check.

You can also have a look at the following link for reference on verifying a digital signature
https://docs.oracle.com/javase/tutorial/security/apisign/versig.html

This repository contains backend validation code snippets for the following programming languages -

 - Java
 - PHP
 - Python
 - Ruby
 - NodeJS
 - C#
