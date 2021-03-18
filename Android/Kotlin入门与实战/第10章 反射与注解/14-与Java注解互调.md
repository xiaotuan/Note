### 10.2.5　与Java注解互调

因为Kotlin在语法上是完全兼容Java的，所以自然也可以在Kotlin中使用Java的注解。代码如下。

```python
import org.junit.Test
import org.junit.Assert.*
import org.junit.Rule
import org.junit.rules.*
class Tests {
    // 将 @Rule 注解应用于属性 getter
    @get:Rule val tempFolder = TemporaryFolder()
    @Test fun simple() {
        val f = tempFolder.newFile()
        assertEquals(42, getTheAnswer())
    }
}
```

因为Java编写的注解没有定义参数顺序，所以不能使用常规函数调用语法来传递参数，但可以使用命名参数语法来调用。代码如下。

```python
// Java
public @interface Ann {
    int intValue();
    String stringValue();
}
//Kotlin调用Java函数
@Ann(intValue = 1, stringValue = "abc") class C
```

和Java一样，如果不需要显式指定value参数的名称，则可以不指定。代码如下。

```python
// Java
public @interface AnnWithValue {
    String value();
}
//在Kotlin调用
@AnnWithValue("abc") class C
```

如果Java中的value参数为数组类型，那么它对应于Kotlin中的vararg类型参数。代码如下。

```python
// Java
public @interface AnnWithArrayValue {
    String[] value();
}
//在Kotlin中调用
@AnnWithArrayValue("abc", "foo", "bar") class C
```

因为Java和Kotlin平台互通，所以Java注解实例的值也会作为属性暴露给Kotlin代码。代码如下。

```python
// Java
public @interface Ann {
    int value();
}
//在Kotlin中使用Java注解实例的属性
fun foo(ann: Ann) {
    val i = ann.value
}
```

