## 原因

Android 7.0 引入一项新的应用签名方案 APK Signature Scheme v2，它能提供更快的应用安装时间和更多针对未授权 APK 文件更改的保护。在默认情况下，Android Studio 2.2 和 Android Plugin for Gradle 2.2 会使用 APK Signature Scheme v2 和传统签名方案来签署您的应用。

如这里所述，Android 7.0引入了新的签名方案V2。V2方案是对整个APK进行签名，而不是像V1一样只对JAR那样签名。如果您仅使用V2进行登录，并尝试在7.0之前的目标上安装，则会收到此错误，因为JAR本身未签名，并且7.0 之前的PackageManager无法检测V2 APK签名的存在。

## 解决方法

所以方案也就有两种

1. 降低gradle版本，像我们这样多人开发，每个人的studio版本都不一样，gradle版本也有不一样的，这样就会好一些。就是要把项目目录下的build.gradle中的gradle配置改一下。比如'classpath 'com.android.tools.build:gradle:2.3.1''改为'classpath 'com.android.tools.build:gradle:2.2.3''
2. 如果是个人的话，用越新的东西越能装逼，当然推荐用最新的gradle了，只是在打包的时候注意要兼容7.0以前和以后，这就需要注意把Signature Scheme V1和Signature Scheme V2都选上。



作者：Sparky
链接：https://www.jianshu.com/p/ea1eaf1ff505
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。