'use strict';

const pemtools = require('pemtools'),
  crypto = require('crypto'),
  https = require('https'),
  NodeCache = require("node-cache");

const ALGO_MAP = {
  'SHA512withRSA': 'RSA-SHA512'
};

const keyCachedForMinutes = 30;

const publicKeyCache = new NodeCache({ stdTTL: keyCachedForMinutes * 60, checkperiod: ((keyCachedForMinutes + 1) * 60) });

const PUBLIC_KEY_LOOKUP_KEY = "truecaller-public-key";

function fetchPublicKey(callback) {
  console.debug("Fetching Truecaller public key");
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
  const doVerification = function (keyResult) {
    const keyStr = keyResult.key;
    var keyBytes = Buffer.from(pemtools(Buffer.from(keyStr, 'base64'), 'PUBLIC KEY').pem);
    var payload = Buffer.from(profile.payload);
    var signature = Buffer.from(profile.signature, 'base64');
    var signatureAlgorithm = ALGO_MAP[profile.signatureAlgorithm];

    var verifier = crypto.createVerify(signatureAlgorithm);
    verifier.update(payload);

    var signatureVerificationResult = verifier.verify(keyBytes, signature);
    cb(null, signatureVerificationResult);
  };

  const publicKeyResult = publicKeyCache.get(PUBLIC_KEY_LOOKUP_KEY);
  if (publicKeyResult == undefined) {
    fetchPublicKey(function (err, keyResult) {
      if (err) {
        cb(err, null);
      } else {
        if (!publicKeyCache.has(PUBLIC_KEY_LOOKUP_KEY)) {
          console.debug("Caching Truecaller public key");
          publicKeyCache.set(PUBLIC_KEY_LOOKUP_KEY, keyResult);
        }
        doVerification(keyResult);
      }
    });
  } else {
    doVerification(publicKeyResult);
  }
}

exports = module.exports = {
  verifyProfile: verify
};
