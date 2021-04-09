### 7.2　pool

本章会介绍 `pool` 包<a class="my_markdown" href="['#anchor71']"><sup class="my_markdown">①</sup></a>。这个包用于展示如何使用有缓冲的通道实现资源池，来管理可以在任意数量的goroutine之间共享及独立使用的资源。这种模式在需要共享一组静态资源的情况（如共享数据库连接或者内存缓冲区）下非常有用。如果goroutine需要从池里得到这些资源中的一个，它可以从池里申请，使用完后归还到资源池里。

让我们看一下 `pool` 包里的 pool.go 代码文件，如代码清单7-14所示。

代码清单7-14　 `pool` /pool.go

```go
 01 // Fatih Arslan和Gabriel Aszalos协助完成了这个示例
 02 // 包pool管理用户定义的一组资源
 03 package pool
 04
 05 import (
 06　　 "errors"
 07　　 "log"
 08　　 "io"
 09　　 "sync"
 10 )
 11
 12 // Pool管理一组可以安全地在多个goroutine间
 13 // 共享的资源。被管理的资源必须
 14 // 实现io.Closer接口
 15 type Pool struct {
 16　　 m　　　　　sync.Mutex
 17　　 resources　chan io.Closer
 18　　 factory　　func() (io.Closer, error)
 19　　 closed　　 bool
 20 }
 21
 22 // ErrPoolClosed表示请求（Acquire）了一个
 23 // 已经关闭的池
 24 var ErrPoolClosed = errors.New("Pool has been closed.")
 25
 26 // New创建一个用来管理资源的池。
 27 // 这个池需要一个可以分配新资源的函数， 
 28 // 并规定池的大小
 29 func New(fn func() (io.Closer, error), size uint) (*Pool, error) {
 30　　 if size <= 0 {
 31　　　　 return nil, errors.New("Size value too small.")
 32　　 }
 33
 34　　 return &Pool{
 35　　　　 factory:　 fn,
 36　　　　 resources: make(chan io.Closer, size),
 37　　 }, nil
 38 }
 39
 40 // Acquire从池中获取一个资源
 41 func (p *Pool) Acquire() (io.Closer, error) {
 42　　 select {
 43　　 // 检查是否有空闲的资源
 44　　 case r, ok := <-p.resources:
 45　　　　 log.Println("Acquire:", "Shared Resource")
 46　　　　 if !ok {
 47　　　　　　 return nil, ErrPoolClosed
 48　　　　 }
 49　　　　 return r, nil
 50
 51　　 // 因为没有空闲资源可用，所以提供一个新资源
 52　　 default:
 53　　　　 log.Println("Acquire:", "New Resource")
 54　　　　 return p.factory()
 55　　 }
 56 }
 57
 58 // Release将一个使用后的资源放回池里
 59 func (p *Pool) Release(r io.Closer) {
 60　　 // 保证本操作和Close操作的安全
 61　　 p.m.Lock()
 62　　 defer p.m.Unlock()
 63
 64　　 // 如果池已经被关闭，销毁这个资源
 65　　 if p.closed {
 66　　　　 r.Close()
 67　　　　 return
 68　　 }
 69
 70　　 select {
 71　　 // 试图将这个资源放入队列
 72　　 case p.resources <- r:
 73　　　　 log.Println("Release:", "In Queue")
 74
 75　　 // 如果队列已满，则关闭这个资源
 76　　 default:
 77　　　　 log.Println("Release:", "Closing")
 78　　　　 r.Close()
 79　　 }
 80 }
 81
 82 // Close会让资源池停止工作，并关闭所有现有的资源
 83 func (p *Pool) Close() {
 84　　 // 保证本操作与Release操作的安全
 85　　 p.m.Lock()
 86　　 defer p.m.Unlock()
 87
 88　　 // 如果pool已经被关闭，什么也不做
 89　　 if p.closed {
 90　　　　 return
 91　　 }
 92
 93　　 // 将池关闭
 94　　 p.closed = true
 95
 96　　 // 在清空通道里的资源之前，将通道关闭
 97　　 // 如果不这样做，会发生死锁
 98　　 close(p.resources)
 99
100　　 // 关闭资源
101　　 for r := range p.resources {
102　　　　 r.Close()
103　　 }
104 }
```

代码清单7-14中的 `pool` 包的代码声明了一个名为 `Pool` 的结构，该结构允许调用者根据所需数量创建不同的资源池。只要某类资源实现了 `io.Closer` 接口，就可以用这个资源池来管理。让我们看一下 `Pool` 结构的声明，如代码清单7-15所示。

代码清单7-15　 `pool` /pool.go：第12行到第20行

```go
12 // Pool管理一组可以安全地在多个goroutine间
13 // 共享的资源。被管理的资源必须
14 // 实现io.Closer接口
15 type Pool struct {
16　　 m　　　　 sync.Mutex
17　　 resources chan io.Closer
18　　 factory　 func() (io.Closer, error)
19　　 closed　　bool
20 }
```

`Pool` 结构声明了4个字段，每个字段都用来辅助以goroutine安全的方式来管理资源池。在第16行，结构以一个 `sync.Mutex` 类型的字段开始。这个互斥锁用来保证在多个goroutine访问资源池时，池内的值是安全的。第二个字段名为 `resources` ，被声明为 `io.Closer` 接口类型的通道。这个通道是作为一个有缓冲的通道创建的，用来保存共享的资源。由于通道的类型是一个接口，所以池可以管理任意实现了 `io.Closer` 接口的资源类型。

`factory` 字段是一个函数类型。任何一个没有输入参数且返回一个 `io.Closer` 和一个 `error` 接口值的函数，都可以赋值给这个字段。这个函数的目的是，当池需要一个新资源时，可以用这个函数创建。这个函数的实现细节超出了 `pool` 包的范围，并且需要由包的使用者实现并提供。

第19行中的最后一个字段是 `closed` 字段。这个字段是一个标志，表示 `Pool` 是否已经被关闭。现在已经了解了 `Pool` 结构的声明，让我们看一下第24行声明的 `error` 接口变量，如代码清单7-16所示。

代码清单7-16　 `pool` /pool.go：第22行到第24行

```go
22 // ErrPoolClosed表示请求（Acquire）了一个
23 // 已经关闭的池
24 var ErrPoolClosed = errors.New("Pool has been closed.")
```

Go语言里会经常创建 `error` 接口变量。这可以让调用者来判断某个包里的函数或者方法返回的具体的错误值。当调用者对一个已经关闭的池调用 `Acquire` 方法时，会返回代码清单7-16里的 `error` 接口变量。因为 `Acquire` 方法可能返回多个不同类型的错误，所以 `Pool` 已经关闭时会关闭时返回这个错误变量可以让调用者从其他错误中识别出这个特定的错误。

既然已经声明了 `Pool` 类型和 `error` 接口值，我们就可以开始看一下 `pool` 包里声明的函数和方法了。让我们从池的工厂函数开始，这个函数名为 `New` ，如代码清单7-17所示。

代码清单7-17　 `pool` /pool.go：第26行到第38行

```go
26 // New创建一个用来管理资源的池。
27 // 这个池需要一个可以分配新资源的函数， 
28 // 并规定池的大小
29 func New(fn func() (io.Closer, error), size uint) (*Pool, error) {
30　　 if size <= 0 {
31　　　　 return nil, errors.New("Size value too small.")
32　　 }
33
34　　 return &Pool{
35　　　　 factory:　 fn,
36　　　　 resources: make(chan io.Closer, size),
37　　 }, nil
38 }
```

代码清单7-17中的 `New` 函数接受两个参数，并返回两个值。第一个参数 `fn` 声明为一个函数类型，这个函数不接受任何参数，返回一个 `io.Closer` 和一个 `error` 接口值。这个作为参数的函数是一个工厂函数，用来创建由池管理的资源的值。第二个参数 `size` 表示为了保存资源而创建的有缓冲的通道的缓冲区大小。

第30行检查了 `size` 的值，保证这个值不小于等于0。如果这个值小于等于0，就会使用 `nil` 值作为返回的 `pool` 指针值，然后为该错误创建一个 `error` 接口值。因为这是这个函数唯一可能返回的错误值，所以不需要为这个错误单独创建和使用一个 `error` 接口变量。如果能够接受传入的 `size` ，就会创建并初始化一个新的 `Pool` 值。在第35行，函数参数 `fn` 被赋值给 `factory` 字段，并且在第36行，使用 `size` 值创建有缓冲的通道。在 `return` 语句里，可以构造并初始化任何值。因此，第34行的 `return` 语句用指向新创建的 `Pool` 类型值的指针和 `nil` 值作为 `error` 接口值，返回给函数的调用者。

在创建并初始化 `Pool` 类型的值之后，接下来让我们来看一下 `Acquire` 方法，如代码清单7-18所示。这个方法可以让调用者从池里获得资源。

代码清单7-18　 `pool` /pool.go：第40行到第56行

```go
40 // Acquire从池中获取一个资源
41 func (p *Pool) Acquire() (io.Closer, error) {
42　　 select {
43　　 // 检查是否有空闲的资源
44　　 case r, ok := <-p.resources:
45　　　　 log.Println("Acquire:", "Shared Resource")
46　　　　 if !ok {
47　　　　　　 return nil, ErrPoolClosed
48　　　　 }
49　　　　 return r, nil
50
51　　 // 因为没有空闲资源可用，所以提供一个新资源
52　　 default:
53　　　　 log.Println("Acquire:", "New Resource")
54　　　　 return p.factory()
55　　 }
56 }
```

代码清单7-18包含了 `Acquire` 方法的代码。这个方法在还有可用资源时会从资源池里返回一个资源，否则会为该调用创建并返回一个新的资源。这个实现是通过 `select/case` 语句来检查有缓冲的通道里是否还有资源来完成的。如果通道里还有资源，如第44行到第49行所写，就取出这个资源，并返回给调用者。如果该通道里没有资源可取，就会执行 `default` 分支。在这个示例中，在第54行执行用户提供的工厂函数，并且创建并返回一个新资源。

如果不再需要已经获得的资源，必须将这个资源释放回资源池里。这是 `Release` 方法的任务。不过在理解 `Release` 方法的代码背后的机制之前，我们需要先看一下 `Close` 方法，如代码清单7-19所示。

代码清单7-19　 `pool` /pool.go：第82行到第104行

```go
 82 // Close会让资源池停止工作，并关闭所有现有的资源
 83 func (p *Pool) Close() {
 84　　 // 保证本操作与Release操作的安全
 85　　 p.m.Lock()
 86　　 defer p.m.Unlock()
 87
 88　　 // 如果pool已经被关闭，什么也不做
 89　　 if p.closed {
 90　　　　 return
 91　　 }
 92
 93　　 // 将池关闭
 94　　 p.closed = true
 95
 96　　 // 在清空通道里的资源之前，将通道关闭
 97　　 // 如果不这样做，会发生死锁
 98　　 close(p.resources)
 99
100　　 // 关闭资源
101　　 for r := range p.resources {
102　　　　 r.Close()
103　　 }
104 }
```

一旦程序不再使用资源池，需要调用这个资源池的 `Close` 方法。代码清单7-19中展示了 `Close` 方法的代码。在第98行到第101行，这个方法关闭并清空了有缓冲的通道，并将缓冲的空闲资源关闭。需要注意的是，在同一时刻只能有一个goroutine执行这段代码。事实上，当这段代码被执行时，必须保证其他goroutine中没有同时执行 `Release` 方法。你一会儿就会理解为什么这很重要。

在第85行到第86行，互斥量被加锁，并在函数返回时解锁。在第89行，检查 `closed` 标志，判断池是不是已经关闭。如果已经关闭，该方法会直接返回，并释放锁。如果这个方法第一次被调用，就会将这个标志设置为 `true` ，并关闭且清空 `resources` 通道。

现在我们可以看一下 `Release` 方法，看看这个方法是如何和 `Close` 方法配合的，如代码清单7-20所示。

代码清单7-20　 `pool` /pool.go：第58行到第80行

```go
58 // Release将一个使用后的资源放回池里
59 func (p *Pool) Release(r io.Closer) {
60　　 // 保证本操作和Close操作的安全
61　　 p.m.Lock()
62　　 defer p.m.Unlock()
63
64　　 // 如果池已经被关闭，销毁这个资源
65　　 if p.closed {
66　　　　 r.Close()
67　　　　 return
68　　 }
69
70　　 select {
71　　 // 试图将这个资源放入队列
72　　 case p.resources <- r:
73　　　　 log.Println("Release:", "In Queue")
74
75　　 // 如果队列已满，则关闭这个资源
76　　 default:
77　　　　 log.Println("Release:", "Closing")
78　　　　 r.Close()
79　　 }
80 }
```

在代码清单7-20中可以找到 `Release` 方法的实现。该方法一开始在第61行和第62行对互斥量进行加锁和解锁。这和 `Close` 方法中的互斥量是同一个互斥量。这样可以阻止这两个方法在不同goroutine里同时运行。使用互斥量有两个目的。第一，可以保护第65行中读取 `closed` 标志的行为，保证同一时刻不会有其他goroutine调用 `Close` 方法写同一个标志。第二，我们不想往一个已经关闭的通道里发送数据，因为那样会引起崩溃。如果 `closed` 标志是 `true` ，我们就知道 `resources` 通道已经被关闭。

在第66行，如果池已经被关闭，会直接调用资源值 `r` 的 `Close` 方法。因为这时已经清空并关闭了池，所以无法将资源重新放回到该资源池里。对 `closed` 标志的读写必须进行同步，否则可能误导其他goroutine，让其认为该资源池依旧是打开的，并试图对通道进行无效的操作。

现在看过了池的代码，了解了池是如何工作的，让我们看一下main.go代码文件里的测试程序，如代码清单7-21所示。

代码清单7-21　 `pool` /main/main.go

```go
01 // 这个示例程序展示如何使用pool包
02 // 来共享一组模拟的数据库连接
03 package main
04
05 import (
06　　 "log"
07　　 "io"
08　　 "math/rand"
09　　 "sync"
10　　 "sync/atomic"
11　　 "time"
12
13　　 "github.com/goinaction/code/chapter7/patterns/pool"
14 )
15
16 const (
17　　 maxGoroutines　 = 25 // 要使用的goroutine的数量
18　　 pooledResources = 2　// 池中的资源的数量
19 )
20
21 // dbConnection模拟要共享的资源
22 type dbConnection struct {
23　　 ID int32
24 }
25
26 // Close实现了io.Closer接口，以便dbConnection
27 // 可以被池管理。Close用来完成任意资源的
28 // 释放管理
29 func (dbConn *dbConnection) Close() error {
30　　 log.Println("Close: Connection", dbConn.ID)
31　　 return nil
32 }
33
34 // idCounter用来给每个连接分配一个独一无二的id
35 var idCounter int32
36
37 // createConnection是一个工厂函数， 
38 // 当需要一个新连接时，资源池会调用这个函数
39 func createConnection() (io.Closer, error) {
40　　 id := atomic.AddInt32(&idCounter, 1)
41　　 log.Println("Create: New Connection", id)
42
43　　 return &dbConnection{id}, nil
44 }
45
46 // main是所有Go程序的入口
47 func main() {
48　　 var wg sync.WaitGroup
49　　 wg.Add(maxGoroutines)
50
51　　 // 创建用来管理连接的池
52　　 p, err := pool.New(createConnection, pooledResources)
53　　 if err != nil {
54　　　　 log.Println(err)
55　　 }
56
57　　 // 使用池里的连接来完成查询
58　　 for query := 0; query < maxGoroutines; query++ {
59　　　　 // 每个goroutine需要自己复制一份要
60　　　　 // 查询值的副本，不然所有的查询会共享
61　　　　 // 同一个查询变量
62　　　　 go func(q int) {
63　　　　　　 performQueries(q, p)
64　　　　　　 wg.Done()
65　　　　 }(query)
66　　 }
67
68　　 // 等待goroutine结束
69　　 wg.Wait()
70
71　　 // 关闭池
72　　 log.Println("Shutdown Program.")
73　　 p.Close()
74 }
75
76 // performQueries用来测试连接的资源池
77 func performQueries(query int, p *pool.Pool) {
78　　 // 从池里请求一个连接
79　　 conn, err := p.Acquire()
80　　 if err != nil {
81　　　　 log.Println(err)
82　　　　 return
83　　 }
84
85　　 // 将该连接释放回池里
86　　 defer p.Release(conn)
87
88　　 // 用等待来模拟查询响应
89　　 time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
90　　 log.Printf("QID[%d] CID[%d]\n", query, conn.(*dbConnection).ID)
91 }
```

代码清单7-21展示的main.go中的代码使用 `pool` 包来管理一组模拟数据库连接的连接池。代码一开始声明了两个常量 `maxGoroutines` 和 `pooledResource` ，用来设置goroutine的数量以及程序将要使用资源的数量。资源的声明以及 `io.Closer` 接口的实现如代码清单7-22所示。

代码清单7-22　 `pool` /main/main.go：第21行到第32行

```go
21 // dbConnection模拟要共享的资源
22 type dbConnection struct {
23　　 ID int32
24 }
25
26 // Close实现了io.Closer接口，以便dbConnection
27 // 可以被池管理。Close用来完成任意资源的
28 // 释放管理
29 func (dbConn *dbConnection) Close() error {
30　　 log.Println("Close: Connection", dbConn.ID)
31　　 return nil
32 }
```

代码清单7-22展示了 `dbConnection` 结构的声明以及 `io.Closer` 接口的实现。 `dbConnection` 类型模拟了管理数据库连接的结构，当前版本只包含一个字段 `ID` ，用来保存每个连接的唯一标识。 `Close` 方法只是报告了连接正在被关闭，并显示出要关闭连接的标识。

接下来我们来看一下创建 `dbConnection` 值的工厂函数，如代码清单7-23所示。

代码清单7-23　 `pool` /main/main.go：第34行到第44行

```go
34 // idCounter用来给每个连接分配一个独一无二的id
35 var idCounter int32
36
37 // createConnection是一个工厂函数， 
38 // 当需要一个新连接时，资源池会调用这个函数
39 func createConnection() (io.Closer, error) {
40　　 id := atomic.AddInt32(&idCounter, 1)
41　　 log.Println("Create: New Connection", id)
42
43　　 return &dbConnection{id}, nil
44 }
```

代码清单7-23展示了 `createConnection` 函数的实现。这个函数给连接生成了一个唯一标识，显示连接正在被创建，并返回指向带有唯一标识的 `dbConnection` 类型值的指针。唯一标识是通过 `atomic.AddInt32` 函数生成的。这个函数可以安全地增加包级变量 `idCounter` 的值。现在有了资源以及工厂函数，我们可以配合使用 `pool` 包了。

接下来让我们看一下 `main` 函数的代码，如代码清单7-24所示。

代码清单7-24　 `pool` /main/main.go：第48行到第55行

```go
48　　 var wg sync.WaitGroup
49　　 wg.Add(maxGoroutines)
50
51　　 // 创建用来管理连接的池
52　　 p, err := pool.New(createConnection, pooledResources)
53　　 if err != nil {
54　　　　 log.Println(err)
55　　 }
```

在第48行， `main` 函数一开始就声明了一个 `WaitGroup` 值，并将 `WaitGroup` 的值设置为要创建的goroutine的数量。之后使用 `pool` 包里的 `New` 函数创建了一个新的 `Pool` 类型。工厂函数和要管理的资源的数量会传入 `New` 函数。这个函数会返回一个指向 `Pool` 值的指针，并检查可能的错误。现在我们有了一个 `Pool` 类型的资源池实例，就可以创建goroutine，并使用这个资源池在goroutine之间共享资源，如代码清单7-25所示。

代码清单7-25　 `pool` /main/main.go：第57行到第66行

```go
57　　 // 使用池里的连接来完成查询
58　　 for query := 0; query < maxGoroutines; query++ {
59　　　　 // 每个goroutine需要自己复制一份要
60　　　　 // 查询值的副本，不然所有的查询会共享
61　　　　 // 同一个查询变量
62　　　　 go func(q int) {
63　　　　　　 performQueries(q, p)
64　　　　　　 wg.Done()
65　　　　 }(query)
66　　 }
```

代码清单7-25中用一个 `for` 循环创建要使用池的goroutine。每个goroutine调用一次 `performQueries` 函数然后退出。 `performQueries` 函数需要传入一个唯一的 `ID` 值用于做日志以及一个指向 `Pool` 的指针。一旦所有的goroutine都创建完成， `main` 函数就等待所有goroutine执行完毕，如代码清单7-26所示。

代码清单7-26　 `pool` /main/main.go：第68行到第73行

```go
68　　 // 等待goroutine结束
69　　 wg.Wait()
70
71　　 // 关闭池
72　　 log.Println("Shutdown Program.")
73　　 p.Close()
```

在代码清单7-26中， `main` 函数等待 `WaitGroup` 实例的 `Wait` 方法执行完成。一旦所有goroutine都报告其执行完成，就关闭 `Pool` ，并且终止程序。接下来，让我们看一下 `performQueries` 函数。这个函数使用了池的 `Acquire` 方法和 `Release` 方法，如代码清单7-27所示。

代码清单7-27　 `pool` /main/main.go：第76行到第91行

```go
76 // performQueries用来测试连接的资源池
77 func performQueries(query int, p *pool.Pool) {
78　　 // 从池里请求一个连接
79　　 conn, err := p.Acquire()
80　　 if err != nil {
81　　　　 log.Println(err)
82　　　　 return
83　　 }
84
85　　 // 将该连接释放回池里
86　　 defer p.Release(conn)
87
88　　 // 用等待来模拟查询响应
89　　 time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
90　　 log.Printf("QID[%d] CID[%d]\n", query, conn.(*dbConnection).ID)
91 }
```

代码清单7-27展示了 `performQueries` 的实现。这个实现使用了 `pool` 的 `Acquire` 方法和 `Release` 方法。这个函数首先调用了 `Acquire` 方法，从池里获得 `dbConnection` 。之后会检查返回的 `error` 接口值，在第86行，再使用 `defer` 语句在函数退出时将 `dbConnection` 释放回池里。在第89行和第90行，随机休眠一段时间，以此来模拟使用 `dbConnection` 工作时间。

