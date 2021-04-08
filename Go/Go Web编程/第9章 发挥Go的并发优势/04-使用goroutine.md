### 9.2.1　使用goroutine

goroutine的用法非常简单：只要把 `go` 关键字添加到任意一个具名函数或者匿名函数的前面，该函数就会成为一个goroutine。作为例子，代码清单9-1展示了如何在名为 `goroutine.go` 的文件中创建goroutine。

代码清单9-1　goroutine使用示例

```go
package main
func printNumbers1() {
　for i := 0; i < 10; i++ {
　　fmt.Printf("%d ", i)
　}
}
func printLetters1() {
　for i := 'A'; i < 'A'+10; i++ {
　　fmt.Printf("%c ", i)
　}
}
func print1() {
　printNumbers1()
　printLetters1()
}
func goPrint1() {
　go printNumbers1()
　go printLetters1()
}
func main() {
}
```

`goroutine.go文件` 中定义了 `printNumbers1` 和 `printLetters1` 两个函数，分别用于循环并打印数字和英文字母，其中 `printNumbers1` 会打印从 `0` 到 `9` 的所有数字，而 `printLetters1` 则会打印从 `A` 到 `J` 的所有英文字母。除此之外， `goroutine.go文件` 中还定义了 `print1` 和 `goPrint1` 两个函数，前者会依次调用 `printNumbers1` 和 `printLetters1` ，而后者则会以goroutine的形式调用 `printNumbers1` 和 `printLetters1` 。

为了检测这个程序的运行时间，我们将通过测试而不是 `main` 函数来运行程序中的 `print1` 函数和 `goPrint1` 函数。这样一来，我们就不必为了测量这两个函数的运行时间而编写测量代码，这也避免了因为编写计时代码而导致测量不准确的问题。

代码清单9-2展示了测试用例的具体代码，这些代码单独记录在了 `goroutine_test.go文件` 当中。

代码清单9-2　运行goroutine示例的测试文件

```go
package main
import "testing"
func TestPrint1(t *testing.T) {  ❶
　print1()
}
func TestGoPrint1(t *testing.T) { ❷
　goPrint1()
}
```

❶ 测试顺序执行的函数

❷ 测试对以goroutine 形式执行的函数

通过使用以下命令执行这一测试：

```go
go test –v
```

我们将得到以下结果：

```go
=== RUN TestPrint1
0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J --- PASS: TestPrint1 (0.00s)
=== RUN TestGoPrint1
--- PASS: TestGoPrint1 (0.00s)
PASS
```

注意，第二个测试用例并没有产生任何输出，这是因为该用例在它的两个goroutine能够产生输出之前就已经结束了。为了让第二个测试用例能够正常地产生输出，我们需要使用 `time` 包中的 `Sleep` 函数，在第二个测试用例的末尾加上一些延迟：

```go
func TestGoPrint1(t *testing.T) {
　　goPrint1()
　　time.Sleep(1 * time.Millisecond)
}
```

这样一来，第二个测试用例就会在该测试用例结束之前正常地产生输出了：

```go
=== RUN TestPrint1
0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J --- PASS: TestPrint1 (0.00s) 
=== RUN TestGoPrint1
0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J --- PASS: TestGoPrint1 (0.00s) 
PASS
```

这两个测试用例都产生了相同的结果。初看上去，是否使用goroutine似乎并没有什么不同，但事实上，这两个测试用例之所以会产生相同的结果，是因为 `printNumbers1` 函数和 `printLetters1` 函数都运行得如此之快，所以是否以goroutine形式运行它们并不会产生任何区别。为了更准确地模拟正常的计算任务，我们将通过 `time` 包中的 `Sleep` 函数人为地给这两个函数加上一点延迟，并把带有延迟的函数重新命名为 `printNumbers2` 和 `printLetters2` 。代码清单9-3展示了这两个新函数，跟原来的函数一样，它们也会被放在 `goroutine.go文件` 中。

代码清单9-3　模拟执行计算任务的goroutine

```go
func printNumbers2() {
　for i := 0; i < 10; i++ {
　　time.Sleep(1 * time.Microsecond） ❶
　　fmt.Printf("%d ", i) ❶
　} ❶
} ❶
func printLetters2() { ❶
　for i := 'A'; i < 'A'+10; i++ { ❶
　　time.Sleep(1 * time.Microsecond) ❶
　　fmt.Printf("%c ", i)❶ 
　}
}
func goPrint2() {
　go printNumbers2()
　go printLetters2()
}
```

❶ 添加1 μs 的延迟，用于模拟计算任务

新定义的两个函数通过在每次迭代中添加1s的延迟来模拟计算任务。为了测试新添加的 `goPrint2` 函数，我们将在 `goroutine_test.go文件` 中添加相应的测试用例，并且和之前一样，为了让被测试的函数能够正常地产生输出，测试用例将在调用 `goPrint2` 函数之后等待1ms：

```go
func TestGoPrint2(t *testing.T) {
　　goPrint2()
　　time.Sleep(1 * time.Millisecond)
}
```

现在，运行测试用例将得到以下输出：

```go
=== RUN TestPrint1
0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J --- PASS: TestPrint1 (0.00s) 
=== RUN TestGoPrint1
0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J --- PASS: TestGoPrint1 (0.00s) 
=== RUN TestGoPrint2
A 0 B 1 C D 2 E 3 F 4 G H 5 I 6 J 7 8 9 --- PASS: TestGoPrint2 (0.00s) 
PASS
```

注意看 `TestGoPrint2` 函数的输出结果，从结果可以看出，程序这次并不是先执行 `printNumbers2` 函数，然后再执行 `printLetters2` 函数，而是交替地执行它们！

如果我们再执行一次这个测试，那么 `TestGoPrint2` 函数的输出结果的最后一行可能会有所不同：这是因为 `printNumbers2` 和 `printLetters2` 都是独立运行的，并且它们都在争先恐后地想要将自己的结果输出到屏幕上，所以随着这两个函数的执行顺序不同，测试产生的结果也会有所不同。唯一的例外是，如果你使用的是Go 1.5之前的版本，那么你每次执行这个测试都会得到相同的结果。

之所以会出现这种情况，是因为Go 1.5之前的版本在用户没有另行设置的情况下，即使计算机拥有多于一个CPU，它默认也只会使用一个CPU。但是从Go 1.5开始，这一情况发生了改变——Go运行时环境会使用计算机拥有的全部CPU。在Go 1.5或以后的版本中，用户如果想要让Go运行时环境只使用一个CPU，就需要执行以下命令：

```go
go test -run x -bench . –cpu 1
```

在执行了这个命令之后，每次执行 `TestGoPrint2` 都将得到完全相同的结果。

