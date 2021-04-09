### 7.1　runner

`runner` 包用于展示如何使用通道来监视程序的执行时间，如果程序运行时间太长，也可以用 `runner` 包来终止程序。当开发需要调度后台处理任务的程序的时候，这种模式会很有用。这个程序可能会作为cron作业执行，或者在基于定时任务的云环境（如iron.io）里执行。

让我们来看一下 `runner` 包里的runner.go代码文件，如代码清单7-1所示。

代码清单7-1　 `runner` /runner.go

```go
 01 // Gabriel Aszalos协助完成了这个示例
 02 // runner包管理处理任务的运行和生命周期
 03 package runner
 04
 05 import (
 06　　 "errors"
 07　　 "os"
 08　　 "os/signal"
 09　　 "time"
 10 )
 11
 12 // Runner在给定的超时时间内执行一组任务，
 13 // 并且在操作系统发送中断信号时结束这些任务
 14 type Runner struct {
 15　　 // interrupt通道报告从操作系统
 16　　 // 发送的信号
 17　　 interrupt chan os.Signal
 18
 19　　 // complete通道报告处理任务已经完成
 20　　 complete chan error
 21
 22　　 // timeout报告处理任务已经超时
 23　　 timeout <-chan time.Time
 24
 25　　 // tasks持有一组以索引顺序依次执行的
 26　　 // 函数
 27　　 tasks []func(int)
 28 }
 29
 30 // ErrTimeout会在任务执行超时时返回
 31 var ErrTimeout = errors.New("received timeout")
 32
 33 // ErrInterrupt会在接收到操作系统的事件时返回
 34 var ErrInterrupt = errors.New("received interrupt")
 35
 36 // New返回一个新的准备使用的Runner
 37 func New(d time.Duration) *Runner {
 38　　 return &Runner{
 39　　　　 interrupt: make(chan os.Signal, 1),
 40　　　　 complete:　make(chan error),
 41　　　　 timeout:　 time.After(d),
 42　　 }
 43 }
 44
 45 // Add将一个任务附加到Runner上。这个任务是一个
 46 // 接收一个int类型的ID作为参数的函数
 47 func (r *Runner) Add(tasks ...func(int)) {
 48　　 r.tasks = append(r.tasks, tasks...)
 49 }
 50
 51 // Start执行所有任务，并监视通道事件
 52 func (r *Runner) Start() error {
 53　　 // 我们希望接收所有中断信号
 54　　 signal.Notify(r.interrupt, os.Interrupt)
 55
 56　　 // 用不同的goroutine执行不同的任务
 57　　 go func() {
 58　　　　 r.complete <- r.run()
 59　　 }()
 60
 61　　 select {
 62　　 // 当任务处理完成时发出的信号
 63　　 case err := <-r.complete:
 64　　　　 return err
 65
 66　　 // 当任务处理程序运行超时时发出的信号
 67　　 case <-r.timeout:
 68　　　　 return ErrTimeout
 69　　 }
 70 }
 71
 72 // run执行每一个已注册的任务
 73 func (r *Runner) run() error {
 74　　 for id, task := range r.tasks {
 75　　　　 // 检测操作系统的中断信号
 76　　　　 if r.gotInterrupt() {
 77　　　　　　 return ErrInterrupt
 78　　　　 }
 79
 80　　　　 // 执行已注册的任务
 81　　　　 task(id)
 82　　 }
 83
 84　　 return nil
 85 }
 86
 87 // gotInterrupt验证是否接收到了中断信号
 88 func (r *Runner) gotInterrupt() bool {
 89　　 select {
 90　　 // 当中断事件被触发时发出的信号
 91　　 case <-r.interrupt:
 92　　　　 // 停止接收后续的任何信号
 93　　　　 signal.Stop(r.interrupt)
 95　　　　 return true
 96
 97　　 // 继续正常运行
 98　　 default:
 99　　　　 return false
100　　 }
101 }
```

代码清单7-1 中的程序展示了依据调度运行的无人值守的面向任务的程序，及其所使用的并发模式。在设计上，可支持以下终止点：

+ 程序可以在分配的时间内完成工作，正常终止；
+ 程序没有及时完成工作，“自杀”；
+ 接收到操作系统发送的中断事件，程序立刻试图清理状态并停止工作。

让我们走查一遍代码，看看每个终止点是如何实现的，如代码清单7-2所示。

代码清单7-2　 `runner` /runner.go：第12行到第28行

```go
12 // Runner在给定的超时时间内执行一组任务，　 
13 // 并且在操作系统发送中断信号时结束这些任务
14 type Runner struct {
15　　 // interrupt通道报告从操作系统
16　　 // 发送的信号
17　　 interrupt chan os.Signal
18
19　　 // complete通道报告处理任务已经完成
20　　 complete chan error
21
22　　 // timeout报告处理任务已经超时
23　　 timeout <-chan time.Time
24
25　　 // tasks持有一组以索引顺序依次执行的
26　　 // 函数
27　　 tasks []func(int)
28 }
```

代码清单7-2从第14行声明 `Runner` 结构开始。这个类型声明了3个通道，用来辅助管理程序的生命周期，以及用来表示顺序执行的不同任务的函数切片。

第17行的 `interrupt` 通道收发 `os.Signal` 接口类型的值，用来从主机操作系统接收中断事件。 `os.Signal` 接口的声明如代码清单7-3所示。

代码清单7-3　golang.org/pkg/os/#Signal

```go
// Signal用来描述操作系统发送的信号。其底层实现通常会
// 依赖操作系统的具体实现：在UNIX系统上是
// syscall.Signal 
type Signal interface {
　　String() string
　　Signal()//用来区分其他Stringer
}
```

代码清单7-3展示了 `os.Signal` 接口的声明。这个接口抽象了不同操作系统上捕获和报告信号事件的具体实现。

第二个字段被命名为 `complete` ，是一个收发 `error` 接口类型值的通道，如代码清单7-4所示。

代码清单7-4　 `runner` /runner.go：第19行到第20行

```go
19　　 // complete通道报告处理任务已经完成
20　　 complete chan error
```

这个通道被命名为 `complete` ，因为它被执行任务的goroutine用来发送任务已经完成的信号。如果执行任务时发生了错误，会通过这个通道发回一个 `error` 接口类型的值。如果没有发生错误，会通过这个通道发回一个 `nil` 值作为 `error` 接口值。

第三个字段被命名为 `timeout` ，接收 `time.Time` 值，如代码清单7-5所示。

代码清单7-5　 `runner` /runner.go：第22行到第23行

```go
22　　 // timeout报告处理任务已经超时
23　　 timeout <-chan time.Time
```

这个通道用来管理执行任务的时间。如果从这个通道接收到一个 `time.Time` 的值，这个程序就会试图清理状态并停止工作。

最后一个字段被命名为 `tasks` ，是一个函数值的切片，如代码清单7-6所示。

代码清单7-6　 `runner` /runner.go：第25行到第27行

```go
25　　 // tasks持有一组以索引顺序依次执行的
26　　 // 函数
27　　 tasks []func(int)
```

这些函数值代表一个接一个顺序执行的函数。会有一个与 `main` 函数分离的goroutine来执行这些函数。

现在已经声明了 `Runner` 类型，接下来看一下两个 `error` 接口变量，这两个变量分别代表不同的错误值，如代码清单7-7所示。

代码清单7-7　 `runner` /runner.go：第30行到第34行

```go
30 // ErrTimeout会在任务执行超时时返回
31 var ErrTimeout = errors.New("received timeout")
32
33 // ErrInterrupt会在接收到操作系统的事件时返回
34 var ErrInterrupt = errors.New("received interrupt")
```

第一个 `error` 接口变量名为 `ErrTimeout` 。这个错误值会在收到超时事件时，由 `Start` 方法返回。第二个 `error` 接口变量名为 `ErrInterrupt` 。这个错误值会在收到操作系统的中断事件时，由 `Start` 方法返回。

现在我们来看一下用户如何创建一个 `Runner` 类型的值，如代码清单7-8所示。

代码清单7-8　 `runner` /runner.go：第36行到第43行

```go
36 // New返回一个新的准备使用的Runner
37 func New(d time.Duration) *Runner {
38　　 return &Runner{
39　　　　 interrupt: make(chan os.Signal, 1),
40　　　　 complete:　make(chan error),
41　　　　 timeout:　 time.After(d),
42　　 }
43 }
```

代码清单7-8 展示了名为 `New` 的工厂函数。这个函数接收一个 `time.Duration` 类型的值，并返回 `Runner` 类型的指针。这个函数会创建一个 `Runner` 类型的值，并初始化每个通道字段。因为 `task` 字段的零值是 `nil` ，已经满足初始化的要求，所以没有被明确初始化。每个通道字段都有独立的初始化过程，让我们探究一下每个字段的初始化细节。

通道 `interrupt` 被初始化为缓冲区容量为1的通道。这可以保证通道至少能接收一个来自语言运行时的 `os.Signal` 值，确保语言运行时发送这个事件的时候不会被阻塞。如果goroutine没有准备好接收这个值，这个值就会被丢弃。例如，如果用户反复敲 Ctrl+C组合键，程序只会在这个通道的缓冲区可用的时候接收事件，其余的所有事件都会被丢弃。

通道 `complete` 被初始化为无缓冲的通道。当执行任务的goroutine完成时，会向这个通道发送一个 `error` 类型的值或者 `nil` 值。之后就会等待 `main` 函数接收这个值。一旦 `main` 接收了这个 `error` 值，goroutine就可以安全地终止了。

最后一个通道 `timeout` 是用 `time` 包的 `After` 函数初始化的。 `After` 函数返回一个 `time.Time` 类型的通道。语言运行时会在指定的 `duration` 时间到期之后，向这个通道发送一个 `time.Time` 的值。

现在知道了如何创建并初始化一个 `Runner` 值，我们再来看一下与 `Runner` 类型关联的方法。第一个方法 `Add` 用来增加一个要执行的任务函数，如代码清单7-9所示。

代码清单7-9　 `runner` /runner.go：第45行到第49行

```go
45 // Add将一个任务附加到Runner上。这个任务是一个
46 // 接收一个int类型的ID作为参数的函数
47 func (r *Runner) Add(tasks ...func(int)) {
48　　 r.tasks = append(r.tasks, tasks...)
49 }
```

代码清单7-9展示了 `Add` 方法，这个方法接收一个名为 `tasks` 的可变参数。 **可变参数** 可以接受任意数量的值作为传入参数。这个例子里，这些传入的值必须是一个接收一个整数且什么都不返回的函数。函数执行时的参数 `tasks` 是一个存储所有这些传入函数值的切片。

现在让我们来看一下 `run` 方法，如代码清单7-10所示。

代码清单7-10　 `runner` /runner.go：第72行到第85行

```go
72 // run执行每一个已注册的任务
73 func (r *Runner) run() error {
74　　 for id, task := range r.tasks {
75　　　　 // 检测操作系统的中断信号
76　　　　 if r.gotInterrupt() {
77　　　　　　 return ErrInterrupt
78　　　　 }
79
80　　　　 // 执行已注册的任务
81　　　　 task(id)
82　　 }
83
84　　 return nil
85 }
```

代码清单7-10的第73行的 `run` 方法会迭代 `tasks` 切片，并按顺序执行每个函数。函数会在第81行被执行。在执行之前，会在第76行调用 `gotInterrupt` 方法来检查是否有要从操作系统接收的事件。

代码清单7-11中的方法 `gotInterrupt` 展示了带 `default` 分支的 `select` 语句的经典用法。

代码清单7-11　 `runner` /runner.go：第87行到第101行

```go
 87 // gotInterrupt验证是否接收到了中断信号
 88 func (r *Runner) gotInterrupt() bool {
 89　　 select {
 90　　 // 当中断事件被触发时发出的信号
 91　　 case <-r.interrupt:
 92　　　　 // 停止接收后续的任何信号
 93　　　　 signal.Stop(r.interrupt)
 95　　　　 return true
 96
 97　　 // 继续正常运行
 98　　 default:
 99　　　　 return false
100　　 }
101 }
```

在第91行，代码试图从 `interrupt` 通道去接收信号。一般来说， `select` 语句在没有任何要接收的数据时会阻塞，不过有了第98行的 `default` 分支就不会阻塞了。 `default` 分支会将接收 `interrupt` 通道的阻塞调用转变为非阻塞的。如果 `interrupt` 通道有中断信号需要接收，就会接收并处理这个中断。如果没有需要接收的信号，就会执行 `default` 分支。

当收到中断信号后，代码会通过在第93行调用 `Stop` 方法来停止接收之后的所有事件。之后函数返回 `true` 。如果没有收到中断信号，在第99行该方法会返回 `false` 。本质上， `gotInterrupt` 方法会让goroutine检查中断信号，如果没有发出中断信号，就继续处理工作。

这个包里的最后一个方法名为 `Start` ，如代码清单7-12所示。

代码清单7-12　 `runner` /runner.go：第51行到第70行

```go
51 // Start执行所有任务，并监视通道事件
52 func (r *Runner) Start() error {
53　　 // 我们希望接收所有中断信号
54　　 signal.Notify(r.interrupt, os.Interrupt)
55
56　　 // 用不同的goroutine执行不同的任务
57　　 go func() {
58　　　　 r.complete <- r.run()
59　　 }()
60
61　　 select {
62　　 // 当任务处理完成时发出的信号
63　　 case err := <-r.complete:
64　　　　 return err
65
66　　 // 当任务处理程序运行超时时发出的信号
67　　 case <-r.timeout:
68　　　　 return ErrTimeout
69　　 }
70 }
```

方法 `Start` 实现了程序的主流程。在代码清单7-12的第52行， `Start` 设置了 `gotInterrupt` 方法要从操作系统接收的中断信号。在第56行到第59行，声明了一个匿名函数，并单独启动goroutine来执行。这个goroutine会执行一系列被赋予的任务。在第58行，在goroutine的内部调用了 `run` 方法，并将这个方法返回的 `error` 接口值发送到 `complete` 通道。一旦 `error` 接口的值被接收，该goroutine就会通过通道将这个值返回给调用者。

创建goroutine后， `Start` 进入一个 `select` 语句，阻塞等待两个事件中的任意一个。如果从 `complete` 通道接收到 `error` 接口值，那么该goroutine要么在规定的时间内完成了分配的工作，要么收到了操作系统的中断信号。无论哪种情况，收到的 `error` 接口值都会被返回，随后方法终止。如果从 `timeout` 通道接收到 `time.Time` 值，就表示goroutine没有在规定的时间内完成工作。这种情况下，程序会返回 `ErrTimeout` 变量。

现在看过了 `runner` 包的代码，并了解了代码是如何工作的，让我们看一下main.go代码文件中的测试程序，如代码清单7-13所示。

代码清单7-13　 `runner` /main/main.go

```go
01 // 这个示例程序演示如何使用通道来监视
02 // 程序运行的时间，以在程序运行时间过长
03 // 时如何终止程序
03 package main
04
05 import (
06　　 "log"
07　　 "time"
08
09　　 "github.com/goinaction/code/chapter7/patterns/runner"
10 )
11
12 // timeout规定了必须在多少秒内处理完成
13 const timeout = 3 * time.Second
14
15 // main是程序的入口
16 func main() {
17　　 log.Println("Starting work.")
18
19　　 // 为本次执行分配超时时间
20　　 r := runner.New(timeout)
21
22　　 // 加入要执行的任务
23　　 r.Add(createTask(), createTask(), createTask())
24
25　　 // 执行任务并处理结果
26　　 if err := r.Start(); err != nil {
27　　　　 switch err {
28　　　　 case runner.ErrTimeout:
29　　　　　　 log.Println("Terminating due to timeout.")
30　　　　　　 os.Exit(1)
31　　　　 case runner.ErrInterrupt:
32　　　　　　 log.Println("Terminating due to interrupt.")
33　　　　　　 os.Exit(2)
34　　　　 }
35　　 }
36
37　　 log.Println("Process ended.")
38 }
39
40 // createTask返回一个根据id 
41 // 休眠指定秒数的示例任务
42 func createTask() func(int) {
43　　 return func(id int) {
44　　　　 log.Printf("Processor - Task #%d.", id)
45　　　　 time.Sleep(time.Duration(id) * time.Second)
46　　 }
47 }
```

代码清单7-13的第16行是 `main` 函数。在第20行，使用 `timeout` 作为超时时间传给 `New` 函数，并返回了一个指向 `Runner` 类型的指针。之后在第23行，使用 `createTask` 函数创建了几个任务，并被加入 `Runner` 里。在第42行声明了 `createTask` 函数。这个函数创建的任务只是休眠了一段时间，用来模拟正在进行工作。增加完任务后，在第26行调用了 `Start` 方法， `main` 函数会等待 `Start` 方法的返回。

当 `Start` 返回时，会检查其返回的 `error` 接口值，并存入 `err` 变量。如果确实发生了错误，代码会根据 `err` 变量的值来判断方法是由于超时终止的，还是由于收到了中断信号终止。如果没有错误，任务就是按时执行完成的。如果执行超时，程序就会用错误码1终止。如果接收到中断信号，程序就会用错误码2终止。其他情况下，程序会使用错误码0正常终止。

