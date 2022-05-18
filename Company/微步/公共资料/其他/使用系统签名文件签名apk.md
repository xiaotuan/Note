[toc]

### 1. MTK 平台

#### 1.1 MT8168 芯片 Android R

1. 在 `Android` 系统源码中的 `out-user\target\product\项目名\obj\PACKAGING\otatools_intermediates\otatools\device\mediatek\security` 目录下找到 `platform.x509.pem` 和 `platform.pk8` 两个文件。

2. 在 `out/host/linux-x86/framework` 目录下找到 `signapk.jar` 文件。

3. 找到 `libconscrypt_openjdk_jni.so` 文件。

   + Linux 系统

     在 `out/host/linux-x86/lib64` 目录下找到 `libconscrypt_openjdk_jni.so` 文件。(这个文件是在 64 位系统上使用的，如果电脑系统是 32 位，则使用 `out/host/linux-x86/lib` 下的对应文件。)

   + Mac OS 系统

     只有在 Mac OS 系统下编译才会生成 `libconscrypt_openjdk_jni.so` 文件，因此这里就不讨论了。

4. 新建 SignTool 文件夹，将 `platform.x509.pem` 、`platform.pk8` 和 `signapk.jar` 放入 SignTool 文件夹中。

5. 在 SignTool 文件夹中创建一个 lib64 文件夹，并将 ``libconscrypt_openjdk_jni.so` 文件放入 lib64 文件夹中。

6. 将要签名的 apk 文件放入 SignTool 文件夹中（例如 test.apk)。

7. 在 SignTool 文件夹中执行如下命令：

   ```shell
   java -Djava.library.path="lib64/" -jar signapk.jar platform.x509.pem platform.pk8 test.apk test_sign.apk
   ```

> 注意：
>
> 1. 签名环境必须是 64 位的 Ubuntu 系统（其他 Linux 系统也可以，但必须是 64 位系统）。
> 2. Java 版本必须是 11 及以上。

#### 1.2 通用签名方法

1. 将要签名的 apk 文件放到源代码跟目录下。

2. 在源代码根目录下执行如下命令签名：

   ```shell
   $ java -Djava.library.path="./out/host/linux-x86/lib64" -jar ./out/host/linux-x86/framework/signapk.jar ./build/target/product/security/platform.x509.pem ./build/target/product/security/platform.pk8 test.apk test_sign.apk
   ```

   
