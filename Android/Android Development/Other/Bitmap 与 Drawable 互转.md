[toc]

### 1. Kotlin

#### 1.1 Bitmap 转 Drawable

```kotlin
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.drawable.Drawable

fun drawableToBitmap(drawable: Drawable): Bitmap {
    val width = drawable.intrinsicWidth
    val height = drawable.intrinsicHeight
    val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
    val canvas = Canvas(bitmap)
    drawable.setBounds(0, 0, width, height)
    drawable.draw(canvas)
    return bitmap
}
```

#### 1.2 Drawable 转 Bitmap

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.graphics.drawable.BitmapDrawable
import android.graphics.drawable.Drawable

fun bitmapToDrawable(context: Context, bitmap: Bitmap): Drawable {
    return BitmapDrawable(context.resources, bitmap)
}
```

### 2. Java

#### 2.1 Bitmap 转 Drawable

```java
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.drawable.Drawable;

public Bitmap drawableToBitmap(Drawable drawable) {
    int width = drawable.getIntrinsicWidth();
    int height = drawable.getIntrinsicHeight();
    Bitmap bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);
    Canvas canvas = new Canvas(bitmap);
    drawable.setBounds(0, 0, width, height);
    drawable.draw(canvas);
    return bitmap;
}
```

#### 2.2 Drawable 转 Bitmap

```java
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;

public Drawable bitmapToDrawable(Context context, Bitmap bitmap) {
    BitmapDrawable drawable = new BitmapDrawable(context.getResources(), bitmap);
    return drawable;
}
```

