在获取手机 root 权限下，通过 adb 的如下命令可以临时关闭 SELinux：

```console
$ adb shell setenforce 0
```

查看 SELinux 状态的命令如下：

```console
$ adb shell getenforce
```

