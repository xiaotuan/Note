可以通过 `-d` 参数设置 `POST` 参数。

```shell
$ curl -d 'login=emma&password=123' -X POST http://127.0.0.1:8124
```

或

```shell
$ curl -d 'login=emma' -d 'password=123' -X POST http://127.0.0.1:8124
```

使用 `-d` 参数以后，`HTTP` 请求会自动加上请求头 `Content-Type: application/x-www-form-urlencoded`。并且会自动将请求转为 `POST` 方法，因此可以省略 `-X POST`.

`-d` 参数可以读取本地文本文件的数据，向服务器发送。

```shell
$ curl -d '@data.txt' http://127.0.0.1:8124
```

上面命令读取 `data.txt` 文件的内容，作为数据体向服务器发送。

`--data-urlencode` 参数等同于 `-d`，发送 `POST` 请求的数据体，区别在于会自动将发送的数据进行 URL 编码。

```shell
$ curl --data-urlencode 'comment=hello world' http://127.0.0.1:8124
```



