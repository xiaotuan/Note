### 6.2　goroutine

让我们再深入了解一下调度器的行为，以及调度器是如何创建goroutine并管理其寿命的。我们会先通过在一个逻辑处理器上运行的例子来讲解，再来讨论如何让goroutine并行运行。代码清单6-1所示的程序会创建两个goroutine，以并发的形式分别显示大写和小写的英文字母。

代码清单6-1　listing01.go

```go
01 // 这个示例程序展示如何创建goroutine
02 // 以及调度器的行为
03 package main
04
05 import (
06　　 "fmt"
07　　 "runtime"
08　　 "sync"
09 )
10
11 // main是所有Go程序的入口
12 func main() {
13　　 // 分配一个逻辑处理器给调度器使用
14　　 runtime.GOMAXPROCS(1)
15
16　　 // wg用来等待程序完成
17　　 // 计数加2，表示要等待两个goroutine
18　　 var wg sync.WaitGroup
19　　 wg.Add(2)
20
21　　 fmt.Println("Start Goroutines")
22
23　　 // 声明一个匿名函数，并创建一个goroutine
24　　 go func() {
25　　　　 // 在函数退出时调用Done来通知main函数工作已经完成
26　　　　 defer wg.Done()
27
28　　　　 // 显示字母表3次
29　　　　 for count := 0; count < 3; count++ {
30　　　　　　 for char := 'a'; char < 'a'+26; char++ {
31　　　　　　　　 fmt.Printf("%c ", char)
32　　　　　　 }
33　　　　 }
34　　 }()
35
36　　 // 声明一个匿名函数，并创建一个goroutine
37　　 go func() {
38　　　　 // 在函数退出时调用Done来通知main函数工作已经完成
39　　　　 defer wg.Done()
40
41　　　　 // 显示字母表3次
42　　　　 for count := 0; count < 3; count++ {
43　　　　　　 for char := 'A'; char < 'A'+26; char++ {
44　　　　　　　　 fmt.Printf("%c ", char)
45　　　　　　 }
46　　　　 }
47　　 }()
48
49　　 // 等待goroutine结束
50　　 fmt.Println("Waiting To Finish")
51　　 wg.Wait()
52
53　　 fmt.Println("\nTerminating Program")
54 }
```

在代码清单6-1的第14行，调用了 `runtime` 包的 `GOMAXPROCS` 函数。这个函数允许程序更改调度器可以使用的逻辑处理器的数量。如果不想在代码里做这个调用，也可以通过修改和这个函数名字一样的环境变量的值来更改逻辑处理器的数量。给这个函数传入1，是通知调度器只能为该程序使用一个逻辑处理器。

在第24行和第37行，我们声明了两个匿名函数，用来显示英文字母表。第24行的函数显示小写字母表，而第37行的函数显示大写字母表。这两个函数分别通过关键字 `go` 创建goroutine来执行。根据代码清单6-2中给出的输出可以看到，每个goroutine执行的代码在一个逻辑处理器上并发运行的效果。

代码清单6-2　listing01.go的输出

```go
Start Goroutines
Waiting To Finish
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m 
n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z
Terminating Program
```

第一个goroutine完成所有显示需要花时间太短了，以至于在调度器切换到第二个goroutine之前，就完成了所有任务。这也是为什么会看到先输出了所有的大写字母，之后才输出小写字母。我们创建的两个goroutine一个接一个地并发运行，独立完成显示字母表的任务。

如代码清单6-3所示，一旦两个匿名函数创建goroutine来执行， `main` 中的代码会继续运行。这意味着 `main` 函数会在goroutine完成工作前返回。如果真的返回了，程序就会在goroutine有机会运行前终止。因此，在第51行， `main` 函数通过 `WaitGroup` ，等待两个goroutine完成它们的工作。

代码清单6-3　listing01.go：第17行到第19行，第23行到第26行，第49行到第51行

```go
16　　 // wg用来等待程序完成
17　　 // 计数加2，表示要等待两个goroutine
18　　 var wg sync.WaitGroup
19　　 wg.Add(2)
23　　 // 声明一个匿名函数，并创建一个goroutine
24　　 go func() {
25　　　　 // 在函数退出时调用Done来通知main函数工作已经完成
26　　　　 defer wg.Done()
49　　 // 等待goroutine结束
50　　 fmt.Println("Waiting To Finish")
51　　 wg.Wait()
```

`WaitGroup` 是一个计数信号量，可以用来记录并维护运行的goroutine。如果 `WaitGroup` 的值大于0， `Wait` 方法就会阻塞。在第18行，创建了一个 `WaitGroup` 类型的变量，之后在第19行，将这个 `WaitGroup` 的值设置为2，表示有两个正在运行的goroutine。为了减小 `WaitGroup` 的值并最终释放 `main` 函数，要在第26和39行，使用 `defer` 声明在函数退出时调用 `Done` 方法。

关键字 `defer` 会修改函数调用时机，在正在执行的函数返回时才真正调用 `defer` 声明的函数。对这里的示例程序来说，我们使用关键字 `defer` 保证，每个goroutine一旦完成其工作就调用 `Done` 方法。

基于调度器的内部算法，一个正运行的goroutine在工作结束前，可以被停止并重新调度。调度器这样做的目的是防止某个goroutine长时间占用逻辑处理器。当goroutine占用时间过长时，调度器会停止当前正运行的goroutine，并给其他可运行的goroutine运行的机会。

图6-4从逻辑处理器的角度展示了这一场景。在第1步，调度器开始运行goroutine A，而goroutine B在运行队列里等待调度。之后，在第2步，调度器交换了goroutine A和goroutine B。由于goroutine A并没有完成工作，因此被放回到运行队列。之后，在第3步，goroutine B完成了它的工作并被系统销毁。这也让goroutine A继续之前的工作。

![40.png](../images/40.png)
<center class="my_markdown"><b class="my_markdown">图6-4　goroutine在逻辑处理器的线程上进行交换</b></center>

可以通过创建一个需要长时间才能完成其工作的goroutine来看到这个行为，如代码清单6-4所示。

代码清单6-4　listing04.go

```go
01 // 这个示例程序展示goroutine调度器是如何在单个线程上
02 // 切分时间片的
03 package main
04
05 import (
06　　 "fmt"
07　　 "runtime"
08　　 "sync"
09 )
10
11 // wg用来等待程序完成
12 var wg sync.WaitGroup
13
14 // main是所有Go程序的入口
15 func main() {
16　　 // 分配一个逻辑处理器给调度器使用
17　　 runtime.GOMAXPROCS(1)
18
19　　 // 计数加2，表示要等待两个goroutine
20　　 wg.Add(2)
21
22　　 // 创建两个goroutine
23　　 fmt.Println("Create Goroutines")
24　　 go printPrime("A")
25　　 go printPrime("B")
26
27　　 // 等待goroutine结束
28　　 fmt.Println("Waiting To Finish")
29　　 wg.Wait()
30
31　　 fmt.Println("Terminating Program")
32 }
33
34 // printPrime 显示5000以内的素数值
35 func printPrime(prefix string) {
36　　 // 在函数退出时调用Done来通知main函数工作已经完成
37　　 defer wg.Done()
38
39 next:
40　　 for outer := 2; outer < 5000; outer++ {
41　　　　 for inner := 2; inner < outer; inner++ {
42　　　　　　 if outer%inner == 0 {
43　　　　　　　　 continue next
44　　　　　　 }
45　　　　 }
46　　　　 fmt.Printf("%s:%d\n", prefix, outer)
47　　 }
48　　 fmt.Println("Completed", prefix)
49 }
```

代码清单6-4中的程序创建了两个goroutine，分别打印1~5000内的素数。查找并显示素数会消耗不少时间，这会让调度器有机会在第一个goroutine找到所有素数之前，切换该goroutine的时间片。

在第12行中，程序启动的时候，声明了一个 `WaitGroup` 变量，并在第20行将其值设置为2。之后在第24行和第25行，在关键字 `go` 后面指定 `printPrime` 函数并创建了两个goroutine来执行。第一个goroutine使用前缀A，第二个goroutine使用前缀B。和其他函数调用一样，创建为goroutine的函数调用时可以传入参数。不过goroutine终止时无法获取函数的返回值。查看代码清单6-5中给出的输出时，会看到调度器在切换第一个goroutine。

代码清单6-5　listing04.go的输出

```go
Create Goroutines
Waiting To Finish
B:2
B:3
...
B:4583
B:4591
A:3　　　　　　 ** 切换goroutine
A:5
...
A:4561
A:4567
B:4603　　　　　** 切换goroutine
B:4621
...
Completed B
A:4457　　　　　** 切换goroutine
A:4463
...
A:4993
A:4999
Completed A
Terminating Program
```

goroutine B先显示素数。一旦goroutine B打印到素数4591，调度器就会将正运行的goroutine切换为goroutine A。之后goroutine A在线程上执行了一段时间，再次切换为goroutine B。这次goroutine B完成了所有的工作。一旦goroutine B返回，就会看到线程再次切换到goroutine A并完成所有的工作。每次运行这个程序，调度器切换的时间点都会稍微有些不同。

代码清单6-1和代码清单6-4中的示例程序展示了调度器如何在一个逻辑处理器上并发运行多个goroutine。像之前提到的，Go标准库的 `runtime` 包里有一个名为 `GOMAXPROCS` 的函数，通过它可以指定调度器可用的逻辑处理器的数量。用这个函数，可以给每个可用的物理处理器在运行的时候分配一个逻辑处理器。代码清单6-6展示了这种改动，让goroutine并行运行。

代码清单6-6　如何修改逻辑处理器的数量

```go
import "runtime"
// 给每个可用的核心分配一个逻辑处理器
runtime.GOMAXPROCS(runtime.NumCPU())
```

包 `runtime` 提供了修改Go语言运行时配置参数的能力。在代码清单6-6里，我们使用两个 `runtime` 包的函数来修改调度器使用的逻辑处理器的数量。函数 `NumCPU` 返回可以使用的物理处理器的数量。因此，调用 `GOMAXPROCS` 函数就为每个可用的物理处理器创建一个逻辑处理器。需要强调的是，使用多个逻辑处理器并不意味着性能更好。在修改任何语言运行时配置参数的时候，都需要配合基准测试来评估程序的运行效果。

如果给调度器分配多个逻辑处理器，我们会看到之前的示例程序的输出行为会有些不同。让我们把逻辑处理器的数量改为2，并再次运行第一个打印英文字母表的示例程序，如代码清单6-7所示。

代码清单6-7　listing07.go

```go
01 // 这个示例程序展示如何创建goroutine
02 // 以及goroutine调度器的行为
03 package main
04
05 import (
06　　 "fmt"
07　　 "runtime"
08　　 "sync"
09 )
10
11 // main是所有Go程序的入口
12 func main() {
13　　 // 分配2个逻辑处理器给调度器使用
14　　 runtime.GOMAXPROCS(2)
15
16　　 // wg用来等待程序完成
17　　 // 计数加2，表示要等待两个goroutine
18　　 var wg sync.WaitGroup
19　　 wg.Add(2)
20
21　　 fmt.Println("Start Goroutines")
22
23　　 // 声明一个匿名函数，并创建一个goroutine
24　　 go func() {
25　　　　 // 在函数退出时调用Done来通知main函数工作已经完成
26　　　　 defer wg.Done()
27
28　　　　 // 显示字母表3次
29　　　　 for count := 0; count < 3; count++ {
30　　　　　　 for char := 'a'; char < 'a'+26; char++ {
31　　　　　　　　 fmt.Printf("%c ", char)
32　　　　　　 }
33　　　　 }
34　　 }()
35
36　　 // 声明一个匿名函数，并创建一个goroutine
37　　 go func() {
38　　　　 // 在函数退出时调用Done来通知main函数工作已经完成
39　　　　 defer wg.Done()
40
41　　　　 // 显示字母表3次
42　　　　 for count := 0; count < 3; count++ {
43　　　　　　 for char := 'A'; char < 'A'+26; char++ {
44　　　　　　　　 fmt.Printf("%c ", char)
45　　　　　　 }
46　　　　 }
47　　 }()
48
49　　 // 等待goroutine结束
50　　 fmt.Println("Waiting To Finish")
51　　 wg.Wait()
52
53　　 fmt.Println("\nTerminating Program")
54 }
```

代码清单6-7中给出的例子在第14行中通过调用 `GOMAXPROCS` 函数创建了两个逻辑处理器。这会让goroutine并行运行，输出结果如代码清单6-8所示。

代码清单6-8　listing07.go的输出

```go
Create Goroutines
Waiting To Finish
A B C a D E b F c G d H e I f J g K h L i M j N k O l P m Q n R o S p T
q U r V s W t X u Y v Z w A x B y C z D a E b F c G d H e I f J g K h L
i M j N k O l P m Q n R o S p T q U r V s W t X u Y v Z w A x B y C z D
a E b F c G d H e I f J g K h L i M j N k O l P m Q n R o S p T q U r V
s W t X u Y v Z w x y z
Terminating Program
```

如果仔细查看代码清单6-8中的输出，会看到goroutine是并行运行的。两个goroutine几乎是同时开始运行的，大小写字母是混合在一起显示的。这是在一台8核的电脑上运行程序的输出，所以每个goroutine独自运行在自己的核上。记住，只有在有多个逻辑处理器且可以同时让每个goroutine运行在一个可用的物理处理器上的时候，goroutine才会并行运行。

现在知道了如何创建goroutine，并了解这背后发生的事情了。下面需要了解一下写并发程序时的潜在危险，以及需要注意的事情。

