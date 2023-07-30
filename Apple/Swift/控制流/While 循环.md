`while` 循环执行一组语句，直到条件变为 `false`。当第一次迭代开始之前迭代次数未知时，最好使用此类循环。`Swift` 提供了两种 `while` 循环：

+   `while` ：在每次循环开始时评估其条件。
+   `repeat-while`：在每次循环结束时评估其条件。

### 1. While 循环

`while` 循环首先评估单个条件，如果条件为 `true`，则重复一组语句，直到条件为 `false`。`while` 循环的一般形式为：

```swift
while <#condition#> {
    <#statements#>
}
```

例如：

```swift
let finalSquare = 25
var board = [Int](repeating: 0, count: finalSquare + 1)

board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08

var square = 0
var diceRoll = 0
while square < finalSquare {
    // roll the dice
    diceRoll += 1
    if diceRoll == 7 { diceRoll = 1 }
    // move by the rolled amount
    square += diceRoll
    if square < board.count {
        // if we're still on the board, move up or down for a snake or a ladder
        square += board[square]
    }
}
print("Game over!")
```

### 2. Repeat-while 循环

`repeat-while` 循环的一般形式为：

```swift
repeat {
    <#statements#>
} while <#condition#>
```

例如：

```swift
let finalSquare = 25
var board = [Int](repeating: 0, count: finalSquare + 1)

board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08

var square = 0
var diceRoll = 0
repeat {
    // move up or down for a snake or ladder
    square += board[square]
    // roll the dice
    diceRoll += 1
    if diceRoll == 7 { diceRoll = 1 }
    // move by the rolled amount
    square += diceRoll
} while square < finalSquare
print("Game over!")
```

