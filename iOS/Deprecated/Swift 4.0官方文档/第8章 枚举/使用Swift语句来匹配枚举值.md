可以用 switch 语句来匹配每一个单独的枚举值：

```swift
directionToHead = .south
switch directionToHead {
case .north:
    print("Lots of planets have a north")
case .south:
    print("Watch out for penguins")
case .east:
    print("Where the sun rises")
case .west:
    print("Where the skies are blue")
}
// prins "Watch out for penguins"
```

如果不能为所有枚举成员都提供一个 case，那你也可以提供一个 default 情况来包含那些不能被明确写出的成员：

```swift
let somePlanet = Planet.earth
switch somePlanet {
case .earth:
    print("Mostly harmless")
default:
    print("Not a safe place for humans")
}
// Prints "Mostly harmless"
```