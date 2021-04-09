### 8.4.3　简单的curl

在Linux和MacOS（曾用名Mac OS X）系统里可以找到一个名为 `curl` 的命令行工具。这个工具可以对指定的URL发起HTTP请求，并保存返回的内容。通过使用 `http` 、 `io` 和 `os` 包，我们可以用很少的几行代码来实现一个自己的 `curl` 工具。

让我们来看一下实现了基础 `curl` 功能的例子，如代码清单8-46所示。

代码清单8-46　listing46.go

```go
01 // 这个示例程序展示如何使用io.Reader和io.Writer接口
02 // 写一个简单版本的curl
03 package main
04
05 import (
06　　 "io"
07　　 "log"
08　　 "net/http"
09　　 "os"
10 )
11
12 // main是应用程序的入口
13 func main() {
14　　 // 这里的r是一个响应，r.Body是io.Reader
15　　 r, err := http.Get(os.Args[1])
16　　 if err != nil {
17　　　　 log.Fatalln(err)
18　　 }
19
20　　 // 创建文件来保存响应内容
21　　 file, err := os.Create(os.Args[2])
22　　 if err != nil {
23　　　　 log.Fatalln(err)
24　　 }
25　　 defer file.Close()
26
27　　 // 使用MultiWriter，这样就可以同时向文件和标准输出设备
28　　 // 进行写操作
29　　 dest := io.MultiWriter(os.Stdout, file)
30
31　　 // 读出响应的内容，并写到两个目的地
32　　 io.Copy(dest, r.Body)
33　　 if err := r.Body.Close(); err != nil {
34　　　　 log.Println(err)
35　　 }
36 }
```

代码清单8-46展示了一个实现了基本骨架功能的 `curl` ，它可以下载、展示并保存任意的HTTP  `Get` 请求的内容。这个例子会将响应的结果同时写入文件以及 `stdout` 。为了让例子保持简单，这个程序没有检查命令行输入参数的有效性，也没有支持更高级的选项。

在这个程序的第15行，使用来自命令行的第一个参数来执行HTTP  `Get` 请求。如果这个参数是一个URL，而且请求没有发生错误，变量 `r` 里就包含了该请求的响应结果。在第21行，我们使用命令行的第二个参数打开了一个文件。如果这个文件打开成功，那么在第25行会使用 `defer` 语句安排在函数退出时执行文件的关闭操作。

因为我们希望同时向 `stdout` 和指定的文件里写请求的内容，所以在第29行我们使用 `io` 包里的 `MultiWriter` 函数将文件和 `stdout` 整合为一个 `io.Writer` 值。在第33行，我们使用 `io` 包的 `Copy` 函数从响应的结果里读取内容，并写入两个目的地。由于有 `MultiWriter` 函数提供的值的支持，我们可使用一次 `Copy` 调用，将内容同时写到两个目的地。

利用 `io` 包里已经提供的支持，以及 `http` 和 `os` 包里已经实现了 `io.Writer` 和 `io.Reader` 接口类型的实现，我们不需要编写任何代码来完成这些底层的函数，借助已经存在的功能，将注意力集中在需要解决的问题上。如果我们自己的类型也实现了这些接口，就可以立刻支持已有的大量功能。

