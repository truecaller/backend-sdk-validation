import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.nio.charset.StandardCharsets;
import java.security.spec.X509EncodedKeySpec;

import com.google.api.client.util.Base64;

import javax.xml.bind.DatatypeConverter;

public class VerifySignatureUtil {

    /**
     * @param keyType (keyType attribute from publicKey api endpoint response. Example RSA)
     * @param publicKeyString (key attribute from publicKey api endpoint response. publicKey can be cached. Try to verify the payload with current key and if its fail reload it from api and try once more.)
     * @param payload (payload attribute from the response)
     * @param signedString (signature attribute from the response)
     * @param signatureAlgorithm (Signature-Algorithm from response header example SHA512withRSA)
     * @return boolean
     * @throws Exception
     */
    public static boolean verify(final String keyType, final String publicKeyString, final String payload, final String signedString, final String signatureAlgorithm) throws Exception {

        final byte[] publicKeyBytes = DatatypeConverter.parseBase64Binary(publicKeyString);
        final PublicKey publicKey =  KeyFactory.getInstance(keyType).generatePublic(new X509EncodedKeySpec(publicKeyBytes));

        final byte[] signatureByteArray = Base64.decodeBase64(signedString.getBytes(StandardCharsets.UTF_8));
        final byte[] payloadArray = payload.getBytes(StandardCharsets.UTF_8);

        Signature vSignature = Signature.getInstance(signatureAlgorithm);
        vSignature.initVerify(publicKey);
        vSignature.update(payloadArray);

        return vSignature.verify(signatureByteArray);
    }
}

