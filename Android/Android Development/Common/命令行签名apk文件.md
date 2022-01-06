> 警告：
>
> 下面方法只支持 V1 签名。

可以使用如下命令对 apk 文件进行签名：

```shell
$ jarsigner -keystore "PATH TO YOUR release.jks FILE" -storepass password -keypass password "PATH TO YOUR RAW APK FILE" "签名别名"
```

例如：

```shell
$ jarsigner -keystore ./release.keystore -storepass 123456 -keypass 123456 ./app-debug.apk YourName
jar 已签名。

警告:
签名者证书为自签名证书。
```

