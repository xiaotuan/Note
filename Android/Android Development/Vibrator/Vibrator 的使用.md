[toc]

### 1. 获取 Vibrator 对象

#### 1.1 Kotlin 版本

```kotlin
import android.os.Build
import android.os.Vibrator
import android.os.VibratorManager
import android.os.VibrationEffect

val vibrator = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
  	(context.getSystemService(Context.VIBRATOR_MANAGER_SERVICE) as VibratorManager).defaultVibrator
} else {
		context.getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
}
```

### 2. 开始振动

#### 2.1 Kotlin 版本

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
  	vibrator.vibrate(VibrationEffect.createWaveform(longArrayOf(0, 1000, 0, 1000), 1))
} else {
  	vibrator.vibrate(longArrayOf(0, 1000, 0, 1000), 1)
}
```

### 3. 停止振动

#### 3.1 Kotlin 版本

```kotlin
vibrator.cancel()
```

