### A.2.1　为Docker daemon配置TLS

启动daemon安全模式，只需在daemon.json配置文件中增加几个守护参数即可。

+ `tlsverify` ：开启TLS认证。
+ `tlscacert` ：指定daemon可信任的CA。
+ `tlscert` ：向Docker指定daemon证书的位置。
+ `tlskey` ：向Docker指定daemon私钥的位置。
+ `hosts` ：向Docker指定需要绑定daemon的具体Socket。

上述内容配置在与平台无关的 `daemon.json` 配置文件当中。在Linux上位于 `/etc/docker` ，在Windows上位于 `C:\ProgramData\Docker\config\` 。

在Docker安全daemon节点上执行下面的全部操作（在示例环境中是 `node3` ）。

编辑 `daemon.json` 文件，并添加如下行。

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

警告：

> 运行 `systemd` 的Linux系统不允许在 `daemon.json` 中使用“hosts”选项。替换方案是在systemd配置文件中进行重写。最简单的方式是通过 `sudo systemdctl edit docker` 命令进行修改。该命令会在编辑器中打开名为 `/etc/systemd/system/docker.service.d/override.conf` 的新文件。在其中加入下列3行内容，然后保存。

```rust
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H tcp://node3:2376
```

现在TLS和主机选型都设置完成，是时候重启Docker了。

一旦Docker重启完成，可以使用 `ps` 命令，根据其输出内容检查新的 `hosts` 值是否生效。

```rust
$ ps -elf | grep dockerd
4 S root ... /usr/bin/dockerd -H tcp://node3:2376
```

输出内容中如果有“ `-H tcp://node3:2376` ”，则可以证明daemon正在监听网络。端口 `2376` 是Docker TLS使用的标准端口。 `2375` 默认是非安全端口。

如果运行的是普通命令，会出现无法工作的情况，如 `docker version` 。这是因为刚才配置了daemon监听网络，但是Docker客户端仍尝试使用本地IPC Socket。加上 `-H tcp://node3:2376` 参数后再次运行该命令。

```rust
$ docker -H tcp://node3:2376 version
Client:
 Version:       18.01.0-ce
 API version:   1.35
<Snip>
Get http://daemon:2376/v1.35/version: net/http: HTTP/1.x transport connectio\
n broken: malformed HTTP response "\x15\x03\x01\x00\x02\x02".
* Are you trying to connect to a TLS-enabled daemon without TLS?
```

命令看起来没什么问题，但是仍然不工作。这是因为daemon拒绝了来自未认证客户端的连接。

恭喜。Docker daemon已经配置为监听网络，并且拒绝了来自未认证客户端的连接。

接下来配置 `node1` 节点上的Docker client使用TLS。

