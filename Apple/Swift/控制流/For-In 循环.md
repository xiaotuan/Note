你可以使用 `for-in` 循环来迭代序列，例如数组中的项目、数字范围或字符串中的字符：

```swift
let names = ["Anna", "Alex", "Brian", "Jack"]
for name in names {
    print("Hello, \(name)!")
}
// Hello, Anna!
// Hello, Alex!
// Hello, Brian!
// Hello, Jack!
```

你还可以迭代字典来访问其键值对。当迭代字典时，字典中的每个元素都作为元组 `(key, value)` 返回，并且你可以将元组的成员分解wield显式命名的常量，以便在循环体中使用。

```swift
let numberOfLegs = ["spider" : 8, "ant" : 6, "cat" : 4]
for (animalName, legCount) in numberOfLegs {
    print("\(animalName)s have \(legCount) legs")
}
// spiders have 8 legs
// ants have 6 legs
// cats have 4 legs
```

你可以使用带有数字范围的 `for-in` 循环：

```swift
for index in 1...5 {
    print("\(index) times 5 is \(index * 5)")
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

如果使用闭域运算符（`...`），迭代的序列是从 1 到 5 的数字范围（5 包括在内）。

如果不需要序列中的每个值，可以通过使用下划线代替变量名称来忽略这些值：

```swift
let base = 3
let power = 10
var answer = 1
for _ in 1...power {
    answer *= base
}
print("\(base) to the power of \(power) is \(answer)")
// Print "3 to the power of 10 is 59049"
```

在某些情况下，你可能不想使用包含两个端点的封闭范围。可以使用半开范围运算符（`..<`）来包含下限，但不包含上限。有关范围的更多信息，请参阅[范围运算符](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators#Range-Operators)。

```swift
let minutes = 60
for tickMark in 0..<minutes {
    // render the tick mark each minute (60 times)
}
```

可以使用 `stride(from:to:by:)` 方法跳过不需要的标记：

```swift
let minuteInterval = 5
for tickMark in stride(from: 0, to: minutes, by: minuteInterval) {
    // render the tick mark every 5 minutes (0, 5, 10, 15, ..., 45, 50, 55)
}
```

也可以使用 `stride(from:through:by)` 方法表示封闭范围：

```swift
let hours = 12
let hourInterval = 3
for tickMark in stride(from: 3, through: hours, by: hourInterval) {
    // render the tick mark every 3 hours (3, 6, 9, 12)
}
```

