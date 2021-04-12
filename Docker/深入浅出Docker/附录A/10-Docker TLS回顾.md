## A.3　Docker TLS回顾

daemon 模式会拒绝那些没有有效签名的客户端命令，客户端模式下客户端不会连接没有有效证书的远端daemon。

通过Docker daemon配置文件完成daemon的TLS配置。文件名为 `daemon.json` ，是跨平台的。

下面的 `daemon.json` 可以在大部分操作系统中使用。

```rust
{
    "hosts": ["tcp://node3:2376"],
    "tls": true,
    "tlsverify": true,
    "tlscacert": "/home/ubuntu/.docker/ca.pem",
    "tlscert": "/home/ubuntu/.docker/cert.pem",
    "tlskey": "/home/ubuntu/.docker/key.pem"
}
```

+ `hosts` 告诉Docker daemon需要绑定的Socket。示例中将其绑定到了某个网络的2376端口上。用户可以选择任意空闲端口，但按惯例Docker安全连接都使用2376端口。使用 `systemd` 的Linux系统不能配置该参数，需要使用 `systemd` 重写文件来实现。
+ `tls` 和 `tlsverify` 强制daemon只使用加密和认证连接。
+ `tlscacert` 告诉Docker可以信任的CA。配置后Docker会信任由该CA签发的全部证书。
+ `tlscert` 告诉Docker daemon证书的位置。
+ `tlskey` 告诉Docker daemon私钥的位置。

修改上述任意配置，都需要重启Docker后才能生效。

只需设置两个环境变量，就可以完成Docker客户端TLS配置。

+ `DOCKER_HOST` 。
+ `DOCKER_TLS_VERIFY` 。

DOCKER_HOST为客户端指定如何查找daemon。

`export DOCKER_HOST=tcp://node3:2376` 让Docker客户端通过主机 `node3` 的 `2376` 端口连接到daemon。

`export DOCKER_TLS_VERIFY=1` 使Docker客户端对其发出的全部命令都进行签名。



