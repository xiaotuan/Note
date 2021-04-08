### 4.2.3　MultipartForm字段

为了取得 `multipart/form-data` 编码的表单数据，我们需要用到 `Request` 结构的 `ParseMultipartForm` 方法和 `MultipartForm` 字段，而不再使用 `ParseForm` 方法和 `Form` 字段，不过 `ParseMultipartForm` 方法在需要时也会自行调用 `ParseForm` 方法。现在，我们需要修改代码清单4-4中展示的服务器程序，把原来的 `ParseForm` 方法调用以及打印语句替换成以下两条语句：

```go
r.ParseMultipartForm(1024)
fmt.Fprintln(w, r.MultipartForm)
```

这里的第一行代码说明了我们想要从multipart编码的表单里面取出多少字节的数据，而第二行语句则会打印请求的 `MultipartForm` 字段。修改后的服务器在执行时将打印以下结果：

```go
&{map[hello:[sau sheong] post:[456]] map[]}
```

因为 `MultipartForm` 字段只包含表单键值对而不包含URL键值对，所以这次打印出来的只有表单键值对而没有URL键值对。另外需要注意的是， `MultipartForm` 字段的值也不再是一个映射，而是一个包含了两个映射的结构，其中第一个映射的键为字符串，值为字符串组成的切片，而第二个映射则是空的——这个映射之所以会为空，是因为它是用来记录用户上传的文件的，关于这个映射的具体信息我们将会在接下来的一节看到。

除了上面提到的几个方法之外， `Request` 结构还提供了另外一些方法，它们可以让用户更容易地获取表单中的键值对。其中， `FormValue` 方法允许直接访问与给定键相关联的值，就像访问 `Form` 字段中的键值对一样，唯一的区别在于：因为 `FormValue` 方法在需要时会自动调用 `ParseForm` 方法或者 `ParseMultipartForm` 方法，所以用户在执行 `FormValue` 方法之前，不需要手动调用上面提到的两个语法分析方法。

这意味着，如果我们把以下语句写到代码清单4-4所示的服务器程序中：

```go
fmt.Fprintln(w,r.FormValue("hello"))
```

并将客户端表单的 `enctype` 属性的值设置为 `application/x-www-form-urlencoded` ，那么服务器将打印出以下结果：

```go
sau sheong
```

因为 `FormValue` 方法即使在给定键拥有多个值的情况下，也只会从 `Form` 结构中取出给定键的第一个值，所以如果想要获取给定键包含的所有值，那么就需要直接访问 `Form` 结构：

```go
fmt.Fprintln(w, r.FormValue("hello"))
fmt.Fprintln(w, r.Form)
```

上面这两条语句将产生以下输出：

```go
sau sheong
map[post:[456] hello:[sau sheong world] thread:[123]]
```

除了访问的是 `PostForm` 字段而不是 `Form` 字段之外， `PostFormValue` 方法的作用跟上面介绍的 `FormValue` 方法的作用基本相同。下面是一个使用 `PostFormValue` 方法的例子：

```go
fmt.Fprintln(w, r.PostFormValue("hello"))
fmt.Fprintln(w, r.PostForm)
```

下面是这两行代码的输出结果：

```go
sau sheong
map[hello:[sau sheong] post:[456]]
```

正如结果所示， `PostFormValue` 方法只会返回表单键值对而不会返回URL键值对。

`FormValue` 方法和 `PostFormValue` 方法都会在需要时自动去调用 `ParseMultipartForm` 方法，因此用户并不需要手动调用 `ParseMultipartForm` 方法，但这里也有一个需要注意的地方（至少对于Go 1.4版本来说）：如果你将表单的 `enctype` 设置成了 `multipart/form-data` ，然后尝试通过 `FormValue` 方法或者 `PostFormValue` 方法来获取键的值，那么即使这两个方法调用了 `ParseMultipartForm` 方法，你也不会得到任何结果。

为了验证这一点，让我们再次修改服务器程序，给它加上以下代码：

```go
fmt.Fprintln(w, "(1)", r.FormValue("hello"))
fmt.Fprintln(w, "(2)", r.PostFormValue("hello"))
fmt.Fprintln(w, "(3)", r.PostForm)
fmt.Fprintln(w, "(4)", r.MultipartForm)
```

以下是在表单的 `enctype` 为 `multipart/form-data` 的情况下，服务器打印出的结果：

```go
(1) world
(2)
(3) map[]
(4) &{map[hello:[sau sheong] post:[456]] map[]}
```

结果中的第一行返回的是键 `hello` 的值，并且这个值来自URL而不是表单。至于结果中的第二行和第三行，则证明了前面提到的“使用 `PostFormValue` 方法不会得到任何值”这一说法，而 `PostForm` 字段为空则是引发这一现象的罪魁祸首。 `PostForm` 字段之所以会为空，是因为 `FormValue` 方法和 `PostFormValue` 方法分别对应 `Form` 字段和 `PostForm` 字段，而表单在使用 `multipart/form-data` 编码时，表单数据将被存储到 `MultipartForm` 字段而不是以上两个字段中。结果的最后一行证明 `ParseMultipartForm` 方法的确被调用了——用户只要访问 `MultipartForm` 字段，就可以取得所有表单值。

本节介绍了 `Request` 结构的很多相关字段以及方法，表4-1对它们进行了回顾，并阐述了各个方法之间的区别。除此之外，这个表还说明了调用哪个方法可以取得哪个字段的值，并阐述了这些值的来源以及这些值的类型。比如，表的第一行就说明了，通过以直接或间接的方式调用 `ParseForm` 方法，用户可以将数据存储到 `Form` 字段里面，然后用户只要访问 `Form` 字段，就可以取得编码类型为 `application/x-www-form-urlencoded` 的URL数据和表单数据。对表4-1中列出的字段以及方法来说，它们唯一令人感到遗憾的地方就是，这些字段以及方法的命名规范并不是特别让人满意，还有很多有待改善的地方。

<center class="my_markdown"><b class="my_markdown">表4-1　对比 `Form、PostForm` 和 `MultipartForm` 字段</b></center>

| 字段 | 需要调用的方法或 | 需要访问的字段 | 键值对的来源 | 内容类型 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| URL | 表单 | URL编码 | Multipart编码 |
| `Form` | `ParseForm` 方法 | ✓ | ✓ | ✓ | — |
| `PostForm` | `Form` 字段 | — | ✓ | ✓ | — |
| `MultipartForm` | `ParseMultipartForm`  方法 | — | ✓ | — | ✓ |
| `FormValue` | 无 | ✓ | ✓ | ✓ | — |
| `PostFormValue` | 无 | — | ✓ | ✓ | — |

