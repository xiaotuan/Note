可以使用如下代码通过视图 `ID` 查找该视图正在显示的 `Fragment`：

**Kotlin**

```kotlin
val currentFragment = supportFragmentManager.findFragmentById(R.id.fragment_container)
```

**Java**

```java
Fragment currentFragment = getSupportFragmentManager().findFragmentById(R.id.fragment_container);
```

