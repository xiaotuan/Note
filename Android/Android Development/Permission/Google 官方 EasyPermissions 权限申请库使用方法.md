[toc]

### 1. EasyPermissions 仓库地址

<https://github.com/googlesamples/easypermissions>

### 2. 使用方法

#### 2.1 添加依赖

在 `build.gradle` 文件中添加如下依赖：

```
dependencies {
    // For developers using AndroidX in their applications
    implementation 'pub.devrel:easypermissions:3.0.0'
 
    // For developers using the Android Support Library
    implementation 'pub.devrel:easypermissions:2.0.1'
}
```

### 2.2 在代码中使用

1. 在 `Activity` 或 `Fragment` 中重写 `onRequestPermissionsResult` 方法：

   ```java
   public class MainActivity extends AppCompatActivity {
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
       }
   
       @Override
       public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
           super.onRequestPermissionsResult(requestCode, permissions, grantResults);
   
           // Forward results to EasyPermissions
           EasyPermissions.onRequestPermissionsResult(requestCode, permissions, grantResults, this);
       }
   }
   ```

2. 请求权限

   下面的示例显示如何为需要 `CAMERA` 和 `ACCESS_FINE_LOCATION` 权限的方法请求权限 。有几点需要注意：

   - 用于 `EasyPermissions#hasPermissions(...)` 检查应用程序是否已拥有所需的权限。此方法可以将任意数量的权限作为其最终参数。
   - 使用 请求权限 `EasyPermissions#requestPermissions` 。此方法将请求系统权限并在必要时显示提供的理由字符串。提供的请求代码对于该请求应该是唯一的，并且该方法可以将任意数量的权限作为其最终参数。
   - 注释的使用 `AfterPermissionGranted` 。这是可选的，但为了方便而提供。如果给定请求中的所有权限都被授予，*则所有*使用正确的请求代码注释的方法都将被执行（确保具有唯一的请求代码）。带注释的方法必须为 *void* 并且*没有输入参数*（相反，您可以使用 *onSaveInstanceState* 来保持抑制参数的状态）。这是为了简化在授予请求方法的所有权限后需要运行请求方法的常见流程。这也可以通过在回调上添加逻辑来实现 `onPermissionsGranted`。

   ```java
   @AfterPermissionGranted(RC_CAMERA_AND_LOCATION)
   private void methodRequiresTwoPermission() {
       String[] perms = {Manifest.permission.CAMERA, Manifest.permission.ACCESS_FINE_LOCATION};
       if (EasyPermissions.hasPermissions(this, perms)) {
           // Already have permission, do the thing
           // ...
       } else {
           // Do not have permissions, request them now
           EasyPermissions.requestPermissions(this, getString(R.string.camera_and_location_rationale),
                   RC_CAMERA_AND_LOCATION, perms);
       }
   }
   ```

   或者为了更好地控制基本原理对话框，请使用`PermissionRequest`：

   ```java
   EasyPermissions.requestPermissions(
           new PermissionRequest.Builder(this, RC_CAMERA_AND_LOCATION, perms)
                   .setRationale(R.string.camera_and_location_rationale)
                   .setPositiveButtonText(R.string.rationale_ask_ok)
                   .setNegativeButtonText(R.string.rationale_ask_cancel)
                   .setTheme(R.style.my_fancy_style)
                   .build());
   ```

   或者，为了更好地控制，您可以让您的`Activity`/`Fragment`实现该`PermissionCallbacks`接口。

   ```java
   public class MainActivity extends AppCompatActivity implements EasyPermissions.PermissionCallbacks {
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
       }
   
       @Override
       public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
           super.onRequestPermissionsResult(requestCode, permissions, grantResults);
   
           // Forward results to EasyPermissions
           EasyPermissions.onRequestPermissionsResult(requestCode, permissions, grantResults, this);
       }
   
       @Override
       public void onPermissionsGranted(int requestCode, List<String> list) {
           // Some permissions have been granted
           // ...
       }
   
       @Override
       public void onPermissionsDenied(int requestCode, List<String> list) {
           // Some permissions have been denied
           // ...
       }
   }
   ```

3. 所需权限

   在某些情况下，如果没有某些权限，您的应用程序将无法正常运行。如果用户使用 “不再询问” 选项拒绝这些权限，您将无法向用户请求这些权限，并且必须在应用设置中更改这些权限。在这种情况下，您可以使用该方法`EasyPermissions.somePermissionPermanentlyDenied(...)` 向用户显示一个对话框，并将他们定向到您的应用程序的系统设置屏幕：

   > **注意**：由于Android框架权限API提供的信息有限，该`somePermissionPermanentlyDenied`方法仅在权限被拒绝并且您的应用程序收到回调后才有效`onPermissionsDenied`。否则图书馆无法区分永久拒绝和“尚未拒绝”的情况。

   ```java
   @Override
   public void onPermissionsDenied(int requestCode, List<String> perms) {
       Log.d(TAG, "onPermissionsDenied:" + requestCode + ":" + perms.size());
   
       // (Optional) Check whether the user denied any permissions and checked "NEVER ASK AGAIN."
       // This will display a dialog directing them to enable the permission in app settings.
       if (EasyPermissions.somePermissionPermanentlyDenied(this, perms)) {
           new AppSettingsDialog.Builder(this).build().show();
       }
   }
   
   @Override
   public void onActivityResult(int requestCode, int resultCode, Intent data) {
       super.onActivityResult(requestCode, resultCode, data);
   
       if (requestCode == AppSettingsDialog.DEFAULT_SETTINGS_REQ_CODE) {
           // Do something after user returned from app settings screen, like showing a Toast.
           Toast.makeText(this, R.string.returned_from_app_settings_to_activity, Toast.LENGTH_SHORT)
                   .show();
       }
   }
   ```

   如果您想与基本原理对话框交互，请实现 `EasyPermissions.RationaleCallbacks`。

   ```java
   @Override
   public void onRationaleAccepted(int requestCode) {
       // Rationale accepted to request some permissions
       // ...
   }
   
   @Override
   public void onRationaleDenied(int requestCode) {
       // Rationale denied to request some permissions
       // ...
   }
   ```

   