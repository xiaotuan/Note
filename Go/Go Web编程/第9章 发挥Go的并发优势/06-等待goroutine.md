### 9.2.3　等待goroutine

在上一节中，我们了解到程序启动的goroutine在程序结束时将会被粗暴地结束，虽然通过 `Sleep` 函数来增加时间延迟可以避免这一问题，但这说到底只是一种权宜之计，并没有真正地解决问题。虽然在实际的代码中，程序本身比goroutine更早结束的情况并不多见，但为了避免意外，我们还是需要有一种机制，使程序可以在确保所有goroutine都已经执行完毕的情况下，再执行下一项工作。

为此，Go语言在 `sync` 包中提供了一种名为等待组（ `WaitGroup` ）的机制，它的运作方式非常简单直接：

+ 声明一个等待组；
+ 使用 `Add` 方法为等待组的计数器设置值；
+ 当一个goroutine完成它的工作时，使用 `Done` 方法对等待组的计数器执行减一操作；
+ 调用 `Wait` 方法，该方法将一直阻塞，直到等待组计数器的值变为0。

代码清单9-6展示了一个使用等待组的例子，在这个例子中，我们复用了之前展示过的 `printNumbers2` 函数以及 `printLetters2` 函数，并为它们分别加上了1μs的延迟。

代码清单9-6　使用等待组

```go
package main
import "fmt"
import "time"
import "sync"
func printNumbers2(wg *sync.WaitGroup) {
　for i := 0; i < 10; i++ {
　　time.Sleep(1 * time.Microsecond)
　　fmt.Printf("%d ", i)
　}
　wg.Done() ❶
}
func printLetters2(wg *sync.WaitGroup) {
　for i := 'A'; i < 'A'+10; i++ {
　　time.Sleep(1 * time.Microsecond)
　　fmt.Printf("%c ", i)
　}
　wg.Done() ❷
}
func main() {
　var wg sync.WaitGroup ❸
　wg.Add(2) ❹
　go printNumbers2(&wg)
　go printLetters2(&wg)
　wg.Wait() ❺
}
```

❶ 对计数器执行减一操作

❷ 对计数器执行减一操作

❸ 声明一个等待组

❹ 为计数器设置值

❺ 阻塞到计数器的值为0

如果我们运行这个程序，那么它将巧妙地打印出 `0 A 1 B 2 C 3 D 4 E 5 F 6 G 7 H 8 I 9 J` 。这个程序的运作原理是这样的：它首先定义一个名为 `wg` 的 `WaitGroup` 变量，然后通过调用 `wg` 的 `Add` 方法将计数器的值设置成 `2` ；在此之后，程序会分别调用 `printNumbers2` 和 `printLetters2` 这两个goroutine，而这两个goroutine都会在末尾对计数器的值执行减一操作。之后程序会调用等待组的 `Wait` 方法，并因此而被阻塞，这一状态将持续到两个goroutine都执行完毕并调用 `Done` 方法为止。当程序解除阻塞状态之后，它就会跟平常一样，自然地结束。

如果我们在某个goroutine里面忘记了对计数器执行减一操作，那么等待组将一直阻塞，直到运行时环境发现所有goroutine都已经休眠为止，这时程序将引发一个panic：

```go
0 A 1 B 2 C 3 D 4 E 5 F 6 G 7 H 8 I 9 J fatal error: all goroutines are asleep - deadlock!
```

等待组这一特性不仅简单，而且好用，它对并发编程来说是一种不可或缺的工具。

