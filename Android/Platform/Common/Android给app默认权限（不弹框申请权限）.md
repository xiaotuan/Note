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
123456789101112131415161718
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

针对第一种修改,还有一种方法
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
1234567
```

3，将这个文件拷贝到 `system/etc/**default-permissions**/default-permissions.xml` 这个目录下。
4, 恢复出厂设置验证