[toc]

### 1. 使用系统相机拍摄后返回拍摄图片

> 提示：示例代码请查阅 <https://gitee.com/qtyresources/ProAndroidMedia>  中的 CameraIntent 示例程序。

#### 1.1 Kotlin 版本

```kotlin
package com.apress.proandroidmedia.ch1.cameraintent

import android.content.Intent
import android.graphics.Bitmap
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.widget.ImageView

class CameraIntent : AppCompatActivity() {

    private lateinit var imv: ImageView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val i = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        startActivityForResult(i, CAMERA_RESULT)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (resultCode == RESULT_OK) {
            val bmp = data?.extras?.get("data") as Bitmap
            imv = findViewById(R.id.ReturnedImageView)
            imv.setImageBitmap(bmp)
        }
    }

    companion object {
        const val CAMERA_RESULT = 0
    }
}
```

#### 1.2 Java 版本

```java
package com.apress.proandroidmedia.ch1.cameraintent;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.widget.ImageView;

public class CameraIntent extends AppCompatActivity {

    private static final int CAMERA_RESULT = 0;

    private ImageView imv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(i, CAMERA_RESULT);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap bmp = (Bitmap) extras.get("data");
            imv = findViewById(R.id.ReturnedImageView);
            imv.setImageBitmap(bmp);
        }
    }
}
```

> 提示：使用上面的方法系统返回的图片是小尺寸图片。

### 2. 使用系统相机拍摄大图片

#### 2.1 通过 MediaStore 存储图片

> 提示：示例代码请查阅 <https://gitee.com/qtyresources/ProAndroidMedia>  中的 MediaStoreCameraIntent 示例程序。

##### 2.1.1 Kotlin 版本

```kotlin
package com.apress.proandroidmedia.ch1.mediastorecameraintent

import android.content.ContentValues
import android.content.Intent
import android.graphics.BitmapFactory
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.util.Log
import android.view.View
import android.widget.*

class MediaStoreCameraIntent : AppCompatActivity() {

    private var imageFileUri: Uri? = null

    // User interface elements, specified in res/layout/main.xml
    private lateinit var returnedImageView: ImageView
    private lateinit var takePictureButton: Button
    private lateinit var saveDataButton: Button
    private lateinit var titleTextView: TextView
    private lateinit var descriptionTextView: TextView
    private lateinit var titleEditText: EditText
    private lateinit var descriptionEditText: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Set the content view to be what is defined in teh res/layout/main.xml
        // file
        setContentView(R.layout.activity_main)

        // Get references to UI elements
        returnedImageView = findViewById(R.id.ReturnedImageView)
        takePictureButton = findViewById(R.id.TakePictureButton)
        saveDataButton = findViewById(R.id.SaveDataButton)
        titleTextView = findViewById(R.id.TitleTextView)
        descriptionTextView = findViewById(R.id.DescriptionTextView)
        titleEditText = findViewById(R.id.TitleEditText)
        descriptionEditText = findViewById(R.id.DescriptionEditText)

        // Set all except takePictureButton to not be visible initially
        // View.GONE is invisible and doesn't take up space in the layout
        returnedImageView.visibility = View.GONE
        saveDataButton.visibility = View.GONE
        titleTextView.visibility = View.GONE
        descriptionTextView.visibility = View.GONE
        titleEditText.visibility = View.GONE
        descriptionEditText.visibility = View.GONE

        // When the Take Picture Button is clicked
        takePictureButton.setOnClickListener(View.OnClickListener {
            // Add a new record without the bitmap
            // returns the URI of the new record
            imageFileUri = contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, ContentValues())

            // Start the Camera App
            val i = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            i.putExtra(MediaStore.EXTRA_OUTPUT, imageFileUri)
            startActivityForResult(i, CAMERA_RESULT)
        })

        saveDataButton.setOnClickListener(View.OnClickListener {
            // Update the MediaStore record with Title and Description
            val contentValues = ContentValues(3)
            contentValues.put(MediaStore.Images.Media.DISPLAY_NAME, titleEditText.text.toString())
            contentValues.put(MediaStore.Images.Media.DESCRIPTION, descriptionEditText.text.toString())
            imageFileUri?.let { uri -> contentResolver.update(uri, contentValues, null, null) }

            // Tell the user
            val bread = Toast.makeText(this@MediaStoreCameraIntent, "Record Updated", Toast.LENGTH_SHORT)
            bread.show()

            // Go back to the initial state, set Take Picture Button Visible
            // hide other UI elements
            takePictureButton.visibility = View.VISIBLE

            returnedImageView.visibility = View.GONE
            saveDataButton.visibility = View.GONE
            titleTextView.visibility = View.GONE
            descriptionTextView.visibility = View.GONE
            titleEditText.visibility = View.GONE
            descriptionEditText.visibility = View.GONE
        })
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (resultCode == RESULT_OK) {
            // The Camera App has returned

            // Hide the Take Picture Button
            takePictureButton.visibility = View.GONE

            // Show the other UI Elements
            returnedImageView.visibility = View.VISIBLE
            saveDataButton.visibility = View.VISIBLE
            titleTextView.visibility = View.VISIBLE
            descriptionTextView.visibility = View.VISIBLE
            titleEditText.visibility = View.VISIBLE
            descriptionEditText.visibility = View.VISIBLE

            // Scale the image
            val dw = 200;   // Make it at most 200 pixels wide
            val dh = 200;   // Make it at most 200 pixels tall

            // Load up the image's dimensions not the image itself
            val bmpFactoryOptions = BitmapFactory.Options()
            bmpFactoryOptions.inJustDecodeBounds = true
            imageFileUri?.let {
                var bmp = BitmapFactory.decodeStream(contentResolver.openInputStream(it), null, bmpFactoryOptions)

                val heightRatio = Math.ceil(bmpFactoryOptions.outHeight / dh.toDouble()).toInt()
                val widthRatio = Math.ceil(bmpFactoryOptions.outWidth / dw.toDouble()).toInt()

                Log.v(TAG, "$heightRatio")
                Log.v(TAG, "$widthRatio")

                // If both of the ratios are greater than 1,
                // one of the sides of the image is greater than the screen
                if (heightRatio > 1 && widthRatio > 1) {
                    if (heightRatio > widthRatio) {
                        // Height ratio is larger, scale according to it
                        bmpFactoryOptions.inSampleSize = heightRatio
                    } else {
                        // Width ratio is larger, scale according to it
                        bmpFactoryOptions.inSampleSize = widthRatio
                    }
                }

                // Decode it for real
                bmpFactoryOptions.inJustDecodeBounds = false
                bmp = BitmapFactory.decodeStream(contentResolver.openInputStream(it), null, bmpFactoryOptions)

                // Display it
                returnedImageView.setImageBitmap(bmp)
            }
        }
    }

    companion object {
        const val TAG = "MediaStoreCameraIntent"
        const val CAMERA_RESULT = 0
    }
}
```

##### 2.1.2 Java 版本

```java
package com.apress.proandroidmedia.ch1.mediastorecameraintent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.FileNotFoundException;

public class MediaStoreCameraIntent extends AppCompatActivity {

    private static final String TAG = "MediaStoreCameraIntent";

    private static final int CAMERA_RESULT = 0;

    private Uri imageFileUri;

    // User interface elements, specified in res/layout/main.xml
    private ImageView returnedImageView;
    private Button takePictureButton;
    private Button saveDataButton;
    private TextView titleTextView;
    private TextView descriptionTextView;
    private EditText titleEditText;
    private EditText descriptionEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Set the content view to be what is defined in the res/layout/main.xml
        // file
        setContentView(R.layout.activity_main);

        // Get references to UI elements
        returnedImageView = findViewById(R.id.ReturnedImageView);
        takePictureButton = findViewById(R.id.TakePictureButton);
        saveDataButton = findViewById(R.id.SaveDataButton);
        titleTextView = findViewById(R.id.TitleTextView);
        descriptionTextView = findViewById(R.id.DescriptionTextView);
        titleEditText = findViewById(R.id.TitleEditText);
        descriptionEditText = findViewById(R.id.DescriptionEditText);

        // Set all except takePictureButton to not be visible initially
        // View.GONE is invisible and doesn't take up space in the layout
        returnedImageView.setVisibility(View.GONE);
        saveDataButton.setVisibility(View.GONE);
        titleTextView.setVisibility(View.GONE);
        descriptionTextView.setVisibility(View.GONE);
        titleEditText.setVisibility(View.GONE);
        descriptionEditText.setVisibility(View.GONE);

        // When the Take Picture Button is clicked
        takePictureButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Add a new record without the bitmap
                // returns the URI of the new record
                imageFileUri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
                        new ContentValues());

                // Start the Camera App
                Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                i.putExtra(MediaStore.EXTRA_OUTPUT, imageFileUri);
                startActivityForResult(i, CAMERA_RESULT);
            }
        });

        saveDataButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Update the MediaStore record with Title and Description
                ContentValues contentValues = new ContentValues(3);
                contentValues.put(MediaStore.Images.Media.DISPLAY_NAME, titleEditText.getText().toString());
                contentValues.put(MediaStore.Images.Media.DESCRIPTION, descriptionEditText.getText().toString());
                getContentResolver().update(imageFileUri, contentValues, null, null);

                // Tell the user
                Toast.makeText(MediaStoreCameraIntent.this, "Record Updated", Toast.LENGTH_SHORT).show();

                // Go back to the initial state, set Take Picture Button Visible
                // hide other UI elements
                takePictureButton.setVisibility(View.VISIBLE);

                returnedImageView.setVisibility(View.GONE);
                saveDataButton.setVisibility(View.GONE);
                titleTextView.setVisibility(View.GONE);
                descriptionTextView.setVisibility(View.GONE);
                titleEditText.setVisibility(View.GONE);
                descriptionEditText.setVisibility(View.GONE);
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK) {
            // The Camera App has returned

            // Hide the Take Picture Button
            takePictureButton.setVisibility(View.GONE);

            returnedImageView.setVisibility(View.VISIBLE);
            saveDataButton.setVisibility(View.VISIBLE);
            titleTextView.setVisibility(View.VISIBLE);
            descriptionTextView.setVisibility(View.VISIBLE);
            titleEditText.setVisibility(View.VISIBLE);
            descriptionEditText.setVisibility(View.VISIBLE);

            // Scale the image
            int dw = 200;   // Make it at most 200 pixels wide
            int dh = 200;   // Make it at most 200 pixels tall

            try {
                // Load up the image's dimensions not the image itself
                BitmapFactory.Options bmpFactoryOptions = new BitmapFactory.Options();
                bmpFactoryOptions.inJustDecodeBounds = true;
                Bitmap bmp = BitmapFactory.decodeStream(getContentResolver().openInputStream(imageFileUri),
                        null, bmpFactoryOptions);

                int heightRatio = (int) Math.ceil(bmpFactoryOptions.outHeight / (double) dh);
                int widthRatio = (int) Math.ceil(bmpFactoryOptions.outWidth / (double) dw);

                Log.v(TAG, "" + heightRatio);
                Log.v(TAG, "" + widthRatio);

                // If both of the ratios are greater than 1,
                // one of the sides of the image is greater than the screen
                if (heightRatio > 1 && widthRatio > 1) {
                    if (heightRatio > widthRatio) {
                        // Height ratio is larger, scale according to it
                        bmpFactoryOptions.inSampleSize = heightRatio;
                    } else {
                        // Width ratio is larger, scale according to it
                        bmpFactoryOptions.inSampleSize = widthRatio;
                    }
                }

                // Decode it for real
                bmpFactoryOptions.inJustDecodeBounds = false;
                bmp = BitmapFactory.decodeStream(getContentResolver().openInputStream(imageFileUri),
                        null, bmpFactoryOptions);

                // Display it
                returnedImageView.setImageBitmap(bmp);
            } catch (FileNotFoundException e) {
                Log.e(TAG, "error: ", e);
            }
        }
    }
}
```

> 注意：上面的示例程序需要 `android.permission.WRITE_EXTERNAL_STORAGE` 权限。

#### 2.2 通过文件路径存储图片

> 提示：示例代码请查阅 <https://gitee.com/qtyresources/ProAndroidMedia>  中的 FileProviderCameraIntent 示例程序。

**file_paths.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <files-path
        name="files"
        path="/" />
    <cache-path
        name="cache"
        path="/" />
    <external-cache-path
        name="external_cache"
        path="/" />
    <external-files-path
        name="external_files"
        path="/" />
    <external-media-path
        name="external_media"
        path="/" />
    <external-path
        name="external"
        path="/" />
</paths>
```

**AndroidManifest.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.apress.proandroidmedia.ch1.fileprovidercameraintent">

    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.FileProviderCameraIntent">

        <provider
            android:authorities="com.apress.proandroidmedia.ch1.fileprovidercameraintent.FileProvider"
            android:name="androidx.core.content.FileProvider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>

        <activity android:name=".FileProviderCameraIntent">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

##### 2.2.1 Kotlin 版本

**FileProviderCameraIntent.kt**

```kotlin
package com.apress.proandroidmedia.ch1.fileprovidercameraintent

import android.content.ContentValues
import android.content.Intent
import android.graphics.BitmapFactory
import android.net.Uri
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.util.Log
import android.view.View
import android.widget.*
import androidx.core.content.FileProvider
import java.io.File
import java.io.FileInputStream

class FileProviderCameraIntent : AppCompatActivity() {

    private var imageFileUri: Uri? = null
    private lateinit var picturePath: String

    // User interface elements, specified in res/layout/main.xml
    private lateinit var returnedImageView: ImageView
    private lateinit var takePictureButton: Button
    private lateinit var saveDataButton: Button
    private lateinit var titleTextView: TextView
    private lateinit var descriptionTextView: TextView
    private lateinit var titleEditText: EditText
    private lateinit var descriptionEditText: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Set the content view to be what is defined in teh res/layout/main.xml
        // file
        setContentView(R.layout.activity_main)

        // Get references to UI elements
        returnedImageView = findViewById(R.id.ReturnedImageView)
        takePictureButton = findViewById(R.id.TakePictureButton)
        saveDataButton = findViewById(R.id.SaveDataButton)
        titleTextView = findViewById(R.id.TitleTextView)
        descriptionTextView = findViewById(R.id.DescriptionTextView)
        titleEditText = findViewById(R.id.TitleEditText)
        descriptionEditText = findViewById(R.id.DescriptionEditText)

        // Set all except takePictureButton to not be visible initially
        // View.GONE is invisible and doesn't take up space in the layout
        returnedImageView.visibility = View.GONE
        saveDataButton.visibility = View.GONE
        titleTextView.visibility = View.GONE
        descriptionTextView.visibility = View.GONE
        titleEditText.visibility = View.GONE
        descriptionEditText.visibility = View.GONE

        // When the Take Picture Button is clicked
        takePictureButton.setOnClickListener(View.OnClickListener {
            // Add a new record without the bitmap
            // returns the URI of the new record
            picturePath = getExternalFilesDir(Environment.DIRECTORY_PICTURES)?.absolutePath + File.separator + "test.jpg"
            if (Build.VERSION.SDK_INT >= 24) {
                imageFileUri = FileProvider.getUriForFile(this@FileProviderCameraIntent, "com.apress.proandroidmedia.ch1.fileprovidercameraintent.FileProvider", File(picturePath))
            } else {
                imageFileUri = Uri.fromFile(File(picturePath))
            }

            // Start the Camera App
            val i = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            i.putExtra(MediaStore.EXTRA_OUTPUT, imageFileUri)
            startActivityForResult(i, CAMERA_RESULT)
        })

        saveDataButton.setOnClickListener(View.OnClickListener {
            // Update the MediaStore record with Title and Description
            val contentValues = ContentValues(3)
            contentValues.put(MediaStore.Images.Media.DISPLAY_NAME, titleEditText.text.toString())
            contentValues.put(MediaStore.Images.Media.DESCRIPTION, descriptionEditText.text.toString())
            imageFileUri?.let { uri -> contentResolver.update(uri, contentValues, null, null) }

            // Tell the user
            val bread = Toast.makeText(this@FileProviderCameraIntent, "Record Updated", Toast.LENGTH_SHORT)
            bread.show()

            // Go back to the initial state, set Take Picture Button Visible
            // hide other UI elements
            takePictureButton.visibility = View.VISIBLE

            returnedImageView.visibility = View.GONE
            saveDataButton.visibility = View.GONE
            titleTextView.visibility = View.GONE
            descriptionTextView.visibility = View.GONE
            titleEditText.visibility = View.GONE
            descriptionEditText.visibility = View.GONE
        })
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (resultCode == RESULT_OK) {
            // The Camera App has returned

            // Hide the Take Picture Button
            takePictureButton.visibility = View.GONE

            // Show the other UI Elements
            returnedImageView.visibility = View.VISIBLE
            saveDataButton.visibility = View.VISIBLE
            titleTextView.visibility = View.VISIBLE
            descriptionTextView.visibility = View.VISIBLE
            titleEditText.visibility = View.VISIBLE
            descriptionEditText.visibility = View.VISIBLE

            // Scale the image
            val dw = 200;   // Make it at most 200 pixels wide
            val dh = 200;   // Make it at most 200 pixels tall

            // Load up the image's dimensions not the image itself
            val bmpFactoryOptions = BitmapFactory.Options()
            bmpFactoryOptions.inJustDecodeBounds = true
            imageFileUri?.let {
                var bmp = BitmapFactory.decodeStream(FileInputStream(picturePath), null, bmpFactoryOptions)

                val heightRatio = Math.ceil(bmpFactoryOptions.outHeight / dh.toDouble()).toInt()
                val widthRatio = Math.ceil(bmpFactoryOptions.outWidth / dw.toDouble()).toInt()

                Log.v(TAG, "$heightRatio")
                Log.v(TAG, "$widthRatio")

                // If both of the ratios are greater than 1,
                // one of the sides of the image is greater than the screen
                if (heightRatio > 1 && widthRatio > 1) {
                    if (heightRatio > widthRatio) {
                        // Height ratio is larger, scale according to it
                        bmpFactoryOptions.inSampleSize = heightRatio
                    } else {
                        // Width ratio is larger, scale according to it
                        bmpFactoryOptions.inSampleSize = widthRatio
                    }
                }

                // Decode it for real
                bmpFactoryOptions.inJustDecodeBounds = false
                bmp = BitmapFactory.decodeStream(FileInputStream(picturePath), null, bmpFactoryOptions)

                // Display it
                returnedImageView.setImageBitmap(bmp)
            }
        }
    }

    companion object {
        const val TAG = "MediaStoreCameraIntent"
        const val CAMERA_RESULT = 0
    }

}
```

##### 2.2.2 Java 版本

**FileProviderCameraIntent.java**

```java
package com.apress.proandroidmedia.ch1.fileprovidercameraintent;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.FileProvider;

import android.content.ContentValues;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class FileProviderCameraIntent extends AppCompatActivity {

    private static final String TAG = "FileProvider";

    private static final int CAMERA_RESULT = 0;

    private Uri imageFileUri;
    private String picturePath;

    // User interface elements, specified in res/layout/main.xml
    private ImageView returnedImageView;
    private Button takePictureButton;
    private Button saveDataButton;
    private TextView titleTextView;
    private TextView descriptionTextView;
    private EditText titleEditText;
    private EditText descriptionEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Set the content view to be what is defined in the res/layout/main.xml
        // file
        setContentView(R.layout.activity_main);

        // Get references to UI elements
        returnedImageView = findViewById(R.id.ReturnedImageView);
        takePictureButton = findViewById(R.id.TakePictureButton);
        saveDataButton = findViewById(R.id.SaveDataButton);
        titleTextView = findViewById(R.id.TitleTextView);
        descriptionTextView = findViewById(R.id.DescriptionTextView);
        titleEditText = findViewById(R.id.TitleEditText);
        descriptionEditText = findViewById(R.id.DescriptionEditText);

        // Set all except takePictureButton to not be visible initially
        // View.GONE is invisible and doesn't take up space in the layout
        returnedImageView.setVisibility(View.GONE);
        saveDataButton.setVisibility(View.GONE);
        titleTextView.setVisibility(View.GONE);
        descriptionTextView.setVisibility(View.GONE);
        titleEditText.setVisibility(View.GONE);
        descriptionEditText.setVisibility(View.GONE);

        // When the Take Picture Button is clicked
        takePictureButton.setOnClickListener(v -> {
            // Add a new record without the bitmap
            // returns the URI of the new record
            picturePath = getExternalFilesDir(Environment.DIRECTORY_PICTURES).getAbsolutePath() + File.separator + "test.jpg";
            if (Build.VERSION.SDK_INT >= 24) {
                imageFileUri = FileProvider.getUriForFile(FileProviderCameraIntent.this,
                        "com.apress.proandroidmedia.ch1.fileprovidercameraintent.FileProvider",
                        new File(picturePath));
            } else {
                imageFileUri = Uri.fromFile(new File(picturePath));
            }

            // Start the Camera App
            Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
            i.putExtra(MediaStore.EXTRA_OUTPUT, imageFileUri);
            startActivityForResult(i, CAMERA_RESULT);
        });

        saveDataButton.setOnClickListener(v -> {
            // Update the MediaStore record with Title and Description
            ContentValues contentValues = new ContentValues(3);
            contentValues.put(MediaStore.Images.Media.DISPLAY_NAME, titleEditText.getText().toString());
            contentValues.put(MediaStore.Images.Media.DESCRIPTION, descriptionEditText.getText().toString());
            getContentResolver().update(imageFileUri, contentValues, null, null);

            // Tell the user
            Toast.makeText(FileProviderCameraIntent.this, "Record Updated", Toast.LENGTH_SHORT).show();

            // Go back to the initial state, set Take Picture Button Visible
            // hide other UI elements
            takePictureButton.setVisibility(View.VISIBLE);

            returnedImageView.setVisibility(View.GONE);
            saveDataButton.setVisibility(View.GONE);
            titleTextView.setVisibility(View.GONE);
            descriptionTextView.setVisibility(View.GONE);
            titleEditText.setVisibility(View.GONE);
            descriptionEditText.setVisibility(View.GONE);
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK) {
            // The Camera App has returned

            // Hide the Take Picture Button
            takePictureButton.setVisibility(View.GONE);

            returnedImageView.setVisibility(View.VISIBLE);
            saveDataButton.setVisibility(View.VISIBLE);
            titleTextView.setVisibility(View.VISIBLE);
            descriptionTextView.setVisibility(View.VISIBLE);
            titleEditText.setVisibility(View.VISIBLE);
            descriptionEditText.setVisibility(View.VISIBLE);

            // Scale the image
            int dw = 200;   // Make it at most 200 pixels wide
            int dh = 200;   // Make it at most 200 pixels tall

            try {
                // Load up the image's dimensions not the image itself
                BitmapFactory.Options bmpFactoryOptions = new BitmapFactory.Options();
                bmpFactoryOptions.inJustDecodeBounds = true;
                Bitmap bmp = BitmapFactory.decodeStream(new FileInputStream(picturePath),
                        null, bmpFactoryOptions);

                int heightRatio = (int) Math.ceil(bmpFactoryOptions.outHeight / (double) dh);
                int widthRatio = (int) Math.ceil(bmpFactoryOptions.outWidth / (double) dw);

                Log.v(TAG, "" + heightRatio);
                Log.v(TAG, "" + widthRatio);

                // If both of the ratios are greater than 1,
                // one of the sides of the image is greater than the screen
                if (heightRatio > 1 && widthRatio > 1) {
                    // Height ratio is larger, scale according to it
                    // Width ratio is larger, scale according to it
                    bmpFactoryOptions.inSampleSize = Math.max(heightRatio, widthRatio);
                }

                // Decode it for real
                bmpFactoryOptions.inJustDecodeBounds = false;
                bmp = BitmapFactory.decodeStream(new FileInputStream(picturePath),
                        null, bmpFactoryOptions);

                // Display it
                returnedImageView.setImageBitmap(bmp);
            } catch (FileNotFoundException e) {
                Log.e(TAG, "error: ", e);
            }
        }
    }

}
```

