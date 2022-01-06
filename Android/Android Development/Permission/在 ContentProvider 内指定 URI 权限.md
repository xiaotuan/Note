在 `AndroidManifest.xml` 文件中可以通过两种方式为 `ContentProvider` 指定 `URI` 权限：

+ 首先，在 `<provide>` 标记中，可将`android:grantUriPermissions` 特性设置为 true 或 false。如果设置为 true，可授予来自此 `ContentProvider` 的任何内容的权限。如果设置为 false，可以执行第二种指定 URI 权限的方式，或者 `ContentProvider` 可以决定不让其他任何实体授予权限。

  ```xml
  <provider
      android:name=".AndroidTestProvider"
      android:authorities="com.android.androidtest.provider"
      android:grantUriPermissions="true"
      android:exported="true"/>
  ```

+ 第二种授予权限的方式是使用 `<provider>` 的子标记指定它。该子标记为 `<grant-uri-permission>`，`<provider>` 可包含多个这样的子标记。`<grant-uri-permission>` 具有 3 个可能的特性。

  + 使用 `android:path` 特性，可以指定一个完整的路径，该路径然后将拥有可授予的权限。
  + 类似地，`android:pathPrefix` 指定 URI 路径的开头。
  + `android:pathPattern` 允许使用通配符（也即星号 * ）来指定路径。

  ```xml
  <provider
      android:name=".AndroidTestProvider"
      android:authorities="com.android.androidtest.provider"
      android:exported="true">
      <grant-uri-permission android:path="content://com.android.contacts/contacts"
          android:pathPattern="content://com.android.contacts/*"
          android:pathPrefix="content://com.android.contacts/" />
  </provider>
  ```

  > 详情请参阅 <https://developer.android.google.cn/guide/topics/manifest/grant-uri-permission-element?hl=en>。

