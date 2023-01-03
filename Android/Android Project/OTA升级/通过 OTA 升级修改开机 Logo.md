[toc]

### 1. 制作 OTA 升级包

通过如下命令制作 OTA 升级包：

```shell
./build/make/tools/releasetools/ota_from_target_files -v -i V02.zip V03.zip update.zip
```

### 2. 将 logo.bin 文件添加到 OTA 升级包文件中

将修改 logo 的 logo.bin 文件（从 Target 包中获取 logo.bin 文件）添加到 OTA 升级包文件中。

### 3. 修改升级脚本

在 OTA 升级压缩包的 `META-INF/com/google/android/` 目录下，将 `updater-script` 文件解压出来。在 `updater-script` 文件中搜索 `package_extract_file("lk.img"`，在搜索结果中 `package_extract_file("lk.img"` 行后添加如下脚本：

```shell
package_extract_file("logo.bin", "/dev/block/platform/bootdevice/by-name/logo");
```

例如：

```shell
ui_print("start to update alt loader image");
package_extract_file("tee.img", "/dev/block/platform/bootdevice/by-name/tee2");
package_extract_file("lk.img", "/dev/block/platform/bootdevice/by-name/lk2");
package_extract_file("logo.bin", "/dev/block/platform/bootdevice/by-name/logo");
package_extract_file("loader_ext.img", "/dev/block/platform/bootdevice/by-name/loader_ext2");
```

> 注意：脚本语法请参照具体的 `lk.img` 行。第二个参数可以参考设备中真是的 logo 文件路径。

将修改的 `updater-script` 文件替换掉压缩包中对应的文件。

### 4. 签名 OTA 升级包

使用下面命令对修改后的 OTA 升级包进行签名：

```shell
java -Xmx2048m -Djava.library.path=/work02/mtk/11/8766/B/mt8766_r/build/make/tools/lib64 -jar /work02/mtk/11/8766/B/mt8766_r/build/make/tools/framework/signapk.jar -w device/mediatek/security/releasekey.x509.pem device/mediatek/security/releasekey.pk8 ./updateV05-V06-test-202204081411.zip ./updatev05-v06.zip
```

> 注意：
>
> + ./updateV05-V06-test-202204081411.zip ：是签名前的 OTA 升级包
> + ./updatev05-v06.zip ：是签名后的 OTA 升级包

> 提示：具体签名命令，可以先在平台上使用如下命令制作一个其他升级包：
>
> ```shell
> ./build/make/tools/releasetools/ota_from_target_files -v -i V02.zip V03.zip update.zip
> ```
>
> 可以在制作完成后的日志中找到签名命令，例如：
>
> ```log
> 2022-05-23 09:10:33 - common.py - INFO    :   Running: "java -Xmx2048m -Djava.library.path=/work02/mtk/11/8766/B/mt8766_r/build/make/tools/lib64 -jar /work02/mtk/11/8766/B/mt8766_r/build/make/tools/framework/signapk.jar -w device/mediatek/security/releasekey.x509.pem device/mediatek/security/releasekey.pk8 /tmp/tmp1s3d7W.zip /tmp/tmpi8N4eb.zip"
> 2022-05-23 09:10:45 - common.py - INFO    :   Running: "zip -d /tmp/tmpi8N4eb.zip META-INF/com/android/metadata"
> 2022-05-23 09:10:46 - common.py - INFO    : deleting: META-INF/com/android/metadata
> 2022-05-23 09:10:46 - common.py - INFO    :   Running: "java -Xmx2048m -Djava.library.path=/work02/mtk/11/8766/B/mt8766_r/build/make/tools/lib64 -jar /work02/mtk/11/8766/B/mt8766_r/build/make/tools/framework/signapk.jar -w device/mediatek/security/releasekey.x509.pem device/mediatek/security/releasekey.pk8 /tmp/tmpi8N4eb.zip update.zip"
> 2022-05-23 09:10:46 - ota_from_target_files - INFO    : done.
> qintuanye@WB-SVR-27:~/work02/mtk/11/8766/B/mt8766_r$ java -Xmx2048m -Djava.library.path=/work02/mtk/11/8766/B/mt8766_r/build/make/tools/lib64 -jar ./work02/mtk/11/8766/B/mt8766_r/build/make/tools/framework/signapk.jar -w device/mediatek/security/releasekey.x509.pem device/mediatek/security/releasekey.pk8 ./updateV05-V06-test-202204081411.zip ./updatev05-v06.zip
> Error: Unable to access jarfile ./work02/mtk/11/8766/B/mt8766_r/build/make/tools/framework/signapk.jar
> ```

```shell
java -Xmx2048m -Djava.library.path=./out/host/linux-x86/lib64 -jar ./out/host/linux-x86/framework/signapk.jar -w build/target/product/security/releasekey.x509.pem build/target/product/security/releasekey.pk8 ./updateV03-V04-test.zip ./updateV03-V04.zip
```

```shell
java -Xmx2048m -Djava.library.path=./out/host/linux-x86/lib64 -jar ./out/host/linux-x86/framework/signapk.jar -w device/mediatek/security/releasekey.x509.pem device/mediatek/security/releasekey.pk8 Acer_AV0S0_P10-11_RV00RC01_RV00RC04_EEA_GEN1.zip  Acer_AV0S0_P10-11_RV00RC01_RV00RC04_EEA_GEN1—new.zip
```

