[toc]

### 1. 代码实现

**Kotlin 版本**

```kotlin

```

**Java 版本**

```java
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;

public class VideoViewDemo extends AppCompatActivity {

    /**
     * TODO: Set the path variable to a streaming video URL or a local media
     * file path.
     */
    private String path = "";
    private VideoView mVideoView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.videoview);
        mVideoView = findViewById(R.id.surface_view);

        if (path == "") {
            // Tell the user to provide a media file URL/path.
            Toast.makeText(this, "Please edit VideoViewDemo Activity, and set path" +
                    " variable to your media file URL/path", Toast.LENGTH_SHORT).show();
        } else {
            /*
             * Alternatively, for streaming media you can use
             * mVideoView.setVideoURI(Uri.parse(URLstring));
             */
            mVideoView.setVideoPath(path);
            mVideoView.setMediaController(new MediaController(this));
            mVideoView.requestFocus();
        }
    }
}
```

### 2. 布局文件

**videoview.xml**

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <VideoView
        android:id="@+id/surface_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</merge>
```

### 3. 所需权限

```xml
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

### 4. 注意事项

`VideoView` 并不能很好的处理视频的宽高，它只会按视频原始分辨率进行播放，如果屏幕分辨率与视频分辨率不匹配的话，它将会按照视频分辨率等比例进行缩放，直至视频能够在屏幕完全显示为止。也就是说，很多时候使用 `VideoView` 播放视频并不能填充满整个屏幕。