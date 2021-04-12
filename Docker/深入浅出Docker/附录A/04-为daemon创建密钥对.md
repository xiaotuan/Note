### A.1.2　为daemon创建密钥对

在本步骤中，会为node3生成新的密钥对。该节点准备运行Docker安全daemon。一共分4步。

（1）创建私钥。

（2）创建签名请求。

（3）添加IP地址，并设置为服务端认证有效。

（4）生成证书。

在CA节点（node2）运行全部命令。

（1）为daemon创建私钥。

```rust
$ openssl genrsa -out daemon-key.pem 4096
<Snip>
```

在当前工作目录下已经创建了名为 `daemon-key.pem`  的新文件，这就是daemon节点的私钥。

（2）创建证书签名请求（CSR）并发送到CA，这样就可以完成daemon证书的创建和签名。要确保使用正确的DNS名称来指代想要运行Docker安全daemon的节点。示例中使用了node3。

```rust
$ openssl req -subj "/CN=node3" \
  -sha256 -new -key daemon-key.pem -out daemon.csr
```

现在工作目录下有了第四个文件。该文件是CSR，名称为 `daemon.csr` 。

（3）为证书添加属性。

需要创建一个文件，其中包含了CA签发证书时需要加入到daemon证书的扩展属性。这些属性包括daemon的DNS名称和IP地址，同时配置证书使用服务端认证。

创建的新文件名为 `extfile.cnf` ，包含下面列举的值。示例中使用了图A.2中daemon节点的DNS名称和IP。读者环境中的值可能会有不同。

```rust
subjectAltName = DNS:node3,IP:10.0.0.12
extendedKeyUsage = serverAuth
```

（4）生成证书。

使用CSR文件、CA密钥、 `extfile.cnf` 文件完成签名以及daemon证书配置。命令输出中包含daemon的公钥（证书）和一个名为 `daemon-cert.perm` 的文件。

```rust
$ openssl x509 -req -days 730 -sha256 \
  -in daemon.csr -CA ca.pem -CAkey ca-key.pem \
  -CAcreateserial -out daemon-cert.pem -extfile extfile.cnf
```

此时，已经拥有了一个可用的CA，同时运行Docker安全daemon的 `node3` 节点也有了自己的一对密钥。

继续下面内容之前，删除 `CSR` 和 `extfile.cnf` 。

```rust
$ rm daemon.csr extfile.cnf
```

