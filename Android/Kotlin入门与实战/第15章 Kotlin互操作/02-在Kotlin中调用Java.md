### 15.1.1　在Kotlin中调用Java

作为一门基于JVM的编程语言，Kotlin借鉴了大量的Java语法，而且在语法上能够完全兼容Java。因此，在Kotlin中可以很容易地调用Java，同时在Java代码中顺利地调用Kotlin。例如，下面是在Kotlin中调用Java的Util工具类的list的实例。

```python
import java.util.*
fun demo(source:List<Int>){
    val list=ArrayList<Int>()
    for(item in list){
        list.add(item)
    }
    for(i in 0..source.size - 1){
          list[i]=source[i]   //调用get和set函数
    }
}
```

Kotlin调用Java的互操作行为如下。

#### 1．属性读写

按照约定，Kotlin可以自动识别Java中的getter/setter方法，而Java也可以通过getter/setter方法来操作Kotlin的字段属性。代码如下。

```python
import java.util.*
fun calendarDemo() {
    val calendar = Calendar.getInstance()
    if (calendar.firstDayOfWeek == Calendar.SUNDAY) {
          calendar.firstDayOfWeek = Calendar.MONDAY
}
    if (!calendar.isLenient) {         // 调用 isLenient()
          calendar.isLenient = true
    }
}
```

值得注意的是，如果Java类只有一个setter方法而没有对应的getter方法，那么它在Kotlin中作为属性时是不可见的，因为Kotlin目前暂不支持只写（set-only）属性。

#### 2．void方法

如果一个Java方法的返回类型为void，那么在Kotlin中调用该方法时直接返回Unit类型。如果需要使用它的返回值，则它将由Kotlin编译器在调用处赋值，因为编译器是预先知道返回结果的。

#### 3．标识符转义

如果一些Kotlin关键字在Java中是有效标识符（如in、object、is等），那么在Java代码中使用Kotlin关键字作为方法名，仍然可以通过反引号（`）字符转义来调用该方法。代码如下。

```python
foo.`is`(bar)
```

#### 4．空安全

在Java语言中，任何引用都可能造成NullPointerException。如果在Kotlin 中针对来自Java的对象进行严格的空安全操作将是不现实的。Java声明的类型在 Kotlin中被称为平台类型，会被特别对待。Kotlin会放宽对这种平台类型对象的空检查，因此它们的安全保证与Java的空安全级别是相同的。代码如下。

```python
val list = ArrayList<String>()   //非空
list.add("Item")
val size = list.size   //非空
val item = list[0]   // 推断为平台类型
```

Kotlin的空安全类型的原理是，Kotlin在编译过程中会增加一个函数调用，对参数类型或者返回类型进行控制。开发者可以通过在代码中添加注解@Nullable和@NotNull的方式来限制Java中空值异常的产生。

此时，如果直接调用平台类型变量的方法，Kotlin不会在编译时报告可空错误，但是在运行调用时有可能会报空指针异常。代码如下。

```python
item.substring(1)    // item==null可能会抛出异常
```

在Kotlin中，平台类型是不可标识的，这意味着不能在代码中明确地标识它们，但是仍然可以通过类型推断系统来判断对象的类型（如上例中item所具有的类型），或者选择期望的类型（可空或非空类型均可）。

```python
val nullable: String? = item    // 允许，类型推断
val notNull: String = item      // 允许，运行时可能为空
```

如果变量的平台类型是一个非空类型，则编译器会在赋值时触发断言，从而防止Kotlin的非空变量保存空值；当把平台的值传递给期待非空值的Kotlin函数时，也会触发一个断言。简单来说，编译器会尽力阻止空值的传递，但是泛型的存在导致空指针异常是不可能完全消除的。

#### 5．平台类型

虽然平台类型不能在程序中显式表述，也没有相应语法来对其进行描述，但是如果有需要（编译器和IDE的错误信息、参数信息等），可以使用助记符来标识它们。常用的助记符有以下几个。

+ T! ：表示“T 或者 T?”。
+ (Mutable)Collection<T>! ：表示可变或不可变、可空或不可空的 T 的 Java 集合。
+ Array<(out) T>!： 表示可空或不可空的泛型（或 T 的子类型）的Java数组。

#### 6．可空注解

具有可空的Java类型注解并不表示其为平台类型，而只能表示为实际可空或非空的Kotlin类型。Kotlin编译器支持多种可空注解，常见的有以下几种。

+ JetBrains：org.jetbrains.annotations包中的@Nullable和@NotNull。
+ Android：com.android.annotations 和 android.support.annotations。
+ JSR-305：javax.annotation。
+ FindBugs：edu.umd.cs.findbugs.annotations。
+ Eclipse：org.eclipse.jdt.annotation。
+ Lombok：lombok.NonNull。

#### 7．Kotlin中的Java泛型

Kotlin将泛型分为类型投影和星投影。当Java类型导入Kotlin时，系统会执行一些转换，如Java的通配符会转换成类型投影，原始类型则转换成星投影。例如，将通配符类型Foo<? extends Bar>转换成Foo<out Bar!>!；将原始类型List转换成List<*>!，即 List<out Any?>!。

与Java一样，Kotlin在运行时是不保留泛型的。也就是说，在Kotlin中调用Java的泛型时，ArrayList<Integer>()和ArrayList <Character>()是不能区分的，这使得在进行集合操作时，is检查不可能照顾到通配符泛型，Kotlin只允许is检查星投影泛型。

```python
val a = arrayListOf<String>("a", "b", "c")
if (a is List<Int>) {   //编译错误，无法检查a是否真的是一个Int类型列表
   //函数体
}
if (a is List<*>) {   // 编译正确，星投影泛型不保证列表的内容
  //函数体
}
```

#### 8．Java数组

与Java不同，Kotlin中的数组是不型变的，这意味着在Kotlin中，不允许把一个Array<String>赋值给一个Array<Any>，从而避免了运行时可能造成的故障。同时，Kotlin也禁止把子类的数组当作超类的数组传递给Kotlin的某个方法，但是如果传递给Java方法，则是被允许的。

在Java平台中，使用原生数据类型可以避免装箱/拆箱操作带来的开销。Kotlin隐藏了这些实现细节，因此Kotlin调用Java的数组时，需要定义一个变通方法来与Java代码进行交互。接受int数组的Java方法如下。

```python
public class JavaArrayExample {
     public void removeIndices(int[] indices) {
        // 函数体
    }
}
```

在Kotlin中调用Java数组时，可以按照下面的方式来传递一个原生类型的数组给Java。

```python
val javaObj = JavaArrayExample()
val array = intArrayOf(0, 1, 2, 3)
javaObj.removeIndices(array)
```

当编译为JVM字节代码时，编译器会优化对数组的访问，这样就不会引入任何开销了。

```python
val array = arrayOf(1, 2, 3, 4)
array[2] = array[2] * 2    //不会生成对get()和set()的调用
for (x in array) {         //不会创建迭代器
   print(x)
}
```

#### 9．可变参数

有时候，需要在Java类中声明一个具有可变数量的参数方法来使用索引。

```python
public class JavaArrayExample {
    public void removeIndicesVarArg(int… indices) {   //定义一个可变参数方法
        //函数体
    }
}
```

此时，如果在Kotlin中调用Java的方法，则需要使用展开运算符*来传递一个数组。

```python
val javaObj = JavaArrayExample()
val array = intArrayOf(0, 1, 2, 3)
javaObj.removeIndicesVarArg(*array)   //使用展开运算符进行调用
```

目前，Kotlin还无法支持传递null给一个声明为可变参数的方法。

#### 10．受检异常

在Kotlin中，所有异常都是非受检的，这意味着编译器不会强迫开发人员进行任何异常捕获。因此，当调用一个声明受检异常的Java方法时，Kotlin不会强迫我们做任何事情。

```python
fun render(list: List<*>, to: Appendable) {
     for (item in list) {
           to.append(item.toString())  // Java会要求在此处捕获IOException
    }
}
```

虽然Kotlin并不要求进行异常受检，但是代码在运行时会抛出异常，因此正确的处理方式是在存在代码异常的地方使用try catch表达式进行捕捉。

#### 11．已映射类型

在Kotlin调用Java时，其编译系统会特殊处理一部分Java类型。这样的类型不是按原样从Java中加载，而是映射到相应的Kotlin类型上。映射只发生在编译期间，运行时则保持不变。

Java的原生类型的对应Kotlin类型映射关系如表15-1所示。

除了原生的基本类型外，一些非原生的内置类型也会在Kotlin中找到对应的映射类型，其映射关系如表15-2所示。

<center class="my_markdown"><b class="my_markdown">表15-1　Java原生类型映射</b></center>

| Java原生类型 | Kotlin类型 | Java原生类型 | Kotlin类型 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| byte | kotlin.Byte | char | kotlin.Char |
| short | kotlin.Short | float | kotlin.Float |
| int | kotlin.Int | double | kotlin.Double |
| long | kotlin.Long | boolean | kotlin.Boolean |

<center class="my_markdown"><b class="my_markdown">表15-2　Kotlin内置类型映射</b></center>

| Java类型 | Kotlin类型 | Java类型 | Kotlin类型 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| java.lang.Object | kotlin.Any! | java.lang.Deprecated | kotlin.Deprecated! |
| java.lang.Cloneable | kotlin.Cloneable! | java.lang.CharSequence | kotlin.CharSequence! |
| java.lang.Comparable | kotlin.Comparable! | java.lang.String | kotlin.String! |
| java.lang.Enum | kotlin.Enum! | java.lang.Number | kotlin.Number! |
| java.lang.Annotation | kotlin.Annotation! | java.lang.Throwable | kotlin.Throwable! |

Java的装箱原始类型，也可以映射到可空的Kotlin类型中，其对应的映射关系如表15-3所示。

<center class="my_markdown"><b class="my_markdown">表15-3　Kotlin装箱类型映射</b></center>

| Java装箱类型 | Kotlin类型 | Java装箱类型 | Kotlin类型 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| java.lang.Byte | kotlin.Byte? | java.lang.Character | kotlin.Char? |
| java.lang.Short | kotlin.Short? | java.lang.Float | kotlin.Float? |
| java.lang.Integer | kotlin.Int? | java.lang.Double | kotlin.Double? |
| java.lang.Long | kotlin.Long? | java.lang.Boolean | kotlin.Boolean? |

需要注意的是，用作类型参数的装箱原始类型映射到Kotlin平台时，会自动转换为平台类型，例如，List<java.lang.Integer>在Kotlin中会转换为List<Int!>。

集合类型在Kotlin中可以是只读的，也可以是可变的，因此Java集合类型对应的Kotlin类型如表15-4所示。

<center class="my_markdown"><b class="my_markdown">表15-4　Java集合类型映射</b></center>

| Java类型 | Kotlin只读类型 | Kotlin可变类型 | 平台类型(Mutable) |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| Iterator<T> | Iterator<T> | MutableIterator<T> | terator<T>! |
| Iterable<T> | Iterable<T> | MutableIterable<T> | Iterable<T>! |
| Collection<T> | Collection<T> | MutableCollection<T> | Collection<T>! |
| Set<T> | Set<T> | MutableSet<T> | Set<T>! |
| List<T> | List<T> | MutableList<T> | List<T>! |
| ListIterator<T> | ListIterator<T> | MutableListIterator<T> | ListIterator<T>! |
| Map<K, V> | Map<K, V> | MutableMap<K, V> | Map<K, V>! |

除此之外，Java数组对应的Kotlin类型的映射如表15-5所示。

<center class="my_markdown"><b class="my_markdown">表15-5　Java数组类型映射</b></center>

| Java类型 | Kotlin类型 |
| :-----  | :-----  | :-----  | :-----  |
| int[] | kotlin.IntArray! |
| String[] | kotlin.Array<(out) String>! |

需要注意的是，Java类型的静态成员在相应Kotlin类型的伴生对象中不能直接访问，可以使用Java类型的完整限定名来调用它们。代码如下。

```python
java.lang.Integer.toHexString(foo)
```

#### 12．访问静态成员

在Kotlin中，Java类的静态成员会形成该类的伴生对象，这样就无法将伴生对象作为值来传递，但可以显式访问其成员。代码如下。

```python
if (Character.isLetter(a)) {
    // 函数体
}
```

要访问已映射到Kotlin类型的Java类型静态成员，可以使用Java类型的完整限定名。代码如下。

```python
java.lang.Integer.bitCount(foo)
```

#### 13．对象方法

当Java类型导入Kotlin平台时，java.lang.Object的所有类型引用都会转换成Any。在Kotlin中，Any并非是平台所指定的，它只声明了一些常用的函数作为其成员函数，如toString()、hashCode()和equals()等。为了使用java.lang.Object的其他成员，Kotlin用到了扩展函数。常见的扩展函数有wait()/notify()、getClass()、clone()和finalize()。下面以getClass()为例，来讲解Kotlin扩展函数的具体使用方法。

在Kotlin中，要获取对象的Java类，可以在类引用上使用Java扩展属性。

```python
val fooClass = foo::class.java
```

Kotlin 1.1版本开始支持绑定的类引用，也就是说，可以使用 javaClass来获取扩展属性。

```python
val fooClass = foo.javaClass
```

#### 14．Java反射

Java反射不仅可以作用于Java类，还可以作用于Kotlin类。也就是说，我们可以使用instance::class.java、ClassName::class.java或者instance.javaClass通过 java.lang.Class来获得Java反射。

其他支持的情况包括为Kotlin属性获取Java的getter/setter方法或者幕后字段，为Java字段获取KProperty，为KFunction获取Java方法或者构造函数，反之亦然。

#### 15．SAM转换

和Java 8一样，Kotlin也支持SAM（Single Abstract Method）转换，这意味着Kotlin函数字面值可以被自动转换成一个只有非默认方法的Java接口的实现。只要这个方法的参数类型能够与Kotlin函数的参数类型相匹配即可。例如，创建只有一个接口作为参数的Java类。

```python
public class SAMInJava {
     private ArrayList<Runnable> runnables = new ArrayList<Runnable>();
     public void addTask(Runnable runnable) {
          runnables.add(runnable);
          System.out.println("add:"+runnable+",size"+runnables.size());
    }
    public void removeTask(Runnable runnable) {
         runnables.remove(runnable);
         System.out.println("remove:"+runnable+"size"+runnables.size());
    }
}
```

然后在Kotlin文件中调用该方法。

```python
fun main(args: Array<String>) {
    var samJava=SAMInJava()
    val lamba={
         print("hello")
    }
    samJava.addTask(lamba)
    samJava.removeTask(lamba)
}
```

运行上面的代码，输出的结果如下。

```python
add:SAMInKotlinKt$sam$Runnable$a1764456@4617c264,size1
remove:SAMInKotlinKt$sam$Runnable$a1764456@36baf30csize1
```

如果Java类含有多个接收函数接口的方法，那么可以将Lambda表达式转换为特定的SAM类型的适配器函数，然后再选择需要调用的方法，这些适配器函数由编译器按需生成。

```python
var samJava=SAMInJava()
    val lamba={
        print("hello")
    }
    samJava.addTask(lamba)
```

值得注意的是，SAM转换只适用于接口而不适用于抽象类，即使这些抽象类只有一个抽象方法。同时，SAM转换只适用于Java互操作，因为Kotlin具有合适的函数类型，所以不需要将函数自动转换为Kotlin接口的实现，因此不需要进行SAM转换。

#### 16．在Kotlin中使用JNI

和Java一样，如果要在Kotlin中使用JNI，首先要在本地（C或C++）代码中声明一个实现的函数，而且需要使用external修饰符来标记它。代码如下。

```python
external fun foo(x: Int): Double
```

