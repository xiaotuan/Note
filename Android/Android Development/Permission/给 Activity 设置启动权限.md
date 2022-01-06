在 `AndroidManifest.xml` 文件注册 `Activity` 时添加 `android:permission` 属性即可：

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="net.zenconsult.libs">

    <permission android:name="net.zenconsult.libs.Mofest.permission.PURGE_DATABASE"
        android:protectionLevel="dangerous"
        android:label="@string/label_purgeDatabase"
        android:description="@string/description_purgeDatabase"
        android:permissionGroup="android.permission-group.COST_MONEY" />
    <uses-permission android:name="net.zenconsult.libs.Mofest.permission.PURGE_DATABASE" />
    <uses-permission android:name="android.permission.SET_WALLPAPER" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.ZenLibrary">
        <activity android:name=".ZenLibraryActivity"
            android:permission="net.zenconsult.libs.Mofest.permission.PURGE_DATABASE"
            android:label="@string/app_name">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

