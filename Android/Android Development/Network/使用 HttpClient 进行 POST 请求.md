[toc]

### 1. Kotlin 版本

```kotlin
import org.apache.http.NameValuePair
import org.apache.http.client.entity.UrlEncodedFormEntity
import org.apache.http.client.methods.HttpPost
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.message.BasicNameValuePair
import org.apache.http.util.EntityUtils
import org.json.JSONObject

val httpClient = DefaultHttpClient()
val post = HttpPost(httpReqPost)
// 设置请求头
post.addHeader("Authorization", "Bearer " + accessToken);
val nvPairs = ArrayList<NameValuePair>()
nvPairs.add(clientId)
nvPairs.add(clientSecret)
nvPairs.add(BasicNameValuePair("code", token.getAuthCode()))
nvPairs.add(redirectURI)
nvPairs.add(BasicNameValuePair("grant_type", "authorization_code"))
try {
    // 设置请求体
    post.entity = UrlEncodedFormEntity(nvPairs)
    val response = httpClient.execute(post)
    val line = EntityUtils.toString(response.entity)
    val jObj = JSONObject(line)
    token.buildToken(jObj)
    writeToken(token)
} catch (e: IOException) {
    Log.e(TAG, "getRequestToken=>error: ", e)
    if (e.message =="No peer certificate") {
        Toast.makeText(act, "Possible HTC Error for Android 2.3.3", Toast.LENGTH_SHORT).show()
    }
} catch (e: Exception) {
    Log.e(TAG, "getRequestToken=>error: ", e)
}
```

### 2. Java 版本

```java
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

HttpClient httpClient = new DefaultHttpClient();
HttpPost post = new HttpPost(httpReqPost);
// 设置请求头
post.addHeader("Authorization", "Bearer " + accessToken);
List<NameValuePair> nvPairs = new ArrayList<NameValuePair>();
nvPairs.add(clientId);
nvPairs.add(clientSecret);
nvPairs.add(new BasicNameValuePair("code", token.getAuthCode()));
nvPairs.add(redirectURI);
nvPairs.add(new BasicNameValuePair("grant_type", "authorization_code"));
try {
    // 设置请求体
    post.setEntity(new UrlEncodedFormEntity(nvPairs));
    HttpResponse response = httpClient.execute(post);
    HttpEntity httpEntity = response.getEntity();
    String line = EntityUtils.toString(httpEntity);
    JSONObject jObj = new JSONObject(line);
    token.buildToken(jObj);
    writeToken(token);
} catch (UnsupportedEncodingException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} catch (ClientProtocolException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} catch (IOException e) {
    if (e.getMessage().equals("No peer certificate")) {
        Toast .makeText(activity.getApplicationContext(),
                        "Possible HTC Error for Android 2.3.3",
                        Toast.LENGTH_SHORT).show();
    }
    Log.e("OAUTH", "IOException " + e.getMessage());
} catch (JSONException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

