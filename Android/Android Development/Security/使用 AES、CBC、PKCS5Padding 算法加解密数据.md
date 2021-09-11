[toc]

### 1. 加解密方法

#### 1.1 Kotlin 版本

##### 1.1.1 KeyManager.kt

```kotlin
package net.zenconsult.android.crypto

import android.content.Context
import java.io.ByteArrayOutputStream

class KeyManager(
    val mContext: Context
) {

    fun setId(data: ByteArray) {
        writer(data, FILE1)
    }

    fun setIv(data: ByteArray) {
        writer(data, FILE2)
    }

    fun getId(): ByteArray {
        return reader(FILE1)
    }

    fun getIv(): ByteArray {
        return reader(FILE2)
    }

    private fun writer(data: ByteArray, file: String) {
        val fos = mContext.openFileOutput(file, Context.MODE_PRIVATE)
        fos.write(data)
        fos.flush()
        fos.close()
    }

    private fun reader(file: String): ByteArray {
        val fis = mContext.openFileInput(file)
        val bos = ByteArrayOutputStream()
        val b = ByteArray(1024)
        var bytesRead = fis.read(b)
        while (bytesRead != -1) {
            bos.write(b, 0, bytesRead)
            bytesRead = fis.read(b)
        }
        return bos.toByteArray()
    }

    companion object {
        const val TAG = "KeyManager"
        const val FILE1 = "id_value"
        const val FILE2 = "iv_value"
    }
}
```

##### 1.1.2 Crypto.kt

```kotlin
package net.zenconsult.android.crypto

import android.content.Context
import android.util.Base64
import javax.crypto.Cipher
import javax.crypto.spec.IvParameterSpec
import javax.crypto.spec.SecretKeySpec

class Crypto(
    val mContext: Context
) {

    fun encrypt(data: ByteArray): ByteArray {
        return cipher(data, Cipher.ENCRYPT_MODE)
    }

    fun decrypt(data: ByteArray): ByteArray {
        return cipher(data, Cipher.DECRYPT_MODE)
    }

    fun armorEncrypt(data: ByteArray): String {
        return Base64.encodeToString(encrypt(data), Base64.DEFAULT)
    }

    fun armorDecrypt(data: String): String {
        return String(decrypt(Base64.decode(data, Base64.DEFAULT)))
    }

    private fun cipher(data: ByteArray, mode: Int): ByteArray {
        val km = KeyManager(mContext)
        val sks = SecretKeySpec(km.getId(), ENGINE)
        val iv = IvParameterSpec(km.getIv())
        val c = Cipher.getInstance(CRYPTO)
        c.init(mode, sks, iv)
        return c.doFinal(data)
    }

    companion object {
        const val ENGINE = "AES"
        const val CRYPTO = "AES/CBC/PKCS5Padding"
    }
}
```

#### 1.2 Java 版本

##### 1.2.1 KeyManager.java

```java
package net.zenconsult.android.crypto;

import android.content.Context;
import android.util.Log;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public class KeyManager {

    private static final String TAG = "KeyManager";

    private static final String FILE1 = "id_value";
    private static final String FILE2 = "iv_value";

    private Context mContext;

    public KeyManager(Context context) {
        mContext = context;
    }

    public void setId(byte[] data) {
        writer(data, FILE1);
    }

    public void setIv(byte[] data) {
        writer(data, FILE2);
    }

    public byte[] getId() {
        return reader(FILE1);
    }

    public byte[] getIv() {
        return reader(FILE2);
    }

    private byte[] reader(String file) {
        byte[] data = null;
        FileInputStream fis = null;
        try {
            int bytesRead = 0;
            fis = mContext.openFileInput(file);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            byte[] b = new byte[1024];
            while ((bytesRead = fis.read(b)) != -1) {
                bos.write(b, 0, bytesRead);
            }
            data = bos.toByteArray();
        } catch (Exception e) {
            Log.e(TAG, "reader=>error: ", e);
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (Exception ignore) {}
            }
        }
        return data;
    }

    private void writer(byte[] data, String file) {
        FileOutputStream fos = null;
        try {
            fos = mContext.openFileOutput(file, Context.MODE_PRIVATE);
            fos.write(data);
            fos.flush();
        } catch (Exception e) {
            Log.e(TAG, "writer=>error: ", e);
        } finally {
            if (fos != null) {
                try {
                    fos.close();
                } catch (Exception ignore) {}
            }
        }
    }
}
```

##### 1.2.2 Crypto.java

```java
package net.zenconsult.android.crypto;

import android.content.Context;
import android.os.Build;

import androidx.annotation.RequiresApi;

import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import android.util.Base64;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Crypto {

    private static final String TAG = "Crypto";

    private static final String ENGINE = "AES";
    private static final String CRYPTO = "AES/CBC/PKCS5Padding";

    private Context mContext;

    public Crypto(Context context) {
        mContext = context;
    }

    public byte[] encrypt(byte[] data)
            throws NoSuchPaddingException, InvalidKeyException,
            NoSuchAlgorithmException, IllegalBlockSizeException,
            BadPaddingException, InvalidAlgorithmParameterException {
        return cipher(data, Cipher.ENCRYPT_MODE);
    }

    public byte[] decrypt(byte[] data)
            throws NoSuchPaddingException, InvalidKeyException,
            NoSuchAlgorithmException, IllegalBlockSizeException,
            BadPaddingException, InvalidAlgorithmParameterException {
        return cipher(data, Cipher.DECRYPT_MODE);
    }

    public String armorEncrypt(byte[] data)
            throws NoSuchPaddingException, InvalidAlgorithmParameterException,
            NoSuchAlgorithmException, IllegalBlockSizeException,
            BadPaddingException, InvalidKeyException {
        return Base64.encodeToString(encrypt(data), Base64.DEFAULT);
    }

    public String armorDecrypt(String data)
            throws NoSuchPaddingException, InvalidAlgorithmParameterException,
            NoSuchAlgorithmException, IllegalBlockSizeException,
            BadPaddingException, InvalidKeyException {
        return new String(decrypt(Base64.decode(data, Base64.DEFAULT)));
    }

    private byte[] cipher(byte[] data, int mode)
            throws NoSuchPaddingException, NoSuchAlgorithmException,
            InvalidAlgorithmParameterException, InvalidKeyException,
            BadPaddingException, IllegalBlockSizeException {
        KeyManager km = new KeyManager(mContext);
        SecretKeySpec sks = new SecretKeySpec(km.getId(), ENGINE);
        IvParameterSpec iv = new IvParameterSpec(km.getIv());
        Cipher c = Cipher.getInstance(CRYPTO);
        c.init(mode, sks, iv);
        return c.doFinal(data);
    }
}
```

