[toc]

### 1. if 语句

`if` 条件语句的标准格式如下：

```swift
if <条件表达式> {
    语句体
}
```

例如：

```swift
var loginErrorCount = 0
if loginErrorCount >= 3 {
    // loginErrorCount 大于等于 3 的时候输出 you，v out
    print("you, v out")
}
```

### 2. If-else 语句

`if-else` 的标准格式如下：

```swift
if <条件表达式> {
    // 如果条件表达式为真则执行语句体1
    语句体1
} else {
    // 如果条件表达式不为真则执行语句体2
    语句体2
}
```

例如：

```swift
var loginErrorCount = 3
if loginErrorCount >= 3 {
    print("you, v out")
} else {
    // application main run
}
```

### 3. if 多分支语句

形式如下所示：

```swift
if <条件表达式1> {
    语句体1
} else if <条件表达式2> {
    语句体2
} else {
    语句体3
}
```

