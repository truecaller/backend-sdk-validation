# Verify Profile (cached key)

## Usage
This usage is similar to the demo in `nodejs` directory.

However, this caches the public key for 30 minutes (can be changed from index.js).


Once key is cached, it won't be fetched until the cache TTL, saving 1 request call per validation.


See `demo.js` for example.
```javascript
    const verifier = require("./index");
    var profile = ... // Truecaller profile object from the mobile SDK
    
    verifier.verifyProfile(profile, function(err, verificationResult) {
        if(err) {
            // Oops, something went wrong
        }
        
        if(verificationResult === true) {
            // Server side verification of profile object succeeded, yay
        } else {
            // Verification failed
            ...
        }
    });
```