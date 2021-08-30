[toc]

### 1. 使用的 URL 有三个类型

```java
mCaptivePortalHttpsUrls = makeCaptivePortalHttpsUrls();
mCaptivePortalHttpUrls = makeCaptivePortalHttpUrls();
mCaptivePortalFallbackUrls = makeCaptivePortalFallbackUrls();
```

### 2. mCaptivePortalHttpsUrls 初始化分析

1. 首先，该变量是通过 `makeCaptivePortalHttpsUrls()` 方法进行初始化的，代码如下所示：

   ```java
   private URL[] makeCaptivePortalHttpsUrls() {
       final String firstUrl = getCaptivePortalServerHttpsUrl();
       try {
           final URL[] settingProviderUrls =
               combineCaptivePortalUrls(firstUrl, CAPTIVE_PORTAL_OTHER_HTTPS_URLS);
           // firstUrl will at least be default configuration, so default value in
           // getProbeUrlArrayConfig is actually never used.
           return getProbeUrlArrayConfig(settingProviderUrls,
                                         R.array.config_captive_portal_https_urls,
                                         DEFAULT_CAPTIVE_PORTAL_HTTPS_URLS, this::makeURL);
       } catch (Exception e) {
           // Don't let a misconfiguration bootloop the system.
           Log.e(TAG, "Error parsing configured https URLs", e);
           // Ensure URL aligned with legacy configuration.
           return new URL[]{makeURL(firstUrl)};
       }
   }
   ```

2. 先看 `getCaptivePortalServerHttpsUrl()` 方法，代码如下所示：

   ```java
   private String getCaptivePortalServerHttpsUrl() {
       final String testUrl = getTestUrl(TEST_CAPTIVE_PORTAL_HTTPS_URL);
       if (isValidTestUrl(testUrl)) return testUrl;
       final Context targetContext = getCustomizedContextOrDefault();
       return getSettingFromResource(targetContext,
                                     R.string.config_captive_portal_https_url, CAPTIVE_PORTAL_HTTPS_URL,
                                     targetContext.getResources().getString(R.string.default_captive_portal_https_url));
   }
   ```

   1. 再来看 `getTestUrl()` 方法，代码如下所示：

      ```java
      @Nullable
      private String getTestUrl(@NonNull String key) {
          final String strExpiration = mDependencies.getDeviceConfigProperty(NAMESPACE_CONNECTIVITY,
                                                                             TEST_URL_EXPIRATION_TIME, null);
          if (strExpiration == null) return null;
      
          final long expTime;
          try {
              expTime = Long.parseUnsignedLong(strExpiration);
          } catch (NumberFormatException e) {
              loge("Invalid test URL expiration time format", e);
              return null;
          }
      
          final long now = System.currentTimeMillis();
          if (expTime < now || (expTime - now) > TEST_URL_EXPIRATION_MS) return null;
      
          return mDependencies.getDeviceConfigProperty(NAMESPACE_CONNECTIVITY,
                                                       key, null /* defaultValue */);
      }
      ```

      该方法最后通过 `DeviceConfig.getProperty(namespace, name)` 获取值，这个是系统设置的默认值，优先级很低，设置其他值后将会覆盖该默认值，因此在这里就不继续分析了。

   2. 我们再来看下 `getSettingFromResource()` 方法，代码如下所示：

      ```java
      private String getSettingFromResource(@NonNull final Context context,
                  @StringRes int configResource, @NonNull String symbol, @NonNull String defaultValue) {
          final Resources res = context.getResources();
          String setting = res.getString(configResource);
      
          if (!TextUtils.isEmpty(setting)) return setting;
      
          setting = mDependencies.getSetting(context, symbol, null);
      
          if (!TextUtils.isEmpty(setting)) return setting;
      
          return defaultValue;
      }
      ```

      在代码中首先读取 `R.string.config_captive_portal_https_url` 的值，该值定义在 `config.xml` 文件中，没有设置值。因此会走 `setting = mDependencies.getSetting(context, symbol, null);` 代码，该代码读取 `SettingsProvider` 中 `Global` 表中的 `captive_portal_other_https_urls` 键对应的值；如果 `SettingProviders` 也没有值，则最后取 `R.string.default_captive_portal_https_url` 的值，该值定义在 `config.xml` 文件中，其值为：`https://www.google.com/generate_204`。

3. 再来看 `combineCaptivePortalUrls()` 方法，代码如下所示：

   ```java
   private URL[] combineCaptivePortalUrls(final String firstUrl, final String propertyName) {
       if (TextUtils.isEmpty(firstUrl)) return new URL[0];
   
       final String otherUrls = mDependencies.getDeviceConfigProperty(
           NAMESPACE_CONNECTIVITY, propertyName, "");
       // otherUrls may be empty, but .split() ignores trailing empty strings
       final String separator = ",";
       final String[] urls = (firstUrl + separator + otherUrls).split(separator);
       return convertStrings(urls, this::makeURL, new URL[0]);
   }
   ```

   从代码中可以看出，该方法通过 `DeviceConfig.getProperty(namespace, name)` 方法获取其他的测试 URL，然后与 firstUrl 组合成一个测试 URL 数组。

4. 最后来看下 `getProbeUrlArrayConfig()` 方法，代码如下所示：

   ```java
   private <T> T[] getProbeUrlArrayConfig(@NonNull T[] providerValue, @ArrayRes int configResId,
               String[] defaultConfig, @NonNull Function<String, T> resourceConverter) {
       final Resources res = getCustomizedContextOrDefault().getResources();
       String[] configValue = res.getStringArray(configResId);
   
       if (configValue.length == 0) {
           if (providerValue.length > 0) {
               return providerValue;
           }
   
           configValue = defaultConfig;
       }
   
       return convertStrings(configValue, resourceConverter, Arrays.copyOf(providerValue, 0));
   }
   ```

   该方法首先读取 `R.array.config_captive_portal_http_urls` 的值，该值定义在 `config.xml` 中，没有设置值；这时如果 providerValue 有值的话，则返回该值；否则将 `configValue` 变量的值设置为 `defaultConfig`，它的值定义如下所示：

   ```java
   public static final String[] DEFAULT_CAPTIVE_PORTAL_HTTP_URLS =
               new String [] {"http://connectivitycheck.gstatic.com/generate_204"};
   ```

   最后通过 `convertStrings()` 方法调用 `makeURL()` 将字符串转换成 URL，并存储在 `ArrayList` 中，然后返回 URL 数组。

### 3. mCaptivePortalHttpUrls 和 mCaptivePortalFallbackUrls 初始化流程

`mCaptivePortalHttpUrls` 和 `mCaptivePortalFallbackUrls` 初始化流程与 `mCaptivePortalHttpsUrls` 初始化流程一样，请参照 `mCaptivePortalHttpsUrls ` 初始化流程进行分析。

### 4. 总结

其实没有必要这么麻烦，只有在 `makeCaptivePortalHttpsUrls()`、`makeCaptivePortalHttpUrls()`、`makeCaptivePortalFallbackUrls()` 返回需要修改的 URL 即可。