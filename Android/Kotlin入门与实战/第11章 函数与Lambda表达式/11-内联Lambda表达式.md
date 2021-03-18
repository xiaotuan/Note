### 11.3.1　内联Lambda表达式

在Kotlin中，使用高阶函数可能会带来一些运行时的效率损失。高阶函数的每一个函数都是一个对象，而且它还会捕获一个闭包，也就是在函数体内会访问的那些外层变量。内存分配和虚拟调用都会带来运行时间开销。为了说明这个问题，先看一个常见的函数调用实例。

```python
fun process(language:(name:String)-> String):String{
    return language("Kotlin")
}
fun main(args: Array<String>) {
    println(process({name -> "{$name} create by JetBrains"}))
}
```

在上面的代码中，函数process接收一个函数类型的参数。当调用该函数进行参数传递时，Kotlin的编译器会单独为Lambda表达式创建一个对象，然后将Lambda表达式转换为函数并执行调用。这样的转换过程势必带来资源上的消耗，尤其在调用频繁的时候，其时间和空间的消耗更大。为了证明前面的理论，可以使用命令“javap –c FunctionKt.class”反编译生成的Class文件，得到如下内容。

```python
public final class com.xzh.FunctionKt {
  public static final void main(java.lang.String[]);
    Code:
       0: aload_0
       1: ldc           #9                 // String args
       3: invokestatic  #15                // Method kotlin/jvm/internal/ Intrinsics.checkParameterIsNotNull:(Ljava/lang/Object;Ljava/lang/String;)V
       6: getstatic     #21                // Field com/xzh/FunctionKt$main$1. INSTANCE:Lcom/xzh/FunctionKt$main$1;
       9: checkcast     #23                // class kotlin/jvm/functions/ Function1
      12: invokestatic  #27                // Method process:(Lkotlin/jvm/ functions/Function1;)Ljava/lang/String;
      15: astore_1
      16: getstatic     #33                // Field java/lang/System.out:Ljava/ io/PrintStream;
      19: aload_1
      20: invokevirtual #39                // Method java/io/PrintStream.println: (Ljava/lang/Object;)V
      23: return
  public static final java.lang.String process(kotlin.jvm.functions.Function1<? super java.lang.String, java.lang.String>);
    Code:
       0: aload_0
       1: ldc           #42                // String language
       3: invokestatic  #15                // Method kotlin/jvm/internal/ Intrinsics.checkParameterIsNotNull:(Ljava/lang/Object;Ljava/lang/String;)V
       6: aload_0
       7: ldc           #44                // String Kotlin
       9: invokeinterface #48,  2          // InterfaceMethod kotlin/jvm/ functions/Function1.invoke:(Ljava/lang/Object;)Ljava/lang/Object;
      14: checkcast     #50                // class java/lang/String
      17: areturn
}
```

在这段代码中，Function1即Kotlin标准库函数提供的一个接口，用来进行对象调用。可以看到，在调用这个函数时，编译器创建了很多额外的对象，并伴随着大量的参数压栈和出栈操作。

在大多数情况下，使用内联Lambda表达式可以消除这类开销问题。因为在编译内联函数时，编译器会直接使用内联函数的函数体替换程序中出现的调用内联函数的表达式，而这样的替换并不会带来多大的性能损耗。使用内联函数的优点在于，函数被内联编译后，就可以通过上下文相关的优化技术对代码进行更深入的优化。

对于函数调用来说，开销并不包括执行函数体所带来的开销，而仅仅指参数压栈、跳转、出栈和返回等操作带来的开销。内联函数也并非是万能的，它以代码膨胀、消耗更多的内存空间为代价来换取程序执行效率上的提升。

