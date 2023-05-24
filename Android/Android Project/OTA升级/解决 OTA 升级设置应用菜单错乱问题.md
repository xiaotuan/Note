[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

修改 `frameworks/base/services/core/java/com/android/server/pm/PackageManagerService.java` 文件的如下内容：

```diff
@@ -816,7 +816,7 @@ public class PackageManagerService extends IPackageManager.Stub
     /**
      * The initial enabled state of the cache before other checks are done.
      */
-    private static final boolean DEFAULT_PACKAGE_PARSER_CACHE_ENABLED = true;
+    private static final boolean DEFAULT_PACKAGE_PARSER_CACHE_ENABLED = false;
```

##### 1.1.2 Android T

修改 `frameworks/base/services/core/java/com/android/server/pm/PackageManagerServiceUtils.java` 文件如下代码：

```diff
@@ -155,7 +155,7 @@ public class PackageManagerServiceUtils {
     /**
      * The initial enabled state of the cache before other checks are done.
      */
-    private static final boolean DEFAULT_PACKAGE_PARSER_CACHE_ENABLED = true;
+    private static final boolean DEFAULT_PACKAGE_PARSER_CACHE_ENABLED = false;
 
     /**
      * Whether to skip all other checks and force the cache to be enabled.
```



