[toc]

> 提示：
>
> 红石 Fota 宏在 `vendor/weibu_sz/products/products.mk` 文件中，将 `REDSTONE_FOTA_SUPPORT` 宏设置为 yes，即可打开红石 Fota。

### 1. 编译 sys_images

```shell
$ source build/envsetup.sh
$ lunch sys_mssi_t_64_ab-user m863pr_bsp_64 m863pr_bsp_64_asb_ac
$ setpaths
$ make installclean
$ make sys_images -j24
```

> 注意：
>
> 1. `lunch` 命令参数说明如下：
>
>    1.  `sys_mssi_t_64_ab-user`：如果工程是 64 位，该值为 `sys_mssi_t_64_ab`；如果工程是 32 为，该值为 `sys_mssi_t_32_ago`；后面的 `-user`，表示你编译的是 user 版本，如果需要编译 userdebug 版本，可以修改为 `-userdebug`。
>    2. `m863pr_bsp_64`：PCB 版型号
>    3. `m863pr_bsp_64_asb_ac`：客制化工程名称
>2. 上面命令不包含 `$` 字符。
> 3. 如果需要编译 GMS 项目，可以将 `make sys_images -j24` 命令修改为 `make BUILD_GMS=yes sys_images -j`
>

### 2. 编译 vnd_images 和 krn_images

```shell
$ source build/envsetup.sh
$ lunch vnd_m863pr_bsp_64-user m863pr_bsp_64 m863pr_bsp_64_asb_ac
$ make installclean
$ make vnd_images krn_images -j24
```

> 注意：
>
> 1. `lunch` 命令参数说明如下：
>
>    1.  `vnd_m863pr_bsp_64-user`：该参数其实是 `vnd_` 加上 PCB 版型名称，上面的 PCB 版型名称是 `m863pr_bsp_64`。后面的 `-user`，表示你编译的是 user 版本，如果需要编译 userdebug 版本，可以修改为 `-userdebug`。
>    2. `m863pr_bsp_64`：PCB 版型号
>    3. `m863pr_bsp_64_asb_ac`：客制化工程名称
>2. 上面命令不包含 `$` 字符。
> 3. 如果需要编译 GMS 项目，可以将 `make sys_images -j24` 命令修改为 `make BUILD_GMS=yes vnd_images krn_images -j`
>

### 3. 执行全编的分割编译命令

```shell
$ python out/target/product/mssi_t_64_ab/images/split_build.py --system-dir out/target/product/mssi_t_64_ab/images --vendor-dir out/target/product/m863pr_bsp_64/images --kernel-dir out/target/product/m863pr_bsp_64/images --output-dir out/target/product/m863pr_bsp_64/merged
```

> 注意：请替换上面命令中的 `mssi_t_64_ab` 字符串和 `m863pr_bsp_64` 字符串成自己工程的对应的字符串。其中 `mssi_t_64_ab` 字符串根据项目是否是 64 位系统来决定，64 位系统的值为 `mssi_t_64_ab`，32 位系统的值为 `mssi_t_32_ago`；`m863pr_bsp_64` 字符串替换成自己项目的 PCB 版型名称。

### 4. 编译 otapackage

```shell
$ setpaths
$ python out/target/product/mssi_t_64_ab/images/split_build.py --system-dir out/target/product/mssi_t_64_ab/images --vendor-dir out/target/product/m863pr_bsp_64/images --kernel-dir out/target/product/m863pr_bsp_64/images --output-dir out/target/product/m863pr_bsp_64/merged   --otapackage --targetfiles
```

> 注意：请替换上面命令中的 `mssi_t_64_ab` 字符串和 `m863pr_bsp_64` 字符串成自己工程的对应的字符串。其中 `mssi_t_64_ab` 字符串根据项目是否是 64 位系统来决定，64 位系统的值为 `mssi_t_64_ab`，32 位系统的值为 `mssi_t_32_ago`；`m863pr_bsp_64` 字符串替换成自己项目的 PCB 版型名称。

### 5. 生成 update.zip 升级包

#### 5.1 拷贝 target 文件

将两次编译 out 中的 `out/target/product/m863pr_bsp_64/merged/target_files.zip` 文件拷贝到工程根目录下，分别命名为 V1.zip 和 V2.zip。

#### 5.2 生成升级包

执行如下命令生成 update.zip 升级包

```shell
$ ./build/tools/releasetools/ota_from_target_files -v --block -p out/host/linux-x86/ -i V1.zip V2.zip update.zip
```

如果需要指定签名文件，可以使用如下命令：

```shell
$ ./build/tools/releasetools/ota_from_target_files -v --block -p out/host/linux-x86/ -k device/mediatek/security/releasekey -i V1.zip V2.zip update.zip
```

### 6. 我自己封装的编译脚本

#### 6.1 脚本使用方法

1. 将脚本文件放置在工程代码目录的上一级目录

2. 修改脚本参数

   + `PROJECT_DIR`：工程代码目录路径
   + `PROJECT_NAME`：公共工程名称
   + `PCB_NAME`：PCB版型名称
   + `CUSTOM_PROJECT_NAME`：客户工程名称
   + `BUILD_TYPE`：编译类型，new 或者 remake
   + `IS_BUILD_GMS`：是否是 GMS 工程
   + `CPU_CORE`：编译线程数
   + `IS_BUILD_OTA`：是否编译 OTA
   + `MY_BOARD`：32 位系统的值为 sys_mssi_t_32_ago，64 位系统的值为 sys_mssi_t_64_ab
   + `MY_BOARD_VND`：不用修改
   + `OUT_TARGET_DIR_MSSI`：32 位系统的值为 mssi_t_32_ago，64 位系统的值为 mssi_t_64_ab
   + `OUT_TARGET_DIR`：不用修改

3. 在脚本文件位置下执行如下命令：

   ```shell
   $ ./complie.sh
   ```

#### 6.2 脚本代码

```shell
#!/bin/bash

start_time=$(date +%s)

PROJECT_DIR="mt8168_r"
PROJECT_NAME="full_m863pr_bsp_64-user"
PCB_NAME="m863pr_bsp_64"
CUSTOM_PROJECT_NAME="m863pr_bsp_64_asb_ac"
# new or remake
BUILD_TYPE="remake"
IS_BUILD_GMS=0
CPU_CORE=30

IS_BUILD_OTA=1
# 64位: sys_mssi_t_64_ab, 32位：sys_mssi_t_32_ago
MY_BOARD=sys_mssi_t_64_ab
MY_BOARD_VND=vnd_$PCB_NAME
OUT_TARGET_DIR_MSSI=mssi_t_64_ab
OUT_TARGET_DIR=$PCB_NAME

function show_complie_time() {
    echo "Build result: $1"
    end_time=$(date +%s)
    times=$((end_time - start_time))
    hours=$((times/3600))
    times=$((times%3600))
    minutes=$((times/60))
    seconds=$((times%60))

    if [ $1 -eq 0 ]; then
        echo -e "\e[1; 32m"
        echo "================================================================"
        echo ""
        echo "  Complie Success"
        echo "  Complie Use: $hours hours, $minutes minutes, $seconds seconds"
        echo ""
        echo "================================================================"
        echo -e "\e[0m"
    else
        echo -e "\e[1; 31m"
        echo "================================================================"
        echo ""
        echo "  Complie Fail"
        echo "  Complie Use: $hours hours, $minutes minutes, $seconds seconds"
        echo ""
        echo "================================================================"
        echo -e "\e[0m"
    fi
}

function make_project() {
    if [ "$BUILD_TYPE" == "new" ];then
        date_str=$(date +%Y%m%d%H%M%S)
        echo ""
        echo -e "\e[1; 33mMove out directory to out_$date_str directory\e[0m"
        echo ""
        mv out/ out_$date_str/
    fi
    if [ "$IS_BUILD_OTA" -eq 1 ];then
        if [[ $PROJECT_NAME =~ eng ]];then
            LUNCH_NUM=$MY_BOARD-eng
            LUNCH_NUM_VND=$MY_BOARD_VND-eng
        elif [[ $PROJECT_NAME =~ user ]];then
            LUNCH_NUM=$MY_BOARD-user
            LUNCH_NUM_VND=$MY_BOARD_VND-user
        elif [[ $PROJECT_NAME =~ userdebug ]];then
            LUNCH_NUM=$MY_BOARD-userdebug
            LUNCH_NUM_VND=$MY_BOARD_VND-userdebug
        else
            echo ""
            echo -e "\e[1; 31mProject name is incorrect: $PROJECT_NAME\e[0m"
            echo ""
            return -1
        fi

        # echo "run weibu_prebuild.pl"
        # perl wb_customer/tools/weibu_prebuild.pl $PCB_NAME $CUSTOM_PROJECT_NAME $(gettop)

        if [ "$IS_BUILD_GMS" -eq 1 ];then
            echo ""
            echo -e "\e[1; 33mStart make BUILD_GMS=yes -j$CPU_CORE\e[0m"
            echo ""
            source build/envsetup.sh
            lunch $LUNCH_NUM $PCB_NAME $CUSTOM_PROJECT_NAME
            setpaths
            make installclean
            make BUILD_GMS=yes sys_images -j$CPU_CORE
            if [ $? -eq 0 ];then
                echo ""
                echo -e "\e[1; 33mmake BUILD_GMS=yes vnd_images krn_images -j$CPU_CORE\e[0m"
                echo ""
                lunch $LUNCH_NUM_VND $PCB_NAME $CUSTOM_PROJECT_NAME
                make installclean
                make BUILD_GMS=yes vnd_images krn_images -j$CPU_CORE
                if [ $? -eq 0 ];then
                    echo ""
                    echo -e "\e[1; 33msplit_build all\e[0m"
                    echo ""
                    python out/target/product/$OUT_TARGET_DIR_MSSI/images/split_build.py --system-dir out/target/product/$OUT_TARGET_DIR_MSSI/images --vendor-dir out/target/product/$OUT_TARGET_DIR/images --kernel-dir out/target/product/$OUT_TARGET_DIR/images --output-dir out/target/product/$OUT_TARGET_DIR/merged
                    if [ $? -eq 0 ];then
                        echo ""
                        echo -e "\e[1; 33msplit_build otapackage\e[0m"
                        echo ""
                        setpaths
                        python out/target/product/$OUT_TARGET_DIR_MSSI/images/split_build.py --system-dir out/target/product/$OUT_TARGET_DIR_MSSI/images --vendor-dir out/target/product/$OUT_TARGET_DIR/images --kernel-dir out/target/product/$OUT_TARGET_DIR/images --output-dir out/target/product/$OUT_TARGET_DIR/merged   --otapackage --targetfiles
                        if [ $? -eq 0 ];then
                            return 0
                        else 
                            echo ""
                            echo -e "\e[1; 31msplit_build otapackage failed.\e[0m"
                            echo ""
                            return -1
                        fi
                    else
                        echo ""
                        echo -e "\e[1; 31msplit_build failed.\e[0m"
                        echo ""
                        return -1
                    fi
                else
                    echo ""
                    echo -e "\e[1; 31mmake BUILD_GMS=yes vnd_images krn_images -j$CPU_CORE failed.\e[0m"
                    echo ""
                    return -1
                fi
            else
                echo ""
                echo -e "\e[1; 31mmake BUILD_GMS=yes sys_images -j$CPU_CORE failed.\e[0m"
                echo ""
                return -1
            fi
        else
            echo ""
            echo -e "\e[1; 33mmake sys_images -j$CPU_CORE\e[0m"
            echo ""
            source build/envsetup.sh
            lunch $LUNCH_NUM $PCB_NAME $CUSTOM_PROJECT_NAME
            setpaths
            make installclean
            make sys_images -j$CPU_CORE
            if [ $? -eq 0 ];then
                echo ""
                echo -e "\e[1; 33mmake vnd_images krn_images -j$CPU_CORE\e[0m"
                echo ""
                lunch $LUNCH_NUM_VND $PCB_NAME $CUSTOM_PROJECT_NAME
                make installclean
                make vnd_images krn_images -j$CPU_CORE
                if [ $? -eq 0 ];then
                    echo ""
                    echo -e "\e[1; 33msplit_build all\e[0m"
                    echo ""
                    python out/target/product/$OUT_TARGET_DIR_MSSI/images/split_build.py --system-dir out/target/product/$OUT_TARGET_DIR_MSSI/images --vendor-dir out/target/product/$OUT_TARGET_DIR/images --kernel-dir out/target/product/$OUT_TARGET_DIR/images --output-dir out/target/product/$OUT_TARGET_DIR/merged
                    if [ $? -eq 0 ];then
                        echo ""
                        echo -e "\e[1; 33msplit_build otapackage\e[0m"
                        echo ""
                        setpaths
                        python out/target/product/$OUT_TARGET_DIR_MSSI/images/split_build.py --system-dir out/target/product/$OUT_TARGET_DIR_MSSI/images --vendor-dir out/target/product/$OUT_TARGET_DIR/images --kernel-dir out/target/product/$OUT_TARGET_DIR/images --output-dir out/target/product/$OUT_TARGET_DIR/merged   --otapackage --targetfiles
                        if [ $? -eq 0 ];then
                            return 0
                        else 
                            echo ""
                            echo -e "\e[1; 31msplit_build otapackage failed.\e[0m"
                            echo ""
                            return -1
                        fi
                    else
                        echo ""
                        echo -e "\e[1; 31msplit_build all failed.\e[0m"
                        echo ""
                        return -1
                    fi
                else
                    echo ""
                    echo -e "\e[1; 31mmake vnd_images krn_images -j$CPU_CORE failed.\e[0m"
                    echo ""
                    return -1
                fi
            else
                echo ""
                echo -e "\e[1; 31mmake sys_images -j$CPU_CORE failed.\e[0m"
                echo ""
                return -1
            fi
        fi
    else
        source build/envsetup.sh
        lunch $PROJECT_NAME $PCB_NAME $CUSTOM_PROJECT_NAME
        if [ "$IS_BUILD_GMS" -eq 1 ];then
            echo ""
            echo -e "\e[1; 33mStart make BUILD_GMS=yes -j$CPU_CORE\e[0m"
            echo ""
            make BUILD_GMS=yes -j$CPU_CORE
        else
            echo ""
            echo -e "\e[1; 33mStart make -j$CPU_CORE\e[0m"
            echo ""
            make -j$CPU_CORE
        fi
    fi
}

cd $PROJECT_DIR
make_project 2>&1 | tee build.log
if [ $? -eq 0 ];then
    ./cp_common.sh
    show_complie_time 0
else
    show_complie_time -1
fi
```



