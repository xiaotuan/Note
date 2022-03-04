[toc]

### 1. 不传递任何参数启动拍照 ACTION

> 注意：
>
> 该方法获取到的图片是压缩过的图片，大小不超过 50k。

#### 1.1 启动拍照应用

##### 1.1.1 Kotlin

```kotlin
import android.content.Intent
import android.provider.MediaStore

val i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
startActivityForResult(i, 0);
```

##### 1.1.2 Java

```java
import android.content.Intent;
import android.provider.MediaStore;

Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
startActivityForResult(i, 0);
```

#### 1.2 获取图片

##### 1.2.1 Kotlin

```kotlin
import android.graphics.Bitmap
import android.content.Intent
import android.widget.*

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    if (requestCode == 0 && resultCode == RESULT_OK) {
        // Now we know that our myPicture Uri
        // refers to the image just take
        data?.apply { 
            val bitmap = extras?.get("data") as Bitmap
            val iv = findViewById<ImageView>(R.id.iv)
            iv.setImageBitmap(bitmap)
        }
    }
}
```

##### 1.2.2 Java

```java
import android.graphics.Bitmap;
import android.content.Intent;
import android.widget.ImageView;

@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == 0 && resultCode == RESULT_OK) {
        // Now we know that our myPicture Uri
        // refers to the image just taken
        Bitmap bitmap = (Bitmap) data.getExtras().get("data");
        ImageView iv = findViewById(R.id.iv);
        iv.setImageBitmap(bitmap);
    }
}
```

### 2. 带参数启动拍照 ACTION

#### 2.1 启动拍照应用

> 注意
>
> 如果 ContentValues 设置 DATA 栏指定照片存储文件：
>
> ```
> values.put(MediaStore.Images.Media.DATA, imageFile);
> ```
>
> 则必须确保该文件不存在，否则拍照失败。

##### 2.1 kotlin

```kotlin
import android.content.ContentValues
import android.content.Intent
import android.os.Environment
import android.provider.MediaStore
import android.util.Log

val imageFile = Environment.getExternalStorageDirectory().absolutePath + "/myPicture1.jpg"
val values = ContentValues()
values.put(MediaStore.Images.Media.TITLE, "My demo image")
values.put(MediaStore.Images.Media.DESCRIPTION, "Image Captured by Camera via an Intent")
values.put(MediaStore.Images.Media.DATA, imageFile)
myPicture = contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)

val i = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
i.putExtra(MediaStore.EXTRA_OUTPUT, myPicture)
startActivityForResult(i, 0)
```

##### 2.2 Java

```java
import android.content.ContentValues;
import android.content.Intent;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
    
String imageFile = Environment.getExternalStorageDirectory().getAbsolutePath() + "/myPicture.jpg";
ContentValues values = new ContentValues();
values.put(MediaStore.Images.Media.TITLE, "My demo image");
values.put(MediaStore.Images.Media.DESCRIPTION, "Image Captured by Camera via an Intent");
// 指定照片保存文件（可以不指定）
values.put(MediaStore.Images.Media.DATA, imageFile);
myPicture = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values);

Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
i.putExtra(MediaStore.EXTRA_OUTPUT, myPicture);
startActivityForResult(i, 0);
```

#### 2. 获取照片

在 Activity  的 onActivityResult() 方法中获取拍好的图片。

##### 2.1 Kotlin

```kotlin
import android.content.Intent
import android.graphics.BitmapFactory
import android.provider.MediaStore
import android.widget.*

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    if (requestCode == 0 && resultCode == RESULT_OK) {
        // Now we know that our myPicture Uri
        // refers to the image just take
        myPicture?.let {
            val cursor = contentResolver.query(it, arrayOf(MediaStore.Images.Media.DATA)
                                               , null, null, null, null)
            cursor?.apply {
                val columnIndex = getColumnIndex(MediaStore.Images.Media.DATA)
                if (moveToFirst()) {
                    val filePath = getString(columnIndex)
                    val bitmap = BitmapFactory.decodeFile(filePath)
                    val iv = findViewById<ImageView>(R.id.iv)
                    iv.setImageBitmap(bitmap)
                }
            }
        }
    }
}
```

##### 2.2 Java

```java
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.provider.MediaStore;
import android.util.Log;
import android.widget.ImageView;

@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == 0 && resultCode == RESULT_OK) {
        // Now we know that our myPicture Uri
        // refers to the image just taken
        Cursor cursor = getContentResolver().query(myPicture, new String[]{MediaStore.Images.Media.DATA},
                                                   null, null, null, null);
        int columnIndex = cursor.getColumnIndex(MediaStore.Images.Media.DATA);
        if (cursor.moveToFirst()) {
            String filePath = cursor.getString(columnIndex);
            Bitmap bitmap = BitmapFactory.decodeFile(filePath);
            ImageView iv = findViewById(R.id.iv);
            iv.setImageBitmap(bitmap);
        }
        cursor.close();
    }
}
```

