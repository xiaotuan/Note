1. 在 `AndroidManifest.xml` 文件中添加如下权限：

   ```xml
   <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
   <uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE" />
   ```

2. 在 `AndroidManifest.xml` 文件的 `application` 节点中添加如下属性：

   ```xml
   android:requestLegacyExternalStorage="true"
   ```

3. 在使用权限的代码中添加如下申请权限方法：

   **Kotlin**

   ```kotlin
   import android.app.AppOpsManager
   import android.content.Intent
   import android.os.Build
   import android.os.Bundle
   import android.provider.Settings
   import androidx.activity.result.ActivityResultLauncher
   import androidx.activity.result.contract.ActivityResultContracts
   import androidx.appcompat.app.AppCompatActivity
   
   const val MANAGE_EXTERNAL_STORAGE_PERMISSION = "android:manage_external_storage"
   
   class MainActivity : AppCompatActivity() {
   
       private lateinit var requestPermissionLauncher: ActivityResultLauncher<Intent>
   
       override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)
           setContentView(R.layout.activity_main)
   
           requestPermissionLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
               result?.apply {
                   if (resultCode == RESULT_OK) {
                       // 获取权限成功后并不一定会返回 Activity.RESULT_OK, 因此没有使用前都需要判断是否获取到权限
                   }
               }
           }
   
           requestManageAllFilesAccessPermissionIfNeed()
       }
   
       private fun requestManageAllFilesAccessPermissionIfNeed() {
           if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
               val appOps = getSystemService(AppOpsManager::class.java)
               val mode = appOps.unsafeCheckOpNoThrow(
                   MANAGE_EXTERNAL_STORAGE_PERMISSION,
                   applicationInfo.uid,
                   packageName
               )
               if (mode != AppOpsManager.MODE_ALLOWED) {
                   val intent = Intent(Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION)
                   requestPermissionLauncher.launch(intent)
               }
           }
       }
   }
   ```
   
   **Java**
   
   ```java
   import android.app.Activity;
   import android.app.AppOpsManager;
   import android.content.Intent;
   import android.os.Build;
   import android.os.Bundle;
   import android.provider.Settings;
   
   import androidx.activity.result.ActivityResultLauncher;
   import androidx.activity.result.contract.ActivityResultContracts;
   
   public class MainActivity extends Activity {
       
       private static final String MANAGE_EXTERNAL_STORAGE_PERMISSION = "android:manage_external_storage";
       
       private ActivityResultLauncher<Intent> requestPermissionLauncher;
       
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
           
           requestPermissionLauncher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(), result -> {
               if (result.getResultCode() == Activity.RESULT_OK) {
                   // 获取权限成功后并不一定会返回 Activity.RESULT_OK, 因此没有使用前都需要判断是否获取到权限
               }
           });
           
           requestManageAllFilesAccessPermissionIfNeed();
       }
       
       private void requestManageAllFilesAccessPermissionIfNeed() {
           if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
               AppOpsManager appOps = getSystemService(AppOpsManager.class);
               int mode = appOps.unsafeCheckOpNoThrow(
                       MANAGE_EXTERNAL_STORAGE_PERMISSION,
                       getApplicationInfo().uid,
                       getPackageName()
               );
               if (mode != AppOpsManager.MODE_ALLOWED) {
                   Intent intent = new Intent(Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION);
                   requestPermissionLauncher.launch(intent);
               }
           }
       }
   }
   ```
   
   