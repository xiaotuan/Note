[toc]

### 1. Android L（Android 9.0）以前

#### 1.1 使用 Intent extra

要将 `extra` 数据信息添加给 `Intent`，需要调用 `Intent.putExtra(...)` 函数，例如：

**Kotlin**

```kotlin
Intent.putExtra(name: String, value: Boolean)
```

**Java**

```java
Intent.putExtra(String name, boolean value)
```



### 2. Android L（Android 9.0）以后

