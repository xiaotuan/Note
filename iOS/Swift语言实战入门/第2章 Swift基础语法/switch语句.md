`switch` 最简单的形式是：

```swift
switch value {
    case value1:
    	语句体1
   	case value2, value3:
    	语句体2
  	default:
    	默认语句体
}
```

例如：

```swift
let weekDay = 3
switch weekDay {
case 1,2,3,4,5:
    print("今天是工作日，星期\(weekDay)")
case 6,7:
    print("今天是周末，星期\(weekDay)，出去逛街吧")
default:
    print("Input Error, Please try again")
}
```

在 `Swift` 语言中你不需要在 `case` 块中显式地使用 `break` 语句跳出 `switch`，当匹配到的 `case` 块中的代码执行完毕后，程序会终止 `switch` 语句，而不会继续执行下一个 `case` 块。

```swift
let somefruits = "fruits"
var fruitShape = "fruit"
switch somefruits {
case "apple":
    fruitShape = "Circle"
case "banana", "plantain":
    fruitShape = "Bending"
default:
    fruitShape = "irregular"
}
```

使用时有几点需要特别注意：

+ 每一个 `case` 块都必须包含至少一条语句。下面的代码是无效的：

    ```swift
    let somefruits = "fruits"
    var fruitShape = "fruit"
    switch somefruits {
        case "apple":
        	// none to do
        case "banana", "plantain":
        	fruitShape = "Bending"
       	default:
        	fruitShape = "irregular"
    }
    ```

+ `switch` 语句不会同时匹配大写字母和小写字母。

可以像下面这样使用元组在同一个 `switch` 语句中匹配多个值，元组中元素可以是值，也可以是范围：

```swift
var xPoint = (1,1)
switch xPoint {
case (0, 0):
    print("(0,0) is at the start")
case (_, 0):
    print("Point: (\(xPoint.0), 0) is on the x-axis")
case (0, _):
    print("Point: (0, \(xPoint.1) is on the y-axis")
default:
    print("Point: (\(xPoint.0), \(xPoint.1)) is outside of the box")
}
```

`switch` 语句也支持值绑定，`case` 块允许将匹配的值绑定到一个临时的常量或变量，这个常量或变量在该 `case` 块里就可以被引用了。在使用值绑定的时候你也可以使用 `where` 语句来判断额外的条件，举个例子：

```swift
var anotherPoint = (2, 3)
switch anotherPoint {
case (var x, 0):
    x -= 1
    print("\(x) on the x-axis")
case (0, var y):
    y += 1
    print("\(y) on the y-axis")
    // 当 x 等于 y 的时候执行此 case 块中的语句
case let (x, y) where x == y:
    print("(\(x), \(y)) is on the line x == y")
// 最后一个 case 块可以包含所有可能出现的元组值匹配，所以不需要使用默认块
case let (x, y):
    print("point at (\(x), \(y))")
}
```

