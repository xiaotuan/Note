<center><font size="5"><b>Swift 的文档注释</b></font></center>

Swift 的文档注释使用 `///` 开头，

1. 首行的文字属于摘要内容

```swift
/// Returns the distance between two indices.
```

2. 参数注释：如果在参数注释前有摘要内容，则摘要内容需要和参数注释之间添加一行空行。

```swift
/// Returns the distance between two indices.
///
/// - Parameters:
///   - start: A valid index of the collection.
///   - end: Another valid index of the collection. If `end` is equal to
///     `start`, the result is zero.
/// - Returns: The distance between `start` and `end`.
```

下面是 String 类的一个完整的文档注释示例：

```swift
/// Returns the distance between two indices.
///
/// - Parameters:
///   - start: A valid index of the collection.
///   - end: Another valid index of the collection. If `end` is equal to
///     `start`, the result is zero.
/// - Returns: The distance between `start` and `end`.
///
/// - Complexity: O(*n*), where *n* is the resulting distance.
@inlinable public func distance(from start: String.Index, to end: String.Index) -> String.IndexDistance
```
