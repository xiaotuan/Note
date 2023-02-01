[toc]

### 1. 在 xml 中定义 ImageView

```xml
<ImageView
    android:id="@+id/image1"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:src="@drawable/icon" />

<ImageView
    android:id="@+id/image2"
    android:layout_width="125dp"
    android:layout_height="125dp"
    android:src="#555555" />

<ImageView
    android:id="@+id/image3"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />

<ImageView
    android:id="@+id/image4"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:maxWidth="35dp"
    android:maxHeight="50dp"
    android:scaleType="centerInside"
    android:src="@drawable/manatee02" />
```

### 2. 在代码中使用 ImageView

#### 2.1 Kotlin

```kotlin
import android.widget.ImageView

val imgView = findViewById<ImageView>(R.id.image3)

imgView.setImageResource(R.drawable.icon)

imgView.setImageBitmap(BitmapFactory.decodeResource(resources, R.drawable.manatee04))

imgView.setImageDrawable(Drawable.createFromPath("/mnt/sdcard/dave2.jpg"))

imgView.setImageURI(Uri.parse("file://mnt/sdcard/dave2.jpg"))
```

#### 2.2 Java

```java
import android.widget.ImageView;

ImageView imgView = (ImageView) findViewById(R.id.image3);

imgView.setImageResource(R.drawable.icon);

imgView.setImageBitmap(BitmapFactory.decodeResource(
  this.getResources(), R.drawable.manatee14));

imgView.setImageDrawable(
  Drawable.createFromPath("/mnt/sdcard/dave2.jpg"));

imgView.setImageURI(Uri.parse("file://mnt/sdcard/dave2.jpg"));
```

