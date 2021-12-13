[toc]

### 1. 展讯平台

#### 1.1 SC9863A Android R

修改 `build/make/core/version_defaults.mk` 文件，将如下代码：

```makefile
BUILD_NUMBER := $(shell date +%s)
```

修改成固定值即可，例如：

```makefile
BUILD_NUMBER := 1632390036
```

### 2. MTK 平台

#### 2.1 MTK8766

##### 2.1.1 Android R

修改 `device/mediatek/system/common/BoardConfig.mk` 文件中 BUILD_NUMBER_WEIBU 宏的值：

```makefile
# BUILD_NUMBER_WEIBU := $(shell date +%s)
BUILD_NUMBER_WEIBU := 1639122475
```

