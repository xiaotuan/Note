[toc]

### 1. MTK

#### 1.1 MT8768

##### 1.1.1 Android S

修改 `build/make/tools/buildinfo.sh` 文件中的如下代码：

```diff
@@ -11,9 +11,9 @@ else
 fi
 
 date=$(date +%Y%m%d)
echo "ro.build.display.id=ML_SO0N_M10_4G_T3.GOV.V1_$date"
 echo "ro.build.display.inner.id=$BUILD_DISPLAY_ID"
-echo "ro.build.version.incremental=$BUILD_NUMBER"
+echo "ro.build.version.incremental=1"
 echo "ro.build.version.sdk=$PLATFORM_SDK_VERSION"
 echo "ro.build.version.preview_sdk=$PLATFORM_PREVIEW_SDK_VERSION"
 echo "ro.build.version.preview_sdk_fingerprint=$PLATFORM_PREVIEW_SDK_FINGERPRINT"
```

