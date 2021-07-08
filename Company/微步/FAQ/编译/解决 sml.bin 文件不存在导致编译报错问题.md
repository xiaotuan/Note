[toc]

### 1. 报错信息

编译报错信息如下：

```
[ 39% 2400/6130] build out/target/product/s9863a3h10/sml.bin
FAILED: out/target/product/s9863a3h10/sml.bin
/bin/bash -c "cp bsp/out/androidr/s9863a3h10_Natv/dist/sml/sml*.bin out/target/product/s9863a3h10"
cp: bad 'bsp/out/androidr/s9863a3h10_Natv/dist/sml/sml*.bin': No such file or directory
[ 39% 2401/6130] build out/target/product/s9863a3h10/tos.bin
FAILED: out/target/product/s9863a3h10/tos.bin
/bin/bash -c "cp bsp/out/androidr/s9863a3h10_Natv/dist/trusty/tos*.bin out/target/product/s9863a3h10"
cp: bad 'bsp/out/androidr/s9863a3h10_Natv/dist/trusty/tos*.bin': No such file or directory
[ 39% 2402/6130] Install: out/target/product/s9863a3h10/vendor/lib/libvcm_dw9800.so
```

### 2. 报错分析

从字面上可以看出是因为没有找到要拷贝的文件。其实这些文件会在编译的时候从 `verdor/sprd/release/IDH` 文件夹中对应工程的文件夹拷贝文件夹的内容到工程根目录下对应的文件夹下。（其实就是拷贝文件夹中的 bsp 和 out 文件夹内容到工程根目录下的 bsp 和 out 文件夹中）

其实编译脚本是有拷贝动作的，但是需要在一定条件下才会触发拷贝动作，其相关的脚本代码如下：

```shell
if [ $STEP0_MAKE_ALL_IMG -ne 0 ];then

    echo -e "\033[;33m

	start to make all img -j$TASK_NUM ...

    \033[0m"

    source build/envsetup.sh
    choosecombo release $MY_BOARD $BUILD_VER gms

    if [ ! -d out/target/product/$OUT_TARGET_DIR/vendor ];then
        echo "IDH out not exist copy them now !!"
        if [ ! -d out/target/product/$OUT_TARGET_DIR ];then
           rm -rf bsp/out
           rm -rf out
        fi
        cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/bsp .
        cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/out .
    fi

    make -j$TASK_NUM
    if [ $? -eq 0 ]; then
        echo "Build images ok!"
    else
        echo "Build images failed!"
        exit 1
    fi

    cp_sign
    makepac

    copy_out_imagefiles

    echo "make all img -j$TASK_NUM finished"
    date "+%Y-%m-%d %H:%M:%S"
fi
```

### 3. 解决办法

**第一种解决办法：**

将 `vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/bsp` 目录下的文件手动拷贝到对应目录中。

**第二种解决方法：**

修改编译脚本，将下面脚本从条件中提取出来，让它始终执行：

```shell
if [ $STEP0_MAKE_ALL_IMG -ne 0 ];then

    echo -e "\033[;33m

	start to make all img -j$TASK_NUM ...

    \033[0m"

    source build/envsetup.sh
    choosecombo release $MY_BOARD $BUILD_VER gms

    #if [ ! -d out/target/product/$OUT_TARGET_DIR/vendor ];then
        echo "IDH out not exist copy them now !!"
        #if [ ! -d out/target/product/$OUT_TARGET_DIR ];then
        #   rm -rf bsp/out
        #   rm -rf out
        #fi
        cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/bsp .
        cp -rf vendor/sprd/release/IDH/${MY_BOARD}-${BUILD_VER}-gms/out .
    #fi

    make -j$TASK_NUM
    if [ $? -eq 0 ]; then
        echo "Build images ok!"
    else
        echo "Build images failed!"
        exit 1
    fi

    cp_sign
    makepac

    copy_out_imagefiles

    echo "make all img -j$TASK_NUM finished"
    date "+%Y-%m-%d %H:%M:%S"
fi
```



