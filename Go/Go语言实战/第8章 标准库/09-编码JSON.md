### 8.3.2　编码JSON

我们要学习的处理JSON的第二个方面是，使用 `json` 包的 `MarshalIndent` 函数进行编码。这个函数可以很方便地将Go语言的 `map` 类型的值或者结构类型的值转换为易读格式的JSON文档。 **序列化** （marshal）是指将数据转换为JSON字符串的过程。下面是一个将 `map` 类型转换为JSON字符串的例子，如代码清单8-31所示。

代码清单8-31　listing31.go

```go
01 // 这个示例程序展示如何序列化JSON字符串
02 package main
03
04 import (
05　　 "encoding/json"
06　　 "fmt"
07　　 "log"
08 )
09
10 func main() {
11　　 // 创建一个保存键值对的映射
12　　 c := make(map[string]interface{})
13　　 c["name"] = "Gopher"
14　　 c["title"] = "programmer"
15　　 c["contact"] = map[string]interface{}{
16　　　　 "home": "415.333.3333",
17　　　　 "cell": "415.555.5555",
18　　 }
19
20　　 // 将这个映射序列化到JSON字符串
21　　 data, err := json.MarshalIndent(c, "", "　　")
22　　 if err != nil {
23　　　　 log.Println("ERROR:", err)
24　　　　 return
25　　 }
26
27　　 fmt.Println(string(data))
28 }
```

代码清单8-31展示了如何使用 `json` 包的 `MarshalIndent` 函数将一个 `map` 值转换为JSON字符串。函数 `MarshalIndent` 返回一个 `byte` 切片，用来保存JSON字符串和一个 `error` 值。下面来看一下 `json` 包中 `MarshalIndent` 函数的声明，如代码清单8-32所示。

代码清单8-32　golang.org/src/encoding/json/encode.go

```go
// MarshalIndent很像Marshal，只是用缩进对输出进行格式化
func MarshalIndent(v interface{}, prefix, indent string) ([]byte, error) {
```

在 `MarshalIndent` 函数里再一次看到使用了空接口类型 `interface{}` 。函数 `MarshalIndent` 会使用反射来确定如何将 `map` 类型转换为JSON字符串。

如果不需要输出带有缩进格式的JSON字符串， `json` 包还提供了名为 `Marshal` 的函数来进行解码。这个函数产生的JSON字符串很适合作为在网络响应（如Web API）的数据。函数 `Marshal` 的工作原理和函数 `MarshalIndent` 一样，只不过没有用于前缀 `prefix` 和缩进 `indent` 的参数。

