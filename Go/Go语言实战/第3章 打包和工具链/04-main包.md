### 3.1.2　 `main` 包

在Go语言里，命名为 `main` 的包具有特殊的含义。Go语言的编译程序会试图把这种名字的包编译为二进制可执行文件。所有用Go语言编译的可执行程序都必须有一个名叫 `main` 的包。

当编译器发现某个包的名字为 `main` 时，它一定也会发现名为 `main()` 的函数，否则不会创建可执行文件。 `main()` 函数是程序的入口，所以，如果没有这个函数，程序就没有办法开始执行。程序编译时，会使用声明 `main` 包的代码所在的目录的目录名作为二进制可执行文件的文件名。

> **命令和包** 　Go文档里经常使用命令（command）这个词来指代可执行程序，如命令行应用程序。这会让新手在阅读文档时产生困惑。记住，在Go语言里，命令是指任何可执行程序。作为对比，包更常用来指语义上可导入的功能单元。

让我们来实际体验一下。首先，在$GOPATH/src/hello/目录里创建一个叫hello.go的文件，并输入代码清单3-1里的内容。这是个经典的“Hello World!”程序，不过，注意一下包的声明以及 `import` 语句。

代码清单3-1　经典的“Hello World!”程序

```go
01 package main
02
03 import "fmt" 　　●――――fmt包提供了完成格式化输出的功能。
04
05 func main() {
06　　 fmt.Println("Hello World!")
07 }

```

> **获取包的文档** 　别忘了，可以访问<a class="my_markdown" href="['http://golang.org/pkg/fmt/']">http://golang.org/pkg/fmt/</a>或者在终端输入 `godoc fmt` 来了解更多关于 `fmt` 包的细节。

保存了文件后，可以在$GOPATH/src/hello/目录里执行命令 `go build` 。这条命令执行完后，会生成一个二进制文件。在UNIX、Linux和Mac OS X系统上，这个文件会命名为hello，而在Windows系统上会命名为hello.exe。可以执行这个程序，并在控制台上显示“Hello World!”。

如果把这个包名改为 `main` 之外的某个名字，如 `hello` ，编译器就认为这只是一个包，而不是命令，如代码清单3-2所示。

代码清单3-2　包含 `main` 函数的无效的Go程序

```go
01 package hello
02
03 import "fmt"
04
05 func main(){
06　　 fmt.Println("Hello, World!")
07 }
```

