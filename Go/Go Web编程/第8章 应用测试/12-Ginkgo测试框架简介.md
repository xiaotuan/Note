### 8.5.2　Ginkgo测试框架简介

Ginkgo是一个行为驱动开发（behavior-driven development，BDD）风格的Go测试框架。BDD是一个非常庞大的主题，想要在小小的一节篇幅里对它进行完整的介绍是不可能的。一言以蔽之，BDD是测试驱动开发（test-driven development，TDD）的一种延伸，但BDD跟TDD的不同之处在于，BDD是一种软件开发方法而不是一种软件测试方法。在BDD中，软件由它的目标行为进行定义，这些目标行为通常是一系列业务需求。BDD的需求是从行为的角度，通过终端用户的语言以及视角来定义的，这些需求在BDD中称为用户故事（user story）。下面是通过用户故事对简单Web服务进行描述的一个例子。

` **故事：** 获取一张帖子&#13;
 **为了** 向用户显示指定的一张帖子&#13;
 **作为** 一个被调用的程序&#13;
 **我需要** 获取用户指定的帖子&#13;
&#13;
 **情景1：** 使用一个ID&#13;
 **给定** 一个值为`` 1`的帖子ID&#13;
 **只要** 我发送一个带有该ID的GET请求&#13;
 **那么** 我就会获得与给定ID相对应的一张帖子&#13;
&#13;
 **情景2：** 使用一个非整数ID&#13;
 **给定** 一个值为` `"hello"` `的帖子ID&#13;
 **只要** 我发送一个带有该ID的GET请求&#13;
 **那么** 我就会获得一个HTTP 500响应

在定义了用户故事之后，我们就可以把这些用户故事转换为测试用例。BDD中的测试用例跟TDD中的测试用例一样，都是在编写实际的代码之前编写的，这些测试用例的目标在于开发出一个程序，让它能够执行用户故事中描述的行为。坦白地说，上面展示的用户故事带有很明显的虚构成分。在更现实的环境中，BDD用户故事最开始通常都是使用更高层次的语言来撰写，然后根据细节进行数次层级划分之后，再分解为更为具体的用户故事，最终，使用高层次语言撰写的用户故事将会被映射到一系列按层级划分的测试套件。

Ginkgo是一个拥有丰富功能的BDD风格的框架，它提供了将用户故事映射为测试用例的工具，并且这些工具也很好地集成到了Go的 `testing` 包当中。虽然Ginkgo的主要用于在Go中实现BDD，但是本节只会把Ginkgo当作一个Go的测试框架来使用。

为了安装Ginkgo，我们需要在终端中执行以下两条命令：

```go
go get github.com/onsi/ginkgo/ginkgo
go get github.com/onsi/gomega
```

第一条命令下载Ginkgo并将命令行接口程序 `ginkgo` 安装到 `$GOPATH/bin` 目录中，而第二条命令则会下载Ginkgo默认的匹配器库Gomega（匹配器可以对比两个不同的组件，这些组件可以是结构、映射、字符串等）。

在开始学习如何使用Ginkgo编写测试用例之前，让我们先来看看如何使用Ginkgo去执行已有的测试用例——Ginkgo能够自动地对前面展示过的 `testing` 包测试用例进行语法重写，把它们转换为Ginkgo测试用例。

为了验证这一点，我们将会使用上一节展示过的带有依赖注入特性的测试套件为起点。如果你想要保留原有的测试套件，让它们免受Ginkgo的修改，那么请在执行后续操作之前先对其进行备份。在一切准备就绪之后，在终端里面执行以下命令：

```go
ginkgo convert .
```

这条命令会在目录中添加一个名为`xxx`_suite_test.go的文件，其中`xxx`为目录的名字。这个文件的具体内容如代码清单8-22所示。

代码清单8-22　Ginkgo测试套件文件

```go
package main_test
import (
　. "github.com/onsi/ginkgo"
　. "github.com/onsi/gomega"
　"testing"
)
func TestGinkgo(t *testing.T) {
　RegisterFailHandler(Fail)
　RunSpecs(t, "Ginkgo Suite")
}
```

除此之外，上述命令还会对 `server_test.go文件` 进行修改，代码清单8-23中以粗体的形式展示了文件中被修改的代码行。

代码清单8-23　修改后的测试文件

```go
package main
import (
　"encoding/json"
　"net/http"
　"net/http/httptest"
　"strings"
　. "github.com/onsi/ginkgo"
)
var _ = Describe("Testing with Ginkgo", func() {
　It("get post", func() {
　　mux := http.NewServeMux()
　　mux.HandleFunc("/post/", handleRequest(&FakePost{}))
　　writer := httptest.NewRecorder()
　　request, _ := http.NewRequest("GET", "/post/1", nil)
　　mux.ServeHTTP(writer, request)
　　if writer.Code != 200 {
　　　GinkgoT().Errorf("Response code is %v", writer.Code)
　　}
　　var post Post
　　json.Unmarshal(writer.Body.Bytes(), &post)
　　if post.Id != 1 {
　　　GinkgoT().Errorf("Cannot retrieve JSON post")
　　}
　})
　It("put post", func() {
　　mux := http.NewServeMux()
　　post := &FakePost{}
　　mux.HandleFunc("/post/", handleRequest(post))
　　writer := httptest.NewRecorder()
　　json := strings.NewReader(`{"content":"Updated post","author":"Sau
　Sheong"}`)
　　request, _ := http.NewRequest("PUT", "/post/1", json)
　　mux.ServeHTTP(writer, request)
　　if writer.Code != 200 {
　　　GinkgoT().Error("Response code is %v", writer.Code)
　　}
　　if post.Content != "Updated post" {
　　　GinkgoT().Error("Content is not correct", post.Content)
　　}
　})
})
```

注意，修改后的测试程序并没有使用Gomega，只是把检查执行结果的语句改成了Ginkgo提供的 `Errorf` 函数和 `Erro` r函数，不过这两个函数跟 `testing` 包以及 `check` 包中的同名函数具有相似的作用。当我们使用以下命令运行这个测试程序时：

```go
ginkgo -v
```

Ginkgo将打印出一段格式非常漂亮的输出：

```go
Running Suite: Ginkgo Suite
===========================
Random Seed: 1431743149
Will run 2 of 2 specs
Testing with Ginkgo
　get post
　server_test.go:29
•
------------------------------
Testing with Ginkgo
　put post
　server_test.go:48
•
Ran 2 of 2 Specs in 0.000 seconds
SUCCESS! -- 2 Passed | 0 Failed | 0 Pending | 0 Skipped PASS
Ginkgo ran 1 suite in 577.104764ms
Test Suite Passed
```

自动转换已有的测试，然后漂亮地打印出它们的执行结果，这给人的感觉真的非常不错！但如果我们根本没有现成的测试用例，是否需要先创建出 `testing` 包的测试用例，然后再把它们转换为Ginkgo测试呢？答案是否定的！没有必要多此一举，让我们来看看如何从零开始创建Ginkgo测试用例吧。

Ginkgo提供了一些实用工具，它们能够帮助用户快速、方便地创建测试。首先，清空与上一次测试有关的全部测试文件，包括之前Ginkgo创建的测试套件文件，然后在程序的目录中执行以下两条命令：

```go
ginkgo bootstrap
ginkgo generate
```

第一条命令会创建新的Ginkgo测试套件文件，而第二条命令则会为测试用例文件生成代码清单8-24所示的骨架。

代码清单8-24　Ginkgo测试文件

```go
package main_test
import (
　. "<path/to/your/go_files>/ginkgo"
　. "github.com/onsi/ginkgo"
　. "github.com/onsi/gomega"
)
var _ = Describe("Ginkgo", func() {
})
```

注意，因为Ginkgo会把测试用例从 `main` 包中隔离开，所以新创建的测试文件将不再属于 `main` 包。此外，测试程序还通过点导入（dot import）语法，将几个库中包含的标识符全部导入到顶层命名空间。这种导入方式并不是必需的，Ginkgo在它的文档里面提供了一些关于如何避免这种导入的说明，但是在不使用点导入语法的情况下，用户必须导出 `main` 包中需要使用Ginkgo测试的所有函数。例如，因为我们接下来就要对简单Web服务的 `HandleRequest` 函数进行测试，所以这个函数一定要被导出，也就是说，这个函数的名字的首字母必须大写。

另外需要注意的是，Ginkgo在调用 `Describe` 函数时使用了 `var _　=` 这一技巧。这种常用的技巧能够在调用 `Describe` 函数的同时，避免引入 `init` 函数。

代码清单8-25展示了使用Ginkgo实现的测试用例代码，这些代码是由早前撰写的用户故事映射而来的。

代码清单8-25　使用Gomega匹配器实现的Ginkgo测试用例

```go
package main_test
import (
　"encoding/json"
　"net/http"
　"net/http/httptest"
　. "github.com/onsi/ginkgo"
　. "github.com/onsi/gomega"
　. "gwp/Chapter_8_Testing_Web_Applications/test_ginkgo"
)
var _ = Describe("Get a post", func() { ❶
　var mux *http.ServeMux
　var post *FakePost
　var writer *httptest.ResponseRecorder
　BeforeEach(func() {
　　post = &FakePost{}
　　mux = http.NewServeMux()
　　mux.HandleFunc("/post/", HandleRequest(post))
　　writer = httptest.NewRecorder()
　})
　Context("Get a post using an id", func() { ❷❸
　　It("should get a post", func() {
　　　request, _ := http.NewRequest("GET", "/post/1", nil)
　　　mux.ServeHTTP(writer, request)
　　　Expect(writer.Code).To(Equal(200)) ❹
　　　var post Post
　　　json.Unmarshal(writer.Body.Bytes(), &post)
　　　Expect(post.Id).To(Equal(1))
　　})
　})
　Context("Get an error if post id is not an integer", func() { ❺
　　It("should get a HTTP 500 response", func() {
　　　request, _ := http.NewRequest("GET", "/post/hello", nil)
　　　mux.ServeHTTP(writer, request)
　　　Expect(writer.Code).To(Equal(500))
　　})
　})
})
```

❶ 用户故事

❷ 使用Gomega匹配器

❸ 情景1

❹ 使用Gomega 对正确性进行断言

❺ 情景2

注意，这个测试程序使用了来自Gomega包的匹配器：Gomega是由Ginkgo开发者开发的一个断言包，包中的匹配器都是测试断言。跟使用 `check` 包时一样，测试程序在调用 `Context` 函数模拟指定的情景之前，会先设置好相应的测试夹具：

```go
var mux *http.ServeMux
var post *FakePost
var writer *httptest.ResponseRecorder
BeforeEach(func() {
　post = &FakePost{}
　mux = http.NewServeMux()
　mux.HandleFunc("/post/", HandleRequest(post)) ❶
　writer = httptest.NewRecorder()
})
```

❶ 对 main 包中导出的函数进行测试

注意，为了从 `main` 包中导出被测试的处理器，我们将处理器的名字从原来的 `handleRequest` 修改成了首字母大写的 `HandleRequest` 。除使用的是Gomega的断言之外，程序中展现的测试场景跟我们之前使用其他包进行测试时的场景非常类似。下面是一个使用Gomega创建的断言：

```go
Expect(post.Id).To(Equal(1))
```

在这个断言中， `post.Id` 是要测试的对象， `Equal` 函数是匹配器，而 `1` 是预期的结果。针对我们写的测试情景，执行 `ginkgo` 命令将返回以下结果：

```go
Running Suite: Post CRUD Suite
==============================
Random Seed: 1431753578
Will run 2 of 2 specs
Get a post using an id
　should get a post
　test_ginkgo_test.go:35
•
------------------------------
Get a post using a non-integer id
　should get aHTTP500 response
　test_ginkgo_test.go:44
•
Ran 2 of 2 Specs in 0.000 seconds
SUCCESS! -- 2 Passed | 0 Failed | 0 Pending | 0 Skipped PASS
Ginkgo ran 1 suite in 648.619232ms
Test Suite Passed
```

好的，关于使用Go对程序进行测试的介绍到这里就结束了，在接下来的一章中，我们将会讨论如何在Web应用中使用Go的一个关键长处——并发。

