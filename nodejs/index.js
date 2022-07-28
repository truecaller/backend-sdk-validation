'use strict';

const pemtools = require('pemtools'),
  crypto = require('crypto'),
  https = require('https');
;
const ALGO_MAP = {
  'SHA512withRSA': 'RSA-SHA512'
};

function fetchPublicKey(callback) {
  https.get("https://api4.truecaller.com/v1/key", res => {
    var data = [];

    res.on('data', chunk => {
      data.push(chunk);
    });

    res.on('end', () => {
      const result = JSON.parse(Buffer.concat(data).toString());
      if (result.length < 1)
        callback("Invalid response while fetching public key");
      else
        callback(null, result[0]);

    });
  }).on('error', err => {
    callback(err.message);
  });
}

function verify(profile, cb) {
  fetchPublicKey(function (err, keyResult) {
    if (err) {
      cb(err, null);
    } else {
      const keyStr = keyResult.key;
      var keyBytes = Buffer.from(pemtools(Buffer.from(keyStr, 'base64'), 'PUBLIC KEY').pem);
      var payload = Buffer.from(profile.payload);
      var signature = Buffer.from(profile.signature, 'base64');
      var signatureAlgorithm = ALGO_MAP[profile.signatureAlgorithm];

      var verifier = crypto.createVerify(signatureAlgorithm);
      verifier.update(payload);

      var signatureVerificationResult = verifier.verify(keyBytes, signature);
      cb(null, signatureVerificationResult);
    }
  });
}

function profileData(profile) {
  return JSON.parse((Buffer.from(profile.payload, 'base64')).toString());
}
 
exports = module.exports = {
  verifyProfile: verify,
  getProfileData: profileData
};
 
