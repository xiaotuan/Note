### 4.10.3　Elvis操作符

Elvis操作符很像Java语言的三目表达式，是三目条件运算符的简略写法。Kotlin对三目表达式进行了升级，升级的Elvis操作符不再支持传统的三目表达式，而是使用了一种全新的语法，其语法格式如下。

```python
<结果> = <表达式1> ?: <表达式2>
```

如果表达式1为空，则返回表达式2的内容；否则返回表达式1的内容。也就是说，当且仅当表达式1为空时，才会对表达式2求值。对于Kotlin的 Elvis操作符可以像以下这么理解。

+ A ?: B等价于if(A == null) B。
+ A?.B ?: C等价于if(A != null) A.B else C。

```python
// Elvis操作符获取b字符串的长度，如果b为null，则返回-1
    var b = "hello world"
    val lenB = b?.length ?: -1
    val lenA: Int = if (b != null) {
        b.length
    } else {
        -1
    }
    println(lenA)    //输出11
```

同时，在空检查方面，Elvis操作符还可以配合安全调用符使用，实现清晰的空检查和空操作判断。

