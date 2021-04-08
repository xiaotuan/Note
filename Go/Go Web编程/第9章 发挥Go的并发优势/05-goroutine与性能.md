### 9.2.2　goroutine与性能

在了解了goroutine的运作方式之后，接下来我们要考虑的就是如何通过goroutine来提高性能。本节在进行性能测试时将沿用上一节定义的 `print1` 、 `goPrint1` 等函数，但为了避免这些函数在并发执行时输出一些乱糟糟的结果，这次我们将把代码中的 `fmt.Println` 语句注释掉。代码清单9-4展示了为 `print1` 函数和 `goPrint1` 函数设置的基准测试用例，这些用例定义在 `goroutine_test.go文件` 中。

代码清单9-4　为无goroutine和有goroutine的函数分别创建基准测试用例

```go
func BenchmarkPrint1(b *testing.B) { ❶
　for i := 0; i < b.N; i++ {
　　print1()
　}
}
func BenchmarkGoPrint1(b *testing.B) { ❷
　for i := 0; i < b.N; i++ {
　　goPrint1()
　}
}
```

❶ 对顺序执行的函数进行基准测试

❷ 对以goroutine 形式执行的函数进行基准测试

在使用以下命令进行性能基准测试并跳过功能测试之后：

```go
go test -run x -bench . –cpu 1
```

我们将看到以下结果：

```go
BenchmarkPrint1　　 100000000　　　　13.9 ns/op
BenchmarkGoPrint1　 1000000　　　　　1090 ns/op
```

（运行这个测试只使用了单个CPU，具体原因本章稍后将会说到。）正如结果所示，函数 `print1`  运行得非常快，只使用了 13.9 ns。令人感到惊讶的是，在使用goroutine运行相同函数时，程序的速度居然慢了如此之多，足足耗费了1090 ns！出现这种情况的原因在于“天下没有免费的午餐”：无论goroutine有多么的轻量级，启动goroutine还是有一定的代价的。因为 `printNumbers1` 函数和 `printLetters1` 函数是如此简单，它们执行的速度是如此快，所以以goroutine方式执行它们反而会比顺序执行的代价更大。

如果我们对每次迭代都带有一定延迟的 `printNumbers2` 函数和 `printLetters2` 函数执行类似的测试，结果又会如何呢？代码清单9-5展示了 `goroutine_test.go文件中` 为以上两个函数设置的基准测试用例。

代码清单9-5　为无goroutine和有goroutine的带延迟函数分别创建基准测试用例

```go
func BenchmarkPrint2(b *testing.B) { ❶
　for i := 0; i < b.N; i++ {
　　print2()
　}
}
func BenchmarkGoPrint2(b *testing.B) { ❷
　for i := 0; i < b.N; i++ {
　　goPrint2()
　}
}
```

❶ 对顺序执行的函数进行基准测试

❷ 对以goroutine 形式执行的函数进行基准测试

在运行这一基准测试之后，我们将得到以下结果：

```go
BenchmarkPrint2　　 10000　　　　　121384 ns/op
BenchmarkGoPrint2　 1000000　　　　17206 ns/op
```

这次的测试结果跟上一次的测试结果有些不同。可以看到，以goroutine方式执行 `print`  Numbers2和 `printLetters2` 的速度是以顺序方式执行这两个函数的速度的差不多7倍。现在，让我们把函数的迭代次数从10次改为100次，然后再运行相同的基准测试：

```go
func printNumbers2() {
　for i := 0; i < 100; i++ {  ❶
　　time.Sleep(1 * time.Microsecond)
　　// fmt.Printf("%d ", i)
　}
}
func printLetters2() {
　for i := 'A'; i < 'A'+100; i++ { ❷
　　time.Sleep(1 * time.Microsecond)
　　// fmt.Printf("%c ", i)
　}
}
```

❶ 迭代100 次而不是10 次

❷ 迭代100 次而不是10 次

下面是这次基准测试的结果：

```go
BenchmarkPrint1　　　 20000000　　　 86.7 ns/op
BenchmarkGoPrint1　　 1000000　　　　1177 ns/op
BenchmarkPrint2　　　 2000　　　　　 1184572 ns/op
BenchmarkGoPrint2　　 1000000　　　　17564 ns/op
```

在这次基准测试中， `print1` 函数的基准测试时间是之前的13倍，而 `goPrint1` 函数的速度跟上一次相比没有出现太大变化。另一方面，通过延迟模拟负载的函数的测试结果变化非常之大——以顺序方式执行的函数和以goroutine方式执行的函数之间，两者的执行时间相差了67倍之多。因为这次基准测试的迭代次数比之前增加了10倍，所以 `print2` 函数在进行基准测试时的速度差不多是上次的1/10，但对于 `goPrint2` 来说，迭代10次所需的时间跟迭代100次所需的时间却几乎是相同的。

注意，到目前为止，我们都是在用一个CPU执行测试，但如果我们执行以下命令，改用两个CPU执行带有100次迭代的基准测试：

```go
go test -run x -bench . -cpu 2
```

那么我们将得到以下结果：

```go
BenchmarkPrint1-2　　　20000000　　　 87.3 ns/op
BenchmarkGoPrint1-2　　5000000　　　　391 ns/op
BenchmarkPrint2-2　　　1000　　　　　 1217151 ns/op
BenchmarkGoPrint2-2　　200000　　　　 8607 ns/op
```

因为 `print1` 函数以顺序方式执行，无论运行时环境提供多少个CPU，它都只能使用一个CPU，所以它这次的测试结果跟上一次的测试结果基本相同。与此相反， `goPrint1` 函数这次因为使用了两个CPU来分担计算负载，所以它的性能提高了将近3倍。此外，因为 `print2` 也只能使用一个CPU，所以它这次的测试结果也跟预料中的一样，并没有发生什么变化。最后，因为 `goPrint2` 使用了两个CPU来分担计算负载，所以它这次的测试比之前快了两倍。

现在，如果我们更进一步，使用4个CPU来运行相同的基准测试，结果将会如何？

```go
BenchmarkPrint1-4　　　20000000　　　 90.6 ns/op
BenchmarkGoPrint1-4　　3000000　　　　479 ns/op
BenchmarkPrint2-4　　　1000　　　　　 1272672 ns/op
BenchmarkGoPrint2-4　　300000　　　　 6193 ns/op
```

正如我们预期的那样， `print1` 函数和 `print2` 函数的测试结果还是一如既往地没有发生什么变化。但令人惊奇的是，尽管 `goPrint1` 在使用4个CPU时的测试结果还是比只使用一个CPU时的测试结果要好，但使用4个CPU的执行速度居然比使用两个CPU的执行速度要慢。与此同时，虽然只有40%的提升，但 `goPrint2` 在使用4个CPU时的成绩还是比使用2个CPU时的成绩要好。使用更多CPU并没有带来性能提升反而导致性能下降的原因跟之前提到的一样：在多个CPU上调度和运行任务需要耗费一定的资源，如果使用多个CPU带来的性能优势不足以抵消随之而来的额外消耗，那么程序的性能就会不升反降。

从上述测试我们可以看出，增加CPU的数量并不一定会带来性能提升，更重要的是要理解代码，并对其进行基准测试，以了解它的性能特质。

