可以使用下面命令进行 `GET` 请求：

```shell
$ curl -X GET http://www.example.com/?name=Json\&age=20
```

> 注意：在设置多个 `GET` 请求参数时使用到了 `&` 符号。由于 `&` 符号在终端中有特殊意义，因此需要对 `&` 符号使用 `\` 进行转义。

可以使用 `-G` 参数来构造 URL 的查询字符串。

```shell
$ curl -G -d 'q=kitties' -d 'count=20' http://127.0.0.1:8124
```

上面命令会发出一个 `GET` 请求，实际请求的 `URL` 为 `http://127.0.0.1:8124?q=kitties&count=20`。如果省略 `-G`，会发出一个 `POST` 请求。

如果数据需要 `URL` 编码，可以结合 `--data-urlencode` 参数。

```shell
$ curl -G --data-urlencode 'comment=hello world' http://127.0.0.1:8124
```

