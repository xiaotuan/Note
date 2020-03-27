<center><font size="5"><b>Character 转换成 Int </b></font></center>

```swift
extension Character {
    
    func intValue() -> Int {
        var number = 0
        for scalar in String(self).unicodeScalars {
            number += Int(scalar.value)
        }
        return number
    }
}
```