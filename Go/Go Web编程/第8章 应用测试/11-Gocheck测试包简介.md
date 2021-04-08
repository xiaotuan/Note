### 8.5.1　Gocheck测试包简介

Gocheck项目提供了 `check` 包，这个包是基于 `testing` 包构建的一个测试框架，并且提供了一系列特性来填补标准 `testing` 包在特性方面的空白，这一系列特性包括：

+ 以套件（suite）为单位对测试进行分组；
+ 为每个测试套件或者测试用例分别设置测试夹具；
+ 带有可扩展检查器接口的断言；
+ 更多错误报告辅助函数；
+ 与 `testing` 包紧密集成。

下载并安装 `check` 包的工作非常简单，可以通过执行以下命令来完成：

```go
go get gopkg.in/check.v1
```

代码清单8-20展示了使用 `check` 包测试简单Web服务的方法。

代码清单8-20　使用 `check` 包的 `server_test.go`

```go
package main
import (
　"encoding/json"
　"net/http"
　"net/http/httptest"
　"testing"
　. "gopkg.in/check.v1" ❶
)
type PostTestSuite struct {}  ❷
func init() {
　Suite(&PostTestSuite{})  ❸
}
func Test(t *testing.T) { TestingT(t) }  ❹
func (s *PostTestSuite) TestHandleGet(c *C) {
　mux := http.NewServeMux()
　mux.HandleFunc("/post/", handleRequest(&FakePost{}))
　writer := httptest.NewRecorder()
　request, _ := http.NewRequest("GET", "/post/1", nil)
　mux.ServeHTTP(writer, request)
　c.Check(writer.Code, Equals, 200) ❺
　var post Post ❺
　json.Unmarshal(writer.Body.Bytes(), &post) ❺
　c.Check(post.Id, Equals, 1) ❺
}
```

❶ 导入check 包中的标识符，使程序可以以不带前缀的方式访问它们

❷ 创建测试套件

❸ 注册测试套件

❹ 集成testing 包

❺ 检查语句的执行结果

这个测试程序做的第一件事就是导入包。需要特别注意的是，因为程序是以点（ `.` ）方式导入 `check` 包的，所以包中所有被导出的标识符在测试程序里面都可以以不带前缀的方式访问。

之后，程序创建了一个测试套件。测试套件将以结构的形式表示，这个结构既可以像这个例子中展示的一样——只是一个空结构，也可以在结构中包含其他字段，这一点在后面将会有更详细的讨论。除了创建测试套件结构之外，程序还需要把这个结构传递给 `Suite` 函数，以便对测试套件进行注册。测试套件中所有遵循 `TestXxx` 格式的方法都会被看作是一个测试用例，跟之前一样，这些测试用例也会在用户运行测试时被执行。

准备工作的最后一步是集成 `testing` 包，这一点可以通过创建一个普通的 `testing` 包测试用例来完成：程序需要创建一个格式为 `TestXxx` 的函数，它接受一个指向 `testing.T` 的指针作为输入，然后把这个指针作为参数在函数体内调用 `TestingT` 函数。

上述集成操作会导致所有用 `Suite` 函数注册了的测试套件被运行，而运行的结果则会被回传至 `testing` 包。在一切预设操作都准备妥当之后，程序接下来就可以定义自己的测试用例了。在上面展示的测试套件当中，有一个名为 `TestHandleGet` 的方法，它接受一个指向 `C` 类型的指针作为参数，这种类型拥有一些非常有趣的方法，但是由于篇幅的关系，本节无法详细介绍 `C` 类型拥有的所有方法，目前来说，我们只需要知道它的 `Check` 方法和 `Assert` 方法能够验证结果的值就可以了。

例如，在代码清单8-20中，测试用例会使用 `Check` 方法检查被返回的HTTP代码是否为200，如果结果不是200，那么这个测试用例将被标记为“已失败”，但测试用例会继续执行直到结束；反之，如果程序使用 `Assert` 来代替 `Check` ，那么测试用例在失败之后将立即返回。

使用Gocheck实现的测试程序同样使用 `go test` 命令执行，但是用户可以使用 `check` 包专有的特别详细（extra verbose）标志 `-check.vv` 显示更多细节：

```go
go test -check.vv
```

下面是这条命令的执行结果：

```go
START: server_test.go:19: PostTestSuite.TestGetPost
PASS: server_test.go:19: PostTestSuite.TestGetPost　0.000s
OK: 1 passed
PASS
ok　　gocheck　　0.007s
```

正如结果所示，带有特别详细标志的命令给我们提供了更多信息，其中包括测试的启动信息。虽然这些信息对于目前这个例子没有太大帮助，但是在之后的例子中，我们将会看到这些信息的重要之处。

为了观察测试程序在出错时的反应，我们可以小小地修改一下 `handleGet` 函数，把以下这个会抛出HTTP 404状态码的语句添加到函数的 `return` 语句之前：

```go
http.NotFound(w, r)
```

现在，再执行 `go test` 命令，我们将看到以下结果：

```go
START: server_test.go:19: PostTestSuite.TestGetPost
server_test.go:29:
　　c.Check(post.Id, Equals, 1)
... obtained int = 0
... expected int = 1
FAIL: server_test.go:19: PostTestSuite.TestGetPost
OOPS: 0 passed, 1 FAILED
--- FAIL: Test (0.00s)
FAIL
exit status 1
FAIL　gocheck　　0.007s
```

正如结果所示，带有特别详细标志的 `go test` 命令在测试出错时将给我们提供非常多有价值的信息。

测试夹具（test fixture）是 `check` 包提供的另外一个非常有用的特性，用户可以通过这些夹具在测试开始之前设置好固定的状态，然后再在测试中对预期的状态进行检查。

`check` 包为整个测试套件以及每个测试用例分别提供了一系列预设函数和拆卸函数。比如，在套件开始运行之前运行一次的 `SetUpSuite` 函数，在所有测试都运行完毕之后运行一次的 `TearDownSuite` 函数，在运行每个测试用例之前都会运行一次的 `SetUpTest` 函数，以及在运行每个测试用例之后都会运行一次的 `TearDownTest` 函数。

为了演示这些测试夹具的使用方法，我们需要复用之前展示过的测试程序，并为 `PUT` 方法添加一个测试用例。如果我们仔细地观察已有的测试用例和新添加的测试用例就会发现，在每个测试用例里面，都出现了以下重复代码：

```go
mux := http.NewServeMux()
mux.HandleFunc("/post/", handlePost(&FakePost{}))
writer := httptest.NewRecorder()
```

这个测试程序的每个测试用例都会创建一个多路复用器，并调用多路复用器的 `HandleFunc` 方法，把一个URL和一个处理器绑定起来。在此之后，测试用例还需要创建一个 `ResponseRecorder` 来记录请求的响应。因为测试套件中的每个测试用例都需要执行这两个步骤，所以我们可以把这两个步骤用作各个测试用例的夹具。

代码清单8-21展示了使用夹具之后的 `server_test.go` 。

代码清单8-21　使用测试夹具实现的测试程序

```go
package main
import (
　"encoding/json"
　"net/http"
　"net/http/httptest"
　"testing"
　"strings"
　. "gopkg.in/check.v1"
)
type PostTestSuite struct {  ❶
　mux *http.ServeMux
　post *FakePost
　　writer *httptest.ResponseRecorder
}
func init() {
　Suite(&PostTestSuite{})
}
func Test(t *testing.T) { TestingT(t) }
func (s *PostTestSuite) SetUpTest(c *C) { ❷
　s.post = &FakePost{}
　s.mux = http.NewServeMux()
　s.mux.HandleFunc("/post/", handleRequest(s.post))
　s.writer = httptest.NewRecorder()
}
func (s *PostTestSuite) TestGetPost(c *C) {
　request, _ := http.NewRequest("GET", "/post/1", nil)
　s.mux.ServeHTTP(s.writer, request)
　c.Check(s.writer.Code, Equals, 200)
　var post Post
　json.Unmarshal(s.writer.Body.Bytes(), &post)
　c.Check(post.Id, Equals, 1)
}
func (s *PostTestSuite) TestPutPost(c *C) {
　json := strings.NewReader(`{"content":"Updated post","author":"Sau
　Sheong"}`)
　request, _ := http.NewRequest("PUT", "/post/1", json)
　s.mux.ServeHTTP(s.writer, request)
　c.Check(s.writer.Code, Equals, 200)
　c.Check(s.post.Id, Equals, 1)
　c.Check(s.post.Content, Equals, "Updated post")
}
```

❶ 存储在测试套件中的测试夹具数据

❷ 创建测试夹具

为了使用测试夹具，程序必须将它的数据存储在某个地方，并让这些数据在测试过程中一直存在。为此，程序需要给测试套件结构 `PostTestSuite` 添加一些字段，并把想要存储的测试夹具数据记录到这些字段里面。因为测试套件中的每个测试用例实际上都是 `PostTestSuite` 结构的一个方法，所以这些测试用例将能够非常方便地访问到结构中存储的夹具数据。在存储好夹具数据之后，程序会使用 `SetUpTest` 函数为每个测试用例设置夹具。

在创建夹具的过程中，程序使用了存储在 `PostTestSuite` 结构中的字段。在设置好夹具之后，我们就可以对测试程序做相应的修改了：需要修改的地方并不多，最主要的工作是移除测试用例中重复出现的语句，并将测试用例中使用的结构修改为测试夹具中设置的结构。在完成修改之后再次执行 `go test` 命令，我们将得到以下结果：

```go
START: server_test.go:31: PostTestSuite.TestGetPost
START: server_test.go:24: PostTestSuite.SetUpTest
PASS: server_test.go:24: PostTestSuite.SetUpTest　0.000s
PASS: server_test.go:31: PostTestSuite.TestGetPost 0.000s
START: server_test.go:41: PostTestSuite.TestPutPost
START: server_test.go:24: PostTestSuite.SetUpTest
PASS: server_test.go:24: PostTestSuite.SetUpTest　0.000s
PASS: server_test.go:41: PostTestSuite.TestPutPost　0.000s
OK: 2 passed
PASS
ok　　gocheck　　0.007s
```

特别详细标志让我们清晰地看到了整个测试套件的运行过程。为了进一步观察整个测试套件的运行顺序，我们可以把以下测试夹具函数添加到测试程序里面：

```go
func (s *PostTestSuite) TearDownTest(c *C) {
　c.Log("Finished test - ", c.TestName())
}
func (s *PostTestSuite) SetUpSuite(c *C) {
　c.Log("Starting Post Test Suite")
}
func (s *PostTestSuite) TearDownSuite(c *C) {
　c.Log("Finishing Post Test Suite")
}
```

再次运行测试将得到以下结果：

```go
START: server_test.go:35: PostTestSuite.SetUpSuite
Starting Post Test Suite
PASS: server_test.go:35: PostTestSuite.SetUpSuite　0.000s
START: server_test.go:44: PostTestSuite.TestGetPost
START: server_test.go:24: PostTestSuite.SetUpTest
PASS: server_test.go:24: PostTestSuite.SetUpTest　0.000s
START: server_test.go:31: PostTestSuite.TearDownTest
Finished test - PostTestSuite.TestGetPost
PASS: server_test.go:31: PostTestSuite.TearDownTest　0.000s
PASS: server_test.go:44: PostTestSuite.TestGetPost　0.000s
START: server_test.go:54: PostTestSuite.TestPutPost
START: server_test.go:24: PostTestSuite.SetUpTest
PASS: server_test.go:24: PostTestSuite.SetUpTest　0.000s
START: server_test.go:31: PostTestSuite.TearDownTest
Finished test - PostTestSuite.TestPutPost
PASS: server_test.go:31: PostTestSuite.TearDownTest　0.000s
PASS: server_test.go:54: PostTestSuite.TestPutPost　0.000s
START: server_test.go:39: PostTestSuite.TearDownSuite
Finishing Post Test Suite
PASS: server_test.go:39: PostTestSuite.TearDownSuite　0.000s
OK: 2 passed
PASS
ok　　gocheck　　0.007s
```

根据测试结果显示， `SetUpSuite` 和 `TearDownSuite` 就如我们之前介绍的一样，只会在测试开始之前和测试结束之后各运行一次，而 `SetUpTest` 和 `TearDownTest` 则会作为每个测试用例的第一行语句和最后一行语句，在测试用例的开头和结尾分别运行一次。

作为 `testing` 包的增强版本，简单而强大的Gocheck为我们的测试“军火库”加上了一件强有力的武器，如果你想要获得比Gocheck更强大的功能，可以试一试下一节介绍的Ginkgo测试框架。

