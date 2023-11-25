通过 [反编译后重新打包 apk](./反编译后重新打包 apk.md) 文件反编译 APK 后，在反编译输出目录中找到 `apktool.yml` 文件，修改文件中 `minSdkVersion` 和 `targetSdkVersion` 的值：

```
!!brut.androlib.meta.MetaInfo
apkFileName: batterylog.apk
compressionType: false
doNotCompress:
- resources.arsc
- png
isFrameworkApk: false
packageInfo:
  forcedPackageId: '127'
  renameManifestPackage: null
sdkInfo:
  minSdkVersion: '8'
  targetSdkVersion: '23'
sharedLibrary: false
sparseResources: false
unknownFiles:
  org/achartengine/image/zoom-1.png: '8'
  org/achartengine/image/zoom_in.png: '8'
  org/achartengine/image/zoom_out.png: '8'
usesFramework:
  ids:
  - 1
  tag: null
version: 2.5.0
versionInfo:
  versionCode: '9'
  versionName: 2.0.3
```

然后重新打包签名 apk 即可。