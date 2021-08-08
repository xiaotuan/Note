### 1. DES 加解密实现方法

```java
package com.qty.encrypt;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.security.Key;
import java.security.SecureRandom;

import javax.crypto.Cipher;
import javax.crypto.CipherInputStream;
import javax.crypto.CipherOutputStream;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;

/**
 * DES 加密类
 * @author xiaotuan
 *
 */
public class DESEncrypt {
	
	/**
	 * 加密算法
	 * 其他算法可以查阅 https://docs.oracle.com/javase/10/docs/specs/security/standard-names.html#cipher-algorithm-names
	 */
	public static final String CIPHER_ALGORITHM = "DES/ECB/PKCS5Padding";
	
	/**
	 * 加密字符串
	 * @param data 要加密的字符串
	 * @param key 加密密码，密码长度为 16 位
	 * @return 返回加密后的 byte 数组
	 * @throws Exception
	 */
	public static byte[] encrypt(byte[] datas, String key) throws Exception {
		Key deskey = keyGenerator(key);
		Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
		SecureRandom random = new SecureRandom();
		cipher.init(Cipher.ENCRYPT_MODE, deskey, random);
		byte[] results = cipher.doFinal(datas);
		return results;
	}
	
	/**
	 * 加密文件
	 * @param originFilePath 要加密的文件路径
	 * @param destFilePath 加密后的文件路径
	 * @param key 加密密码，密码长度为 16 位
	 * @throws Exception
	 */
	public static void encryptFile(String originFilePath, String destFilePath, String key) throws Exception {
		Key deskey = keyGenerator(key);
		Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
		SecureRandom random = new SecureRandom();
		cipher.init(Cipher.ENCRYPT_MODE, deskey, random);
		InputStream is = new FileInputStream(originFilePath);
		OutputStream os = new FileOutputStream(destFilePath);
		CipherInputStream cis = new CipherInputStream(is, cipher);
		byte[] buffer = new byte[1024];
		int r = 0;
		while ((r = cis.read(buffer)) > 0) {
			os.write(buffer, 0 , r);
		}
		cis.close();
		is.close();
		os.close();
	}
	
	/**
	 * 解密 byte 数组
	 * @param data 要解密的 byte 数组
	 * @param key 解密密码，密码长度为 16 位
	 * @return 返回解密后的 byte 数组
	 * @throws Exception
	 */
	public static byte[] decrypt(byte[] datas, String key) throws Exception {
		Key deskey = keyGenerator(key);
		Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
		cipher.init(Cipher.DECRYPT_MODE, deskey);
		return cipher.doFinal(datas);
	}
	
	/**
	 * 解密文件
	 * @param originFilePath 要解密的文件路径
	 * @param destFilePath 解密后的文件路径
	 * @param key 解密密码，密码长度为 16 位
	 * @throws Exception
	 */
	public static void decryptFile(String originFilePath, String destFilePath, String key) throws Exception {
		Key deskey = keyGenerator(key);
		Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
		SecureRandom random = new SecureRandom();
		cipher.init(Cipher.DECRYPT_MODE, deskey, random);
		InputStream is = new FileInputStream(originFilePath);
		OutputStream os = new FileOutputStream(destFilePath);
		CipherOutputStream cis = new CipherOutputStream(os, cipher);
		byte[] buffer = new byte[1024];
		int r = 0;
		while ((r = is.read(buffer)) > 0) {
			cis.write(buffer, 0 , r);
		}
		cis.close();
		is.close();
		os.close();
	}
	
	/**
	 * 加密秘钥生成方法
	 * @param keyStr 加密密码
	 * @return 返回生成后的秘钥
	 * @throws Exception
	 */
	private static SecretKey keyGenerator(String keyStr) throws Exception {
		byte input[] = hexStringToBytes(keyStr);
		DESKeySpec desKey = new DESKeySpec(input);
		SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("DES");
		SecretKey secureKey = keyFactory.generateSecret(desKey);
		return secureKey;
	}
	
	/**
	 * 十六进制字符串转换成 byte 数组
	 * @param hexStr 十六进制字符串
	 * @return
	 */
	private static byte[] hexStringToBytes(String hexStr) {
		byte[] b = new byte[hexStr.length() / 2];
		int j = 0;
		for (int i = 0; i < b.length; i++) {
			char c0 = hexStr.charAt(j++);
			char c1 = hexStr.charAt(j++);
			b[i] = (byte)((parse(c0) << 4) | parse(c1));
		}
		return b;
	}
	
	/**
	 * 将一个十六进制字符转换成 int 类型
	 * @param c 十六进制字符
	 * @return 返回十六进制字符对应的 int 值
	 */
	private static int parse(char c) {
		if (c >= 'a') {
			return (c - 'a' + 10) & 0x0f;
		}
		if (c >= 'A') {
			return (c - 'A' + 10) & 0x0f;
		}
		return (c - '0') & 0x0f;
	}

}
```

### 2. 使用示例

```java
package com.qty.encrypt;

import java.security.Provider;
import java.security.Security;
import java.util.Arrays;
import java.util.Base64;

public class EncryptDemo {

	public static void main(String[] args) throws Exception {
		String publicKeyPath = "C:\\Users\\xiaotuan\\Desktop\\public.keystore";
		String privateKeyPath = "C:\\Users\\xiaotuan\\Desktop\\private.keystore";
		String source = "Hello World!";
		System.out.println("原文： " + source);
		String key = "e8v98n23kvc89sdf";
		byte[] encryptDatas = DESEncrypt.encryptString(source, key);
		String encryptDatasStr = Base64.getEncoder().encodeToString(encryptDatas);
		System.out.println("加密后: " + encryptDatasStr);
		byte[] decryptDatas = DESEncrypt.decrypt(encryptDatas, key);
		System.out.println("解密后：" + new String(decryptDatas));
		Provider[] providers = Security.getProviders();
		for (int i = 0; i < providers.length; i++) {
			System.out.println(providers[i].getName());
		}
		DESEncrypt.encryptFile("C:\\WorkSpace\\GitSpace\\Xiaotuan\\Notes\\Common\\12306Bypass使用说明.md", 
				"C:\\Users\\xiaotuan\\Desktop\\encryptFile.md", key);
		DESEncrypt.decryptFile("C:\\Users\\xiaotuan\\Desktop\\encryptFile.md", 
				"C:\\Users\\xiaotuan\\Desktop\\12306Bypass使用说明.md", key);
    }
}
```

