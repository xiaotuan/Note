[toc]

### 1. MTK

#### 1.1 MT8768

##### 1.1.1 Android S

修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/Android.bp` 文件中的如下代码：

```diff
@@ -58,7 +58,7 @@ android_library {
         "src/**/I*.aidl",
         //google home button animation effect feature is off by default, remove "//" to open it.
         //"src-opa/**/*.java",
-       //"opa/src/**/*.java",
+               "opa/src/**/*.java",
     ],
     resource_dirs: [
         "res-product",
@@ -68,7 +68,7 @@ android_library {
         "res_ext",
         //google home button animation effect feature is off by default, remove "//" to open it.
         //"res-opa",
-       //"opa/res",
+               "opa/res",
     ],
     defaults: [
         "MtkSettingsLibDefaults",
@@ -163,7 +163,7 @@ android_library {
         "res",
         "res-keyguard_ext",
         "res_ext",
-       //"opa/res",
+               "opa/res",
     ],
     srcs: [
         "tests/src/**/*.kt",
@@ -171,7 +171,7 @@ android_library {
         "src/**/*.kt",
         "src/**/*.java",
         "src/**/I*.aidl",
-       //"opa/src/**/*.java",
+               "opa/src/**/*.java",
     ],
     defaults: [
         "MtkSettingsLibDefaults",
```

