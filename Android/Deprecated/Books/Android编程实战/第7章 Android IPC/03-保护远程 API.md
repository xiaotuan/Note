### 7.3 保护远程 API

不管哪方面，设计 Android 应用时，安全问题应该是一个永远需要优先考虑的事情。当为其他应用提供 API 时，安全问题会变得更为重要。（第 12 章会详细介绍 Android 应用开发安全方面的话题。）幸好保护发布的 Service 以及其他组件是很容易的事情，如下所示：

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.apt1.sampleapi">
	
    <permission android:name="com.apt1.sampleapi.CALL_SERVICE"
                android:protectionLevel="normal" />
    
    <uses-sdk
              android:minSdkVersion="17"
              android:targetSdkVersion="17" />
    <application
                 android:icon="@drawable/icon"
                 android:label="@string/app_name">
    
        <service
                 android:name=".AidlService"
                 android:exported="true"
                 android:permission="com.sampleapi.CALL_SERVICE">
        
            <intent-filter>
            	<action android:name="com.apt1.sampleapi.AIDL_SERVICE" />
            </intent-filter>
            
        </service>
    </application>
</manifest>
```

该 XML 文件显示了发布 Service 时， AndroidManifest.xml 可能显示的内容。重要的部分已用粗体显示。首先，需要将 android:exported 属性的值设置为 true。该属性的默认值取决于是否在 Service 中定义了 intent-filter。如果 Service 不包含 intent-filter，那么该 Service 仅用于内部使用（通过组件名访问），并不会被输出。如果定义了 intent-filter，Service 默认会被输出。强烈建议始终定义该属性，并且根据是否需要输出 Service 来设置它的值。

如果要输出 Service，最重要的部分是设置权限。第 12 章会详细介绍权限的定义，但前面的例子显示了最简单的形式。上例在 application 标签上定义了权限，并设置了 protectionLevel 属性的值。接下来，为 Service 设置 android:permission 属性，以此来说明使用该 Service 的客户端必须在它们的清单文件中声明该权限。

通常，像上面代码块中那样声明权限就足够了，但有时候 Android 的权限管理系统并不能满足需求。第 12 章会讨论保护应用以及发布 API 的更高级的方法。

