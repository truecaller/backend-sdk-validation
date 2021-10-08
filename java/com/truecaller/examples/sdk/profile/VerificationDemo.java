package com.truecaller.examples.sdk.profile;

public class VerificationDemo {

    private static String get(String[] args, int index, String fallback) {
        return (args.length > index) ? args[index] : fallback;
    }

    public static void main(String[] args) {
        if(args.length < 2 || args.length > 5) {
            System.out.println("Invalid arguments.\nUsage: VerifySignatureUtil payload signature [publicKey] [keyType] [signatureAlgorithm]");
            System.exit(0);
        }
        String payload = args[0];
        String signedString = args[1];
        String publicKeyString = get(args, 2, "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB");
        String keyType = get(args, 3, "RSA");
        String signatureAlgorithm = get(args, 4, "SHA512withRSA");

        try {
            boolean result = VerifySignatureUtil.verify(keyType, publicKeyString, payload, signedString, signatureAlgorithm);
            System.out.println("Result: " + (result?"Success":"Failure"));
        } catch(Exception e) {
            System.out.println("Failed to verify");
            e.printStackTrace();
        }
    }
}

