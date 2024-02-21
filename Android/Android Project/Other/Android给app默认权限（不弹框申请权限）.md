[toc]

### 1. 直接在代码中修改

关于APK默认权限修改
1.系统签名应用
frameworks/base/services/core/java/com/android/server/pm/DefaultPermissionGrantPolicy.java
在 `grantDefaultSystemHandlerPermissions` 中修改

```java
    // Camera
    Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    PackageParser.Package cameraPackage = getDefaultSystemHandlerActivityPackageLPr(
            cameraIntent, userId);
    if (cameraPackage != null
            && doesPackageSupportRuntimePermissions(cameraPackage)) {
        grantRuntimePermissionsLPw(cameraPackage, CAMERA_PERMISSIONS, userId);
        grantRuntimePermissionsLPw(cameraPackage, MICROPHONE_PERMISSIONS, userId);
        grantRuntimePermissionsLPw(cameraPackage, STORAGE_PERMISSIONS, userId);
    }

//  feedback
+            PackageParser.Package feedBackPackage = getPackageLPr("android.com.feedback");
+            if (feedBackPackage != null
+                    && doesPackageSupportRuntimePermissions(feedBackPackage)) {
+                grantRuntimePermissionsLPw(feedBackPackage, STORAGE_PERMISSIONS, userId);
+                grantRuntimePermissionsLPw(feedBackPackage, CAMERA_PERMISSIONS, userId);
+            } 
```

2.非系统签名应用，（手动安装以及v2签名应用）
frameworks/base/services/core/java/com/android/server/pm/PackageManagerService.java
在 `grantPermissionsLpw` 函数中添加如下代码

```java
    //Permissions for com.xxx.xxx
     if(pkg.packageName.contains("com.xxx.xxx")) {
              final int permsSize = pkg.requestedPermissions.size();
              for (int i=0; i<permsSize; i++) {
                  final String name = pkg.requestedPermissions.get(i);
                  final BasePermission bp = mSettings.mPermissions.get(name);
                  if(null != bp && permissionsState.grantInstallPermission(bp) != PermissionsState.PERMISSION_OPERATION_FAILURE) {
                      Slog.d(TAG, "zrx--- grant permission " + name + " to package " + pkg.packageName);
                      changedInstallPermission = true;
                  }
              }
          } 
123456789101112
```

### 2. 通过配置文件进行修改
1， 需要新建一个以.xml结尾的XML文件，例如default-permissions.xml
2，这个文件的内容如下：

```java
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<exceptions>
            <exception package="com.mediatek.filemanager">
                  <permission name="android.permission.READ_EXTERNAL_STORAGE" fixed="true"/>
                   <permission name="android.permission.WRITE_EXTERNAL_STORAGE" fixed="true"/>
            </exception>
</exceptions>
```

3，将这个文件拷贝到 `system/etc/default-permissions/default-permissions.xml` 这个目录下。或者使用如下 bp 文件（注意，需要将该模块添加到编译中）：

```bp
prebuilt_etc {
    name: "default-permissions-allowlist-ygps",
    sub_dir: "default-permissions",
    src: "default-permissions-ygps.xml",
    filename_from_src: true,
}

```

如果需要安装到其他路径，可以如下配置：

| product_specific: true | product/etc/subdir |
| ---------------------- | ------------------ |
| proprietary : true     | vendor/etc/subdir  |

4, 恢复出厂设置验证

### 3. Android 13 给应用添加默认权限

修改 `frameworks/base/services/core/java/com/android/server/pm/permission/DefaultPermissionGrantPolicy.java` 文件中 `grantDefaultSystemHandlerPermissions(PackageManagerWrapper pm, int userId)` 方法的如下代码：

```diff
@@ -714,6 +714,11 @@ public final class DefaultPermissionGrantPolicy {
                 getDefaultSystemHandlerActivityPackageForCategory(pm,
                         Intent.CATEGORY_APP_CALENDAR, userId),
                 userId, CALENDAR_PERMISSIONS, CONTACTS_PERMISSIONS, NOTIFICATION_PERMISSIONS);
+                               
+        // The notification permission is granted to the alarm application by default by qty at 2023-03-15 {{&&
+        // DeskClock
+        grantPermissionsToSystemPackage(pm, "com.google.android.deskclock", userId, NOTIFICATION_PERMISSIONS);
+        // &&}}
 
         // Calendar provider
         String calendarProvider =
```

