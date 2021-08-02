[toc]

### 1. 报错信息

```
Exception in thread "main" javax.crypto.IllegalBlockSizeException: Data must not be longer than 117 bytes
	at java.base/com.sun.crypto.provider.RSACipher.doFinal(RSACipher.java:348)
	at java.base/com.sun.crypto.provider.RSACipher.engineDoFinal(RSACipher.java:405)
	at java.base/javax.crypto.Cipher.doFinal(Cipher.java:2205)
	at EncryptionDemo/com.qty.encrypt.RSAEncrypt.encrypt(RSAEncrypt.java:52)
	at EncryptionDemo/com.qty.encrypt.EncryptDemo.main(EncryptDemo.java:35)
```

### 2. 分析原因

RSA非对称加密解密内容长度是有限制的，加密长度不超过117Byte，解密长度不超过128Byte。

### 3. 解决办法

对加密、解密内容分段处理，然后拼接。

代码如下：

```java
package com.qty.encrypt;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.security.Key;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;

import javax.crypto.Cipher;

public class RSAEncrypt {
	
	/**
	 * 加密算法
	 */
	private static final String ALGORITHM = "RSA";
	/**
	 * 密钥的长度
	 */
	private static final int KEY_SIZE = 1024;
	/**
     * RSA最大加密明文大小
     */
    private static final int MAX_ENCRYPT_BLOCK = 117;
    /**
     * RSA最大解密密文大小
     */
    private static final int MAX_DECRYPT_BLOCK = 128;
	
	
	/**
	 * 加密字符串
	 * @param data 要加密的字符串
	 * @param key 加密密码，密码长度为 16 位
	 * @return 返回加密后的 byte 数组
	 * @throws Exception
	 */
	public static byte[] encrypt(byte[] datas, String keystorePath) throws Exception {
		// 将文件中的公钥对象读出
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(keystorePath));
		Key key = (Key) ois.readObject();
		ois.close();
		
		Cipher cipher = Cipher.getInstance(ALGORITHM);
		cipher.init(Cipher.ENCRYPT_MODE, key);
        int inputLen = datas.length;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        int offSet = 0;
        byte[] cache;
        int i = 0;
        // 对数据分段解密
        while (inputLen - offSet > 0) {
            if (inputLen - offSet > MAX_DECRYPT_BLOCK) {
                cache = cipher.doFinal(datas, offSet, MAX_DECRYPT_BLOCK);
            } else {
                cache = cipher.doFinal(datas, offSet, inputLen - offSet);
            }
            out.write(cache, 0, cache.length);
            i++;
            offSet = i * MAX_DECRYPT_BLOCK;
        }
        byte[] encryptDatas = out.toByteArray();
        out.close();
        return encryptDatas;
	}
	
	/**
	 * 加密文件
	 * @param originFilePath 要加密的文件路径
	 * @param destFilePath 加密后的文件路径
	 * @param key 加密密码，密码长度为 16 位
	 * @throws Exception
	 */
	public static void encryptFile(String originFilePath, String destFilePath, String keystorePath) throws Exception {
		// 将文件中的公钥对象读出
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(keystorePath));
		Key key = (Key) ois.readObject();
		ois.close();
		
		Cipher cipher = Cipher.getInstance(ALGORITHM);
		cipher.init(Cipher.ENCRYPT_MODE, key);
		InputStream is = new FileInputStream(originFilePath);
		OutputStream os = new FileOutputStream(destFilePath);
		byte[] buffer = new byte[MAX_ENCRYPT_BLOCK];
		int len = 0;
		byte[] cache;
		while ((len = is.read(buffer)) > 0) {
			cache = cipher.doFinal(buffer, 0, len);
			os.write(cache);
		}
        os.close();
        is.close();
	}
	
	/**
	 * 解密 byte 数组
	 * @param data 要解密的 byte 数组
	 * @param key 解密密码，密码长度为 16 位
	 * @return 返回解密后的 byte 数组
	 * @throws Exception
	 */
	public static byte[] decrypt(byte[] datas, String keystorePath) throws Exception {
		// 将文件中的私钥对象读出
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(keystorePath));
		Key key = (Key) ois.readObject();
		ois.close();
		
		Cipher cipher = Cipher.getInstance(ALGORITHM);
		cipher.init(Cipher.DECRYPT_MODE, key);
        int inputLen = datas.length;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        int offSet = 0;
        byte[] cache;
        int i = 0;
        // 对数据分段解密
        while (inputLen - offSet > 0) {
            if (inputLen - offSet > MAX_DECRYPT_BLOCK) {
                cache = cipher.doFinal(datas, offSet, MAX_DECRYPT_BLOCK);
            } else {
                cache = cipher.doFinal(datas, offSet, inputLen - offSet);
            }
            out.write(cache, 0, cache.length);
            i++;
            offSet = i * MAX_DECRYPT_BLOCK;
        }
        byte[] decryptedData = out.toByteArray();
        out.close();
        return decryptedData;
	}
	
	/**
	 * 解密文件
	 * @param originFilePath 要解密的文件路径
	 * @param destFilePath 解密后的文件路径
	 * @param key 解密密码，密码长度为 16 位
	 * @throws Exception
	 */
	public static void decryptFile(String originFilePath, String destFilePath, String keystorePath) throws Exception {
		// 将文件中的私钥对象读出
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream(keystorePath));
		Key key = (Key) ois.readObject();
		ois.close();
		
		Cipher cipher = Cipher.getInstance(ALGORITHM);
		cipher.init(Cipher.DECRYPT_MODE, key);
		InputStream is = new FileInputStream(originFilePath);
		OutputStream os = new FileOutputStream(destFilePath);
		byte[] buffer = new byte[MAX_DECRYPT_BLOCK];
		int len = 0;
		byte[] cache;
		while ((len = is.read(buffer)) > 0) {
			cache = cipher.doFinal(buffer, 0, len);
			os.write(cache);
		}
        os.close();
        is.close();
	}
	
	/**
	 * 生成密钥对
	 * @param key 加密密码
	 * @param publicKeyStorePath  公钥文件路径
	 * @param privateKeyStorePath 私钥文件路径
	 * @throws Exception
	 */
	public static void generateKeyPair(String key, String publicKeyStorePath, String privateKeyStorePath) throws Exception {
		// RSA 算法要求有一个可信任的随机数源
		SecureRandom sr = new SecureRandom();
		sr.setSeed(key.getBytes());
		// 为 RSA 算法创建一个 KeyPairGenerator 对象
		KeyPairGenerator kpg = KeyPairGenerator.getInstance(ALGORITHM);
		// 利用上面的随机数据源初始化这个 KeyPairGenerator 对象
		kpg.initialize(KEY_SIZE, sr);
		// 生成密钥对
		KeyPair kp = kpg.generateKeyPair();
		// 得到公钥
		Key publicKey = kp.getPublic();
		// 得到私钥
		Key privateKey = kp.getPrivate();
		// 用对象流将生成的密钥写入文件
		ObjectOutputStream oos1 = new ObjectOutputStream(new FileOutputStream(publicKeyStorePath));
		ObjectOutputStream oos2 = new ObjectOutputStream(new FileOutputStream(privateKeyStorePath));
		oos1.writeObject(publicKey);
		oos2.writeObject(privateKey);
		// 清空缓存，关闭文件流
		oos1.close();
		oos2.close();
	}
	
}
```



