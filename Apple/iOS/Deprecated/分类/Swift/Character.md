<center><font size="5"><b>Character 的扩展</b></font></center>

```swift
extension Character {
    
    /// 将 Character 转换成 Int
    ///
    /// - Returns: 返回该字符的 Int 值
    func intValue() -> Int {
        var number = 0
        for scalar in String(self).unicodeScalars {
            number += Int(scalar.value)
        }
        return number
    }
}
```

