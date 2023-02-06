在项目目录中的 `app/build.gradle` 文件添加如下依赖项：

**Kotlin**

```
def lifecycle_version = "2.5.1"

// ViewModel
implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version"
// ViewModel utilities for Compose
implementation "androidx.lifecycle:lifecycle-viewmodel-compose:$lifecycle_version"
```

**Java**

```java
def lifecycle_version = "2.5.1"
    
// ViewModel
implementation "androidx.lifecycle:lifecycle-viewmodel:$lifecycle_version"
```

例如：

**Kotlin**

```kotlin
dependencies {
    def lifecycle_version = "2.5.1"

    // ViewModel
    implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version"
    // ViewModel utilities for Compose
    implementation "androidx.lifecycle:lifecycle-viewmodel-compose:$lifecycle_version"
    ......
}
```

**Java**

```java
```

