[toc]

### 1. UF223 Android P(9.0)

1.1 修改 `device/mediateksample/工程名/mid/工程名/system.prop` 文件的如下代码：

```properties
ro.build.display.id=WK-N2.P0.V10.1.RC-V08.8766.M64.20200917
```

### 2. MT8168 Android R(11.0)

2.1 修改 `build/make/tools/buildinfo.sh` 文件中的如下代码：

```shell
echo "ro.build.display.id=MT8168_10_M860PR200-PB33D-64.`date +%Y%m%d`.H"
```

