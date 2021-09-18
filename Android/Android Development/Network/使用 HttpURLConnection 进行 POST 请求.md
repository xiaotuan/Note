[toc]

### 1. Kotlin 版本

```kotlin
import java.io.*
import java.lang.StringBuilder
import java.net.HttpURLConnection
import java.net.URL

var result: String? = null
val url = URL("http://www.amazingrace.cn/logindemo")
val connection = url.openConnection() as HttpURLConnection

connection.apply {
    requestMethod = "POST"
    doOutput = true
    doInput = true
    useCaches = false
}

connection.connect()

val body = "username=$username&password=$password"
val writer = BufferedWriter(OutputStreamWriter(connection.outputStream))
writer.write(body)
writer.flush()
writer.close()

if (connection.responseCode == HttpURLConnection.HTTP_OK) {
    var sb = StringBuilder()
    var reader = BufferedReader(InputStreamReader(connection.inputStream))
    var line = reader.readLine()
    while (line != null) {
        sb.append(line)
        line = reader.readLine()
    }
    reader.close()
    result = sb.toString()
} else {
    result = "Status code other than HTTP 200 received"
}
connection.disconnect()
```

### 2. Java 版本

```java
import android.net.Uri;
import android.util.Log;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

String result = null;
URL url = new URL("http://www.amazingrace.cn/logindemo");
HttpURLConnection  connection = (HttpURLConnection) url.openConnection();

connection.setRequestMethod("POST");
connection.setDoInput(true);
connection.setDoOutput(true);
connection.setUseCaches(false);

connection.connect();

String body = "username=" + username + "&password=" + password;
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()));
bw.write(body);
bw.flush();
bw.close();

if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
    StringBuilder sb = new StringBuilder();
    BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
    String line = null;
    while ((line = br.readLine()) != null) {
        sb.append(line);
    }
    br.close();
    result = sb.toString();
} else {
    result = "Status code other than HTTP 200 received";
}
connection.disconnect();
```

