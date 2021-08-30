通过 `DocumentUI` 应用选择文件的方法如下所示：

**Kotlin 版本**

```kotlin
package com.qty.kotlintest

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.os.Environment
import android.provider.DocumentsContract
import android.provider.MediaStore
import android.util.Log
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity(), View.OnClickListener {


    private var mSelectBtn: Button? = null
    private var mFilePath: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mSelectBtn = findViewById(R.id.select)
        mSelectBtn?.setOnClickListener(this)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        Log.d(TAG,"onActivityResult=>requestCode: $requestCode, resultCode: $resultCode")
        if (requestCode == OPEN_DOCUMENT_REQUEST_CODE && resultCode == RESULT_OK) {
            val documentUri = data?.data
            if (documentUri != null) {
                contentResolver.takePersistableUriPermission(documentUri, Intent.FLAG_GRANT_READ_URI_PERMISSION)
                mFilePath = getFilePathFromUri(documentUri)
                Log.d(TAG, "onActivityResult=>File path: $mFilePath")
            } else {
                Log.e(TAG, "onActivityResult=>Uri is null.")
            }
        }
    }

    override fun onClick(v: View?) {
        when (v?.id) {
            R.id.select -> {
                Log.d(TAG, "onclick...")
                selectFile()
            }
        }
    }

    private fun selectFile() {
        val intent = Intent(Intent.ACTION_OPEN_DOCUMENT)
        intent.type = "audio/mpeg"
        intent.addCategory(Intent.CATEGORY_OPENABLE)
        startActivityForResult(intent, OPEN_DOCUMENT_REQUEST_CODE)
    }

    private fun getFilePathFromUri(uri: Uri): String? {
        var path: String? = null
        if (DocumentsContract.isDocumentUri(this, uri)) {
            if (isMediaDocument(uri)) {
                val id = DocumentsContract.getDocumentId(uri).split(":")[1]
                val selection = "_id = $id"
                val type = DocumentsContract.getDocumentId(uri).split(":")[0]
                when (type) {
                    "audio" -> path = getFilePath(MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, selection)
                    "video" -> path = getFilePath(MediaStore.Video.Media.EXTERNAL_CONTENT_URI, selection)
                    "image" -> path = getFilePath(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, selection)
                }
            } else if (isDownloadsDocument(uri)) {
                path = DocumentsContract.getDocumentId(uri).substring(DocumentsContract.getDocumentId(uri).indexOf(":"))
            } else if (isExternalStorageDocument(uri)) {
                var subPath = uri.toString()
                subPath = subPath.substring(subPath.lastIndexOf("/"))
                subPath = subPath.substring(0, subPath.indexOf("%"))
                if ("primary" == subPath) {
                    path = "/storage/emulated/0"
                } else {
                    path = "/storage" + subPath
                }
                path = "$path/${DocumentsContract.getDocumentId(uri).split(":")[1]}"
            } else if ("content" == uri.scheme?.lowercase()) {
                path = getFilePath(uri, null)
            } else if ("file" == uri.scheme?.lowercase()) {
                path = uri.path
            }
        }
        return path
    }

    private fun getFilePath(uri: Uri, selection: String?): String? {
        var path: String? = null
        val cursor = contentResolver.query(uri, null, selection, null, null)
        if (cursor != null) {
            if (cursor.moveToFirst()) {
                path = cursor.getString(cursor.getColumnIndex("_data"))
            }
            cursor.close()
        }
        return path
    }

    private fun isExternalStorageDocument(uri: Uri): Boolean {
        return "com.android.externalstorage.documents" == uri.authority
    }

    private fun isDownloadsDocument(uri: Uri): Boolean {
        return "com.android.providers.downloads.documents" == uri.authority
    }

    private fun isMediaDocument(uri: Uri): Boolean {
        return "com.android.providers.media.documents" == uri.authority
    }

    companion object {
        const val TAG = "MainActivity"
        const val OPEN_DOCUMENT_REQUEST_CODE = 0x33
    }
}
```

**Java 版本**

```java
package com.qty.test;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.DocumentsContract;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private static final String TAG = MainActivity.class.getSimpleName();

    private static final int OPEN_DOCUMENT_REQUEST_CODE = 0X33;

    private Button mSelectBtn;

    private String mFilePath;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mSelectBtn = findViewById(R.id.select);

        mSelectBtn.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.select:
                selectFile();
                break;
        }
    }

    private void selectFile() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.setType("audio/mpeg");
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        startActivityForResult(intent, OPEN_DOCUMENT_REQUEST_CODE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        Log.d(TAG, "onActivityResult=>requestCode: " + requestCode + ", resultCode: " + resultCode);
        if (requestCode == OPEN_DOCUMENT_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            Uri documentUri = data.getData();
            if (documentUri != null) {
                getContentResolver().takePersistableUriPermission(documentUri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
                Log.d(TAG, "onActivityResult=>documentUri: " + documentUri);
                Log.d(TAG, "onActivityResult=>author: " + documentUri.getAuthority());
                Log.d(TAG, "onActivityResult=>External Path: " + Environment.getExternalStorageDirectory());
                Toast.makeText(this, documentUri.toString(), Toast.LENGTH_LONG).show();
                mFilePath = getFilePathFromUri(documentUri);
                Log.d(TAG, "onActivityResult=>File path: " + mFilePath);
            } else {
                Log.e(TAG, "onActivityResult=>Uri is null.");
            }
        }
    }

    private String getFilePathFromUri(Uri uri) {
        Log.d(TAG, uri.toString());
        String path = null;
        if (DocumentsContract.isDocumentUri(this, uri)) {
            if (isMediaDocument(uri)) {
                String id = DocumentsContract.getDocumentId(uri).split(":")[1];
                String selection = "_id = " + id;
                String type = DocumentsContract.getDocumentId(uri).split(":")[0];
                if (type.equals("audio"))
                    path = getFilePath(MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, selection);
                else if (type.equals("video"))
                    path = getFilePath(MediaStore.Video.Media.EXTERNAL_CONTENT_URI, selection);
                else if (type.equals("image"))
                    path = getFilePath(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, selection);
            } else if (isDownloadsDocument(uri)) {
                path = DocumentsContract.getDocumentId(uri).substring(DocumentsContract.getDocumentId(uri).indexOf(":"));
            } else if (isExternalStorageDocument(uri)) {
                String subPath = uri.toString();
                subPath = subPath.substring(subPath.lastIndexOf("/"));
                subPath = subPath.substring(0, subPath.indexOf("%"));
                if (subPath.contains("primary")) {
                    path = "/storage/emulated/0";
                } else {
                    path = "/storage" + subPath;
                }
                Log.d(TAG, "getFilePathFromUri=>path: " + path + ", subPath: " + subPath);
                path = path + "/" + DocumentsContract.getDocumentId(uri).split(":")[1];
            }
        } else if ("content".equalsIgnoreCase(uri.getScheme())) {
            path = getFilePath(uri, null);
        } else if ("file".equalsIgnoreCase(uri.getScheme())) {
            path = uri.getPath();
        }
        return path;
    }

    private String getFilePath(Uri uri, String selection) {
        String path = null;
        Cursor cursor = getContentResolver().query(uri, null, selection, null, null);
        if (cursor != null) {
            if (cursor.moveToFirst()) {
                path = cursor.getString(cursor.getColumnIndex("_data"));
            }
            cursor.close();
        }
        return path;
    }

    public boolean isExternalStorageDocument(Uri uri) {
        return "com.android.externalstorage.documents".equals(uri.getAuthority());
    }

    public boolean isDownloadsDocument(Uri uri) {
        return "com.android.providers.downloads.documents".equals(uri.getAuthority());
    }

    public boolean isMediaDocument(Uri uri) {
        return "com.android.providers.media.documents".equals(uri.getAuthority());
    }
}
```

