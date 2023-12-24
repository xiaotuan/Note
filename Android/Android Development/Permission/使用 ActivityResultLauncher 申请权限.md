**1. 申请单个权限**

```kotlin
fun requestQueryAllPackagesPermission(context: AppCompatActivity, callback: ActivityResultCallback<Boolean>) {
    val launcher = context.registerForActivityResult(ActivityResultContracts.RequestPermission(), callback)
    launcher.launch(Manifest.permission.QUERY_ALL_PACKAGES)
}
```

**2. 申请多个权限**

```kotlin
private fun requestAndroidRLaterPermission(context: AppCompatActivity, callback: RequestPermissionCallback) {
    val launcher = context.registerForActivityResult(ActivityResultContracts.RequestMultiplePermissions()) { result ->
        var allGraint = true
        result.forEach { (permission, graint) ->
            QLog.i(TAG, "requestAndroidRLaterPermission=>permission: $permission, graint: $graint")
            if (!graint) {
                allGraint = false
            }
        }
        callback.onResult(allGraint)
    }
    launcher.launch(ANDROID_R_LATER_PERMISSIONS.toTypedArray())
}
```

