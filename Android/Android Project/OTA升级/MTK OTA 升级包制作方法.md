[toc]

### 1. 打开 OTA 编译开关

修改编译脚本 `auto-compile-android-src-code.sh`，打开 OTA 编译：

```shell
STEP4_MAKE_OTA=1
```

或者执行如下命令：

```shell
make otapackage  -j8 2>&1 | tee ota.log
```

### 2. 拷贝 `otatools` 文件夹到根目录

`otatools` 文件夹位于 `out/target/product/mssi_t_64_ab/obj/PACKAGING/otatools_intermediates/` 目录下。将 `otatools` 文件夹拷贝到源代码根目录下。

> 注意：生成差分包需要使用 Java 8 以上的 Java SDK（不包括 Java 8）。因此，如果服务器没有安装，则需要安装。也可以拷贝到安装有 Java 8 以上的 Linux 设备上。

### 3. 拷贝 `target` 文件到 `otatools` 根目录下

`target` 文件位于 `out/target/product/tb8168p1_64_bsp/merged/target_files.zip`。

> 注意：MTK 编译不会保存上次编译出来的 target 文件，因此在编译完成后需要马上将其拷贝出来。

### 4. 将旧的 `target_files.zip`文件命名为 `old.zip` ，将新的 `target_files.zip` 文件命名为 `new.zip`。

### 5. 在 `otatools` 文件夹下执行下面命令生成差分包

```shell
$ ./bin/ota_from_target_files --block -v -i old.zip new.zip update.zip
```

其他可用命令：

```
1. 命令如下：
  ./bin/ota_from_target_files [flags] input_target_files output_ota_package
  1）制作整体升级包
    ./bin/ota_from_target_files -k sign_key target.zip full_update.zip
  2）制作差分升级包
    ./bin/ota_from_target_files  -k sign_key -i target_base.zip target_target.zip delta_base-to-target.zip
  3）制作降级的差分包,即新版本升级到旧版本的升级
    ./bin/ota_from_target_files --downgrade -k sign_key -i target_newer_build.zip target_older_build.zip delta_downgrade.zip
  4）制作擦除用户数据的升级包,包括整包和差分包
    ./bin/ota_from_target_files --wipe_user_data -k sign_key target_target.zip delta_wipe_userdata.zip
    ./bin/ota_from_target_files --wipe_user_data -k sign_key -i target_base.zip target_target.zip delta_wipe_userdata.zip

2. 参数名词说明
sign_key：                  user版本为 device/mediatek/security/releasekey
                            userdebug版本为 device/mediatek/security/testkey 或 build/make/target/product/security/testkey
target_base.zip：           基准版本target包
target_target.zip：         目标版本target包
```

如果 `out` 目录中没有 `out/target/product/mssi_t_64_ab/obj/PACKAGING/otatools_intermediates/` 文件夹，可以在源码根目录下使用如下命令编译生成差分包：

```shell
$ ./build/tools/releasetools/ota_from_target_files –v –s device/mediate/build/releasetools/mt_ota_from_target_files.py -i old.zip new.zip update.zip
```

参数说明如下：

+ `-v` ：显示具体命令
+ `-s`： MTK 特有脚本文件
+ `-i`：制作差分包  

如果没有 `device/mediate/build/releasetools/mt_ota_from_target_files.py` 文件，可以将上面的命令修改成如下命令：

```shell
$ ./build/tools/releasetools/ota_from_target_files –v -i old.zip new.zip update.zip
```

### 5.1 block 差分包生成方法

```shell
$ ./build/tools/releasetools/ota_from_target_files -v --block -s device/mediatek/build/releasetools/mt_ota_from_target_files.py -i old.zip new.zip update.zip
```

参数说明如下：

+ `-v` ：显示具体命令
+ `-s`： MTK 特有脚本文件
+ `--block`：生成基于模块式的 OTA  
+ `-i`：制作差分包  
