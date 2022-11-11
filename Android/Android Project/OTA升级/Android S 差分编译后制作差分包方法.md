如果是使用 Split build（分割编译），需要使用如下命令制作差分包：

```shell
out/host/linux-x86/bin/ota_from_target_files -p out/host/linux-x86 -k device/mediatek/security/releasekey -i Acer_AV0S0_P10-11_0_000.02_PAPAP_GEN1_target_files.zip Acer_AV0S0_P10-11_0_000.03_PAPAP_GEN1_target_files.zip AB_V02_V03.zip
```

