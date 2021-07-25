[toc]

### 1. 报错信息

```
Exception in thread "main" javax.crypto.IllegalBlockSizeException: Input length not multiple of 8 bytes
	at java.base/com.sun.crypto.provider.CipherCore.finalNoPadding(CipherCore.java:1115)
	at java.base/com.sun.crypto.provider.CipherCore.fillOutputBuffer(CipherCore.java:1059)
	at java.base/com.sun.crypto.provider.CipherCore.doFinal(CipherCore.java:855)
	at java.base/com.sun.crypto.provider.DESCipher.engineDoFinal(DESCipher.java:314)
	at java.base/javax.crypto.Cipher.doFinal(Cipher.java:2205)
	at EncryptionDemo/com.qty.encrypt.DESEncrypt.encrypt(DESEncrypt.java:20)
	at EncryptionDemo/com.qty.encrypt.EncryptUtils.encrypt(EncryptUtils.java:13)
	at EncryptionDemo/com.qty.encrypt.EncryptDemo.main(EncryptDemo.java:13)
```

### 2. 分析原因

DES、AES 或者 3DES 属于块加密算法，一般来说原文必须是 8 的整数倍，所以块加密算法除子加密模式之外，还涉及到一个填充模式。

如果一定要用 NoPadding 的话，那么必须保证原文字节是 8 的倍数，否则的话需要使用其他的填充模式。

在 Sun JCE 中默认的填充模式除了 NoPadding 之外，还有：

PKCS5Padding 和 ISO10126Padding

PKCS5Padding 的填充规则是：

填充至符合块大小的整数倍，填充值为填充数量数。例如：
原始：FF FF FF FF FF FF FF FF FF
填充：FF FF FF FF FF FF FF FF FF 07 07 07 07 07 07 07

ISO10126Padding 的填充规则是：

填充至符合块大小的整数倍，填充值最后一个字节为填充的数量数，其他字节随机处理。例如：
原始：FF FF FF FF FF FF FF FF FF
填充：FF FF FF FF FF FF FF FF FF 3F 7A B4 09 14 36 07


使用填充模式后原文字节并不需要是 8 的整数倍，采用填充模式之后，块加密的密文长度为：

(N / 8 * 8) + 8

如上，假如原文长度为 15 个字节，密文长度就是 16 个字节。假如原文长度为 16 个字节，密文长度就为 24 个字节。也就是说，采用填充模式后必须进行填充，哪怕是 8 的整数倍。

> 注意：
>
> + 2.1 使用哪一种填充模式加密的，也必须采用哪种填充模式解密;
> + 2.2 CBC 加密模式需要有一个 IV 参数（也就是初始化向量），这个值在加 密时会随机生成，但必须保存下来，否则无法完成解密工作。
> + 2.3 建议采用 ECB 模式，或者在使用 CBC 时将初始化向量保存，在解密时使用。

### 3. 解决方法

查看代码发现 DES 加密中使用到了 `DES/ECB/NoPadding` 加密算法，只要将加密算法该为 `DES/ECB/PKCS5Padding` 即可。

