'use strict';

const verifier = require("./index");

function main() {
  const profile = {
    payload: "your-payload",
    signature: "your-signature",
    signatureAlgorithm: "SHA512withRSA" //Change if required
  };

  verifier.verifyProfile(profile, function (err, res) {
    if (err) {
      console.error("Error: " + err);
    } else {
      console.info("Verified: " + (res ? "yes" : "no"));
    }
  });
}

main();
