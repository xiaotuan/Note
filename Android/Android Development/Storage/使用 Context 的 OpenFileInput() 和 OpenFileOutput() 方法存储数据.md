可以使用 `Context` 对象的 `openFileInput()` 和 `openFileOutput()` 方法读取或存储数据，且不需要在 `AndroidManifester.xml` 文件中添加读写存储器权限。例如：

**Kotlin 版本**

```kotlin
fun get(context: Context): ByteArray {
    var bytesRead = 0
    val fis = context.openFileInput(file)
    val bos = ByteArrayOutputStream()
    val b = ByteArray(1024)
    bytesRead = fis.read(b)
    while (bytesRead != -1) {
        bos.write(b, 0, bytesRead)
        bytesRead = fis.read(b)
    }
    return bos.toByteArray()
}

fun storeData(data: ByteArray, context: Context) {
    val fos = context.openFileOutput(file, Context.MODE_PRIVATE)
    fos.write(data)
    fos.flush()
    fos.close()
}
```

**Java 版本**

```java
public static byte[] get(Context context) {
    byte[] data = null;
    try {
        int bytesRead = 0;
        FileInputStream fis = context.openFileInput(FILE);
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        byte[] b = new byte[1024];
        while ((bytesRead = fis.read(b)) != -1) {
            bos.write(b, 0, bytesRead);
        }
        data = bos.toByteArray();
    } catch (FileNotFoundException e) {
        Log.e(TAG, "get=>error: ", e);
    } catch (IOException e) {
        Log.e(TAG, "get=>error: ", e);
    }
    return data;
}

public static void storeData(byte[] data, Context context) {
    try {
        FileOutputStream fos = context.openFileOutput(FILE, Context.MODE_PRIVATE);
        fos.write(data);
        fos.flush();
        fos.close();
    } catch (FileNotFoundException e) {
        Log.e(TAG, "storeData=>error: ", e);
    } catch (IOException e) {
        Log.e(TAG, "storeData=>error: ", e);
    }
}
```

