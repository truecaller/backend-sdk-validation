package com.truecaller.examples.sdk.profile

import java.nio.charset.StandardCharsets
import java.security.spec.X509EncodedKeySpec
import java.security.{KeyFactory, Signature}
import java.util.Base64

object VerifySignatureUtil {

  /**
   * @param keyType            (keyType attribute from publicKey api endpoint response. Example RSA)
   * @param publicKeyString    (key attribute from publicKey api endpoint response. publicKey can be cached. Try to verify the payload with current key and if its fail reload it from api and try once more.)
   * @param payload            (payload attribute from the response)
   * @param signedString       (signature attribute from the response)
   * @param signatureAlgorithm (Signature-Algorithm from response header example SHA512withRSA)
   * @return boolean
   */
  def verify(keyType: String, publicKeyString: String, payload: String, signedString: String, signatureAlgorithm: String): Boolean = {
    val publicKeyBytes = Base64.getDecoder.decode(publicKeyString)
    val publicKey = KeyFactory.getInstance(keyType).generatePublic(new X509EncodedKeySpec(publicKeyBytes))

    val signatureByteArray = Base64.getDecoder.decode(signedString.getBytes(StandardCharsets.UTF_8))
    val payloadArray = payload.getBytes(StandardCharsets.UTF_8)

    val vSignature = Signature.getInstance(signatureAlgorithm)
    vSignature.initVerify(publicKey)
    vSignature.update(payloadArray)
    vSignature.verify(signatureByteArray)
  }
}

