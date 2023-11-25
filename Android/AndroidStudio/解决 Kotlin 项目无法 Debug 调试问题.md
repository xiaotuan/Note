您需要先执行以下操作，然后才能开始调试：

- 在设备上启用调试功能。

  如果您使用的是模拟器，则默认情况下会启用调试功能。但是，对于已连接的设备，您需要[在设备开发者选项中启用调试功能](https://developer.android.com/studio/debug/dev-options?hl=zh-cn)。

- 运行可调试的 build 变体。

  使用 build 配置中包含 [`debuggable true`](https://developer.android.com/studio/build/build-variants?hl=zh-cn#build-types)（Kotlin 脚本中 `isDebuggable = true`）的[build 变体](https://developer.android.com/studio/build/build-variants?hl=zh-cn)。通常，您可以选择每个 Android Studio 项目中都包含的默认“debug”变体（即使它在 `build.gradle` 文件中不可见）。不过，如果您想将新 build 类型定义为可调试，则必须将 `debuggable true` 添加到该 build 类型中：

  **Groovy**

  ```Groovy
  android {
      defaultConfig {
          manifestPlaceholders = [hostName:"www.example.com"]
          ...
      }
      buildTypes {
          release {
              minifyEnabled true
              proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
          }
  
          debug {
              applicationIdSuffix ".debug"
              debuggable true
          }
  
          /**
           * The `initWith` property lets you copy configurations from other build types,
           * then configure only the settings you want to change. This one copies the debug build
           * type, and then changes the manifest placeholder and application ID.
           */
          staging {
              initWith debug
              manifestPlaceholders = [hostName:"internal.example.com"]
              applicationIdSuffix ".debugStaging"
          }
      }
  }
  ```
  **Kotlin 版本**
  
  ```Kotlin
  android {
      defaultConfig {
          manifestPlaceholders["hostName"] = "www.example.com"
          ...
      }
      buildTypes {
          getByName("release") {
              isMinifyEnabled = true
              proguardFiles(getDefaultProguardFile("proguard-android.txt"), "proguard-rules.pro")
          }
  
          getByName("debug") {
              applicationIdSuffix = ".debug"
              isDebuggable = true
          }
  
          /**
           * The `initWith` property lets you copy configurations from other build types,
           * then configure only the settings you want to change. This one copies the debug build
           * type, and then changes the manifest placeholder and application ID.
           */
          create("staging") {
              initWith(getByName("debug"))
              manifestPlaceholders["hostName"] = "internal.example.com"
              applicationIdSuffix = ".debugStaging"
          }
      }
  }
  ```
  
  此属性也适用于[包含 C/C++ 代码的模块](https://developer.android.com/studio/projects/add-native-code?hl=zh-cn)。
  
  > **注意**：`jniDebuggable` 属性已废弃。