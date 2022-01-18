[toc]

过 SMR 认证的软件，需要修改 `ro.build.version.base_os` 的修改成该项目第一次过 GMS 认证的固件的 fingerprint 的值。

### 1. MTK 平台

#### 1.1 MT8766

##### 1.1.1 Android R

修改 `build/make/tools/buildinfo.sh` 文件中 `ro.build.version.base_os` 属性的值为第一次过 GMS 认证的 fingerprint ：

```shell
echo "ro.build.version.base_os=Masstel/Masstel_Tab8_Edu/Masstel_Tab8_Edu:11/RP1A.200720.011/1640591398:user/release-keys"
```

