可以通过如下代码将 `Fragment` 与一个视图容器相关联（在该视图容器内显示该 `Fragment`）：

**Kotlin**

```kotlin
val fragment = CrimeFragment()
supportFragmentManager
    .beginTransaction()
    .add(R.id.fragment_container, fragment)
    .commit()
```

**Java**

```java
CrimeFragment fragment = new CrimeFragment();
getSupportFragmentManager().beginTransaction()
        .add(R.id.fragment_container, fragment)
        .commit();
```



