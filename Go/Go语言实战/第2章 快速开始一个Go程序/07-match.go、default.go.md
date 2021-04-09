### 2.3.3　match.go/default.go

match.go代码文件包含创建不同类型匹配器的代码，这些匹配器用于在 `Run` 函数里对数据进行搜索。让我们回头看看 `Run` 函数里使用不同匹配器执行搜索的代码，如代码清单2-33所示。

代码清单2-33　search/search.go：第29行到第42行

```go
29     // 为每个数据源启动一个goroutine来查找结果
30     for _, feed := range feeds {
31        // 获取一个匹配器用于查找
32        matcher, exists := matchers[feed.Type]
33        if !exists {
34            matcher = matchers["default"]
35        }
36
37        // 启动一个goroutine执行查找
38        go func(matcher Matcher, feed *Feed) {
39            Match(matcher, feed, searchTerm, results)
40            waitGroup.Done()
41        }(matcher, feed)
42     }
```

代码的第32行，根据数据源类型查找一个匹配器值。这个匹配器值随后会用于在特定的数据源里处理搜索。之后在第38行到第41行启动了一个goroutine，让匹配器对数据源的数据进行搜索。让这段代码起作用的关键是这个架构使用一个接口类型来匹配并执行具有特定实现的匹配器。这样，就能使用这段代码，以一致且通用的方法，来处理不同类型的匹配器值。让我们看一下match.go里的代码，看看如何才能实现这一功能。

代码清单2-34给出的是match.go的前17行代码。

代码清单2-34　search/match.go：第01行到第17行

```go
01 package search
02
03 import (
04     "log"
05 )
06
07 // Result保存搜索的结果
08 type Result struct {
09     Field   string
10     Content string
11 }
12
13 // Matcher定义了要实现的
14 // 新搜索类型的行为
15 type Matcher interface {
16     Search(feed *Feed, searchTerm string) ([]*Result, error)
17 }
```

让我们看一下第15行到第17行，这里声明了一个名为 `Matcher` 的接口类型。之前，我们只见过声明结构类型，而现在看到如何声明一个 `interface` （接口）类型。我们会在第5章介绍接口的更多细节，现在只需要知道， `interface` 关键字声明了一个接口，这个接口声明了结构类型或者具名类型需要实现的行为。一个接口的行为最终由在这个接口类型中声明的方法决定。

对于 `Matcher` 这个接口来说，只声明了一个 `Search` 方法，这个方法输入一个指向 `Feed` 类型值的指针和一个 `string` 类型的搜索项。这个方法返回两个值：一个指向 `Result` 类型值的指针的切片，另一个是错误值。 `Result` 类型的声明在第08行到第11行。

命名接口的时候，也需要遵守Go语言的命名惯例。如果接口类型只包含一个方法，那么这个类型的名字以 `er` 结尾。我们的例子里就是这么做的，所以这个接口的名字叫作 `Matcher` 。如果接口类型内部声明了多个方法，其名字需要与其行为关联。

如果要让一个用户定义的类型实现一个接口，这个用户定义的类型要实现接口类型里声明的所有方法。让我们切换到default.go代码文件，看看默认匹配器是如何实现 `Matcher` 接口的，如代码清单2-35所示。

代码清单2-35　search/default.go：第01行到第15行

```go
01 package search
02
03 // defaultMatcher实现了默认匹配器
04 type defaultMatcher struct{}
05
06 // init函数将默认匹配器注册到程序里
07 func init() {
08     var matcher defaultMatcher
09     Register("default", matcher)
10 }
11
12 // Search 实现了默认匹配器的行为
13 func (m defaultMatcher) Search(feed *Feed, searchTerm string) ([]*Result, error) {
14     return nil, nil
15 }
```

在第04行，我们使用一个空结构声明了一个名叫 `defaultMatcher` 的结构类型。空结构在创建实例时，不会分配任何内存。这种结构很适合创建没有任何状态的类型。对于默认匹配器来说，不需要维护任何状态，所以我们只要实现对应的接口就行。

在第13行到第15行，可以看到 `defaultMatcher` 类型实现 `Matcher` 接口的代码。实现接口的方法 `Search` 只返回两个 `nil` 值。其他的实现，如RSS匹配器的实现，会在这个方法里使用特定的业务逻辑规则来处理搜索。

`Search` 方法的声明也声明了 `defaultMatcher` 类型的值的接收者，如代码清单2-36所示。

代码清单2-36　search/default.go：第13行

```go
13 func (m defaultMatcher) Search
```

如果声明函数的时候带有接收者，则意味着声明了一个方法。这个方法会和指定的接收者的类型绑在一起。在我们的例子里， `Search` 方法与 `defaultMatcher` 类型的值绑在一起。这意味着我们可以使用 `defaultMatcher` 类型的值或者指向这个类型值的指针来调用 `Search` 方法。无论我们是使用接收者类型的值来调用这个方，还是使用接收者类型值的指针来调用这个方法，编译器都会正确地引用或者解引用对应的值，作为接收者传递给 `Search` 方法，如代码清单2-37所示。

代码清单2-37　调用方法的例子

```go
// 方法声明为使用defaultMatcher类型的值作为接收者
func (m defaultMatcher) Search(feed *Feed, searchTerm string)
// 声明一个指向defaultMatcher类型值的指针
dm := new(defaultMatcher)
// 编译器会解开dm指针的引用，使用对应的值调用方法
dm.Search(feed, "test")
// 方法声明为使用指向defaultMatcher类型值的指针作为接收者
func (m *defaultMatcher) Search(feed *Feed, searchTerm string)
// 声明一个defaultMatcher类型的值
var dm defaultMatcher
// 编译器会自动生成指针引用dm值，使用指针调用方法
dm.Search(feed, "test")
```

因为大部分方法在被调用后都需要维护接收者的值的状态，所以，一个最佳实践是，将方法的接收者声明为指针。对于 `defaultMatcher` 类型来说，使用值作为接收者是因为创建一个 `defaultMatcher` 类型的值不需要分配内存。由于 `defaultMatcher` 不需要维护状态，所以不需要指针形式的接收者。

与直接通过值或者指针调用方法不同，如果通过接口类型的值调用方法，规则有很大不同，如代码清单2-38所示。使用指针作为接收者声明的方法，只能在接口类型的值是一个指针的时候被调用。使用值作为接收者声明的方法，在接口类型的值为值或者指针时，都可以被调用。

代码清单2-38　接口方法调用所受限制的例子

```go
// 方法声明为使用指向defaultMatcher类型值的指针作为接收者
func (m *defaultMatcher) Search(feed *Feed, searchTerm string)
// 通过interface类型的值来调用方法
var dm defaultMatcher
var matcher Matcher = dm     // 将值赋值给接口类型
matcher.Search(feed, "test") // 使用值来调用接口方法
> go build
cannot use dm (type defaultMatcher) as type Matcher in assignment
// 方法声明为使用defaultMatcher类型的值作为接收者
func (m defaultMatcher) Search(feed *Feed, searchTerm string)
// 通过interface类型的值来调用方法
var dm defaultMatcher
var matcher Matcher = &dm    // 将指针赋值给接口类型
matcher.Search(feed, "test") // 使用指针来调用接口方法
> go build
Build Successful
```

除了 `Search` 方法， `defaultMatcher` 类型不需要为实现接口做更多的事情了。从这段代码之后，不论是 `defaultMatcher` 类型的值还是指针，都满足 `Matcher` 接口，都可以作为 `Matcher` 类型的值使用。这是代码可以工作的关键。 `defaultMatcher` 类型的值和指针现在还可以作为 `Matcher` 的值，赋值或者传递给接受 `Matcher` 类型值的函数。

让我们看看match.go代码文件里实现 `Match` 函数的代码，如代码清单2-39所示。这个函数在search.go代码文件的第39行中由 `Run` 函数调用。

代码清单2-39　search/match.go：第19行到第33行

```go
19 // Match函数，为每个数据源单独启动goroutine来执行这个函数
20 // 并发地执行搜索
21 func Match(matcher Matcher, feed *Feed, searchTerm string, results chan<- *Result) {
22     // 对特定的匹配器执行搜索
23     searchResults, err := matcher.Search(feed, searchTerm)
24     if err != nil {
25         log.Println(err)
26         return
27     }
28
29     // 将结果写入通道
30     for _, result := range searchResults {
31         results <- result
32     }
33 }
```

这个函数使用实现了 `Matcher` 接口的值或者指针，进行真正的搜索。这个函数接受 `Matcher` 类型的值作为第一个参数。只有实现了 `Matcher` 接口的值或者指针能被接受。因为 `defaultMatcher` 类型使用值作为接收者，实现了这个接口，所以 `defaultMatcher` 类型的值或者指针可以传入这个函数。

在第23行，调用了传入函数的 `Matcher` 类型值的 `Search` 方法。这里执行了 `Matcher` 变量中特定的 `Search` 方法。 `Search` 方法返回后，在第24行检测返回的错误值是否真的是一个错误。如果是一个错误，函数通过 `log` 输出错误信息并返回。如果搜索并没有返回错误，而是返回了搜索结果，则把结果写入通道，以便正在监听通道的 `main` 函数就能收到这些结果。

match.go中的最后一部分代码就是 `main` 函数在第56行调用的 `Display` 函数，如代码清单2-40所示。这个函数会阻止程序终止，直到接收并输出了搜索goroutine返回的所有结果。

代码清单2-40　search/match.go：第35行到第43行

```go
35 // Display从每个单独的goroutine接收到结果后
36 // 在终端窗口输出
37 func Display(results chan *Result) {
38     // 通道会一直被阻塞，直到有结果写入
39     // 一旦通道被关闭，for循环就会终止
40     for result := range results {
41         fmt.Printf("%s:\n%s\n\n", result.Field, result.Content)
42     }
43 }
```

当通道被关闭时，通道和关键字 `range` 的行为，使这个函数在处理完所有结果后才会返回。让我们再来简单看一下 `Run` 函数的代码，特别是关闭 `results` 通道并调用 `Display` 函数那段，如代码清单2-41所示。

代码清单2-41　search/search.go：第44行到第57行

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

第45行到第52行定义的goroutine会等待 `waitGroup` ，直到搜索goroutine调用了 `Done` 方法。一旦最后一个搜索goroutine调用了 `Done` ， `Wait` 方法会返回，之后第51行的代码会关闭 `results` 通道。一旦通道关闭，goroutine就会终止，不再工作。

在match.go代码文件的第30行到第32行，搜索结果会被写入通道，如代码清单2-42所示。

代码清单2-42　search/match.go：第29行到第32行

```go
29     // 将结果写入通道
30     for _, result := range searchResults {
31         results <- result
32     }
```

如果回头看一看match.go代码文件的第40行到第42行的 `for range` 循环，如代码清单2-43所示，我们就能把写入结果、关闭通道和处理结果这些流程串在一起。

代码清单2-43　search/match.go：第38行到第42行

```go
38     // 通道会一直被阻塞，直到有结果写入
39     // 一旦通道被关闭，for循环就会终止
40     for result := range results {
41         fmt.Printf("%s:\n%s\n\n", result.Field, result.Content)
42     }
```

match.go代码文件的第40行的 `for range` 循环会一直阻塞，直到有结果写入通道。在某个搜索goroutine向通道写入结果后（如在match.go代码文件的第31行所见）， `for range` 循环被唤醒，读出这些结果。之后，结果会立刻写到日志中。看上去这个 `for range` 循环会无限循环下去，但其实不然。一旦search.go代码文件第51行关闭了通道， `for range` 循环就会终止， `Display` 函数也会返回。

在我们去看RSS匹配器的实现之前，再看一下程序开始执行时，如何初始化不同的匹配器。为此，我们需要先回头看看default.go代码文件的第07行到第10行，如代码清单2-44所示。

代码清单2-44　search/default.go：第06行到第10行

```go
06 // init函数将默认匹配器注册到程序里
07 func init() {
08     var matcher defaultMatcher
09     Register("default", matcher)
10 }
```

在代码文件default.go里有一个特殊的函数，名叫 `init` 。在main.go代码文件里也能看到同名的函数。我们之前说过，程序里所有的 `init` 方法都会在 `main` 函数启动前被调用。让我们再看看main.go代码文件导入了哪些代码，如代码清单2-45所示。

代码清单2-45　main.go：第07行到第08行

```go
07     _ "github.com/goinaction/code/chapter2/sample/matchers"
08      "github.com/goinaction/code/chapter2/sample/search"
```

第8行导入 `search` 包，这让编译器可以找到default.go代码文件里的 `init` 函数。一旦编译器发现 `init` 函数，它就会给这个函数优先执行的权限，保证其在 `main` 函数之前被调用。

代码文件default.go里的 `init` 函数执行一个特殊的任务。这个函数会创建一个 `defaultMatcher` 类型的值，并将这个值传递给search.go代码文件里的 `Register` 函数，如代码清单2-46所示。

代码清单2-46　search/search.go：第59行到第67行

```go
59 // Register调用时，会注册一个匹配器，提供给后面的程序使用
60 func Register(feedType string, matcher Matcher) {
61     if _, exists := matchers[feedType]; exists {
62         log.Fatalln(feedType, "Matcher already registered")
63     }
64
65     log.Println("Register", feedType, "matcher")
66     matchers[feedType] = matcher
67 }
```

这个函数的职责是，将一个 `Matcher` 值加入到保存注册匹配器的映射中。所有这种注册都应该在 `main` 函数被调用前完成。使用 `init` 函数可以非常完美地完成这种初始化时注册的任务。

