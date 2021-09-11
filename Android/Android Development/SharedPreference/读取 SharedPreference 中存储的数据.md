读取 `SharedPreferences` 中存储的数据的代码如下所示：

**Kotlin 版本**

```kotlin
val hostname = "hostname"
val port = "port"
val ssl = "ssl"

val data = Hashtable<String, Any?>()
val prefs = PreferenceManager.getDefaultSharedPreferences(context)
data[hostname] = prefs.getString(hostname, null)
data[port] = prefs.getInt(port, 0)
data[ssl] = prefs.getBoolean(ssl, true)
```

**Java 版本**

```java
String hostname = "hostname";
String port = "port";
String ssl = "ssl";

Hashtable<String, Object> data = new Hashtable<>();
SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(ctx);
data.put(hostname, prefs.getString(hostname, null));
data.put(port, prefs.getInt(port, 0));
data.put(ssl, prefs.getBoolean(ssl, true));
```

