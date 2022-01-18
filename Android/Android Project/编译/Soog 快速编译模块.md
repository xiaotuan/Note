命令如下：

```shell
$ ./prebuilts/build-tools/linux-x86/bin/ninja -f out/combined-xxx.ninja -j16 模块名
```

例如：

```shell
$ ./prebuilts/build-tools/linux-x86/bin/ninja -f out/combined-full_m863u_bsp_64.ninja -j16 MtkSettings
$ ./prebuilts/build-tools/linux-x86/bin/ninja -f out/combined-full_m863u_bsp_64.ninja -j16 boot
```

