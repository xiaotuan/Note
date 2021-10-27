[toc]

### 1. Kotlin 版本

```kotlin
try {
    val baidu = URL("https://www.baidu.com/")
    val connection = baidu.openConnection() as HttpURLConnection
    connection.requestMethod = "GET"
    connection.useCaches = false
    connection.doInput = true
    connection.doOutput = false
    connection.connect()
    Log.d(TAG, "start=>response code: ${connection.responseCode}")
    if (connection.responseCode == HttpURLConnection.HTTP_OK) {
      val sb = StringBuilder()
      val reader = BufferedReader(InputStreamReader(connection.inputStream))
      var line = reader.readLine()
      while (line != null) {
        sb.append(line)
        line = reader.readLine()
      }
      Log.d(TAG, "start=>response: $sb")
    }
    connection.disconnect()
} catch (e: Exception) {
  	Log.e(TAG, "error: $e")
}
```

