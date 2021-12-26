`Swift` 使用字符串插值的方式来把常量名或者变量名当做占位符加入到更长的字符串中，然后让 `Swift` 用常量或变量的当前值替换这些占位符。将常量或变量名放入圆括号中并在括号前使用反斜杠将其转义：

```swift
var friendlyWelcome = "Hello!"
print("The current value of friendlyWelcome is \(friendlyWelcome)")
```

