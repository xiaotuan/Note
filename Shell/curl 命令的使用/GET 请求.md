可以使用下面命令进行 `GET` 请求：

```shell
$ curl -X GET http://www.example.com/?name=Json\&age=20
```

> 注意：在设置多个 `GET` 请求参数时使用到了 `&` 符号。由于 `&` 符号在终端中有特殊意义，因此需要对 `&` 符号使用 `\` 进行转义。