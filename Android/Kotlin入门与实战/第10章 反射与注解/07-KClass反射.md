### 10.1.6　KClass反射

在Java中，获取Class对象及其属性的方法主要有以下几种。

+ Class.forName("类名字符串")。
+ 类名.class。
+ 实例对象.getClass()。

在Kotlin中，可以通过系统提供的API来获取以上内容，不过，要想使用Kotlin的反射API，首先需要获取对应的KClass对象。Kotlin获取KClass对象的方式和Java类似，主要有以下几种。

+ 类名::class。

```python
val clazz = Person::class
```

+ 对象.javaClass.kotlin。

```python
val clazz = person.javaClass.kotlin
```

在这当中，KClass是一个泛型接口，该接口的定义如下。

```python
public interface KClass<T : Any> : KDeclarationContainer, KAnnotatedElement, KClassifier {
    public val simpleName: String?    //返回类的名字
    public val qualifiedName: String?   //返回类的全包
    val members: Collection<KCallable<*>>   //返回该类可访问的所有函数和属性
    public val constructors: Collection<KFunction<T>>  //返回该类的所有构造器
    public val nestedClasses: Collection<KClass<*>>    //返回这个类中定义的其
    他类，包括内部类和嵌套类
    public val objectInstance: T?
    //…
}
```

除此之外，KClass还提供了一些很有用的扩展函数和属性。代码如下。

```python
//返回所有基类
val KClass<*>.allSuperclasses: Collection<KClass<*>>  
//返回companionObject
val KClass<*>.companionObject: KClass<*>?  
//返回声明的所有函数
val KClass<*>.declaredFunctions: Collection<KFunction<*>>  
//返回扩展函数和属性
val KClass<*>.declaredMemberExtensionFunctions: Collection<KFunction<*>>
val <T : Any> KClass<T>.declaredMemberExtensionProperties: Collection<KProperty2<T, *, *>>
//返回自身声明的函数和属性
val KClass<*>.declaredMemberFunctions: Collection<KFunction<*>>
val <T : Any> KClass<T>.declaredMemberProperties: Collection<KProperty1<T, *>>
```

在Kotlin中，通过反射获取的KClass对象，其函数和属性具有共同的接口KCallable，而且可以调用call方法来使用函数或者访问属性的getter方法。代码如下。

```python
fun main(args: Array<String>) {
    val jack= Person("jack", 30)
    val clazz = jack.javaClass.kotlin
    val list = clazz.members
    for (calls in list) {
        when (calls.name) {
            "name" -> println("name is：" + calls.call(jack))
            "age" -> println("age is：" + calls.call(jack))
        }
    }
    println(jack.selfDescribe())
}
data class Person(val name: String, var age: Int) {
    fun selfDescribe(): String {
        return "My name is $name,I am $age years old"
    }
}
```

运行上面的代码，输出的结果如下。

```python
age is：30
name is：jack
My name is jack,I am 30 years old
```

需要说明的是，call方法的参数类型是vararg Any?，如果使用错误的类型实参去调用call函数是会报错的。为了避免报错，可以使用更具体的方式来调用这个函数。代码如下。

```python
fun main(args: Array<String>) {
    val jack = Person("jack", 30)
    val fun1= Person::selfDescribe
    val fun2 = Person::grow
    println(fun1.invoke(jack))   //输出My name is jack,I am 30 years old
    println(fun2.invoke(jack,20))   //输出50
}
data class Person(val name: String, var age: Int) {
    fun selfDescribe(): String {
        return "My name is $name,I am $age years old"
    }
    fun grow(a: Int): Int {
        age += a
        return age
    }
}
```

在这当中，fun1是KFunction0<String>类型，fun2是KFunction1<Int,Int>类型。KFunctionN <…>代表不同数量的参数。这类函数都继承KFunction类并带有invoke成员，对于这种编译器生成的类型，不需要声明就可以在任意数量参数的函数接口中使用它。

call函数是访问所有类型的通用手段，但它不保证访问的安全性。当然，如果系统提供了属性的getter和setter函数，也可以通过getter和setter函数来获取对象的属性。

```python
val ageP = Person::age
//通过setter-call调用（不安全)
ageP.setter.call(30)
//通过set()调用(安全)
ageP.set(Jack,30)
//通过getter-call调用(不安全)
ageP.getter.call()
//通过get调用(安全）
ageP.get(Jack)
```

所有对象的属性都是KProperty的实例，它是一个泛型类型，KProperty<R,T>中的R为接收者类型，T为属性类型。

当然，作为同属于JVM语系的编程语言，Kotlin也支持Java中原有的反射机制，可以通过类的javaClass来获取Class对象。例如，在Android应用程序中通过反射来获取R文件中的控件id。

```python
fun findId(): String {
    val viewId : String by lazy {
        val c = R.id()
        val fields = c.javaClass.declaredFields
        val r = fields.find { it.getInt(c) == view.id }?.name?:"Not found"
        return@lazy r
    }
    return viewId
}
```

需要注意的是，直接调用R.id::class获取的是KClass对象，它代表Kotlin反射的入口，要获取Java的Class对象需要调用.java属性。代码如下。

```python
val c = R.id::class
val fields = c.java.fields
val r = fields.find { it.getInt(c) == view.id }?.name?:"Not found"
```

以上代表了通过对象和类名访问Java原有反射API的两种方式。

