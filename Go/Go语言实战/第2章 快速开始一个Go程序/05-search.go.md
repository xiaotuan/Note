### 2.3.1　search.go

代码清单2-8中展示的是search.go代码文件的前9行代码。之前提到的 `Run` 函数就在这个文件里。

代码清单2-8　search/search.go：第01行到第09行

```go
01 package search
02
03 import (
04     "log"
05     "sync"
06 )
07
08 // 注册用于搜索的匹配器的映射
09 var matchers = make(map[string]Matcher)
```

可以看到，每个代码文件都以 `package` 关键字开头，随后跟着包的名字。文件夹 `search` 下的每个代码文件都使用 `search` 作为包名。第03行到第06行代码导入标准库的 `log` 和 `sync` 包。

与第三方包不同，从标准库中导入代码时，只需要给出要导入的包名。编译器查找包的时候，总是会到 `GOROOT` 和 `GOPATH` 环境变量（如代码清单2-9所示）引用的位置去查找。

代码清单2-9　 `GOROOT` 和 `GOPATH` 环境变量

```go
GOROOT="/Users/me/go"
GOPATH="/Users/me/spaces/go/projects"
```

`log` 包提供打印日志信息到标准输出（ `stdout` ）、标准错误（ `stderr` ）或者自定义设备的功能。 `sync` 包提供同步goroutine的功能。这个示例程序需要用到同步功能。第09行是全书第一次声明一个变量，如代码清单2-10所示。

代码清单2-10　search/search.go：第08行到第09行

```go
08 // 注册用于搜索的匹配器的映射
09 var matchers = make(map[string]Matcher)
```

这个变量没有定义在任何函数作用域内，所以会被当成包级变量。这个变量使用关键字 `var` 声明，而且声明为 `Matcher` 类型的映射（ `map` ），这个映射以 `string` 类型值作为键， `Matcher` 类型值作为映射后的值。 `Matcher` 类型在代码文件matcher.go中声明，后面再讲这个类型的用途。这个变量声明还有一个地方要强调一下：变量名 `matchers` 是以小写字母开头的。

在Go语言里，标识符要么从包里公开，要么不从包里公开。当代码导入了一个包时，程序可以直接访问这个包中任意一个公开的标识符。这些标识符以大写字母开头。以小写字母开头的标识符是不公开的，不能被其他包中的代码直接访问。但是，其他包可以间接访问不公开的标识符。例如，一个函数可以返回一个未公开类型的值，那么这个函数的任何调用者，哪怕调用者不是在这个包里声明的，都可以访问这个值。

这行变量声明还使用赋值运算符和特殊的内置函数 `make` 初始化了变量，如代码清单2-11所示。

代码清单2-11　构建一个映射

```go
make(map[string]Matcher)
```

`map` 是Go语言里的一个引用类型，需要使用 `make` 来构造。如果不先构造 `map` 并将构造后的值赋值给变量，会在试图使用这个 `map` 变量时收到出错信息。这是因为 `map` 变量默认的零值是 `nil` 。在第4章我们会进一步了解关于映射的细节。

在Go语言中，所有变量都被初始化为其零值。对于数值类型，零值是 `0` ；对于字符串类型，零值是空字符串；对于布尔类型，零值是 `false` ；对于指针，零值是 `nil` 。对于引用类型来说，所引用的底层数据结构会被初始化为对应的零值。但是被声明为其零值的引用类型的变量，会返回 `nil` 作为其值。

现在，让我们看看之前在 `main` 函数中调用的 `Run` 函数的内容，如代码清单2-12所示。

代码清单2-12　search/search.go：第11行到第57行

```go
11 // Run执行搜索逻辑
12 func Run(searchTerm string) {
13     // 获取需要搜索的数据源列表
14     feeds, err := RetrieveFeeds()
15     if err != nil {
16         log.Fatal(err)
17     }
18
19     // 创建一个无缓冲的通道，接收匹配后的结果
20     results := make(chan *Result)
21
22     // 构造一个waitGroup，以便处理所有的数据源
23     var waitGroup sync.WaitGroup
24
25     // 设置需要等待处理
26     // 每个数据源的goroutine的数量
27     waitGroup.Add(len(feeds))
28
29     // 为每个数据源启动一个goroutine来查找结果
30     for _, feed := range feeds {
31         // 获取一个匹配器用于查找
32         matcher, exists := matchers[feed.Type]
33         if !exists {
34             matcher = matchers["default"]
35         }
36
37         // 启动一个goroutine来执行搜索
38         go func(matcher Matcher, feed *Feed) {
39             Match(matcher, feed, searchTerm, results)
40             waitGroup.Done()
41         }(matcher, feed)
42     }
43
44     // 启动一个goroutine来监控是否所有的工作都做完了
45     go func() {
46         // 等候所有任务完成
47         waitGroup.Wait()
48
49         // 用关闭通道的方式，通知Display函数
50         // 可以退出程序了
51         close(results)
52     }()
53
54     // 启动函数，显示返回的结果，并且
55     // 在最后一个结果显示完后返回
56     Display(results)
57 }
```

`Run` 函数包括了这个程序最主要的控制逻辑。这段代码很好地展示了如何组织Go程序的代码，以便正确地并发启动和同步goroutine。先来一步一步考察整个逻辑，再考察每步实现代码的细节。

先来看看 `Run` 函数是怎么定义的，如代码清单2-13所示。

代码清单2-13　search/search.go：第11行到第12行

```go
11 // Run 执行搜索逻辑
12 func Run(searchTerm string) {
```

Go语言使用关键字 `func` 声明函数，关键字后面紧跟着函数名、参数以及返回值。对于 `Run` 这个函数来说，只有一个参数，是 `string` 类型的，名叫 `searchTerm` 。这个参数是 `Run` 函数要搜索的搜索项，如果回头看看 `main` 函数（如代码清单2-14所示），可以看到如何传递这个搜索项。

代码清单2-14　main.go：第17行到第21行

```go
17 // main 是整个程序的入口
18 func main() {
19     // 使用特定的项做搜索
20     search.Run("president")
21 }
```

`Run` 函数做的第一件事情就是获取数据源 `feeds` 列表。这些数据源从互联网上抓取数据，之后对数据使用特定的搜索项进行匹配，如代码清单2-15所示。

代码清单2-15　search/search.go：第13行到第17行

```go
13     // 获取需要搜索的数据源列表
14     feeds, err := RetrieveFeeds()
15     if err != nil {
16         log.Fatal(err)
17     }
```

这里有几个值得注意的重要概念。第14行调用了 `search` 包的 `RetrieveFeeds` 函数。这个函数返回两个值。第一个返回值是一组 `Feed` 类型的切片。切片是一种实现了一个动态数组的引用类型。在Go语言里可以用切片来操作一组数据。第4章会进一步深入了解有关切片的细节。

第二个返回值是一个错误值。在第15行，检查返回的值是不是真的是一个错误。如果真的发生错误了，就会调用 `log` 包里的 `Fatal` 函数。 `Fatal` 函数接受这个错误的值，并将这个错误在终端窗口里输出，随后终止程序。

不仅仅是Go语言，很多语言都允许一个函数返回多个值。一般会像 `RetrieveFeeds` 函数这样声明一个函数返回一个值和一个错误值。如果发生了错误，永远不要使用该函数返回的另一个值<a class="my_markdown" href="['#anchor21']"><sup class="my_markdown">①</sup></a>。这时必须忽略另一个值，否则程序会产生更多的错误，甚至崩溃。

让我们仔细看看从函数返回的值是如何赋值给变量的，如代码清单2-16所示。

代码清单2-16　search/search.go：第13行到第14行

```go
13     // 获取需要搜索的数据源列表
14     feeds, err := RetrieveFeeds()
```

这里可以看到简化变量声明运算符（ `:=` ）。这个运算符用于声明一个变量，同时给这个变量赋予初始值。编译器使用函数返回值的类型来确定每个变量的类型。简化变量声明运算符只是一种简化记法，让代码可读性更高。这个运算符声明的变量和其他使用关键字 `var` 声明的变量没有任何区别。

现在我们得到了数据源列表，进入到后面的代码，如代码清单2-17所示。

代码清单2-17　search/search.go：第19行到第20行

```go
19     // 创建一个无缓冲的通道，接收匹配后的结果
20     results := make(chan *Result)
```

在第20行，我们使用内置的 `make` 函数创建了一个无缓冲的通道。我们使用简化变量声明运算符，在调用 `make` 的同时声明并初始化该通道变量。根据经验，如果需要声明初始值为零值的变量，应该使用 `var` 关键字声明变量；如果提供确切的非零值初始化变量或者使用函数返回值创建变量，应该使用简化变量声明运算符。

在Go语言中，通道（channel）和映射（map）与切片（slice）一样，也是引用类型，不过通道本身实现的是一组带类型的值，这组值用于在goroutine之间传递数据。通道内置同步机制，从而保证通信安全。在第6章中，我们会介绍更多关于通道和goroutine的细节。

之后两行是为了防止程序在全部搜索执行完之前终止，如代码清单2-18所示。

代码清单2-18　search/search.go：第22行到第27行

```go
22     // 构造一个wait group，以便处理所有的数据源
23     var waitGroup sync.WaitGroup
24
25     // 设置需要等待处理
26     // 每个数据源的goroutine的数量
27     waitGroup.Add(len(feeds))
```

在Go语言中，如果 `main` 函数返回，整个程序也就终止了。Go程序终止时，还会关闭所有之前启动且还在运行的goroutine。写并发程序的时候，最佳做法是，在 `main` 函数返回前，清理并终止所有之前启动的goroutine。编写启动和终止时的状态都很清晰的程序，有助减少bug，防止资源异常。

这个程序使用 `sync` 包的 `WaitGroup` 跟踪所有启动的goroutine。非常推荐使用 `WaitGroup` 来跟踪goroutine的工作是否完成。 `WaitGroup` 是一个计数信号量，我们可以利用它来统计所有的goroutine是不是都完成了工作。

在第23行我们声明了一个 `sync` 包里的 `WaitGroup` 类型的变量。之后在第27行，我们将 `WaitGroup` 变量的值设置为将要启动的goroutine的数量。马上就能看到，我们为每个数据源都启动了一个goroutine来处理数据。每个goroutine完成其工作后，就会递减 `WaitGroup` 变量的计数值，当这个值递减到0时，我们就知道所有的工作都做完了。

现在让我们来看看为每个数据源启动goroutine的代码，如代码清单2-19所示。

代码清单2-19　search/search.go：第29行到第42行

```go
29     // 为每个数据源启动一个goroutine来查找结果
30     for _, feed := range feeds {
31         // 获取一个匹配器用于查找
32         matcher, exists := matchers[feed.Type]
33         if !exists {
34             matcher = matchers["default"]
35         }
36
37         // 启动一个 goroutine来执行搜索
38         go func(matcher Matcher, feed *Feed) {
39             Match(matcher, feed, searchTerm, results)
40             waitGroup.Done()
41         }(matcher, feed)
42     }
```

第30行到第42行迭代之前获得的 `feeds` ，为每个 `feed` 启动一个goroutine。我们使用关键字 `for range` 对 `feeds` 切片做迭代。关键字 `range` 可以用于迭代数组、字符串、切片、映射和通道。使用 `for range` 迭代切片时，每次迭代会返回两个值。第一个值是迭代的元素在切片里的索引位置，第二个值是元素值的一个副本。

如果仔细看一下第30行的 `for range` 语句，会发现再次使用了下划线标识符，如代码清单2-20所示。

代码清单2-20　search/search.go：第29行到第30行

```go
29     // 为每个数据源启动一个 goroutine来查找结果
30     for _, feed := range feeds {
```

这是第二次看到使用了下划线标识符。第一次是在main.go里导入 `matchers` 包的时候。这次，下划线标识符的作用是占位符，占据了保存 `range` 调用返回的索引值的变量的位置。如果要调用的函数返回多个值，而又不需要其中的某个值，就可以使用下划线标识符将其忽略。在我们的例子里，我们不需要使用返回的索引值，所以就使用下划线标识符把它忽略掉。

在循环中，我们首先通过 `map` 查找到一个可用于处理特定数据源类型的数据的 `Matcher` 值，如代码清单2-21所示。

代码清单2-21　search/search.go：第31行到第35行

```go
31         // 获取一个匹配器用于查找
32         matcher, exists := matchers[feed.Type]
33         if !exists {
34             matcher = matchers["default"]
35         }
```

我们还没有说过 `map` 里面的值是如何获得的。一会儿就会在程序初始化的时候看到如何设置 `map` 里的值。在第32行，我们检查 `map` 是否含有符合数据源类型的值。查找 `map` 里的键时，有两个选择：要么赋值给一个变量，要么为了精确查找，赋值给两个变量。赋值给两个变量时第一个值和赋值给一个变量时的值一样，是 `map` 查找的结果值。如果指定了第二个值，就会返回一个布尔标志，来表示查找的键是否存在于 `map` 里。如果这个键不存在， `map` 会返回其值类型的零值作为返回值，如果这个键存在， `map` 会返回键所对应值的副本。

在第33行，我们检查这个键是否存在于 `map` 里。如果不存在，使用默认匹配器。这样程序在不知道对应数据源的具体类型时，也可以执行，而不会中断。之后，启动一个goroutine来执行搜索，如代码清单2-22所示。

代码清单2-22　search/search.go：第37行到第41行

```go
37         // 启动一个 goroutine来执行搜索
38         go func(matcher Matcher, feed *Feed) {
39             Match(matcher, feed, searchTerm, results)
40             waitGroup.Done()
41         }(matcher, feed)
```

我们会在第6章进一步学习goroutine，现在只要知道，一个goroutine是一个独立于其他函数运行的函数。使用关键字 `go` 启动一个goroutine，并对这个goroutine做并发调度。在第38行，我们使用关键字 `go` 启动了一个匿名函数作为goroutine。 **匿名函数** 是指没有明确声明名字的函数。在 `for range` 循环里，我们为每个数据源，以goroutine的方式启动了一个匿名函数。这样可以并发地独立处理每个数据源的数据。

匿名函数也可以接受声明时指定的参数。在第38行，我们指定匿名函数要接受两个参数，一个类型为 `Matcher` ，另一个是指向一个 `Feed` 类型值的指针。这意味着变量 `feed` 是一个 **指针变量** 。指针变量可以方便地在函数之间共享数据。使用指针变量可以让函数访问并修改一个变量的状态，而这个变量可以在其他函数甚至是其他goroutine的作用域里声明。

在第41行， `matcher` 和 `feed` 两个变量的值被传入匿名函数。在Go语言中，所有的变量都以值的方式传递。因为指针变量的值是所指向的内存地址，在函数间传递指针变量，是在传递这个地址值，所以依旧被看作以值的方式在传递。

在第39行到第40行，可以看到每个goroutine是如何工作的，如代码清单2-23所示。

代码清单2-23　search/search.go：第39行到第40行

```go
39         Match(matcher, feed, searchTerm, results)
40         waitGroup.Done()
```

goroutine做的第一件事是调用一个叫 `Match` 的函数，这个函数可以在match.go文件里找到。 `Match` 函数的参数是一个 `Matcher` 类型的值、一个指向 `Feed` 类型值的指针、搜索项以及输出结果的通道。我们一会儿再看这个函数的内部细节，现在只要知道， `Match` 函数会搜索数据源的数据，并将匹配结果输出到 `results` 通道。

一旦 `Match` 函数调用完毕，就会执行第40行的代码，递减 `WaitGroup` 的计数。一旦每个goroutine都执行调用 `Match` 函数和 `Done` 方法，程序就知道每个数据源都处理完成。调用 `Done` 方法这一行还有一个值得注意的细节： `WaitGroup` 的值没有作为参数传入匿名函数，但是匿名函数依旧访问到了这个值。

Go语言支持闭包，这里就应用了闭包。实际上，在匿名函数内访问 `searchTerm` 和 `results` 变量，也是通过闭包的形式访问的。因为有了闭包，函数可以直接访问到那些没有作为参数传入的变量。匿名函数并没有拿到这些变量的副本，而是直接访问外层函数作用域中声明的这些变量本身。因为 `matcher` 和 `feed` 变量每次调用时值不相同，所以并没有使用闭包的方式访问这两个变量，如代码清单2-24所示。

代码清单2-24　search/search.go：第29行到第32行

```go
29     // 为每个数据源启动一个goroutine来查找结果
30     for _, feed := range feeds {
31         // 获取一个匹配器用于查找
32         matcher, exists := matchers[feed.Type]
```

可以看到，在第30行到第32行，变量 `feed` 和 `matcher` 的值会随着循环的迭代而改变。如果我们使用闭包访问这些变量，随着外层函数里变量值的改变，内层的匿名函数也会感知到这些改变。所有的goroutine都会因为闭包共享同样的变量。除非我们以函数参数的形式传值给函数，否则绝大部分goroutine最终都会使用同一个 `matcher` 来处理同一个 `feed` ——这个值很有可能是 `feeds` 切片的最后一个值。

随着每个goroutine搜索工作的运行，将结果发送到 `results` 通道，并递减 `waitGroup` 的计数，我们需要一种方法来显示所有的结果，并让 `main` 函数持续工作，直到完成所有的操作，如代码清单2-25所示。

代码清单2-25　search/search.go：第44行到第57行

```go
44     // 启动一个goroutine来监控是否所有的工作都做完了
45     go func() {
46         // 等候所有任务完成
47         waitGroup.Wait()
48
49         // 用关闭通道的方式，通知Display函数
50         // 可以退出程序了
51         close(results)
52     }()
53
54     // 启动函数，显示返回的结果， 
55     // 并且在最后一个结果显示完后返回
56     Display(results)
57 }
```

第45行到第56行的代码解释起来比较麻烦，等我们看完 `search` 包里的其他代码后再来解释。我们现在只解释表面的语法，随后再来解释底层的机制。在第45行到第52行，我们以goroutine的方式启动了另一个匿名函数。这个匿名函数没有输入参数，使用闭包访问了 `WaitGroup` 和 `results` 变量。这个goroutine里面调用了 `WaitGroup` 的 `Wait` 方法。这个方法会导致goroutine阻塞，直到 `WaitGroup` 内部的计数到达0。之后，goroutine调用了内置的 `close` 函数，关闭了通道，最终导致程序终止。

`Run` 函数的最后一段代码是第56行。这行调用了match.go文件里的 `Display` 函数。一旦这个函数返回，程序就会终止。而之前的代码保证了所有 `results` 通道里的数据被处理之前， `Display` 函数不会返回。

