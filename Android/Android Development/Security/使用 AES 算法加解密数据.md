[toc]

> 提示：示例工程请看 

### 1. 生成随机秘钥方法

**Kotlin 版本**

```kotlin
package net.zenconsult.android.crypto

import java.security.SecureRandom
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey

class Crypto {

    companion object {

        public fun generateKey(randomNumberSeed: ByteArray): ByteArray {
            val keyGen = KeyGenerator.getInstance("AES")
            val random = SecureRandom.getInstance("SHA1PRNG")
            random.setSeed(randomNumberSeed)
            keyGen.init(128, random)
            val sKey = keyGen.generateKey()
            return sKey.encoded
        }

    }
}
```

**Java 版本**

```java
package net.zenconsult.android.crypto;

import android.util.Log;

import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

public class Crypto {

    private static final String TAG = "Crypto";

    public static byte[] generateKey(byte[] randomNumberSeed) {
        SecretKey sKey = null;
        try {
            KeyGenerator keyGen = KeyGenerator.getInstance("AES");
            SecureRandom random = SecureRandom.getInstance("SHA1PRNG");
            random.setSeed(randomNumberSeed);
            keyGen.init(128, random);
            sKey = keyGen.generateKey();
        } catch (NoSuchAlgorithmException e) {
            Log.e(TAG, "No such algorithm exception");
        }
        return sKey.getEncoded();
    }
}
```

### 2. 加解密方法

**Kotlin 版本**

```kotlin
package net.zenconsult.android.controller

import android.content.Context
import android.os.Binder
import android.os.Environment
import android.util.Log
import net.zenconsult.android.model.Contact
import net.zenconsult.android.model.Location
import java.io.*
import java.lang.Exception
import javax.crypto.Cipher
import javax.crypto.spec.SecretKeySpec

class SaveController {

    companion object {
        private const val TAG = "SaveController"

        public fun saveContact(context: Context, contact: Contact, key: ByteArray) {
            if (isReadWrite()) {
                try {
                    val outputFile = File(context.getExternalFilesDir(null), contact.firstName)
                    val outputStream = FileOutputStream(outputFile)
                    val data = encrypt(key, contact.getBytes())
                    outputStream.write(data)
                    outputStream.close()
                } catch (e: FileNotFoundException) {
                    Log.e(TAG, "File not found")
                } catch (e: IOException) {
                    Log.e(TAG, "IO Exception")
                }
            } else {
                Log.e(TAG, "Error opening media card in read/write mode!");
            }
        }

        public fun readContact(context: Context, fileName: String, key: ByteArray): ByteArray? {
            var data: ByteArray? = null
            if (isReadWrite()) {
                try {
                    val inputFile = File(context.getExternalFilesDir(null), fileName)
                    val inputStream = FileInputStream(inputFile)
                    val encryptData = ByteArray(inputStream.available())
                    inputStream.read(encryptData)
                    data = decrypt(key, encryptData)
                    inputStream.close()
                } catch (e: FileNotFoundException) {
                    Log.e(TAG, "File not found")
                } catch (e: IOException) {
                    Log.e(TAG, "IO Exception")
                }
            } else {
                Log.e(TAG, "Error opening media card in read/write mode!");
            }
            return data
        }

        public fun saveLocation(context: Context, location: Location, key: ByteArray) {
            if (isReadWrite()) {
                try {
                    val outputFile = File(context.getExternalFilesDir(null), location.identifier)
                    val outputStream = FileOutputStream(outputFile)
                    val data = encrypt(key, location.getBytes())
                    outputStream.write(data)
                    outputStream.close()
                } catch (e: FileNotFoundException) {
                    Log.e(TAG, "File not found")
                } catch (e: IOException) {
                    Log.e(TAG, "IO Exception")
                } catch (e: Exception) {
                    Log.e(TAG, "Other Exception: ", e)
                }
            } else {
                Log.e(TAG, "Error opening media card in read/write mode!");
            }
        }

        public fun readLocation(context: Context, fileName: String, key: ByteArray): ByteArray? {
            var data: ByteArray? = null
            if (isReadWrite()) {
                try {
                    val inputFile = File(context.getExternalFilesDir(null), fileName)
                    val inputStream = FileInputStream(inputFile)
                    val encryptData = ByteArray(inputStream.available())
                    inputStream.read(encryptData)
                    data = decrypt(key, encryptData)
                    inputStream.close()
                } catch (e: FileNotFoundException) {
                    Log.e(TAG, "File not found")
                } catch (e: IOException) {
                    Log.e(TAG, "IO Exception")
                } catch (e: Exception) {
                    Log.e(TAG, "Other Exception: ", e)
                }
            } else {
                Log.e(TAG, "Error opening media card in read/write mode!");
            }
            return data
        }

        private fun isReadOnly(): Boolean {
            Log.d(TAG, Environment.getExternalStorageState())
            return Environment.MEDIA_MOUNTED_READ_ONLY == Environment.getExternalStorageState()
        }

        private fun isReadWrite(): Boolean {
            Log.d(TAG, Environment.getExternalStorageState())
            return Environment.MEDIA_MOUNTED == Environment.getExternalStorageState()
        }

        private fun encrypt(key: ByteArray, data: ByteArray): ByteArray {
            val sKeySpec = SecretKeySpec(key, "AES")
            val cipher = Cipher.getInstance("AES")
            cipher.init(Cipher.ENCRYPT_MODE, sKeySpec)
            return cipher.doFinal(data)
        }

        private fun decrypt(key: ByteArray, data: ByteArray): ByteArray {
            val sKeySpec = SecretKeySpec(key, "AES")
            val cipher = Cipher.getInstance("AES")
            cipher.init(Cipher.DECRYPT_MODE, sKeySpec)
            return cipher.doFinal(data)
        }
    }
}
```

**Java 版本**

```java
package net.zenconsult.android.controller;

import android.content.Context;
import android.os.Environment;
import android.util.Log;

import net.zenconsult.android.crypto.Crypto;
import net.zenconsult.android.model.Contact;
import net.zenconsult.android.model.Location;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;

public class SaveController {

    private static final String TAG = "SaveController";

    public static void saveContact(Context context, Contact contact, byte[] key) {
        if (isReadWrite()) {
            try {
                File outputFile = new File(context.getExternalFilesDir(null), contact.getFirstName());
                Log.d(TAG, "saveContact=>path: " + outputFile.getAbsolutePath());
                FileOutputStream outputStream = new FileOutputStream(outputFile);
                byte[] data = encrypt(key, contact.getBytes());
                Log.d(TAG, "saveLocation=>length: " + data.length);
                outputStream.write(data);
                outputStream.close();
            } catch (FileNotFoundException e) {
                Log.e(TAG, "File not found");
            } catch (IOException e) {
                Log.e(TAG, "IO Exception");
            }
        } else {
            Log.e(TAG, "Error opening media card in read/write mode!");
        }
    }

    public static void saveLocation(Context context, Location location) {
        if (isReadWrite()) {
            try {
                File outputFile = new File(context.getExternalFilesDir(null), location.getIdentifier());
                Log.d(TAG, "saveLocation=>path: " + outputFile.getAbsolutePath());
                FileOutputStream outputStream = new FileOutputStream(outputFile);
                byte[] key = Crypto.generateKey("randomtext".getBytes());
                byte[] data = encrypt(key, location.getBytes());
                Log.d(TAG, "saveLocation=>length: " + data.length);
                outputStream.write(data);
                outputStream.close();
            } catch (FileNotFoundException e) {
                Log.e(TAG, "File not found");
            } catch (IOException e) {
                Log.e(TAG, "IO Exception");
            }
        } else {
            Log.e(TAG, "Error opening media card in read/write mode!");
        }
    }

    public static byte[] readContact(Context context, Contact contact, byte[] key) {
        byte[] data = null;
        if (isReadWrite()) {
            try {
                File outputFile = new File(context.getExternalFilesDir(null), contact.getFirstName());
                Log.d(TAG, "saveContact=>path: " + outputFile.getAbsolutePath());
                FileInputStream inputStream = new FileInputStream(outputFile);
                byte[] encryptdata = new byte[inputStream.available()];
                Log.d(TAG, "readContact=>length: " + encryptdata.length);
                inputStream.read(encryptdata);
                data = dencrypt(key, encryptdata);
                inputStream.close();
            } catch (FileNotFoundException e) {
                Log.e(TAG, "File not found");
            } catch (IOException e) {
                Log.e(TAG, "IO Exception");
            }
        } else {
            Log.e(TAG, "Error opening media card in read/write mode!");
        }
        return data;
    }

    private static boolean isReadOnly() {
        Log.e(TAG, Environment.getExternalStorageState());
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(Environment.getExternalStorageState());
    }

    private static boolean isReadWrite() {
        Log.e(TAG, Environment.getExternalStorageState());
        return Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState());
    }

    private static byte[] encrypt(byte[] key, byte[] data) {
        SecretKeySpec sKeySpec = new SecretKeySpec(key, "AES");
        Cipher cipher;
        byte[] ciphertext = null;
        try {
            cipher = Cipher.getInstance("AES");
            cipher.init(Cipher.ENCRYPT_MODE, sKeySpec);
            ciphertext = cipher.doFinal(data);
        } catch (NoSuchAlgorithmException e) {
            Log.e(TAG, "NoSuchAlgorithmException");
        } catch (NoSuchPaddingException e) {
            Log.e(TAG, "NoSucuPaddingException");
        } catch (IllegalBlockSizeException e) {
            Log.e(TAG, "IllegalBlockSizeException");
        } catch (BadPaddingException e) {
            Log.d(TAG, "BadPaddingException");
        } catch (InvalidKeyException e) {
            Log.d(TAG, "InvalidKeyException");
        }
        return ciphertext;
    }

    private static byte[] dencrypt(byte[] key, byte[] data) {
        SecretKeySpec sKeySpec = new SecretKeySpec(key, "AES");
        Cipher cipher;
        byte[] ciphertext = null;
        try {
            cipher = Cipher.getInstance("AES");
            cipher.init(Cipher.DECRYPT_MODE, sKeySpec);
            ciphertext = cipher.doFinal(data);
        } catch (NoSuchAlgorithmException e) {
            Log.e(TAG, "NoSuchAlgorithmException");
        } catch (NoSuchPaddingException e) {
            Log.e(TAG, "NoSucuPaddingException");
        } catch (IllegalBlockSizeException e) {
            Log.e(TAG, "IllegalBlockSizeException");
        } catch (BadPaddingException e) {
            Log.d(TAG, "BadPaddingException");
        } catch (InvalidKeyException e) {
            Log.d(TAG, "InvalidKeyException");
        }
        return ciphertext;
    }
}
```

### 3. 使用加解密方法

**Kotlin 版本**

```kotlin
val contact = Contact("Sheran", "Gunasekera", "", "", "sheran@zenconsult.net", "12120031337")
val key = Crypto.generateKey("randomtext".toByteArray())
SaveController.saveContact(this, contact, key)
val contactData = SaveController.readContact(this, contact.firstName!!, key)
if (contactData != null) {
    var contactStr = String(contactData)
    Log.d(TAG, "onResume=>Contact: $contactStr")
} else {
    Log.e(TAG, "onResume=>Data is null.")
}
```

**Java 版本**

```java
final Contact contact = new Contact();
contact.setFirstName("Sheran");
contact.setLastName("Gunasekera");
contact.setAddress1("");
contact.setAddress2("");
contact.setEmail("sheran@zenconsult.net");
contact.setPhone("12120031337");
byte[] key = Crypto.generateKey("randomtext".getBytes());
SaveController.saveContact(this, contact, key);
byte[] data = SaveController.readContact(this, contact, key);
if (data != null) {
    String str = null;
    try {
        str = new String(data, "utf-8");
    } catch (UnsupportedEncodingException e) {
        e.printStackTrace();
    }
    Log.d(TAG, "onResume=>str： " + str);
} else {
    Log.e(TAG, "onResume=>data is null.");
}
```

