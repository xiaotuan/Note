[toc]

### 1. Camera.PreviewCallback

定义一个方法 `onPreviewFrame(byte[] data, Camera camera)` ，当预览帧可用时调用该方法。 可以传入保存图像当前像素的字节数组。可以通过三种不同的方式在 Camera 对象上使用此回调。

+ `setPreviewCallback(Camera.PreviewCallback)`：使用此方法注册 `Camera.PreviewCallback` 可确保只要有新的预览帧可用并显示在屏幕上，就会调用 `onPreviewFrame` 方法。 传递到 `onPreviewFrame` 方法的数据字节数组很可能是 YUV 格式。 不幸的是，`Android 2.2` 是第一个拥有 YUV 格式解码器（YuvImage）的版本； 在以前的版本中，解码必须手动完成
+ `setOneShotPreviewCallback(Camera.PreviewCallback)`：在 `Camera` 对象上使用此方法注册 `Camera.PreviewCallback` 会导致在下一个预览图像可用时调用一次 `onPreviewFrame`。 同样，传递给 `onPreviewFrame` 方法的预览图像数据很可能是 YUV 格式。 这可以通过 `Camera.getParameters().getPreviewFormat()` 来获取 ImageFormat 值。
+ `setPreviewCallbackWithBuffer(Camera.PreviewCallback)`：在 `Android 2.2` 中引入，此方法与普通 `setPreviewCallback` 的工作方式相同，但需要我们指定一个字节数组，该数组将用作预览图像数据的缓冲区。 这样做是为了让我们能够更好地管理处理预览图像时将使用的内存。

### 2. Camera.ErrorCallback

定义一个 `onError` 方法，当发生 Camera 错误时调用该方法。 有两个常量可以与传入的错误代码进行比较：`CAMERA_ERROR_UNKNOWN` 和 `CAMERA_ERROR_SERVER_DIED`。

### 3. Camera.AutoFocusCallback

定义一个方法 `onAutoFocus`，当自动聚焦活动完成时调用该方法。 可以通过调用 `Camera` 对象上的 `autoFocus` 方法，传入此回调接口的实例来触发自动对焦。

### 4. Camera.ShutterCallback

定义一个方法 `onShutter`，在捕获图像时调用该方法。

