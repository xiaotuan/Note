[toc]

> 提示：完整工程请看 <https://gitee.com/qtyresources/android-apps-security/tree/master/Chapter08>

### 1. Kotlin 版本

#### 1.1 AuthActivity.kt

```kotlin
package net.zenconsult.android

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.webkit.WebView
import org.apache.http.message.BasicNameValuePair
import java.lang.Exception
import java.net.URI

class AuthActivity : AppCompatActivity() {

    private val clientId = BasicNameValuePair("client_id", "200744748489.apps.googleusercontent.com")
    private val clientSecret = BasicNameValuePair("client_secret", "edxCTl_L8_SFl1rz2klZ4DbB")
    private val redirectURI = BasicNameValuePair("redirect_uri", "urn:ietf:wg:oauth:2.0:oob")
    private val scope = "scope=https://picasaweb.google.com/data/"
    private val oAuth = "https://accounts.google.com/o/oauth2/auth?"
    private val httpReqPost = "https://accounts.google.com/o/oauth2/token"
    private val FILENAME = ".oauth_settings"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_auth)
        doAuth()
    }

    private fun doAuth() {
        try {
            val uri = URI("$oAuth$clientId&$redirectURI&$scope&response_type=code")
            val wv = findViewById<WebView>(R.id.webview)
            wv.webChromeClient = ClientHandler(this)
            wv.webViewClient = MWebClient()
            wv.settings.javaScriptEnabled = true
            wv.loadUrl(uri.toASCIIString())
            Log.v(TAG, "Calling ${uri.toASCIIString()}")
        } catch (e: Exception) {
            Log.e(TAG, "doAuth=>error: ", e)
        }
    }

    companion object {
        const val TAG = "AuthActivity"
    }
}
```

#### 1.2 ClientHandler.kt

```kotlin
package net.zenconsult.android

import android.app.Activity
import android.util.Log
import android.webkit.WebChromeClient
import android.webkit.WebView
import android.widget.Toast

class ClientHandler(
    private val activity: Activity,
): WebChromeClient() {

    private val oAuth = OAuth(activity)

    override fun onReceivedTitle(view: WebView?, title: String?) {
        var code = ""
        title?.let {
            if (it.contains("Success")) {
                code = title.substring(title.indexOf("=") + 1, it.length)
                setAuthCode(code)
                Log.v(TAG, "onReceivedTitle=>Code is $code")
                oAuth.getRequestToken()
                oAuth.writeToken(oAuth.getToken())
                Toast.makeText(activity.applicationContext, "Authorization Successful", Toast.LENGTH_SHORT).show()
                activity.finish()
            } else if (it.contains("Denied")) {
                code = it.substring(it.indexOf("=") + 1, it.length)
                setAuthCode(code)
                Log.v(TAG, "Denied, error was $code")
                Toast.makeText(activity, "Authorization Failed", Toast.LENGTH_SHORT).show()
                activity.finish()
            }
        }
    }

    override fun onProgressChanged(view: WebView?, newProgress: Int) {
        super.onProgressChanged(view, newProgress)
    }

    public fun getAuthCode(): String {
        return oAuth.getToken().getAuthCode()
    }

    public fun setAuthCode(authCode: String) {
        oAuth.getToken().setAuthCode(authCode)
    }

    companion object {
        const val TAG = "ClientHandler"
    }
}
```

#### 1.3 DataFetcher.kt

```kotlin
package net.zenconsult.android

import android.util.Log
import org.apache.http.client.methods.HttpGet
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.util.EntityUtils
import java.lang.Exception

class DataFetcher(
    private val token: Token
) {

    private val httpClient = DefaultHttpClient();

    public fun fetchAlbums(userId: String) {
        val url = "https://picasaweb.google.com/data/feed/api/user/$userId"
        try {
            val resp = httpClient.execute(buildGet(token.getAccessToken(), url))
            if (resp.statusLine.statusCode == 200) {
                val line = EntityUtils.toString(resp.entity)
                // Do your XML Parsing here
            }
        } catch (e: Exception) {
            Log.e(TAG, "fetchAlbums=>error: ", e)
        }
    }

    private fun buildGet(accessToken: String, url: String): HttpGet {
        val get = HttpGet(url)
        get.addHeader("Authorization", "Bearer " + accessToken)
        return get
    }

    companion object {
        const val TAG = "DataFetcher"
    }
}
```

#### 1.4 MWebClient.kt

```kotlin
package net.zenconsult.android

import android.webkit.WebView
import android.webkit.WebViewClient

class MWebClient: WebViewClient() {

    override fun onPageFinished(view: WebView?, url: String?) {
        super.onPageFinished(view, url)
    }
}
```

#### 1.5 OAuth.kt

```kotlin
package net.zenconsult.android

import android.app.Activity
import android.content.Context
import android.util.Log
import android.widget.Toast
import org.apache.http.NameValuePair
import org.apache.http.client.entity.UrlEncodedFormEntity
import org.apache.http.client.methods.HttpPost
import org.apache.http.client.methods.HttpUriRequest
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.message.BasicNameValuePair
import org.apache.http.util.EntityUtils
import org.json.JSONObject
import java.io.*
import java.lang.Exception
import java.net.URI

class OAuth(
    private val act: Activity
) {

    private val clientId = BasicNameValuePair("client_id", "200744748489.apps.googleusercontent.com")
    private val clientSecret = BasicNameValuePair("client_secret", "edxCTl_L8_SFl1rz2klZ4DbB")
    private val redirectURI = BasicNameValuePair("redirect_uri", "urn:ietf:wg:oauth:2.0:oob")
    private val httpReqPost = "https://accounts.google.com/o/oauth2/token"
    private var token = readToken()

    public fun readToken(): Token {
        var token = Token()
        var fis: FileInputStream? = null
        try {
            fis = act.openFileInput(FILENAME)
            fis?.let {
                val ois = ObjectInputStream(BufferedInputStream(it))
                token = ois.readObject() as Token
                if (token == null) {
                    token = Token()
                    writeToken(token)
                }
                ois.close()
            }
        } catch (e: FileNotFoundException) {
            Log.e(TAG, "readToken=>error: ", e)
            writeToken(Token())
        } catch (e: Exception) {
            Log.e(TAG, "readToken=>error: ", e)
        } finally {
            fis?.close()
        }
        return token
    }

    public fun writeToken(token: Token) {
        try {
            val f = File(FILENAME)
            if (f.exists()) {
                f.delete()
            }
            val fos = act.openFileOutput(FILENAME, Context.MODE_PRIVATE)

            val out = ObjectOutputStream(BufferedOutputStream(fos))
            out.writeObject(token)
            out.close()
            fos.close()
        } catch (e: FileNotFoundException) {
            Log.e(TAG, "Error creating settings file")
        } catch (e: Exception) {
            Log.e(TAG, "writeToken=>error: ", e)
        }
    }

    public fun getRequestToken() {
        val httpClient = DefaultHttpClient()
        val post = HttpPost(httpReqPost)
        val nvPairs = ArrayList<NameValuePair>()
        nvPairs.add(clientId)
        nvPairs.add(clientSecret)
        nvPairs.add(BasicNameValuePair("code", token.getAuthCode()))
        nvPairs.add(redirectURI)
        nvPairs.add(BasicNameValuePair("grant_type", "authorization_code"))
        try {
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
    }

    public fun getToken(): Token {
        return token
    }

    public fun setToken(token: Token) {
        this.token = token
    }

    companion object {
        const val TAG = "OAuth"
        const val FILENAME = ".oauth_settings"
    }
}
```

#### 1.6 OAuthPicasaActivity.kt

```kotlin
package net.zenconsult.android

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.ListView
import android.widget.TextView
import android.widget.Toast

class OAuthPicasaActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val lv = findViewById<ListView>(android.R.id.list)

        Thread {
            val o = OAuth(this)
            val t = o.getToken()

            if (!t.isValidForReq()) {
                val intent = Intent(this, AuthActivity::class.java)
                startActivity(intent)
            }

            if (t.isExpired()) {
                o.getRequestToken()
            }

            val df = DataFetcher(t)
            df.fetchAlbums("sheranapress")
            val names = ArrayList<String>() // Add bridge code here to parse XML from DataFetcher and populate your List

            runOnUiThread {
                lv.adapter = ArrayAdapter<String>(this, R.layout.list_item, names)

                lv.isTextFilterEnabled = true

                lv.setOnItemClickListener { _, view, _, _ ->
                    Toast.makeText(applicationContext, (view as TextView).text, Toast.LENGTH_SHORT).show()
                }
            }
        }.start()
    }
}
```

#### 1.7 Token.kt

```kotlin
package net.zenconsult.android

import org.json.JSONException
import org.json.JSONObject
import java.io.Serializable
import java.util.*

class Token(
    private var refreshToken: String = "",
    private var accessToken: String = "",
    private var expiryDate: Calendar = Calendar.getInstance(),
    private var authCode: String = "",
    private var tokenType: String = "",
    private var name: String = ""
): Serializable {

    constructor(response: JSONObject): this() {
        try {
            setExpiryDate(response.getInt("expires_in"))
        } catch (e: JSONException) {
            setExpiryDate(0)
        }
        tokenType = try {
            response.getString("token_type")
        } catch (e: JSONException) {
            ""
        }
        accessToken = try {
            response.getString("access_token")
        } catch (e: JSONException) {
            ""
        }
        refreshToken = try {
            response.getString("refresh_token")
        } catch (e: JSONException) {
            ""
        }
    }

    public fun buildToken(response: JSONObject) {
        try {
            setExpiryDate(response.getInt("expires_in"))
        } catch (e: JSONException) {
            setExpiryDate(0)
        }
        tokenType = try {
            response.getString("token_type")
        } catch (e: JSONException) {
            ""
        }
        accessToken = try {
            response.getString("access_token")
        } catch (e: JSONException) {
            ""
        }
        refreshToken = try {
            response.getString("refresh_token")
        } catch (e: JSONException) {
            ""
        }
    }

    public fun getExpiryDate(): Calendar {
        return expiryDate
    }

    public fun setExpiryDate(seconds: Int) {
        val now = Calendar.getInstance()
        now.add(Calendar.SECOND, seconds)
        expiryDate = now
    }

    public fun isValidForReq(): Boolean {
        return (accessToken != null && accessToken != "")
    }

    public fun isExpired(): Boolean {
        return Calendar.getInstance().after(expiryDate)
    }

    public fun getRefreshToken(): String {
        return refreshToken
    }

    public fun setRefreshToken(refreshToken: String?) {
        this.refreshToken = refreshToken ?: ""
    }

    public fun getAccessToken(): String {
        return accessToken
    }

    public fun setAccessToken(accessToken: String) {
        this.accessToken = accessToken
    }

    public fun getAuthCode(): String {
        return authCode
    }

    public fun setAuthCode(authCode: String?) {
        this.authCode = authCode ?: ""
    }

    public fun getTokenType(): String {
        return tokenType
    }

    public fun setTokenType(tokenType: String?) {
        this.tokenType = tokenType ?: ""
    }

    public fun getName(): String {
        return name
    }

    public fun setName(name: String) {
        this.name = name
    }

    companion object {
        const val serialVersionUID = 6534067628631656760L
    }
}
```

### 2. Java 版本

#### 2.1 AuthActivity.java

```java
package net.zenconsult.android;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.webkit.WebView;

import org.apache.http.message.BasicNameValuePair;

import java.net.URI;
import java.net.URISyntaxException;

public class AuthActivity extends AppCompatActivity {

    private BasicNameValuePair clientId = new BasicNameValuePair("client_id",
            "200744748489.apps.googleusercontent.com");
    private BasicNameValuePair clientSecret = new BasicNameValuePair("client_secret",
            "edxCTl_L8_SFl1rz2klZ4DbB");
    private BasicNameValuePair redirectURI = new BasicNameValuePair("redirect_uri",
            "urn:ietf:wg:oauth:2.0:oob");
    private String scope = "scope=https://picasaweb.google.com/data/";
    private String oAuth = "https://accounts.google.com/o/oauth2/auth?";
    private String httpReqPost = "https://accounts.google.com/o/oauth2/token";
    private final String FILENAME = ".oauth_settings";
    private URI uri;
    private WebView wv;
    private Context ctx;
    private Token token;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_auth);
        doAuth();
    }

    public void doAuth() {
        try {
            uri = new URI(oAuth + clientId + "&" + redirectURI + "&" + scope
            + "&response_type=code");
            wv = findViewById(R.id.webview);
            wv.setWebChromeClient(new ClientHandler(this));
            wv.setWebViewClient(new MWebClient());
            wv.getSettings().setJavaScriptEnabled(true);
            wv.loadUrl(uri.toASCIIString());
            Log.v("OAUTH", "Calling " + uri.toASCIIString());
        } catch (URISyntaxException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```

#### 2.2 ClientHandler.java

```java
package net.zenconsult.android;

import android.app.Activity;
import android.util.Log;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.widget.Toast;

public class ClientHandler extends WebChromeClient {

    private Activity activity;
    private OAuth oAuth;

    public ClientHandler(Activity act) {
        activity = act;
        oAuth = new OAuth(activity);
    }

    @Override
    public void onReceivedTitle(WebView view, String title) {
        String code = "";
        if (title.contains("Success")) {
            code = title.substring(title.indexOf("=") + 1, title.length());
            setAuthCode(code);
            Log.v("OAUTH", "Code is " + code);
            oAuth.getRequestToken();
            oAuth.writeToken(oAuth.getToken());
            Toast.makeText(activity.getApplicationContext(),
                    "Authorization Successful", Toast.LENGTH_SHORT).show();
            activity.finish();
        } else if (title.contains("Denied")) {
            code = title.substring(title.indexOf("=") + 1, title.length());
            setAuthCode(code);
            Log.v("OAUTH", "Denied, error was " + code);
            Toast.makeText(activity, "Authorization Failed", Toast.LENGTH_SHORT).show();
            activity.finish();
        }
    }

    public String getAuthCode() {
        return oAuth.getToken().getAuthCode();
    }

    public void setAuthCode(String authCode) {
        oAuth.getToken().setAuthCode(authCode);
    }

    @Override
    public void onProgressChanged(WebView view, int newProgress) {
        super.onProgressChanged(view, newProgress);
    }
}
```

#### 2.3 DataFetcher.java

```java
package net.zenconsult.android;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class DataFetcher {

    private HttpClient httpClient;
    private Token token;

    public DataFetcher(Token t) {
        token = t;
        httpClient = new DefaultHttpClient();
    }

    public void fetchAlbums(String userId) {
        String url = "https://picasaweb.google.com/data/feed/api/user/" + userId;
        try {
            HttpResponse resp = httpClient.execute(buildGet(token.getAccessToken(), url));
            if (resp.getStatusLine().getStatusCode() == 200) {
                HttpEntity httpEntity = resp.getEntity();
                String line = EntityUtils.toString(httpEntity);
                // Do your XML Parsing here
            }
        } catch (ClientProtocolException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public HttpGet buildGet(String accessToken, String url) {
        HttpGet get = new HttpGet(url);
        get.addHeader("Authorization", "Bearer " + accessToken);
        return get;
    }
}
```

#### 2.4 MWebClient.java

```java
package net.zenconsult.android;

import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MWebClient extends WebViewClient {

    public MWebClient() {}

    @Override
    public void onPageFinished(WebView view, String url) {
        super.onPageFinished(view, url);
    }
}
```

#### 2.5 OAuth.java

```java
package net.zenconsult.android;

import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.webkit.WebView;
import android.widget.Toast;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.conn.DefaultHttpClientConnectionOperator;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;
import org.xml.sax.helpers.DefaultHandler;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
import java.io.StreamCorruptedException;
import java.io.UnsupportedEncodingException;
import java.net.URI;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

public class OAuth {

    private BasicNameValuePair clientId = new BasicNameValuePair("client_id",
            "200744748489.apps.googleusercontent.com");
    private BasicNameValuePair clientSecret = new BasicNameValuePair("client_secret",
            "edxCTl_L8_SFl1rz2klZ4DbB");
    private BasicNameValuePair redirectURI = new BasicNameValuePair("redirect_uri",
            "urn:ietf:wg:oauth:2.0:oob");
    private String scope = "scope=https://picasaweb.google.com/data/";
    private String oAuth = "https://accounts.google.com/o/oauth2/auth?";
    private String httpReqPost = "https://accounts.google.com/o/oauth2/token";
    private final String FILENAME = ".oauth_settings";
    private URI uri;
    private WebView wv;
    private Context ctx;
    private Activity activity;
    private boolean authenticated;
    private Token token;

    public OAuth(Activity act) {
        ctx = act.getApplication();
        activity = act;
        token = readToken();
    }

    public Token readToken() {
        Token token = new Token();
        FileInputStream fis;
        try {
            fis = ctx.openFileInput(FILENAME);
            ObjectInputStream in = new ObjectInputStream(new BufferedInputStream(fis));
            token = (Token) in.readObject();
            if (token == null) {
                token = new Token();
                writeToken(token);
            }
            in.close();
            fis.close();
        } catch (FileNotFoundException e) {
            writeToken(new Token());
        } catch (StreamCorruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return token;
    }

    public void writeToken(Token token) {
        try {
            File f = new File(FILENAME);
            if (f.exists()) {
                f.delete();
            }
            FileOutputStream fos = ctx.openFileOutput(FILENAME, Context.MODE_PRIVATE);

            ObjectOutputStream out = new ObjectOutputStream(new BufferedOutputStream(fos));
            out.writeObject(token);
            out.close();
            fos.close();
        } catch (FileNotFoundException e) {
            Log.e("OAUTH", "Error creating settings file");
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public void getRequestToken() {
        HttpClient httpClient = new DefaultHttpClient();
        HttpPost post = new HttpPost(httpReqPost);
        List<NameValuePair> nvPairs = new ArrayList<NameValuePair>();
        nvPairs.add(clientId);
        nvPairs.add(clientSecret);
        nvPairs.add(new BasicNameValuePair("code", token.getAuthCode()));
        nvPairs.add(redirectURI);
        nvPairs.add(new BasicNameValuePair("grant_type", "authorization_code"));
        try {
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
    }

    public Token getToken() {
        return token;
    }

    public void setToken(Token token) {
        this.token = token;
    }
}
```

#### 2.6 OAuthPicasaActivity.java

```java
package net.zenconsult.android;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

public class OAuthPicasaActivity extends ListActivity {

    protected OAuthPicasaActivity act;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        act = this;
        new Thread(() -> {
            OAuth o = new OAuth(this);
            Token t = o.getToken();

            if (!t.isValidForReq()) {
                Intent intent = new Intent(this, AuthActivity.class);
                startActivity(intent);
            }

            if (t.isExpired()) {
                o.getRequestToken();
            }

            DataFetcher df = new DataFetcher(t);
            df.fetchAlbums("sheranapress");
            String[] names = new String[] {};   // Add bridge code here to parse XML from DataFetcher and populate your List

            runOnUiThread(() -> {
                setListAdapter(new ArrayAdapter<String>(this, R.layout.list_item, names));

                ListView lv = getListView();
                lv.setTextFilterEnabled(true);

                lv.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Toast.makeText(getApplicationContext(), ((TextView) view).getText(), Toast.LENGTH_SHORT).show();
                    }
                });
            });
        }).start();

    }
}
```

#### 2.7 Token.java

```java
package net.zenconsult.android;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.Serializable;
import java.util.Calendar;

public class Token implements Serializable {

    private static final long serialVersionUID = 6534067628631656760L;
    private String refreshToken;
    private String accessToken;
    private Calendar expiryDate;
    private String authCode;
    private String tokenType;
    private String name;

    public Token() {
        setExpiryDate(0);
        setTokenType("");
        setAccessToken("");
        setRefreshToken("");
        setName("");
    }

    public Token(JSONObject response) {
        try {
            setExpiryDate(response.getInt("expires_in"));
        } catch (JSONException e) {
            setExpiryDate(0);
        }
        try {
            setTokenType(response.getString("token_type"));
        } catch (JSONException e) {
            setTokenType("");
        }
        try {
            setAccessToken(response.getString("access_token"));
        } catch (JSONException e) {
            setAccessToken("");
        }
        try {
            setRefreshToken(response.getString("refresh_token"));
        } catch (JSONException e) {
            setRefreshToken("");
        }
    }

    public void buildToken(JSONObject response) {
        try {
            setExpiryDate(response.getInt("expires_in"));
        } catch (JSONException e) {
            setExpiryDate(0);
        }
        try {
            setTokenType(response.getString("token_type"));
        } catch (JSONException e) {
            setTokenType("");
        }
        try {
            setAccessToken(response.getString("access_token"));
        } catch (JSONException e) {
            setAccessToken("");
        }
        try {
            setRefreshToken(response.getString("refresh_token"));
        } catch (JSONException e) {
            setRefreshToken("");
        }
    }

    public boolean isValidForReq() {
        if (getAccessToken() != null && !getAccessToken().equals("")) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isExpired() {
        Calendar now = Calendar.getInstance();
        if (now.after(getExpiryDate())) {
            return true;
        } else {
            return false;
        }
    }

    public String getRefreshToken() {
        return refreshToken;
    }

    public void setRefreshToken(String refreshToken) {
        if (refreshToken == null) {
            refreshToken = "";
        }
        this.refreshToken = refreshToken;
    }

    public String getAccessToken() {
        return accessToken;
    }

    public void setAccessToken(String accessToken) {
        if (accessToken == null) {
            accessToken = "";
        }
        this.accessToken = accessToken;
    }

    public Calendar getExpiryDate() {
        return expiryDate;
    }

    public void setExpiryDate(int seconds) {
        Calendar now = Calendar.getInstance();
        now.add(Calendar.SECOND, seconds);
        this.expiryDate = now;
    }

    public String getAuthCode() {
        return authCode;
    }

    public void setAuthCode(String authCode) {
        if (authCode == null) {
            authCode = "";
        }
        this.authCode = authCode;
    }

    public String getTokenType() {
        return tokenType;
    }

    public void setTokenType(String tokenType) {
        if (tokenType == null) {
            tokenType = "";
        }
        this.tokenType = tokenType;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

### 3. 资源文件

#### 3.1 activity_auth.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<WebView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/webview"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
```

#### 3.2 activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<ListView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@android:id/list"
    android:layout_width="match_parent"
    android:layout_height="match_parent"/>
```

#### 3.3 list_item.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingTop="10dp"
    android:textSize="16sp">

</TextView>
```

#### 3.4 AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="net.zenconsult.android">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:usesCleartextTraffic="true"
        android:theme="@style/Theme.OAuthPicasa">

        <uses-library
            android:name="org.apache.http.legacy"
            android:required="false"/>

        <activity android:name=".AuthActivity"></activity>
        <activity android:name=".OAuthPicasaActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

#### 3.5 build.gradle

```gradle
plugins {
    id 'com.android.application'
    id 'kotlin-android'
}

android {
    compileSdkVersion 30
    buildToolsVersion "30.0.3"

    defaultConfig {
        applicationId "net.zenconsult.android"
        minSdkVersion 19
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    useLibrary 'org.apache.http.legacy'

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }

    packagingOptions {
        exclude 'META-INF/DEPENDENCIES'
        exclude 'META-INF/NOTICE'
        exclude 'META-INF/LICENSE'
        exclude 'META-INF/LICENSE.txt'
        exclude 'META-INF/NOTICE.txt'
    }

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = '1.8'
    }
}

dependencies {

    implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
    implementation 'androidx.core:core-ktx:1.3.1'
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'com.google.android.material:material:1.2.1'
    implementation 'androidx.constraintlayout:constraintlayout:2.0.1'
    testImplementation 'junit:junit:4.+'
    androidTestImplementation 'androidx.test.ext:junit:1.1.2'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.3.0'
}
```

