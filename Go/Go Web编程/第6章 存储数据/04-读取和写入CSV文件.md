### 6.2.1　读取和写入CSV文件

CSV格式是一种文件格式，它可以让文本编辑器非常方便地读写由文本和数字组成的表格数据。CSV的应用非常广泛，包括微软的Excel和苹果的Numbers在内的绝大多数电子表格程序都支持CSV格式，因此包括Go在内的很多编程语言都提供了能够生成和处理CSV文件数据的函数库。

对Go语言来说，CSV文件可以通过 `encoding/csv` 包进行操作，代码清单6-3展示了如何通过这个包来读写CSV文件。

代码清单6-3　读写CSV文件

```go
package main
import (
　　"encoding/csv"
　　"fmt"
　　"os"
　　"strconv"
)
type Post struct {
　　Id　　 int
　　Content string
　　Author　string
}
func main() {
　   csvFile, err := os.Create("posts.csv") ❶
　　if err != nil {
　　　　panic(err)
　　}
　　defer csvFile.Close()
　　allPosts := []Post{
　　　　Post{Id: 1, Content: "Hello World!", Author: "Sau Sheong"},
　　　　Post{Id: 2, Content: "Bonjour Monde!", Author: "Pierre"},
　　　　Post{Id: 3, Content: "Hola Mundo!", Author: "Pedro"},
　　　　Post{Id: 4, Content: "Greetings Earthlings!", Author: "Sau Sheong"},
　　}
　　writer := csv.NewWriter(csvFile)
　　for _, post := range allPosts {
　　　　line := []string{strconv.Itoa(post.Id), post.Content, post.Author}
　　　　err := writer.Write(line)
　　　　if err != nil {
　　　　　　panic(err)
　　　　}
　　}
　　writer.Flush()
  　 file, err := os.Open("posts.csv") ❷
　　if err != nil {
　　　　panic(err)
　　}
　　defer file.Close()
　　reader := csv.NewReader(file)
　　reader.FieldsPerRecord = -1
　　record, err := reader.ReadAll()
　　if err != nil {
　　　　panic(err)
　　}
　　var posts []Post
　　for _, item := range record {
　　　　id, _ := strconv.ParseInt(item[0], 0, 0)
　　　　post := Post{Id: int(id), Content: item[1], Author: item[2]}
　　　　posts = append(posts, post)
　　}
　　fmt.Println(posts[0].Id)
　　fmt.Println(posts[0].Content)
　　fmt.Println(posts[0].Author)
}
```

❶ 创建一个CSV 文件

❷ 打开一个CSV 文件

首先让我们来了解一下如何对CSV文件执行写操作。在一开始，程序会创建一个名为 `posts.csv` 的文件以及一个名为 `csvFile` 的变量，而后续代码的目标则是将 `allPosts` 变量中的所有帖子都写入这个文件。为了完成这一目标，程序会使用 `NewWriter` 函数创建一个新的写入器（writer），并把文件用作参数，将其传递给写入器。在此之后，程序会为每个待写入的帖子都创建一个由字符串组成的切片。最后，程序调用写入器的 `Write` 方法，将一系列由字符串组成的切片写入之前创建的CSV文件。

如果程序进行到这一步就结束并退出，那么前面提到的所有数据都会被写入文件，但由于程序在接下来的代码中立即就要对写入的 `posts.csv` 文件进行读取，而刚刚写入的数据有可能还滞留在缓冲区中，所以程序必须调用写入器的 `Flush` 方法来保证缓冲区中的所有数据都已经被正确地写入文件里面了。

读取CSV文件的方法和写入文件的方法类似。首先，程序会打开文件，并通过将文件传递给 `NewReader` 函数来创建出一个读取器（reader）。接着，程序会将读取器的 `FieldsPerRecord` 字段的值设置为负数，这样的话，即使读取器在读取时发现记录（record）里面缺少了某些字段，读取进程也不会被中断。反之，如果 `FieldsPerRecord` 字段的值为正数，那么这个值就是用户要求从每条记录里面读取出的字段数量，当读取器从CSV文件里面读取出的字段数量少于这个值时，Go就会抛出一个错误。最后，如果 `FieldsPerRecord` 字段的值为 `0` ，那么读取器就会将读取到的第一条记录的字段数量用作 `FieldsPerRecord` 的值。

在设置好 `FieldsPerRecord` 字段之后，程序会调用读取器的 `ReadAll` 方法，一次性地读取文件中包含的所有记录；但如果文件的体积较大，用户也可以通过读取器提供的其他方法，以每次一条记录的方式读取文件。 `ReadAll` 方法将返回一个由一系列切片组成的切片作为结果，程序会遍历这个切片，并为每条记录创建对应的 `Post` 结构。如果我们运行代码清单6-3所示的程序，那么程序将创建一个名为 `posts.csv` 的CSV文件，该文件将包含以下多个由逗号分隔的文本行：

```go
1,Hello World!,Sau Sheong
2,Bonjour Monde!,Pierre
3,Hola Mundo!,Pedro
4,Greetings Earthlings!,Sau Sheong
```

除此之外，这个程序还会读取 `posts.csv` 文件，并打印出该文件第一行的内容：

```go
1
Hello World!
Sau Sheong
```

