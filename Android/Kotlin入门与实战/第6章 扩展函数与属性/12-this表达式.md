### 6.3　this表达式

为了限定接收者的使用范围，Kotlin提供了this表达式。this表达式主要有以下几个作用。

+ 在类的成员中，this指代该类的当前对象。
+ 在扩展函数或者带接收者的函数字面值中，this表示在点左侧传递的接收者参数。

如果this没有限定符，则指的是最内层包含它的作用域，如果要引用其他作用域中的this对象，请使用标签限定符。标签限定符的格式为this@label，其中@label是一个代指this来源的标签。

```python
class A {                         //隐式标签@A
    inner class B {               //隐式标签@B
        fun Int.foo() {           //隐式标签@foo
            val a = this@A        //A的this
            val b = this@B        //B的this
            val c = this          //foo()的接收者，Int类型
            val c1 = this@foo     //foo()的接收者，Int类型
            val funLit = lambda@ fun String.() {
                val d = this      //funLit的接收者
            }
            val funLit2 = { 
            //foo()的接收者，它包含的Lambda表达式没有任何接收者
            s: String -> val d1 = this
            }
        }
    }
}
```

