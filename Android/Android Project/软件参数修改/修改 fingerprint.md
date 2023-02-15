[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

修改 `device/mediatek/system/common/BoardConfig.mk` 文件如下代码：

```diff
@@ -249,7 +249,7 @@ include device/mediatek/system/common/connectivity/BoardConfig.mk
 
 include device/mediatek/system/common/BoardConfig-image.mk
 
-WEIBU_BUILD_NUMBER := $(shell date +%s)
+WEIBU_BUILD_NUMBER := 1675854124
```

##### 1.1.2 Android T

1. 修改 `vnd/build/make/core/weibu_config.mk` 文件如下代码：

   ```diff
   @@ -1 +1 @@
   -WEIBU_BUILD_NUMBER ?= $(shell date +%s)
   +WEIBU_BUILD_NUMBER ?= 1675905906
   ```

2. 修改 `sys/device/mediatek/system/common/BoardConfig.mk` 文件如下代码：

   ```diff
   @@ -249,7 +249,7 @@ include device/mediatek/system/common/connectivity/BoardConfig.mk
    
    include device/mediatek/system/common/BoardConfig-image.mk
    
   -WEIBU_BUILD_NUMBER := $(shell date +%s)
   +WEIBU_BUILD_NUMBER := 1675854124
    
    #Add MTK's hook
    ifndef MTK_TARGET_PROJECT
   ```

   