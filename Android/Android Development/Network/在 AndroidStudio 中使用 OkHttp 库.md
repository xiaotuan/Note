1. 在 `build.gradle` 文件中的 `android` 节点添加 `useLibrary 'org.apache.http.legacy'`：

   ```
   android {
   
       useLibrary 'org.apache.http.legacy'
       
   }
   ```
   
2. 在 `build.gradle` 文件中的 `android` 节点添加如下配置信息：

   ```
   android {
   	......
   
       packagingOptions {
           exclude 'META-INF/DEPENDENCIES'
           exclude 'META-INF/NOTICE'
           exclude 'META-INF/LICENSE'
           exclude 'META-INF/LICENSE.txt'
           exclude 'META-INF/NOTICE.txt'
       }
   
   	......
   }
   ```

3. 在 `AndroidManifest.xml` 文件中的 `application` 节点内添加如下代码：

   ```xml
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
       ...
   </application>
   ```

   

