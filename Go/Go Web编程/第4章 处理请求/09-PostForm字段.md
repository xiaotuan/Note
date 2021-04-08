### 4.2.2　PostForm字段

对上一节提到的 `post` 这种只会出现在表单或者URL两者其中一个地方的键来说，执行语句 `r.Form["post"]` 将返回一个切片，切片里面包含了这个键的表单值或者URL值，就像这样： `[456]` 。而对 `hello` 这种同时出现在表单和URL两个地方的键来说，执行语句 `r.Form["hello"]` 将返回一个同时包含了键的表单值和URL值的切片，并且表单值在切片中总是排在URL值的前面，就像这样： `[sau sheong world]` 。

如果一个键同时拥有表单键值对和URL键值对，但是用户只想要获取表单键值对而不是URL键值对，那么可以访问 `Request` 结构的 `PostForm` 字段，这个字段只会包含键的表单值，而不包含任何同名键的URL值。举个例子，如果我们把前面代码中的 `r.Form` 语句改为 `r.PostForm` 语句，那么程序将打印出以下结果：

```go
map[post:[456] hello:[sau sheong]]
```

上面这个输出使用的是 `application/x-www-form-urlencoded` 内容类型，如果我们修改一下客户端的HTML表单，让它使用 `multipart/form-data` 作为内容类型，并对服务器代码进行调整，让它重新使用 `r.Form` 语句而不是 `r.PostForm` 语句，那么程序将打印出以下结果：

```go
map[hello:[world] thread:[123]]
```

因为 `PostForm` 字段只支持 `application/x-www-form-urlencoded` 编码，所以现在的 `r.Form` 语句将不再返回任何表单值，而是只返回URL查询值。为了解决这个问题，我们需要通过 `MultipartForm` 字段来获取 `multipart/form-data` 编码的表单数据。

