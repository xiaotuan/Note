如果在 `Kotlin` 源代码文件中，没有创建类，而是直接定义变量或方法，这时在其他类中就可以直接使用这些不带类名的变量和方法。例如下面是一个这样的源代码文件：

**PermissionUtils.kt**

```kotlin
/*
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.samples.filemanager

import android.Manifest
import android.app.AppOpsManager
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Environment
import android.provider.Settings
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat


// AppOpsManager.OPSTR_MANAGE_EXTERNAL_STORAGE is a @SystemAPI at the moment
// We should remove the annotation for applications to avoid hardcoded value
const val MANAGE_EXTERNAL_STORAGE_PERMISSION = "android:manage_external_storage"
const val NOT_APPLICABLE = "N/A"

fun getStoragePermissionName(): String {
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        MANAGE_EXTERNAL_STORAGE_PERMISSION
    } else {
        Manifest.permission.READ_EXTERNAL_STORAGE
    }
}

fun openPermissionSettings(activity: AppCompatActivity) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        requestStoragePermissionApi30(activity)
    }
    else {
        activity.startActivity(
            Intent(
                Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
                Uri.fromParts("package", activity.packageName, null)
            )
        )
    }
}

fun getLegacyStorageStatus(): String {
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
        Environment.isExternalStorageLegacy().toString()
    } else {
        NOT_APPLICABLE
    }
}

fun getPermissionStatus(activity: AppCompatActivity): String {
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        checkStoragePermissionApi30(activity).toString()
    } else {
        checkStoragePermissionApi19(activity).toString()
    }
}

fun checkStoragePermission(activity: AppCompatActivity): Boolean {
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        checkStoragePermissionApi30(activity)
    } else {
        checkStoragePermissionApi19(activity)
    }
}

fun requestStoragePermission(activity: AppCompatActivity) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
        requestStoragePermissionApi30(activity)
    }
    // If you want to see the default storage behavior on Android Q once the permission is granted
    // Set the "requestLegacyExternalStorage" flag in the AndroidManifest.xml file to false
    else {
        requestStoragePermissionApi19(activity)
    }
}

@RequiresApi(30)
fun checkStoragePermissionApi30(activity: AppCompatActivity): Boolean {
    val appOps = activity.getSystemService(AppOpsManager::class.java)
    val mode = appOps.unsafeCheckOpNoThrow(
        MANAGE_EXTERNAL_STORAGE_PERMISSION,
        activity.applicationInfo.uid,
        activity.packageName
    )

    return mode == AppOpsManager.MODE_ALLOWED
}

@RequiresApi(30)
fun requestStoragePermissionApi30(activity: AppCompatActivity) {
    val intent = Intent(Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION)

    activity.startActivityForResult(intent, MANAGE_EXTERNAL_STORAGE_PERMISSION_REQUEST)
}

@RequiresApi(19)
fun checkStoragePermissionApi19(activity: AppCompatActivity): Boolean {
    val status =
        ContextCompat.checkSelfPermission(activity, Manifest.permission.READ_EXTERNAL_STORAGE)

    return status == PackageManager.PERMISSION_GRANTED
}

@RequiresApi(19)
fun requestStoragePermissionApi19(activity: AppCompatActivity) {
    val permissions = arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE)
    ActivityCompat.requestPermissions(
        activity,
        permissions,
        READ_EXTERNAL_STORAGE_PERMISSION_REQUEST
    )
}
```

如果使用上面文件中的方法或变量的类在同一级目录下，可以直接使用方法名或变量名。例如：

**FileExplorerActivity.kt**

```kotlin
/*
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.samples.filemanager

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.os.Environment.getExternalStorageDirectory
import android.view.View
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import com.android.samples.filemanager.databinding.ActivityFileExplorerBinding
import java.io.File

const val MANAGE_EXTERNAL_STORAGE_PERMISSION_REQUEST = 1
const val READ_EXTERNAL_STORAGE_PERMISSION_REQUEST = 2

class FileExplorerActivity : AppCompatActivity() {
    private var hasPermission = false
    private lateinit var binding: ActivityFileExplorerBinding
    private lateinit var currentDirectory: File
    private lateinit var filesList: List<File>
    private lateinit var adapter: ArrayAdapter<String>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityFileExplorerBinding.inflate(layoutInflater)
        binding.toolbar.inflateMenu(R.menu.file_manager_menu)
        setContentView(binding.root)

        setupUi()
    }

    override fun onResume() {
        super.onResume()

        hasPermission = checkStoragePermission(this)
        if (hasPermission) {
            if (Build.VERSION.SDK_INT == Build.VERSION_CODES.Q) {
                if (!Environment.isExternalStorageLegacy()) {
                    binding.rationaleView.visibility = View.GONE
                    binding.legacyStorageView.visibility = View.VISIBLE
                    return
                }
            }

            binding.rationaleView.visibility = View.GONE
            binding.filesTreeView.visibility = View.VISIBLE

            // TODO: Use getStorageDirectory instead https://developer.android.com/reference/android/os/Environment.html#getStorageDirectory()
            open(getExternalStorageDirectory())
        } else {
            binding.rationaleView.visibility = View.VISIBLE
            binding.filesTreeView.visibility = View.GONE
        }
    }

    private fun setupUi() {
        binding.toolbar.setOnMenuItemClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
            true
        }

        binding.permissionButton.setOnClickListener {
            requestStoragePermission(this)
        }

        adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, mutableListOf<String>())
        binding.filesTreeView.adapter = adapter
        binding.filesTreeView.setOnItemClickListener { _, _, position, _ ->
            val selectedItem = filesList[position]
            open(selectedItem)
        }
    }

    private fun open(selectedItem: File) {
        if (selectedItem.isFile) {
            return openFile(this, selectedItem)
        }

        currentDirectory = selectedItem
        filesList = getFilesList(currentDirectory)

        adapter.clear()
        adapter.addAll(filesList.map {
            if (it.path == selectedItem.parentFile.path) {
                renderParentLink(this)
            } else {
                renderItem(this, it)
            }
        })

        adapter.notifyDataSetChanged()
    }
}
```

如果使用的类与 `PermissionUtils.kt` 文件不在同一个目录下，则在使用方法或变量时，在前面添加包名，例如：

```kotlin
hasPermission = com.android.samples.filemanager.checkStoragePermission(this)
```

或者使用 `import` 导入该方法：

```kotlin
import com.android.samples.filemanager.checkStoragePermission
```

但是，如果希望 `Java` 代码也可以访问该文件中的方法和变量，则需要再文件的第一行代码前添加如下注解：

```kotlin
/*
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

@file:JvmName("PermissionUtils")
package com.android.samples.filemanager
```

注解内的字符串表示在 `Java` 代码中使用 `PermissionUtils` 作为该文件的类名，比如要使用里面的方法，可以这样写：

```java
import com.android.samples.filemanager.PermissionUtils;

boolean hasPermission = PermissionUtils.checkStoragePermission(this)
```

