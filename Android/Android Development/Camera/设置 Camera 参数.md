[toc]

### 1. 设置 Camera 参数代码范例

#### 1.1 Kotlin 版本

```kotlin
val parameters = camera.parameters
parameters["some parameter"] = "some value"
// or
parameters["some parameter"] = some_int
camera.parameters = parameters
```

#### 1.2 Java 版本

```java
Camera.Parameters parameters = camera.getParameters();
parameters.set("some parameter", "some value");
// or
parameters.set("some parameter", some_int);
camera.setParameters(parameters);
```

> 注意：设置 Camera 参数应该在 `surfaceCreated()` 方法中执行。

### 2. 设置 Camera 的方向

#### 2.1 Kotlin 版本

```kotlin
// Android SDK_INT 5 (Android 2.0) 以下
// 可用值 "portrait"，"landscape"
parameters["orientation"] = "portrait"
// Android SDK_INT 5 (Android 2.0) 以上
// 可用值 0，90,180，270
parameters.setRotation(90)
// Android SDK_INT 7 (Android 2.2) 以上
// 可用值 0，90,180，270
parameters.setDisplayOrientation(90)
```

#### 2.2 Java 版本

```java
// Android SDK_INT 5 (Android 2.0) 以下
// 可用值 "portrait"，"landscape"
parameters.set("orientation", "portrait");
// Android SDK_INT 5 (Android 2.0) 以上
// 可用值 0，90,180，270
parameters.setRotation(90);
// Android SDK_INT 7 (Android 2.2) 以上
// 可用值 0，90,180，270
parameters.setDisplayOrientation(90);
```

### 3. 设置闪光灯模式

#### 3.1 Kotlin 版本

```kotlin
parameters.flashMode = Camera.Parameters.FLASH_MODE_AUT
```

#### 3.2 Java 版本

```java
parameters.setFlashMode(Camera.Parameters.FLASH_MODE_AUTO);
```

闪光灯模式有如下几种：

+ `FLASH_MODE_OFF`：闪光灯不会被触发。
+ `FLASH_MODE_AUTO`：需要时会自动触发闪光灯。 闪光灯可能会在预览、自动对焦或拍照期间闪光，具体取决于驱动程序。
+ `FLASH_MODE_ON`：在拍照期间将始终触发 Flash。 根据驱动程序，闪光灯也可能在预览或自动对焦期间闪光。
+ `FLASH_MODE_RED_EYE`：闪光灯将在减轻红眼模式下闪光。
+ `FLASH_MODE_TORCH`：在预览、自动对焦和拍照期间持续发光。 这也可以用于视频录制。

### 4. 设置相机颜色效果

#### 4.1 Kotlin 版本

```kotlin
parameters.colorEffect = Camera.Parameters.EFFECT_SOLARIZE
```

#### 4.2 Java 版本

```java
parameters.setColorEffect(Camera.Parameters.EFFECT_SOLARIZE);
```

> 注意：在设置相机颜色效果前，必须先判断相机是否支持该效果。例如：
>
> **Kotlin 版本**
>
> ```kotlin
> val colorEffects = parameters.supportedColorEffects
> val iterable = colorEffects.iterator()
> while (iterable.hasNext()) {
>     val currentEffect = iterable.next()
>     if (currentEffect.equals(Camera.Parameters.EFFECT_SOLARIZE)) {
>         parameters.colorEffect = Camera.Parameters.EFFECT_SOLARIZE
>         break
>     }
> }
> ```
>
> **Java 版本**
>
> ```java
> List<String> colorEffects = parameters.getSupportedColorEffects();
> Iterator<String> cei = colorEffects.iterator();
> while (cei.hasNext()) {
>     String currentEffect =cei.next();
>     if (currentEffect.equals(Camera.Parameters.EFFECT_SOLARIZE)) {
>         parameters.setColorEffect(Camera.Parameters.EFFECT_SOLARIZE);
>         break;
>     }
> }
> ```

颜色模式有如下几种：

+ `EFFECT_NONE`
+ `EFFECT_MONO`
+ `EFFECT_NEGATIVE`
+ `EFFECT_SOLARIZE`
+ `EFFECT_SEPIA`
+ `EFFECT_POSTERIZE`
+ `EFFECT_WHITEBOARD`
+ `EFFECT_BLACKBOARD`
+ `EFFECT_AQUA`

### 5. 设置相机预览尺寸

#### 5.1 Kotlin 版本

```kotlin
parameters.setPictureSize(1080, 1920)
```

#### 5.2 Java 版本

```java
parameters.setPictureSize(1080, 1920);
```

> 注意：在设置相机预览尺寸时，必须先判断该尺寸相机是否支持。例如：
>
> **Kotlin 版本**
>
> ```kotlin
> var bestWidth = 0
> var bestHeight = 0
> val previewSizes = parameters.supportedPreviewSizes
> if (previewSizes.size > 1) {
>     val cei = previewSizes.iterator()
>     while (cei.hasNext()) {
>         val aSize = cei.next()
>         Log.d(TAG, "Checking ${aSize.width} x ${aSize.height}")
>         if (aSize.width > bestWidth && aSize.width <= LARGEST_WIDTH
>             && aSize.width > bestHeight && aSize.height <= LARGEST_HEIGHT) {
>             // So far it is the biggest without going over the screen dimensions
>             bestWidth = aSize.width
>             bestHeight = aSize.height
>         }
>     }
> }
> if (bestWidth != 0 && bestHeight != 0) {
>     Log.d(TAG, "Using $bestWidth x $bestHeight")
>     parameters.setPreviewSize(bestWidth, bestHeight)
> }
> ```
>
> **Java 版本**
>
> ```java
> int bestWidth = 0;
> int bestHeight = 0;
> List<Camera.Size> previewSizes = parameters.getSupportedPreviewSizes();
> if (previewSizes.size() > 1) {
>     Iterator<Camera.Size> cei = previewSizes.iterator();
>     while (cei.hasNext()) {
>         Camera.Size aSize = cei.next();
>         Log.d(TAG, "Checking " + aSize.width + " x " + aSize.height);
>         if (aSize.width > bestWidth && aSize.width <= LARGEST_WIDTH
>             && aSize.height > bestHeight && aSize.height <= LARGEST_HEIGHT) {
>             // So far it is the biggest without going over the screen dimensions
>             bestWidth = aSize.width;
>             bestHeight = aSize.height;
>         }
>     }
> }
> if (bestWidth != 0 && bestHeight != 0) {
>     Log.d(TAG, "Using " + bestWidth + " x " + bestHeight);
>     parameters.setPreviewSize(bestWidth, bestHeight);
> }
> ```

