### 6.2.2　gob包

`encoding/gob` 包用于管理由gob组成的流（stream），这是一种在编码器（encoder）和解码器（decoder）之间进行交换的二进制数据，这种数据原本是为序列化以及数据传输而设计的，但它也可以用于对数据进行持久化，并且为了让用户能够方便地对文件进行读写，编码器和解码器一般都会分别包裹起程序的写入器以及读取器。代码清单6-4展示了如何使用 `gob` 包去创建二进制数据文件，以及如何去读取这些文件。

代码清单6-4　使用 `gob` 包读写二进制数据

```go
package main
import (
　　"bytes"
　　"encoding/gob"
　　"fmt"
　　"io/ioutil"
)
type Post struct {
　　Id　　 int
　　Content string
　　Author string
}
func store(data interface{}, filename string) {  ❶
　　buffer := new(bytes.Buffer)
　　encoder := gob.NewEncoder(buffer)
　　err := encoder.Encode(data)
　　if err != nil {
　　　　panic(err)
　　}
　　err = ioutil.WriteFile(filename, buffer.Bytes(), 0600)
　　if err != nil {
　　　　panic(err)
　　}
}
func load(data interface{}, filename string) {  ❷
　　raw, err := ioutil.ReadFile(filename)
　　if err != nil {
　　　　panic(err)
　　}
　　buffer := bytes.NewBuffer(raw)
　　dec := gob.NewDecoder(buffer)
　　err = dec.Decode(data)
　　if err != nil {
　　　　panic(err)
　　}
}
func main() {
　　post := Post{Id: 1, Content: "Hello World!", Author: "Sau Sheong"}
　　store(post, "post1")
　　var postRead Post
　　load(&postRead, "post1")
　　fmt.Println(postRead)
}
```

❶ 存储数据

❷ 载入数据

跟前面展示的程序一样，代码清单6-4所示的程序也会用到 `Post` 结构，并且也包含了相应的 `store` 方法和 `load` 方法，但是跟之前不一样的是，这次的 `store` 方法会将帖子存储为二进制数据，而 `load` 方法则会通过读取这些二进制数据来获取帖子。

首先来分析一下 `store` 函数，这个函数的第一个参数是一个空接口，而第二个参数则是被存储的二进制文件的名字。虽然空接口参数能够接受任意类型的数据作为值，但是在这个函数里面，它接受的将是一个 `Post` 结构。在接受了相应的参数之后， `store` 函数会创建一个 `bytes.Buffer` 结构，这个结构实际上就是一个拥有 `Read` 方法和 `Write` 方法的可变长度（variable-sized）字节缓冲区，换句话说， `bytes.Buffer` 既是读取器也是写入器。

在此之后， `store` 函数会把缓冲区传递给 `NewEncoder` 函数，以此来创建出一个gob编码器，接着调用编码器的 `Encode` 方法将数据（也就是 `Post` 结构）编码到缓冲区里面，最后再将缓冲区中已编码的数据写入文件。

程序在调用 `store` 函数时，会将一个 `Post` 结构和一个文件名作为参数，而这个函数则会创建出一个名为 `post1` 的二进制数据文件。

接下来，让我们来研究一下 `load` 函数，这个函数从二进制数据文件中载入数据的步骤跟创建并写入这个文件的步骤正好相反：首先，程序会从文件里面读取出未经处理的原始数据；接着，程序会根据这些原始数据创建一个缓冲区，并借此为原始数据提供相应的 `Read` 方法和 `Write` 方法；在此之后，程序会调用 `NewDecoder` 函数，为缓冲区创建相应的解码器，然后使用解码器去解码从文件中读取的原始数据，并最终得到之前写入的 `Post` 结构。

在 `main` 函数里面，程序定义了一个名为 `postRead` 的 `Post` 结构，并将这个结构的引用以及二进制数据文件的名字传递给了 `load` 函数，而 `load` 函数则会把读取二进制文件所得的数据载入给定的 `Post` 结构。

当我们运行代码清单6-4所示的程序时，将创建出一个包含二进制数据的 `post1` 文件——因为这个文件包含的是二进制数据，所以如果直接打开这个文件，将会看到一些似乎毫无意义的数据。除创建 `post1` 文件之外，程序还会读取文件中的数据并将其载入 `Post` 结构里面，然后在控制终端打印出这个结构：

```go
{1 Hello World! Sau Sheong}
```

好了，关于使用文件存储数据的介绍到此就结束了，本章接下来的内容将会讨论如何将数据存储到一种名为数据库服务器的特殊服务器端程序里面。

