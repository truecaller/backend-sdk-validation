# Verify Profile

## Usage
See `demo.js` for example
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