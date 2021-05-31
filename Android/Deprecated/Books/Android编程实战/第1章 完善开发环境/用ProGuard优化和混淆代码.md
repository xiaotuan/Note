开发者使用集成在 Android SDK 中的 ProGuard 工具来对 Android 代码进行混淆。Gradle 构建工具也支持该工具，所要做的是在 build.gradle 文件的 android 部分加入如下的代码。

```
buildType {
    release {
        runProguard true
        proguardFile getDefaultProguardFile('proguard-android.txt')
    }
}
```

另一个混淆代码的原因是这样做能执行一些额外的优化，同时，删除无用的代码能压缩生成的二进制 dex 文件。这在引入一个大的第三方库时特别有用，因为它可以显著减小最终的文件大小和运行时的内存使用量。