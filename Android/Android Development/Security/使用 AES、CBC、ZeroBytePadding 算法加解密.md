[toc]

### 1. 加解密方法

使用 `AES/CBC/ZeroBytePadding` 加密算法对数据进行加解密代码如下所示：

**Kotlin 版本**

```kotlin
import android.util.Log
import javax.crypto.Cipher
import javax.crypto.spec.IvParameterSpec
import javax.crypto.spec.SecretKeySpec

// 加密方法
fun encryptData(key: String, data: String): ByteArray {
    val sks = SecretKeySpec(key.toByteArray(), "AES")
    Log.d(TAG, "encryptData=>sks: ${sks.toString()}")
    val c = Cipher.getInstance("AES/CBC/ZeroBytePadding")
    c.init(Cipher.ENCRYPT_MODE, sks, IvParameterSpec(key.toByteArray()))
    return c.doFinal(data.toByteArray())
}

// 解密方法
fun decryptData(key: String, data: ByteArray): String {
    val sks = SecretKeySpec(key.toByteArray(), "AES")
    Log.d(TAG, "decryptData=>sks: ${sks.toString()}")
    val c = Cipher.getInstance("AES/CBC/ZeroBytePadding")
    c.init(Cipher.DECRYPT_MODE, sks, IvParameterSpec(key.toByteArray()))
    return String(c.doFinal(data))
}
```

**Java 版本**

```java
import android.util.Log;

import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

// 加密方法
private byte[] encryptData(String key, String data)
    throws NoSuchPaddingException, NoSuchAlgorithmException,
InvalidAlgorithmParameterException, InvalidKeyException,
BadPaddingException, IllegalBlockSizeException {
    SecretKeySpec sks = new SecretKeySpec(key.getBytes(), "AES");
    Cipher c = Cipher.getInstance("AES/CBC/ZeroBytePadding");
    c.init(Cipher.ENCRYPT_MODE, sks, new IvParameterSpec(key.getBytes()));
    return c.doFinal(data.getBytes());
}

// 解密方法
private String decryptData(String key, byte[] data)
    throws NoSuchPaddingException, NoSuchAlgorithmException,
InvalidAlgorithmParameterException, InvalidKeyException,
BadPaddingException, IllegalBlockSizeException {
    SecretKeySpec sks = new SecretKeySpec(key.getBytes(), "AES");
    Cipher c = Cipher.getInstance("AES/CBC/ZeroBytePadding");
    c.init(Cipher.DECRYPT_MODE, sks, new IvParameterSpec(key.getBytes()));
    return new String(c.doFinal(data));
}
```

### 2. 示例代码

**Kotlin 版本**

```kotlin
val key = "3106166021166038"
val message = "This is a secret message"
val encryptData = encryptData(key, message)
val decryptStr = decryptData(key, encryptData)
Log.d(TAG, "onResume=>decryptStr: $decryptStr")
```

**Java 版本**

```java
String key = "3106166021166038";
String message = "This is a secret message";
try {
    byte[] encryptData = encryptData(key, message);
    String decryptStr = decryptData(key, encryptData);
    Log.d(TAG, "onResume=>decryptStr: " + decryptStr);
} catch (Exception e) {
    Log.e(TAG, "onResume=>error: ", e);
}
```

> 注意：
>
> 使用 `AES/CBC/ZeroBytePadding` 算法加解密时，在调用 `Cipher` 类的 `init()` 方法时，必须使用 `public final void init(int opmode, Key key, AlgorithmParameterSpec params)` 这个方法，不然会报如下错误：
>
> ```
> java.lang.RuntimeException: Unable to resume activity {net.zenconsult.mobile/net.zenconsult.mobile.CryptoExample1Activity}: java.security.InvalidKeyException: no IV set when one expected
> ```

