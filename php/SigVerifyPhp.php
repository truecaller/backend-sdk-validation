<?php

require 'vendor/autoload.php';
use phpseclib3\Crypt\RSA;
use phpseclib3\Crypt\PublicKeyLoader;

	// Signature from SDK Response
	$signature = "<<>SIGNATURE_STRING_FROM_TRUECALLER_SDK>";

	// Payload from SDK response
	$package = "<<PAYLOAD_STRING_FROM_TRUECALLER_SDK>>";
	
	// Public Key Fetched from 'https://api4.truecaller.com/v1/key'
	$keyStr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB";

	$publicKey = PublicKeyLoader::load($keyStr)->withHash("sha512")->withPadding(RSA::SIGNATURE_PKCS1);
	
	if( $publicKey->verify( $package, base64_decode($signature) ) ){
		echo "Verified";
	}else{
		echo "Not Verified";
	}

?>
