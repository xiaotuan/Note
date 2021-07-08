源代码编译完成后会在 `out` 目录下生成 `androidmk` 执行文件，可以通过 `find` 找到该文件：

```shell
$ find . -type f -iname androidmk 
./out/soong/host/linux-x86/bin/androidmk
```

可以通过如下命令将 `Android.mk` 文件转换成 `Android.bp` 文件：

```shell
$ androidmk Android.mk > Android.bp
```

> 提示：该命令不一定能够转换成适合的 `Android.bp` 文件。

