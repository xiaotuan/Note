### A.2.2　为Docker客户端配置TLS

本节将从以下两方面配置node1节点上的Docker客户端。

+ 通过网络连接某个远程daemon。
+ 为所有 `docker` 命令进行签名。

在将要运行Docker安全客户端的节点上（示例环境中为 `node1` ）执行下面的全部命令。

配置下列环境变量，使客户端可以通过网络连接到远端daemon。

```rust
export DOCKER_HOST=tcp://node3:2376
```

尝试下面的命令。

```rust
$ docker version
Client:
 Version:       18.01.0-ce
<Snip>
Get http://daemon:2376/v1.35/version: net/http: HTTP/1.x transport connectio\
n broken: malformed HTTP response "\x15\x03\x01\x00\x02\x02".
* Are you trying to connect to a TLS-enabled daemon without TLS?
```

Docker客户端通过网络发送命令到远端daemon，但是daemon只接收受认证的连接。

设置另外一个环境变量，告知Docker客户端使用自己证书对全部命令进行签名。

```rust
export DOCKER_TLS_VERIFY=1
```

再次运行 `docker version` 命令。

```rust
$ docker version
Client:
 Version:       18.01.0-ce
<Snip>
Server:
 Engine:
  Version:      18.01.0-ce
  API version:  1.35 (minimum version 1.12)
  Go version:   go1.9.2
  Git commit:   03596f5
  Built:        Wed Jan 10 20:09:37 2018
  OS/Arch:      linux/amd64
  Experimental: false
```

恭喜。客户端成功通过安全连接与远程daemon完成通信。最终配置如图A.4所示。

![147.png](./images/147.png)
<center class="my_markdown"><b class="my_markdown">图A.4　最终配置</b></center>

在进行快速回顾前，有几点需要说明一下。

（1）最后的示例可以成功，是因为将客户端TLS密钥复制到了Docker期望的目录下。该目录位于用户home目录下，名为 `.docker` 。同时密钥也修改为Docker期望的名称（ `ca.pem` 、 `cert.pem` ，以及 `key.pem` ）。可以通过配置环境变量 `DOCKER_CERT_PATH` 来指定其他的目录。

（2）读者可能希望持久化环境中的变量（ `DOCKER_HOST` 和 `DOCKER_TLS_VERIFY` ）。

