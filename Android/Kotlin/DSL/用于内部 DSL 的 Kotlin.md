[toc]

### 1. 分号可选

Kotlin 并不坚持使用分号，不使用它对于创建富有表现力的 DSL 语法尤其重要。

我们可以比较两个表达式：

```kotlin
starts.at(14.30)
ends.by(15.20)
```

第一种比这种混乱要少：

```kotlin
starts.at(14.30);
ends.by(15.20);
```

### 2. 点和圆括号不与中缀在一起

对 DSL 来说，Kotlin 对使用 `infix` 关键字的中缀表示法的支持是另一个受欢迎的特性。看看下面的代码：

```kotlin
starts.at(14.30)
ends.by(15.20)
```

使用 `infix`，我们可以这样写：

```kotlin
starts at 14.30
ends by 15.20
```

### 3. 使用扩展函数获得特定的域

尽管 Kotlin 是静态类型的，但它允许执行编译时函数注入。因此，你可以通过想 `Int` 中注入 `days()` 这样的函数来为库函数的使用者设计如下代码。即使 `Int` 中没有内置的 `days()` 函数，一旦将这个函数注入 `Int` 中，就可以这样写：

```kotlin
2.days(ago)
```

此外，扩展函数也可以用 `infix` 关键字注释，然后，我们可以这样写来代替之前的例子：

```kotlin
2 days ago
```

### 4. 传递 lambda 不需要圆括号

如果函数最后一个参数的类型是 `lambda` 表达式，那么你可以将 `lambda` 表达式参数放在圆括号外。另外，如果函数只接受一个 `lambda` 表达式作为参数，那么就不需要在调用中使用圆括号。如果函数与类相关联，那么可以使用 `infix` 关键字来去掉点和圆括号。

因此，我们可以这样写：

```kotlin
"Release Planning".meeting({
    starts.at(14.30)
    ends.by(15.20)
})
```

但我们可以通过 Kotlin 的能力实现如下的流畅性：

```kotlin
"Release Planning".meeting {
    starts.at(14.30)
    ends.by(15.20)
}
```



