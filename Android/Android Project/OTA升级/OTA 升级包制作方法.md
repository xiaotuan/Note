[toc]

### 1. 微步

#### 1.1 MTK 平台

##### 1.1.1 mt8766_r

1. 将 `out/soong/host/linux-x86/framework` 和 `out/soong/host/linux-x86/lib64` 文件夹拷贝到 `build/make/tools/` 目录下。

2. 将源 TargetFile 文件命名为 V1.zip，并拷贝到源码根目录下。

3. 将目标 TargetFile 文件重命名为 V2.zip，并拷贝到源码根目录下。

4. 在源码根目录下执行如下命令生成升级包：

   ```shell
   $ ./build/make/tools/releasetools/ota_from_target_files -v -i V1.zip V2.zip update.zip
   ```

   如果需要指定签名秘钥，可以使用如下命令：

   ```shell
   $ ./build/make/tools/releasetools/ota_from_target_files -k 签名文件路径 -v -i V1.zip V2.zip update.zip
   ```

   > 注意：签名文件路径根据项目进行设置，例如：
   >
   > ```shell
   > $ ./build/make/tools/releasetools/ota_from_target_files -k ./device/mediatek/security/releasekey -v -i V1.zip V2.zip update.zip
   > ```

   如果需要使用 block 方式生成升级包，可以使用如下命令：

   ```shell
   $ ./build/make/tools/releasetools/ota_from_target_files -v --block -i V1.zip V2.zip update.zip
   ```

   

