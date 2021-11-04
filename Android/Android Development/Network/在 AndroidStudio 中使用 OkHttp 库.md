1. 在 `defaultConfig` 中添加 `useLibrary 'org.apache.http.legacy'`：

   ```
   defaultConfig {
       applicationId "net.zenconsult.android"
       minSdkVersion 19
       targetSdkVersion 30
       versionCode 1
       versionName "1.0"
   
       useLibrary 'org.apache.http.legacy'
   
       testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
   }
   ```

2. 在 `android` 中添加如下配置信息：

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

3. 在 `dependencies` 中添加如下依赖：

   ```
   implementation 'org.apache.httpcomponents:httpclient:4.4.1'
   ```

   

