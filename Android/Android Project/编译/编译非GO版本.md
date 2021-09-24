[toc]

### 1. MTK 平台

#### 1.1 mt8766_r

修改 `device/mediateksample/工程名/ProjectConfig.mk` 文件，将 `BUILD_AGO_GMS` 宏设置为 `no` 即可，例如修改 `device/mediateksample/m863u_bsp_64/ProjectConfig.mk` 文件：

```makefile
BUILD_AGO_GMS = no
```

