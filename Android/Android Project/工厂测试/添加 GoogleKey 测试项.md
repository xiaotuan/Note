下面以添加 Google Key 状态属性为例，修改 `frameworks/base/services/core/java/com/android/server/policy/PhoneWindowManager.java` 文件如下代码：

```diff
@@ -237,6 +237,32 @@ import java.io.IOException;
 import java.io.PrintWriter;
 import java.util.HashSet;
 
+import android.os.SystemProperties;
+import android.security.keystore.KeyGenParameterSpec;
+
+import java.io.ByteArrayInputStream;
+import java.security.InvalidAlgorithmParameterException;
+import java.security.InvalidKeyException;
+import java.security.KeyPairGenerator;
+import java.security.KeyStore;
+import java.security.NoSuchAlgorithmException;
+import java.security.NoSuchProviderException;
+import java.security.PublicKey;
+import java.security.SignatureException;
+import java.security.cert.Certificate;
+import java.security.cert.CertificateException;
+import java.security.cert.CertificateExpiredException;
+import java.security.cert.CertificateFactory;
+import java.security.cert.CertificateNotYetValidException;
+import java.security.cert.X509Certificate;
+import java.security.spec.ECGenParameterSpec;
+import java.util.Arrays;
+
+import static android.security.keystore.KeyProperties.DIGEST_NONE;
+import static android.security.keystore.KeyProperties.DIGEST_SHA256;
+import static android.security.keystore.KeyProperties.DIGEST_SHA512;
+import static android.security.keystore.KeyProperties.KEY_ALGORITHM_EC;
+
 /**
  * WindowManagerPolicy implementation for the Android phone UI.  This
  * introduces a new method suffix, Lp, for an internal lock of the
@@ -333,6 +359,8 @@ public class PhoneWindowManager implements WindowManagerPolicy {
             .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
             .setUsage(AudioAttributes.USAGE_ASSISTANCE_SONIFICATION)
             .build();
+                       
+       public static final String GOOGLE_ROOT_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIFYDCCA0igAwIBAgIJAOj6GWMU0voYMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNVBAUTEGY5MjAwOWU4NTNiNmIwNDUwHhcNMTYwNTI2MTYyODUyWhcNMjYwNTI0MTYyODUyWjAbMRkwFwYDVQQFExBmOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHsK7Qui8xUFmOr75gvMsd/dTEDDJdSSxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfdnJLmN0pTy/4lj4/7tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y//0rb+T+W8a9nsNL/ggjnar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB/M0n1n/W9nGqC4FSYa04T6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl/m00QLVWutHQoVJYnFPlXTcHYvASLu+RhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+OJtvsBslHZvPBKCOdT0MS+tgSOIfga+z1Z1g7+DVagf7quvmag8jfPioyKvxnK/EgsTUVi2ghzq8wm27ud/mIM7AY2qEORR8Go3TVB4HzWQgpZrt3i5MIlCaY504LzSRiigHCzAPlHws+W0rB5N+er5/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6tUXHI/+MRPjy02i59lINMRRev56GKtcd9qO/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9EaDK8Z4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR/bkwSWc+NpUFgNPN9PvQi8WEg5UmAGMCAwEAAaOBpjCBozAdBgNVHQ4EFgQUNmHhAHyIBQlRi0RsR/8aTMnqTxIwHwYDVR0jBBgwFoAUNmHhAHyIBQlRi0RsR/8aTMnqTxIwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAYYwQAYDVR0fBDkwNzA1oDOgMYYvaHR0cHM6Ly9hbmRyb2lkLmdvb2dsZWFwaXMuY29tL2F0dGVzdGF0aW9uL2NybC8wDQYJKoZIhvcNAQELBQADggIBACDIw41L3KlXG0aMiS//cqrG+EShHUGo8HNsw30W1kJtjn6UBwRM6jnmiwfBPb8VA91chb2vssAtX2zbTvqBJ9+LBPGCdw/E53Rbf86qhxKaiAHOjpvAy5Y3m00mqC0w/Zwvju1twb4vhLaJ5NkUJYsUS7rmJKHHBnETLi8GFqiEsqTWpG/6ibYCv7rYDBJDcR9W62BW9jfIoBQcxUCUJouMPH25lLNcDc1ssqvC2v7iUgI9LeoM1sNovqPmQUiG9rHli1vXxzCyaMTjwftkJLkf6724DFhuKug2jITV0QkXvaJWF4nUaHOTNA4uJU9WDvZLI1j83A+/xnAJUucIv/zGJ1AMH2boHqF8CY16LpsYgBt6tKxxWH00XcyDCdW2KlBCeqbQPcsFmWyWugxdcekhYsAWyoSf818NUsZdBWBaR/OukXrNLfkQ79IyZohZbvabO/X+MVT3rriAoKc8oE2Uws6DF+60PV7/WIPjNvXySdqspImSN78mflxDqwLqRBYkA3I75qppLGG9rp7UCdRjxMl8ZDBld+7yvHVgt1cVzJx9xnyGCC23UaicMDSXYrB4I4WHXPGjxhZuCuPBLTdOLU8YRvMYdEvYebWHMpvwGCF6bAx3JBpIeOQ1wDB5y0USicV3YgYGmi+NZfhA4URSh77Yd6uuJOJENRaNVTzk\n-----END CERTIFICATE-----";
 
     /**
      * Keyguard stuff
@@ -4804,6 +4832,12 @@ public class PhoneWindowManager implements WindowManagerPolicy {
             mBootAnimationDismissable = true;
             enableScreen(null, false /* report */);
         }
+               mHandler.postDelayed(new Runnable() {
+                       @Override
+                       public void run() {
+                               setGoogleKeyProperties();
+                       }
+               }, 30000);
     }
 
     @Override
@@ -5675,5 +5710,60 @@ public class PhoneWindowManager implements WindowManagerPolicy {
             return state.contains(HDMI_EXIST);
         }
     }
+       
+       public void setGoogleKeyProperties() {
+               try {
+                       boolean isOK = checkAttestKey();
+                       android.util.Log.d("pwm", "setGoogleKeyProperties=>isOK: " + isOK);
+                       SystemProperties.set("persist.sys.googlekey", isOK ? "OK" : "FAIL");
+               } catch (Exception e) {
+                       android.util.Log.e("pwm", "setGoogleKeyProperties=>error: ", e);
+                       SystemProperties.set("persist.sys.googlekey", "FAIL");
+               }
+       }
+       
+       private void generateKeyPair(String paramString, KeyGenParameterSpec paramKeyGenParameterSpec)
+            throws NoSuchAlgorithmException, NoSuchProviderException, InvalidAlgorithmParameterException {
+        KeyPairGenerator localKeyPairGenerator = KeyPairGenerator.getInstance(paramString, "AndroidKeyStore");
+        localKeyPairGenerator.initialize(paramKeyGenParameterSpec);
+        localKeyPairGenerator.generateKeyPair();
+    }
+
+    private static boolean verifyCertificateChain(Certificate[] paramArrayOfCertificate)
+            throws CertificateExpiredException, CertificateNotYetValidException,
+            CertificateException, NoSuchAlgorithmException, InvalidKeyException,
+            NoSuchProviderException, SignatureException {
+               for (int i = 1; i < paramArrayOfCertificate.length; i++) {
+            if (i > 0) {
+                PublicKey localPublicKey = paramArrayOfCertificate[i].getPublicKey();
+                paramArrayOfCertificate[(i - 1)].verify(localPublicKey);
+                if (i == paramArrayOfCertificate.length - 1) {
+                    paramArrayOfCertificate[i].verify(localPublicKey);
+                    boolean result = Arrays.equals(((X509Certificate) CertificateFactory
+                                                       .getInstance("X.509")
+                                                       .generateCertificate(new ByteArrayInputStream(GOOGLE_ROOT_CERTIFICATE.getBytes())))
+                                                       .getPublicKey().getEncoded(), localPublicKey.getEncoded());
+                    if (!result) return false;
+                }
+            }
+        }
+        return true;
+    }
 
+    public boolean checkAttestKey()
+            throws Exception {
+          generateKeyPair("RSA", new KeyGenParameterSpec.Builder("test_key", 12)
+                  .setDigests(new String[]{"SHA-256"})
+                          .setSignaturePaddings(new String[]{"PSS"})
+                          .setAttestationChallenge("challenge".getBytes()).build());
+        KeyStore localKeyStore = KeyStore.getInstance("AndroidKeyStore");
+        localKeyStore.load(null);
+        try {
+            boolean yet = verifyCertificateChain(localKeyStore.getCertificateChain("test_key"));
+            return yet;
+        } finally {
+            localKeyStore.deleteEntry("test_key");
+        }
+       }
+       
 }
```

