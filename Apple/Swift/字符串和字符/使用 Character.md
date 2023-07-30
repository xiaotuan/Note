您可以通过使用 `for-in` 循环遍历字符串来访问字符串中的各个字符：

```swift
for character in "Dog!🐶" {
    print(character)
}
// D
// o
// g
// !
// 🐶
```

或者，您可以通过提供 Character 类型注解从单字符字符串文字创建独立的 Character 常量或变量：

```swift
let exclamationMark: Character = "!"
```

`String` 可以通过将 `Character` 值数组作为参数传递给其初始化程序来构造值：

```swift
let catCharacters: [Character] = ["C", "a", "t", "!", "🐱"]
let catString = String(catCharacters)
print(catString)
// Prints "Cat!🐱"
```

