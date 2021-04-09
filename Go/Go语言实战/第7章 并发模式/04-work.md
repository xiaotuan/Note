### 7.3　work

`work` 包的目的是展示如何使用无缓冲的通道来创建一个goroutine池，这些goroutine执行并控制一组工作，让其并发执行。在这种情况下，使用无缓冲的通道要比随意指定一个缓冲区大小的有缓冲的通道好，因为这个情况下既不需要一个工作队列，也不需要一组goroutine配合执行。无缓冲的通道保证两个goroutine之间的数据交换。这种使用无缓冲的通道的方法允许使用者知道什么时候goroutine池正在执行工作，而且如果池里的所有goroutine都忙，无法接受新的工作的时候，也能及时通过通道来通知调用者。使用无缓冲的通道不会有工作在队列里丢失或者卡住，所有工作都会被处理。

让我们来看一下 `work` 包里的work.go代码文件，如代码清单7-28所示。

代码清单7-28　 `work` /work.go

```go
01 // Jason Waldrip协助完成了这个示例
02 // work包管理一个goroutine池来完成工作
03 package work
04
05 import "sync"
06
07 // Worker必须满足接口类型，
08 // 才能使用工作池
09 type Worker interface {
10　　 Task()
11 }
12
13 // Pool提供一个goroutine池，这个池可以完成
14 // 任何已提交的Worker任务
15 type Pool struct {
16　　 work chan Worker
17　　 wg　 sync.WaitGroup
18 }
19
20 // New创建一个新工作池
21 func New(maxGoroutines int) *Pool {
22　　 p := Pool{
23　　　　 work: make(chan Worker),
24　　 }
25
26　　 p.wg.Add(maxGoroutines)
27　　 for i := 0; i < maxGoroutines; i++ {
28　　　　 go func() {
29　　　　　　 for w := range p.work {
30　　　　　　　　 w.Task()
31　　　　　　 }
32　　　　　　 p.wg.Done()
33　　　　 }()
34　　 }
35
36　　 return &p
37 }
38
39 // Run提交工作到工作池
40 func (p *Pool) Run(w Worker) {
41　　 p.work <- w
42 }
43
44 // Shutdown等待所有goroutine停止工作
45 func (p *Pool) Shutdown() {
46　　 close(p.work)
47　　 p.wg.Wait()
48 }
```

代码清单7-28中展示的 `work` 包一开始声明了名为 `Worker` 的接口和名为 `Pool` 的结构，如代码清单7-29所示。

代码清单7-29　 `work` /work.go：第07行到第18行

```go
07 // Worker必须满足接口类型， 
08 // 才能使用工作池
09 type Worker interface {
10　　 Task()
11 }
12
13 // Pool提供一个goroutine池，这个池可以完成
14 // 任何已提交的Worker任务
15 type Pool struct {
16　　 work chan Worker
17　　 wg　 sync.WaitGroup
18 }
```

代码清单7-29的第09行中的 `Worker` 接口声明了一个名为 `Task` 的方法。在第15行，声明了名为 `Pool` 的结构，这个结构类型实现了goroutine池，并实现了一些处理工作的方法。这个结构类型声明了两个字段，一个名为 `work` （一个 `Worker` 接口类型的通道），另一个名为 `wg` 的 `sync.WaitGroup` 类型。

接下来，让我们来看一下 `work` 包的工厂函数，如代码清单7-30所示。

代码清单7-30　 `work` /work.go：第20行到第37行

```go
20 // New创建一个新工作池
21 func New(maxGoroutines int) *Pool {
22　　 p := Pool{
23　　　　 work: make(chan Worker),
24　　 }
25
26　　 p.wg.Add(maxGoroutines)
27　　 for i := 0; i < maxGoroutines; i++ {
28　　　　 go func() {
29　　　　　　 for w := range p.work {
30　　　　　　　　 w.Task()
31　　　　　　 }
32　　　　　　 p.wg.Done()
33　　　　 }()
34　　 }
35
36　　 return &p
37 }
```

代码清单7-30展示了 `New` 函数，这个函数使用固定数量的goroutine来创建一个工作池。goroutine的数量作为参数传给 `New` 函数。在第22行，创建了一个 `Pool` 类型的值，并使用无缓冲的通道来初始化 `work` 字段。

之后，在第26行，初始化 `WaitGroup` 需要等待的数量，并在第27行到第34行，创建了同样数量的goroutine。这些goroutine只接收 `Worker` 类型的接口值，并调用这个值的 `Task` 方法，如代码清单7-31所示。

代码清单7-31　 `work` /work.go：第28行到第33行

```go
28　　　　 go func() {
29　　　　　　 for w := range p.work {
30　　　　　　　　 w.Task()
31　　　　　　 }
32　　　　　　 p.wg.Done()
33　　　　 }()
```

代码清单7-31里的 `for range` 循环会一直阻塞，直到从 `work` 通道收到一个 `Worker` 接口值。如果收到一个值，就会执行这个值的 `Task` 方法。一旦 `work` 通道被关闭， `for range` 循环就会结束，并调用 `WaitGroup` 的 `Done` 方法。然后goroutine终止。

现在我们可以创建一个等待并执行工作的goroutine池了。让我们看一下如何向池里提交工作，如代码清单7-32所示。

代码清单7-32　 `work` /work.go：第39行到第42行

```go
39 // Run提交工作到工作池
40 func (p *Pool) Run(w Worker) {
41　　 p.work <- w
42 }
```

代码清单7-32展示了 `Run` 方法。这个方法可以向池里提交工作。该方法接受一个 `Worker` 类型的接口值作为参数，并将这个值通过 `work` 通道发送。由于 `work` 通道是一个无缓冲的通道，调用者必须等待工作池里的某个goroutine接收到这个值才会返回。这正是我们想要的，这样可以保证调用的 `Run` 返回时，提交的工作已经开始执行。

在某个时间点，需要关闭工作池。这是 `Shutdown` 方法所做的事情，如代码清单7-33所示。

代码清单7-33　 `work` /work.go：第44行到第48行

```go
44 // Shutdown等待所有goroutine停止工作
45 func (p *Pool) Shutdown() {
46　　 close(p.work)
47　　 p.wg.Wait()
48 }
```

代码清单7-33中的 `Shutdown` 方法做了两件事，首先，它关闭了 `work` 通道，这会导致所有池里的goroutine停止工作，并调用 `WaitGroup` 的 `Done` 方法；然后， `Shutdown` 方法调用 `WaitGroup` 的 `Wait` 方法，这会让 `Shutdown` 方法等待所有goroutine终止。

我们看了 `work` 包的代码，并了解了它是如何工作的，接下来让我们看一下main.go源代码文件中的测试程序，如代码清单7-34所示。

代码清单7-34　 `work` /main/main.go

```go
01 // 这个示例程序展示如何使用work包
02 // 创建一个goroutine池并完成工作
03 package main
04
05 import (
06　　 "log"
07　　 "sync"
08　　 "time"
09
10　　 "github.com/goinaction/code/chapter7/patterns/work"
11 )
12
13 // names提供了一组用来显示的名字
14 var names = []string{
15　　 "steve",
16　　 "bob",
17　　 "mary",
18　　 "therese",
19　　 "jason",
20 }
21
22 // namePrinter使用特定方式打印名字
23 type namePrinter struct {
24　　 name string
25 }
26
27 // Task实现Worker接口
28 func (m *namePrinter) Task() {
29　　 log.Println(m.name)
30　　 time.Sleep(time.Second)
31 }
32
33 // main是所有Go程序的入口
34 func main() {
35　　 // 使用两个goroutine来创建工作池
36　　 p := work.New(2)
37
38　　 var wg sync.WaitGroup
39　　 wg.Add(100 * len(names))
40
41　　 for i := 0; i < 100; i++ {
42　　　　 // 迭代names切片
43　　　　 for _, name := range names {
44　　　　　　 // 创建一个namePrinter并提供
45　　　　　　 // 指定的名字
46　　　　　　 np := namePrinter{
47　　　　　　　　 name: name,
48　　　　　　 }
49
50　　　　　　 go func() {
51　　　　　　　　 // 将任务提交执行。当Run返回时
52　　　　　　　　 // 我们就知道任务已经处理完成
53　　　　　　　　 p.Run(&np)
54　　　　　　　　 wg.Done()
55　　　　　　 }()
56　　　　 }
57　　 }
58
59　　 wg.Wait()
60
61　　 // 让工作池停止工作，等待所有现有的
62　　 // 工作完成
63　　 p.Shutdown()
64 }
```

代码清单7-34展示了使用 `work` 包来完成名字显示工作的测试程序。这段代码一开始在第14行声明了名为 `names` 的包级的变量，这个变量被声明为一个字符串切片。这个切片使用5个名字进行了初始化。然后声明了名为 `namePrinter` 的类型，如代码清单7-35所示。

代码清单7-35　 `work` /main/main.go：第22行到第31行

```go
22 // namePrinter使用特定方式打印名字
23 type namePrinter struct {
24　　 name string
25 }
26
27 // Task实现Worker接口
28 func (m *namePrinter) Task() {
29　　 log.Println(m.name)
30　　 time.Sleep(time.Second)
31 }
```

在代码清单7-35的第23行，声明了 `namePrinter` 类型，接着是这个类型对 `Worker` 接口的实现。这个类型的工作任务是在显示器上显示名字。这个类型只包含一个字段，即 `name` ，它包含要显示的名字。 `Worker` 接口的实现 `Task` 函数用 `log.Println` 函数来显示名字，之后等待1 秒再退出。等待这1秒只是为了让测试程序运行的速度慢一些，以便看到并发的效果。

有了 `Worker` 接口的实现，我们就可以看一下 `main` 函数内部的代码了，如代码清单7-36所示。

代码清单7-36　 `work` /main/main.go：第33行到第64行

```go
33 // main是所有Go程序的入口
34 func main() {
35　　 // 使用两个goroutine来创建工作池
36　　 p := work.New(2)
37
38　　 var wg sync.WaitGroup
39　　 wg.Add(100 * len(names))
40
41　　 for i := 0; i < 100; i++ {
42　　　　 // 迭代names切片
43　　　　 for _, name := range names {
44　　　　　　 // 创建一个namePrinter并提供
45　　　　　　 // 指定的名字
46　　　　　　 np := namePrinter{
47　　　　　　　　 name: name,
48　　　　　　 }
49
50　　　　　　 go func() {
51　　　　　　　　 // 将任务提交执行。当Run返回时
52　　　　　　　　 // 我们就知道任务已经处理完成
53　　　　　　　　 p.Run(&np)
54　　　　　　　　 wg.Done()
55　　　　　　 }()
56　　　　 }
57　　 }
58
59　　 wg.Wait()
60
61　　 // 让工作池停止工作，等待所有现有的
62　　 // 工作完成
63　　 p.Shutdown()
64 }
```

在代码清单7-36第36行，调用 `work` 包里的 `New` 函数创建一个工作池。这个调用传入的参数是2，表示这个工作池只会包含两个执行任务的goroutine。在第38行和第39行，声明了一个 `WaitGroup` ，并初始化为要执行任务的goroutine数。在这个例子里， `names` 切片里的每个名字都会创建100个goroutine来提交任务。这样就会有一堆goroutine互相竞争，将任务提交到池里。

在第41行到第43行，内部和外部的 `for` 循环用来声明并创建所有的goroutine。每次内部循环都会创建一个 `namePrinter` 类型的值，并提供一个用来打印的名字。之后，在第50行，声明了一个匿名函数，并创建一个goroutine执行这个函数。这个goroutine会调用工作池的 `Run` 方法，将 `namePrinter` 的值提交到池里。一旦工作池里的goroutine接收到这个值， `Run` 方法就会返回。这也会导致goroutine将 `WaitGroup` 的计数递减，并终止goroutine。

一旦所有的goroutine都创建完成， `main` 函数就会调用 `WaitGroup` 的 `Wait` 方法。这个调用会等待所有创建的goroutine提交它们的工作。一旦 `Wait` 返回，就会调用工作池的 `Shutdown` 方法来关闭工作池。 `Shutdown` 方法直到所有的工作都做完才会返回。在这个例子里，最多只会等待两个工作的完成。

