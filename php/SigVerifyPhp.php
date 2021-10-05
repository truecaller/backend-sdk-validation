<?php

require 'vendor/autoload.php';
use phpseclib3\Crypt\RSA;
use phpseclib3\Crypt\PublicKeyLoader;

	// Signature from SDK Response
	$signature = "aC5XmkK5YCrNHjvmrOdwh2JFeh7gOlFXguFApTzfax281hGtlwoydDZX9JfK3tUxermuBUS3m+KL13FrN+TF1G0/vJ29Zk91yC0ASDPCOVF6RkU4x9DrlUP0jFZvqnIF4oSCGKPBquFp8KxnqEEWQ7fyrZJ/zVIUqeEn7VuzvYU=";

	// Payload from SDK response
	$package = "eyJyZXF1ZXN0Tm9uY2UiOiJlNGMxNDU0Mi0wMmU5LTQzNmUtYTcxMC1mM2QyYjljOWQyYmYiLCJyZXF1ZXN0VGltZSI6MTUxMDI1MTg2MiwicGhvbmVOdW1iZXIiOiIrOTE4MTQ2ODE0MTg0IiwiZmlyc3ROYW1lIjoiWW9nZXNoIiwibGFzdE5hbWUiOiJTaW5naGFsIiwiZ2VuZGVyIjoiTiIsImNvdW50cnlDb2RlIjoiaW4iLCJlbWFpbCI6InNpbmdoYWwueW9nZXNoMDdAZ21haWwuY29tIiwiaXNUcnVlTmFtZSI6dHJ1ZSwiaXNBbWJhc3NhZG9yIjpmYWxzZX0=";
	
	// Public Key Fetched from 'https://api4.truecaller.com/v1/key'
	$keyStr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB";

	$publicKey = PublicKeyLoader::load($keyStr)->withHash("sha512")->withPadding(RSA::SIGNATURE_PKCS1);
	
	if( $publicKey->verify( $package, base64_decode($signature) ) ){
		echo "Verified";
	}else{
		echo "Not Verified";
	}

?>
