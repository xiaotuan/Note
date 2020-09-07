1. 设置代理命令

```shell
$ git config --global http.proxy socks5://127.0.0.1:1080
$ git config --global https.proxy socks5://127.0.0.1:1080
```

2. 取消代理命令

```shell
$ git config --system（或--global 或--local）--unset http.proxy
$ git config --system（或--global 或--local）--unset https.proxy
```

3. 获取代理设置状态命令

```shell
$ git config --global --get http.proxy
$ git config --global --get https.proxy
```

