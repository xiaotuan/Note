### 8.3.1　解码JSON

我们要学习的处理JSON的第一个方面是，使用 `json` 包的 `NewDecoder` 函数以及 `Decode` 方法进行解码。如果要处理来自网络响应或者文件的JSON，那么一定会用到这个函数及方法。让我们来看一个处理 `Get` 请求响应的JSON的例子，这个例子使用 `http` 包获取Google搜索API返回的JSON。代码清单8-23展示了这个响应的内容。

代码清单8-23　Google搜索API的JSON响应例子

```go
{
　　"responseData": {
　　　　"results": [
　　　　　　{
　　　　　　　　"GsearchResultClass": "GwebSearch",
　　　　　　　　"unescapedUrl": "https://www.reddit.com/r/golang",
　　　　　　　　"url": "https://www.reddit.com/r/golang",
　　　　　　　　"visibleUrl": "www.reddit.com",
　　　　　　　　"cacheUrl": "http://www.google.com/search?q=cache:W...",
　　　　　　　　"title": "r/\u003cb\u003eGolang\u003c/b\u003e - Reddit",
　　　　　　　　"titleNoFormatting": "r/Golang - Reddit",
　　　　　　　　"content": "First Open Source \u003cb\u003eGolang\u..."
　　　　　　},
　　　　　　{
　　　　　　　　"GsearchResultClass": "GwebSearch",
　　　　　　　　"unescapedUrl": "http://tour.golang.org/",
　　　　　　　　"url": "http://tour.golang.org/",
　　　　　　　　"visibleUrl": "tour.golang.org",
　　　　　　　　"cacheUrl": "http://www.google.com/search?q=cache:O...",
　　　　　　　　"title": "A Tour of Go",
　　　　　　　　"titleNoFormatting": "A Tour of Go",
　　　　　　　　"content": "Welcome to a tour of the Go programming ..."
　　　　　　}
　　　　]
　　}
}

```

代码清单8-24给出的是如何获取响应并将其解码到一个结构类型里的例子。

代码清单8-24　listing24.go

```go
01 // 这个示例程序展示如何使用json包和NewDecoder函数
02 // 来解码JSON响应
03 package main
04
05 import (
06　　 "encoding/json"
07　　 "fmt"
08　　 "log"
09　　 "net/http"
10 )
11
12 type (
13　　 // gResult映射到从搜索拿到的结果文档
14　　 gResult struct {
15　　　　 GsearchResultClass string `json:"GsearchResultClass"`
16　　　　 UnescapedURL　　　 string `json:"unescapedUrl"`
17　　　　 URL　　　　　　　　 string `json:"url"`
18　　　　 VisibleURL　　　　 string `json:"visibleUrl"`
19　　　　 CacheURL　　　　　  string `json:"cacheUrl"`
20　　　　 Title　　　　　　　 string `json:"title"`
21　　　　 TitleNoFormatting　string `json:"titleNoFormatting"`
22　　　　 Content　　　　　　 string `json:"content"`
23　　 }
24
25　　 // gResponse包含顶级的文档
26　　 gResponse struct {
27　　　　 ResponseData struct {
28　　　　　　 Results []gResult `json:"results"`
29　　　　 } `json:"responseData"`
30　　 }
31 )
32
33 func main() {
34　　 uri := "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&q=golang"
35
36　　 // 向Google发起搜索
37　　 resp, err := http.Get(uri)
38　　 if err != nil {
39　　　　 log.Println("ERROR:", err)
40　　　　 return
41　　 }
42　　 defer resp.Body.Close()
43
44　　 // 将JSON响应解码到结构类型
45　　 var gr gResponse
46　　 err = json.NewDecoder(resp.Body).Decode(&gr)
47　　 if err != nil {
48　　　　 log.Println("ERROR:", err)
49　　　　 return
50　　 }
51
52　　 fmt.Println(gr)
53 }

```

代码清单8-24中代码的第37行，展示了程序做了一个HTTP  `Get` 调用，希望从Google得到一个JSON文档。之后，在第46行使用 `NewDecoder` 函数和 `Decode` 方法，将响应返回的JSON文档解码到第26行声明的一个结构类型的变量里。在第52行，将这个变量的值写到 `stdout` 。

如果仔细看第26行和第14行的 `gResponse` 和 `gResult` 的类型声明，你会注意到每个字段最后使用单引号声明了一个字符串。这些字符串被称作 **标签** （tag），是提供每个字段的元信息的一种机制，将JSON文档和结构类型里的字段一一映射起来。如果不存在 **标签** ，编码和解码过程会试图以大小写无关的方式，直接使用字段的名字进行匹配。如果无法匹配，对应的结构类型里的字段就包含其零值。

执行HTTP  `Get` 调用和解码JSON到结构类型的具体技术细节都由标准库包办了。让我们看一下标准库里 `NewDecoder` 函数和 `Decode` 方法的声明，如代码清单8-25所示。

代码清单8-25　golang.org/src/encoding/json/stream.go

```go
// NewDecoder返回从r读取的解码器
//
// 解码器自己会进行缓冲，而且可能会从r读比解码JSON值
// 所需的更多的数据
func NewDecoder(r io.Reader) *Decoder
// Decode从自己的输入里读取下一个编码好的JSON值， 
// 并存入v所指向的值里
//
// 要知道从JSON转换为Go的值的细节， 
// 请查看Unmarshal的文档
func (dec *Decoder) Decode(v interface{}) error
```

在代码清单8-25中可以看到 `NewDecoder` 函数接受一个实现了 `io.Reader` 接口类型的值作为参数。在下一节，我们会更详细地介绍 `io.Reader` 和 `io.Writer` 接口，现在只需要知道标准库里的许多不同类型，包括 `http` 包里的一些类型，都实现了这些接口就行。只要类型实现了这些接口，就可以自动获得许多功能的支持。

函数 `NewDecoder` 返回一个指向 `Decoder` 类型的指针值。由于Go语言支持复合语句调用，可以直接调用从 `NewDecoder` 函数返回的值的 `Decode` 方法，而不用把这个返回值存入变量。在代码清单8-25里，可以看到 `Decode` 方法接受一个 `interface{}` 类型的值做参数，并返回一个 `error` 值。

在第5章中曾讨论过，任何类型都实现了一个空接口 `interface{}` 。这意味着 `Decode` 方法可以接受任意类型的值。使用反射， `Decode` 方法会拿到传入值的类型信息。然后，在读取JSON响应的过程中， `Decode` 方法会将对应的响应解码为这个类型的值。这意味着用户不需要创建对应的值， `Decode` 会为用户做这件事情，如代码清单8-26所示。

在代码清单8-26中，我们向 `Decode` 方法传入了指向 `gResponse` 类型的指针变量的地址，而这个地址的实际值为 `nil` 。该方法调用后，这个指针变量会被赋给一个 `gResponse` 类型的值，并根据解码后的JSON文档做初始化。

代码清单8-26　使用 `Decode` 方法

```go
var gr *gResponse
err = json.NewDecoder(resp.Body).Decode(&gr)
```

有时，需要处理的JSON文档会以 `string` 的形式存在。在这种情况下，需要将 `string` 转换为 `byte` 切片（ `[]byte` ），并使用 `json` 包的 `Unmarshal` 函数进行反序列化的处理，如代码清单8-27所示。

代码清单8-27　listing27.go

```go
01 // 这个示例程序展示如何解码JSON字符串
02 package main
03
04 import (
05　　 "encoding/json"
06　　 "fmt"
07　　 "log"
08 )
09
10 // Contact结构代表我们的JSON字符串
11 type Contact struct {
12　　 Name　　string `json:"name"`
13　　 Title　 string `json:"title"`
14　　 Contact struct {
15　　　　 Home string `json:"home"`
16　　　　 Cell string `json:"cell"`
17　　 } `json:"contact"`
18 }
19
20 // JSON包含用于反序列化的演示字符串
21 var JSON = `{
22　　 "name": "Gopher",
23　　 "title": "programmer",
24　　 "contact": {
25　　　　 "home": "415.333.3333",
26　　　　 "cell": "415.555.5555"
27　　 }
28 }`
29
30 func main() {
31　　 // 将JSON字符串反序列化到变量
32　　 var c Contact
33　　 err := json.Unmarshal([]byte(JSON), &c)
34　　 if err != nil {
35　　　　 log.Println("ERROR:", err)
36　　　　 return
37　　 }
38
39　　 fmt.Println(c)
40 }
```

在代码清单8-27中，我们的例子将JSON文档保存在一个字符串变量里，并使用 `Unmarshal` 函数将JSON文档解码到一个结构类型的值里。如果运行这个程序，会得到代码清单8-28所示的输出。

代码清单8-28　listing27.go的输出

```go
{Gopher programmer {415.333.3333 415.555.5555}}
```

有时，无法为JSON的格式声明一个结构类型，而是需要更加灵活的方式来处理JSON文档。在这种情况下，可以将JSON文档解码到一个 `map` 变量中，如代码清单8-29所示。

代码清单8-29　listing29.go

```go
01 // 这个示例程序展示如何解码JSON字符串
02 package main
03
04 import (
05　　 "encoding/json"
06　　 "fmt"
07　　 "log"
08 )
09
10 // JSON包含要反序列化的样例字符串
11 var JSON = `{
12　　 "name": "Gopher",
13　　 "title": "programmer",
14　　 "contact": {
15　　　　 "home": "415.333.3333",
16　　　　 "cell": "415.555.5555"
17　　 }
18 }`
19
20 func main() {
21　　 // 将JSON字符串反序列化到map变量
22　　 var c map[string]interface{}
23　　 err := json.Unmarshal([]byte(JSON), &c)
24　　 if err != nil {
25　　　　 log.Println("ERROR:", err)
26　　　　 return
27　　 }
28
29　　 fmt.Println("Name:", c["name"])
30　　 fmt.Println("Title:", c["title"])
31　　 fmt.Println("Contact")
32　　 fmt.Println("H:", c["contact"].(map[string]interface{})["home"])
33　　 fmt.Println("C:", c["contact"].(map[string]interface{})["cell"])
34 }
```

代码清单8-29中的程序修改自代码清单8-27，将其中的结构类型变量替换为 `map` 类型的变量。变量 `c` 声明为一个 `map` 类型，其键是 `string` 类型，其值是 `interface{}` 类型。这意味着这个 `map` 类型可以使用任意类型的值作为给定键的值。虽然这种方法为处理JSON文档带来了很大的灵活性，但是却有一个小缺点。让我们看一下访问 `contact` 子文档的 `home` 字段的代码，如代码清单8-30所示。

代码清单8-30　访问解组后的映射的字段的代码

```go
fmt.Println("\tHome:", c["contact"].(map[string]interface{})["home"])
```

因为每个键的值的类型都是 `interface{}` ，所以必须将值转换为合适的类型，才能处理这个值。代码清单8-30展示了如何将 `contact` 键的值转换为另一个键是 `string` 类型，值是 `interface{}` 类型的 `map` 类型。这有时会使映射里包含另一个文档的JSON文档处理起来不那么友好。但是，如果不需要深入正在处理的JSON文档，或者只打算做很少的处理，因为不需要声明新的类型，使用 `map` 类型会很快。

