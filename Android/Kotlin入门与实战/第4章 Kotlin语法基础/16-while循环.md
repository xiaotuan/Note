### 4.5.4　while循环

Kotlin的while循环和Java中的while循环是一样的，主要分为while 和do…while两种形式。

#### 1．while语句

while语句在循环刚开始时会计算一次布尔表达式的值。如果满足条件，则进入循环；如果不满足条件，则跳出循环。

```python
var x=10;
    while (x > 0) {
        x--
        println(x)
    }
```

#### 2．do…while语句

do…while语句与while语句的功能类似，唯一的区别是do…while语句至少会执行一次，即使布尔表达式的第一次计算结果是false；而在while语句中，如果布尔表达式的第一次计算的结果是false，则该循环不会被执行。

```python
var x=10;
    do {
        if(x == 7) continue
        println(x)
        if(x == 6) break
    } while (x-->0)
```

运行上面的代码，输出结果如下。

```python
10
9
8
6
```

