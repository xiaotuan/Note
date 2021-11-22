### 1. 定义构造函数

```kotlin
open class MonitoredActivity(): AppCompatActivity() {
    
    private var tag: String? = null
  
    constructor(intag: String): this() {
        this.tag = intag
    }
}
```

>   注意：定义构造函数后需要在 `MonitoredActivity` 后面添加括号 `()`，在没有定义其他类型构造函数时是如下形式的：
>
>   ```kotlin
>   open class MonitoredActivity: AppCompatActivity() {
>     
>   }
>   ```

### 2. 继承上面的类

```kotlin
open abstract class MonitoredDebugActivity: MonitoredActivity, IReportBack {
  
    // private variables set by constructor
    private var menuId: Int = 0
    private var m_retainState: Boolean = false

    constructor(inMenuId: Int, inTag: String) : super(inTag) {
        tag = inTag
        menuId = inMenuId
    }
}
```

>   注意：在继承类上，不需要在类名后面添加括号`()`，连继承的类都不需要括号 `()`。