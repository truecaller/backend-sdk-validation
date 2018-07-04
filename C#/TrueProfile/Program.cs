using System;
using System.Security.Cryptography;
using System.Text;
namespace TrueProfile
{
    class Program
    {

        //Signature From SDK Response
        private static string signature = "aC5XmkK5YCrNHjvmrOdwh2JFeh7gOlFXguFApTzfax281hGtlwoydDZX9JfK3tUxermuBUS3m+KL13FrN+TF1G0/vJ29Zk91yC0ASDPCOVF6RkU4x9DrlUP0jFZvqnIF4oSCGKPBquFp8KxnqEEWQ7fyrZJ/zVIUqeEn7VuzvYU=";

        //Payload
        private static string payload = "eyJyZXF1ZXN0Tm9uY2UiOiJlNGMxNDU0Mi0wMmU5LTQzNmUtYTcxMC1mM2QyYjljOWQyYmYiLCJyZXF1ZXN0VGltZSI6MTUxMDI1MTg2MiwicGhvbmVOdW1iZXIiOiIrOTE4MTQ2ODE0MTg0IiwiZmlyc3ROYW1lIjoiWW9nZXNoIiwibGFzdE5hbWUiOiJTaW5naGFsIiwiZ2VuZGVyIjoiTiIsImNvdW50cnlDb2RlIjoiaW4iLCJlbWFpbCI6InNpbmdoYWwueW9nZXNoMDdAZ21haWwuY29tIiwiaXNUcnVlTmFtZSI6dHJ1ZSwiaXNBbWJhc3NhZG9yIjpmYWxzZX0=";

        //Public Key From SDK Response
        //private static string publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEpFwIarbm48m6ueG+jhpt2vCGaqXZlwR/HPuL4zH1DQ/eWFbgQtVnrta8QhQz3ywLnbX6s7aecxUzzNJsTtS8VxKAYll4E1lJUqrNdWt8CU+TaUQuFm8vzLoPiYKEXl4bX5rzMQUMqA228gWuYmRFQnpduQTgnYIMO8XVUQXl5wIDAQAB";
       
        //Modulus & Exponent Generated From Public Key
        private static string modulus = "xKRcCGq25uPJurnhvo4abdrwhmql2ZcEfxz7i+Mx9Q0P3lhW4ELVZ67WvEIUM98sC521+rO2nnMVM8zSbE7UvFcSgGJZeBNZSVKqzXVrfAlPk2lELhZvL8y6D4mChF5eG1+a8zEFDKgNtvIFrmJkRUJ6XbkE4J2CDDvF1VEF5ec=";
        private static string exponent = "AQAB";


        static void Main(string[] args)
        {

            bool response = VerifyData();
            if(response){
                Console.WriteLine("Verified");
            }else{
                Console.WriteLine("Not Verified");
            }
        }
        private static bool VerifyData()  
        {
          
             bool success = false;
             using (var rsa = new RSACryptoServiceProvider())  
             {  
                
                var encoder = new UTF8Encoding();  
                byte[] bytesToVerify = encoder.GetBytes(payload);  
                byte[] signedBytes = Base64UrlDecode(signature);  
                try  
                {  
                    //RSAParameters parameters = new RSAParameters();
                    var parameters = rsa.ExportParameters(false);
                    parameters.Modulus = System.Convert.FromBase64String(modulus) ; // Your calculated modulus
                    parameters.Exponent =System.Convert.FromBase64String(exponent); // Your calculated exponent
                    rsa.ImportParameters(parameters);

                    SHA512Managed Hash = new SHA512Managed();
                    byte[] hashedData = Hash.ComputeHash(signedBytes);  
                    success = rsa.VerifyData(bytesToVerify, CryptoConfig.MapNameToOID("SHA512"), signedBytes); 
                    //Console.WriteLine("success :"+success + "bytesToVerify : "+bytesToVerify);
                }  
                catch (CryptographicException e)  
                {  
                    success = false;
                    Console.WriteLine("exception :",e);
                }  
                finally  
                {  
                     rsa.PersistKeyInCsp = false;  
                }  
             } 

             return success;   
        }  
        private static byte[] Base64UrlDecode(string input)  
        {  
             var output = input;  
             output = output.Replace('-', '+'); // 62nd char of encoding  
             output = output.Replace('_', '/'); // 63rd char of encoding  
             switch (output.Length % 4) // Pad with trailing '='s  
             {  
               case 0: break; // No pad chars in this case  
               case 2: output += "=="; break; // Two pad chars  
               case 3: output += "="; break; // One pad char  
               default: throw new System.Exception("Illegal base64url string!");  
             }  
             var converted = Convert.FromBase64String(output); // Standard base64 decoder  
             return converted;  
       }  
    }
}
