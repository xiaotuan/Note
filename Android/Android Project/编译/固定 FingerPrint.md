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

##### 2.1.2 Android T

1. 修改 `sys/device/mediatek/system/common/BoardConfig.mk` 文件的如下代码：

   ```diff
   @@ -249,7 +249,7 @@ include device/mediatek/system/common/connectivity/BoardConfig.mk
    
    include device/mediatek/system/common/BoardConfig-image.mk
    
   -WEIBU_BUILD_NUMBER := $(shell date +%s)
   +WEIBU_BUILD_NUMBER := 1696757177
    
    BUILD_BROKEN_ELF_PREBUILT_PRODUCT_COPY_FILES := true
    
   ```

2. 修改 `vnd/build/make/core/build_id.mk` 文件的如下代码：

   ```diff
   @@ -18,4 +18,4 @@
    # (like "CRB01").  It must be a single word, and is
    # capitalized by convention.
    
   -BUILD_ID=SP1A.210812.016
   +BUILD_ID=TP1A.220624.014
   ```

3. 修改 `vnd/build/make/core/weibu_config.mk` 文件如下代码：

   ```diff
   @@ -1 +1 @@
   -WEIBU_BUILD_NUMBER ?= $(shell date +%s)
   +WEIBU_BUILD_NUMBER ?= 1696757177
   ```

   
