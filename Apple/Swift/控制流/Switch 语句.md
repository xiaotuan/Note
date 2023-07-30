[toc]

`switch` 语句将一个值与一个或多个相同类型的值进行比较，其一般形式为：

```swift
switch <#some value to consider#> {
    case <#value 1#>:
    	<#respond to value 1#>
    case <#value 2#>,
    	<#value 3#>:
    	<#respond to value 2 or 3#>
    default:
    	<#otherwise, do something else#>
}
```

每一个 `switch` 陈述都必须详尽无遗。也就是说，所考虑的类型的每个可能只都必须与其中一种情况相匹配 `switch`。如果不适合为每个可能的值提供一个案例，你可以定义一个默认案例来涵盖任何为明确解决的值。这种默认情况由关键字 `default` 表示，并且必须始终出现在最后。

例如：

```swift
let someCharacter: Character = "z"
switch someCharacter {
case "a":
    print("The first letter of the Latin alphabet")
case "z":
    print("The last letter of the Latin alphabet")
default:
    print("Some other character")
}
// Prints "The last letter of the Latin alphabet"
```

与 `if` 语句一样，`switch` 语句也有表达式形式：

```swift
let anotherCharacter: Character = "a"
let message = switch anotherCharacter {
case "a":
    "The first letter of the Latin alphabet"
case "z":
    "The last letter of the Latin alphabet"
default:
    "Some other character"
}


print(message)
// Prints "The first letter of the Latin alphabet"
```

与 `if` 表达式一样，你可以抛出错误或调用类似永不返回的 `fatalError(_:file:line:)` 函数，而不是为给定情况提供值。

### 1. 无隐式失败

`switch` 与 `C` 和 `Objective-C` 中的语句相比，`Swift` 中的 `switch` 语句默认不会从每个 `case` 的底部落入下一个 `case`。相反，一旦第一个匹配案例完成，整个语句就会完成执行，而不需要显示 `break` 语句。

>   提示：尽管 `break` 在`switch` 中不是必需的，但你可以使用 `break` 语句来匹配并忽略特定情况，或者在匹配情况完成之前打破该情况。

每个案例的主体必须至少包含一个可执行语句。下面的代码编译将会报错：

```swift
let anotherCharacter: Character = "a"
switch anotherCharacter {
case "a": // Invalid, the case has an empty body
case "A":
    print("The letter A")
default:
    print("Not the letter A")
}
// This will report a compile-time error.
```

要使用 `switch` 语句匹配 `a` 和 `A` ，可以将两个值组合成一个复合大小写，并用逗号分隔：

```swift
let anotherCharacter: Character = "a"
switch anotherCharacter {
case "a", "A":
    print("The letter A")
default:
    print("Not the letter A")
}
// Prints "The letter A"
```

>   提示：`switch` 要在特定情况结束时显式失败，请使用 `fallthrough` 关键字。

### 2. 区间匹配

`switch` 可以检查案例中的值是否包含在某个区间中：

```swift
let approximateCount = 62
let countedThings = "moons orbiting Saturn"
let naturalCount: String
switch approximateCount {
case 0:
    naturalCount = "no"
case 1..<5:
    naturalCount = "a few"
case 5..<12:
    naturalCount = "several"
case 12..<100:
    naturalCount = "dozens of"
case 100..<1000:
    naturalCount = "hundreds of"
default:
    naturalCount = "many"
}
print("There are \(naturalCount) \(countedThings).")
// Prints "There are dozens of moons orbiting Saturn."
```

### 3. 元组

你可以使用元组来测试同一 `switch` 语句中的多个值。可以针对不同的值或值区间来测试元组的每个元素。或者，使用下划线字符（`_`）来匹配任何可能的值。

```swift
let somePoint = (1, 1)
switch somePoint {
case (0, 0):
    print("\(somePoint) is at the origin")
case (_, 0):
    print("\(somePoint) is on the x-axis")
case (0, _):
    print("\(somePoint) is on the y-axis")
case (-2...2, -2...2):
    print("\(somePoint) is inside the box")
default:
    print("\(somePoint) is outside of the box")
}
// Prints "(1, 1) is inside the box"
```

与 `C` 不同，`Swift` 允许多种 `switch` 情况考虑相同的值或多个值。事实上，上例中点 `(0,0)` 可以匹配本例中的所有四种情况。但是，如果可以进行多个匹配，则始终使用第一个匹配情况。点 `(0,0)` 将 `case (0, 0)` 首先匹配，因此所有其他匹配情况将被忽略。

### 3. 值绑定

`switch` 案例可以命名与临时常量或变量匹配的一个或多个值，以在案例主体重使用。这种行为称为之值绑定，因为值绑定到案例主体内的临时常量或变量。

```swift
let anotherPoint = (2, 0)
switch anotherPoint {
case (let x, 0):
    print("on the x-axis with an x value of \(x)")
case (0, let y):
    print("on the y-axis with a y value of \(y)")
case let (x, y):
    print("somewhere else at (\(x), \(y))")
}
// Prints "on the x-axis with an x value of 2"
```

上面例子中没有 `default` 案例。最后一种情况，`case let (x, y)` 声明了两个可以匹配任何值的占位符常量的元组，所以这种情况会匹配所有可能的剩余值。

### 4. Where 子句

`switch` 案例可以使用 `where` 子句来检查附加条件：

```swift
let yetAnotherPoint = (1, -1)
switch yetAnotherPoint {
case let (x, y) where x == y:
    print("(\(x), \(y)) is on the line x == y")
case let (x, y) where x == -y:
    print("(\(x), \(y)) is on the line x == -y")
case let (x, y):
    print("(\(x), \(y)) is just some arbitrary point")
}
// Prints "(1, -1) is on the line x == -y"
```

### 5. 复合案例

`switch` 共享同一个主体的多个 `case` 可以通过在后面写入多个模式来组合 `case`，每个模式之间用逗号分隔。如果任何模式匹配，则会执行主体语句。如果列表很长，则可以将模式写在多行上。

```swift
let someCharacter: Character = "e"
switch someCharacter {
case "a", "e", "i", "o", "u":
    print("\(someCharacter) is a vowel")
case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z":
    print("\(someCharacter) is a consonant")
default:
    print("\(someCharacter) isn't a vowel or a consonant")
}
// Prints "e is a vowel"
```

复合案例还可以包括值绑定。复合案例的所有模式必须包含同一组值的绑定，并且每个绑定必须从复合案例中的所有模式获取相同类型的值。

```swift
let stillAnotherPoint = (9, 0)
switch stillAnotherPoint {
case (let distance, 0), (0, let distance):
    print("On an axis, \(distance) from the origin")
default:
    print("Not on an axis")
}
// Prints "On an axis, 9 from the origin"
```

