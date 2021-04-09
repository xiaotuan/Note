### 2.4　RSS匹配器

最后要看的一部分代码是RSS匹配器的实现代码。我们之前看到的代码搭建了一个框架，以便能够实现不同的匹配器来搜索内容。RSS匹配器的结构与默认匹配器的结构很类似。每个匹配器为了匹配接口， `Search` 方法的实现都不同，因此匹配器之间无法互相替换。

代码清单2-47中的RSS文档是一个例子。当我们访问数据源列表里RSS数据源的链接时，期望获得的数据就和这个例子类似。

代码清单2-47　期望的RSS数据源文档

```go
<rss xmlns:npr="http://www.npr.org/rss/" xmlns:nprml="http://api"
    <channel>
        <title>News</title>
        <link>...</link>
        <description>...</description>
        <language>en</language>
        <copyright>Copyright 2014 NPR - For Personal Use
        <image>...</image>
        <item>
            <title>
                Putin Says He'll Respect Ukraine Vote But U.S.
            </title>
            <description>
                The White House and State Department have called on the
            </description>

```

如果用浏览器打开代码清单2-47中的任意一个链接，就能看到期望的RSS文档的完整内容。RSS匹配器的实现会下载这些RSS文档，使用搜索项来搜索标题和描述域，并将结果发送给 `results` 通道。让我们先看看rss.go代码文件的前12行代码，如代码清单2-48所示。

代码清单2-48　matchers/rss.go：第01行到第12行

```go
01 package matchers
02
03 import (
04     "encoding/xml"
05     "errors"
06     "fmt"
07     "log"
08     "net/http"
09     "regexp"
10
11     "github.com/goinaction/code/chapter2/sample/search"
12 )
```

和其他代码文件一样，第1行定义了包名。这个代码文件处于名叫 `matchers` 的文件夹中，所以包名也叫 `matchers` 。之后，我们从标准库中导入了6个库，还导入了 `search` 包。再一次，我们看到有些标准库的包是从标准库所在的子文件夹导入的，如 `xml` 和 `http` 。就像 `json` 包一样，路径里最后一个文件夹的名字代表包的名字。

为了让程序可以使用文档里的数据，解码RSS文档的时候需要用到4个结构类型，如代码清单2-49所示。

代码清单2-49　matchers/rss.go：第14行到第58行

```go
14 type (
15     // item根据item字段的标签，将定义的字段
16     // 与rss文档的字段关联起来
17     item struct {
18         XMLName     xml.Name `xml:"item"`
19         PubDate     string   `xml:"pubDate"`
20         Title       string   `xml:"title"`
21         Description string   `xml:"description"`
22         Link        string   `xml:"link"`
23         GUID        string   `xml:"guid"`
24         GeoRssPoint string   `xml:"georss:point"`
25     }
26
27     // image根据image字段的标签，将定义的字段
28     // 与rss文档的字段关联起来
29     image struct {
30         XMLName xml.Name `xml:"image"`
31         URL     string   `xml:"url"`
32         Title   string   `xml:"title"`
33         Link    string   `xml:"link"`
34     }
35
36     // channel根据channel字段的标签，将定义的字段
37     // 与rss文档的字段关联起来
38     channel struct {
39         XMLName        xml.Name `xml:"channel"`
40         Title          string   `xml:"title"`
41         Description    string   `xml:"description"`
42         Link           string   `xml:"link"`
43         PubDate        string   `xml:"pubDate"`
44         LastBuildDate   string   `xml:"lastBuildDate"`
45         TTL            string   `xml:"ttl"`
46         Language       string   `xml:"language"`
47         ManagingEditor string   `xml:"managingEditor"`
48         WebMaster      string   `xml:"webMaster"`
49         Image          image    `xml:"image"`
50         Item           []item   `xml:"item"`
51     }
52
53     // rssDocument定义了与rss文档关联的字段
54     rssDocument struct {
55         XMLName xml.Name `xml:"rss"`
56         Channel channel  `xml:"channel"`
57     }
58 )
```

如果把这些结构与任意一个数据源的RSS文档对比，就能发现它们的对应关系。解码XML的方法与我们在feed.go代码文件里解码JSON文档一样。接下来我们可以看看 `rssMatcher` 类型的声明，如代码清单2-50所示。

代码清单2-50　matchers/rss.go：第60行到第61行

```go
60 // rssMatcher 实现了Matcher接口
61 type rssMatcher struct{}
```

再说明一次，这个声明与 `defaultMatcher` 类型的声明很像。因为不需要维护任何状态，所以我们使用了一个空结构来实现 `Matcher` 接口。接下来看看匹配器 `init` 函数的实现，如代码清单2-51所示。

代码清单2-51　matchers/rss.go：第63行到第67行

```go
63 // init 将匹配器注册到程序里
64 func init() {
65     var matcher rssMatcher
66     search.Register("rss", matcher)
67 }
```

就像在默认匹配器里看到的一样， `init` 函数将 `rssMatcher` 类型的值注册到程序里，以备后用。让我们再看一次main.go代码文件里的导入部分，如代码清单2-52所示。

代码清单2-52　main.go：第07行到第08行

```go
07     _ "github.com/goinaction/code/chapter2/sample/matchers"
08      "github.com/goinaction/code/chapter2/sample/search"
```

main.go代码文件里的代码并没有直接使用任何 `matchers` 包里的标识符。不过，我们依旧需要编译器安排调用rss.go代码文件里的 `init` 函数。在第07行，我们使用下划线标识符作为别名导入 `matchers` 包，完成了这个调用。这种方法可以让编译器在导入未被引用的包时不报错，而且依旧会定位到包内的 `init` 函数。我们已经看过了所有的导入、类型和初始化函数，现在来看看最后两个用于实现 `Matcher` 接口的方法，如代码清单2-53所示。

代码清单2-53　matchers/rss.go：第114行到第140行

```go
114 // retrieve发送HTTP Get请求获取rss数据源并解码
115 func (m rssMatcher) retrieve(feed *search.Feed) (*rssDocument, error) {
116     if feed.URI == "" {
117         return nil, errors.New("No rss feed URI provided")
118     }
119
120     // 从网络获得rss数据源文档
121     resp, err := http.Get(feed.URI)
122     if err != nil {
123         return nil, err
124     }
125
126     // 一旦从函数返回，关闭返回的响应链接
127     defer resp.Body.Close()
128
129     // 检查状态码是不是200，这样就能知道
130     // 是不是收到了正确的响应
131     if resp.StatusCode != 200 {
132         return nil, fmt.Errorf("HTTP Response Error %d\n", resp.StatusCode)
133     }
134
135     // 将rss数据源文档解码到我们定义的结构类型里
136     // 不需要检查错误，调用者会做这件事
137     var document rssDocument
138     err = xml.NewDecoder(resp.Body).Decode(&document)
139     return &document, err
140 }
```

方法 `retrieve` 并没有对外暴露，其执行的逻辑是从RSS数据源的链接拉取RSS文档。在第121行，可以看到调用了 `http` 包的 `Get` 方法。我们会在第8章进一步介绍这个包，现在只需要知道，使用 `http` 包，Go语言可以很容易地进行网络请求。当 `Get` 方法返回后，我们可以得到一个指向 `Response` 类型值的指针。之后会监测网络请求是否出错，并在第127行安排函数返回时调用 `Close` 方法。

在第131行，我们检测了 `Response` 值的 `StatusCode` 字段，确保收到的响应是 `200` 。任何不是 `200` 的请求都需要作为错误处理。如果响应值不是 `200` ，我们使用 `fmt` 包里的 `Errorf` 函数返回一个自定义的错误。最后3行代码很像之前解码JSON数据文件的代码。只是这次使用 `xml` 包并调用了同样叫作 `NewDecoder` 的函数。这个函数会返回一个指向 `Decoder` 值的指针。之后调用这个指针的 `Decode` 方法，传入 `rssDocument` 类型的局部变量 `document` 的地址。最后返回这个局部变量的地址和 `Decode` 方法调用返回的错误值。

最后我们来看看实现了 `Matcher` 接口的方法，如代码清单2-54所示。

代码清单2-54　matchers/rss.go: 第69行到第112行

```go
 69 // Search在文档中查找特定的搜索项
 70 func (m rssMatcher) Search(feed *search.Feed, searchTerm string) 
                                                   ([]*search.Result, error) {
 71     var results []*search.Result
 72
 73     log.Printf("Search Feed Type[%s] Site[%s] For Uri[%s]\n", 
                                               feed.Type, feed.Name, feed.URI)
 74
 75     // 获取要搜索的数据
 76     document, err := m.retrieve(feed)
 77     if err != nil {
 78         return nil, err
 79     }
 80
 81     for _, channelItem := range document.Channel.Item {
 82         // 检查标题部分是否包含搜索项
 83         matched, err := regexp.MatchString(searchTerm, channelItem.Title)
 84         if err != nil {
 85             return nil, err
 86         }
 87
 88         // 如果找到匹配的项，将其作为结果保存
 89         if matched {
 90             results = append(results, &search.Result{
 91                 Field:   "Title",
 92                 Content: channelItem.Title,
 93             })
 94         }
 95
 96         // 检查描述部分是否包含搜索项
 97         matched, err = regexp.MatchString(searchTerm, channelItem.Description)
 98         if err != nil {
 99             return nil, err
100         }
101
102         // 如果找到匹配的项，将其作为结果保存
103         if matched {
104             results = append(results, &search.Result{
105                 Field:   "Description",
106                 Content: channelItem.Description,
107             })
108         }
109     }
110
111     return results, nil
112 }
```

我们从第71行 `results` 变量的声明开始分析，如代码清单2-55所示。这个变量用于保存并返回找到的结果。

代码清单2-55　matchers/rss.go：第71行

```go
71     var results []*search.Result
```

我们使用关键字 `var` 声明了一个值为 `nil` 的切片，切片每一项都是指向 `Result` 类型值的指针。 `Result` 类型的声明在之前match.go代码文件的第08行中可以找到。之后在第76行，我们使用刚刚看过的 `retrieve` 方法进行网络调用，如代码清单2-56所示。

代码清单2-56　matchers/rss.go：第75行到第79行

```go
75     // 获取要搜索的数据
76     document, err := m.retrieve(feed)
77     if err != nil {
78         return nil, err
79     }
```

调用 `retrieve` 方法返回了一个指向 `rssDocument` 类型值的指针以及一个错误值。之后，像已经多次看过的代码一样，检查错误值，如果真的是一个错误，直接返回。如果没有错误发生，之后会依次检查得到的RSS文档的每一项的标题和描述，如果与搜索项匹配，就将其作为结果保存，如代码清单2-57所示。

代码清单2-57　matchers/rss.go：第81行到第86行

```go
81     for _, channelItem := range document.Channel.Item {
82         // 检查标题部分是否包含搜索项
83         matched, err := regexp.MatchString(searchTerm, channelItem.Title)
84         if err != nil {
85             return nil, err
86         }
```

既然 `document.Channel.Item` 是一个 `item` 类型值的切片，我们在第81行对其使用 `for range` 循环，依次访问其内部的每一项。在第83行，我们使用 `regexp` 包里的 `MatchString` 函数，对 `channelItem` 值里的 `Title` 字段进行搜索，查找是否有匹配的搜索项。之后在第84行检查错误。如果没有错误，就会在第89行到第94行检查匹配的结果，如代码清单2-58所示。

代码清单2-58　matchers/rss.go：第88行到第94行

```go
88         // 如果找到匹配的项，将其作为结果保存
89         if matched {
90             results = append(results, &search.Result{
91                 Field:   "Title",
92                 Content: channelItem.Title,
93             })
94         }
```

如果调用 `MatchString` 方法返回的 `matched` 的值为真，我们使用内置的 `append` 函数，将搜索结果加入到 `results` 切片里。 `append` 这个内置函数会根据切片需要，决定是否要增加切片的长度和容量。我们会在第4章了解关于内置函数 `append` 的更多知识。这个函数的第一个参数是希望追加到的切片，第二个参数是要追加的值。在这个例子里，追加到切片的值是一个指向 `Result` 类型值的指针。这个值直接使用字面声明的方式，初始化为 `Result` 类型的值。之后使用取地址运算符（ `&` ），获得这个新值的地址。最终将这个指针存入了切片。

在检查标题是否匹配后，第97行到第108行使用同样的逻辑检查 `Description` 字段。最后，在第111行， `Search` 方法返回了 `results` 作为函数调用的结果。

