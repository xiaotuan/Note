[toc]

### 1. 通过类名启动 Activity

**Kotlin 版本**

```kotlin
import android.content.Intent

val intent = Intent(this, OtherActivity::class.java)
startActivity(intent)
```

**Java 版本**

```java
import android.content.Intent;

Intent intent = new Intent(this, OtherActivity.class);
startActivity(intent);
```

### 2. 通过类路径启动 Activity

**Kotlin 版本**

```kotlin
import android.content.Intent
import android.content.ComponentName

val intent = Intent()
intent.component = ComponentName("com.qty.useresources", "com.qty.useresources.OtherActivity")
startActivity(intent)
```

**Java 版本**

```java
import android.content.Intent;
import android.content.ComponentName;

Intent intent = new Intent();
ComponentName cn = new ComponentName("com.qty.useresources", "com.qty.useresources.OtherActivity");
intent.setComponent(cn);
startActivity(intent);
```

### 3. 通过 Action 启动 Activity

**Kotlin 版本**

```kotlin
import android.content.Intent

val intent = Intent("com.qty.useresources.action.other")
startActivity(intent);
```

**Java 版本**

```java
import android.content.Intent;

Intent intent = new Intent("com.qty.useresources.action.other");
startActivity(intent);
```

> 注意：在 `AndroidManifest.xml` 中注册使用 `action` 启动的 `Activity` 时，不能只写 `action` 标签，而不写 `category` 标签，这样启动 `Activity` 时会报错的。正确的注册方式如下：
>
> ```xml
> <activity android:name=".OtherActivity">
>     <intent-filter>
>         <action android:name="com.qty.useresources.action.other" />
>         <category android:name="android.intent.category.DEFAULT" />
>     </intent-filter>
> </activity>
> ```

