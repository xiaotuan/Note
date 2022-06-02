如果是使用 Split build（分割编译），需要使用如下命令制作差分包：

```shell
out/host/linux-x86/bin/ota_from_target_files -v --block --path out/host/linux-x86/ -i old.zip new.zip ota_update.zip
```

