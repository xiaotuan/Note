[toc]

### 1. Kotlin 版本

```kotlin
import org.json.JSONObject

val sb = StringBuilder()
val users = JSONObject(sb.toString()).getJSONObject("users")
val jArray = users.getJSONArray("user")
val names = ArrayList<String>()
var i = 0
while (i < jArray.length()) {
    val jsonObject = jArray.getJSONObject(i)
    names.add(jsonObject.getString("name"))
    i++
}
```

### 2. Java 版本

```java
import org.json.JSONArray;
import org.json.JSONObject;

StringBuilder sb = new StringBuilder();
JSONObject users = new JSONObject(sb.toString()).getJSONObject("users");
JSONArray jArray = users.getJSONArray("user");
String[] names = new String[jArray.length()];
for (int i = 0; i < jArray.length(); i++) {
    JSONObject jsonObject = jArray.getJSONObject(i);
    names[i] = jsonObject.getString("name");
}
```

### 3. 要解析的 JSON 内容

```json
{
    users:{
        user:[
            {
                name:"Sheran",
                email:"sheranapress@gmail.com"
            },
            {
                name:"Kevin",
                email:"kevin@example.com"
            },
            {
                name:"Scott",
                email:"scott@example.com"
            }
        ]
    }
}'
```

