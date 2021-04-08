### 3.2.2　通过HTTPS提供服务

当客户端和服务器需要共享密码或者信用卡信息这样的私密信息时，大多数网站都会使用HTTPS对客户端和服务器之间的通信进行加密和保护。在一些情况下，这种保护甚至是强制性的。比如说，如果一个网站提供了信用卡支付功能，那么按照支付卡行业数据安全标准（Payment Card Industry Data Security Standard），这个网站就必须对客户端和服务器之间的通信进行加密。像Gmail和Facebook这样带有隐私性质的网站甚至在整个网站上都启用了HTTPS。如果你打算开发一个网站，而这个网站又需要提供用户登录功能，那么你也需要在这个网站上启用HTTPS。

HTTPS实际上就是将HTTP通信放到SSL之上进行。通过使用 `ListenAndServeTLS` 函数，我们可以让之前展示过的简单Web应用也提供HTTPS服务，代码清单3-4展示了具体的实现代码。

代码清单3-4　通过HTTPS提供服务

```go
package main
import (
　　"net/http"
)
func main() {
　　server := http.Server{
　　　　Addr: "127.0.0.1:8080",
　　　　Handler: nil,
　　}
　　server.ListenAndServeTLS("cert.pem", "key.pem")
}
```

这段代码中的 `cert.pem` 文件是SSL证书，而 `key.pem` 则是服务器的私钥（private key）。在生产环境中使用的SSL证书需要通过VeriSign、Thawte或者Comodo SSL这样的CA取得，但如果是出于测试目的才使用证书和私钥，那么使用自行生成的证书就可以了。生成证书的办法有很多种，其中一种就是使用Go标准库中的 `crypto` 包群（library group）。

SSL、TLS和HTTPS

> SSL（Secure Socket Layer，安全套接字层）是一种通过公钥基础设施（Public Key Infrastructure，PKI）为通信双方提供数据加密和身份验证的协议，其中通信的双方通常是客户端和服务器。SSL最初由Netscape公司开发，之后由IETF（Internet Engineering Task Force，互联网工程任务组）接手并将其改名为TLS（Transport Layer Security，传输层安全协议）。HTTPS，即SSL之上的HTTP，实际上就是在SSL/TLS连接的上层进行HTTP通信。
> HTTPS需要使用SSL/TLS证书来实现数据加密以及身份验证（本书使用SSL证书这一名称，因为它更常用）。SSL证书存储在服务器之上，它是一种使用X.509格式进行格式化的数据，这些数据包含了公钥以及其他一些相关信息。为了保证证书的可靠性，证书一般由证书分发机构（Certificate Authority，CA）签发。服务器在接收到客户端发送的请求之后，会将证书和响应一并返回给客户端，而客户端在确认证书的真实性之后，就会生成一个随机密钥（random key），并使用证书中的公钥对随机密钥进行加密，此次加密产生的对称密钥（symmetric key）就是客户端和服务器在进行通信时，负责对通信实施加密的实际密钥（actual key）。

虽然我们不会在生产环境中使用自行生成的证书和私钥，但了解SSL证书和私钥的生成方法，并学会如何在开发和测试的过程中使用证书和私钥，也是一件非常有意义的事情。代码清单3-5展示了生成SSL证书以及服务器私钥的具体代码。

代码清单3-5　生成个人使用的SSL证书以及服务器私钥

```go
package main
import (
　　"crypto/rand"
　　"crypto/rsa"
　　"crypto/x509"
　　"crypto/x509/pkix"
　　"encoding/pem"
　　"math/big"
　　"net"
　　"os"
　　"time"
)
func main() {
　　max := new(big.Int).Lsh(big.NewInt(1), 128)
　　serialNumber, _ := rand.Int(rand.Reader, max)
　　subject := pkix.Name{
　　　　Organization:　　　 []string{"Manning Publications Co."},
　　　　OrganizationalUnit: []string{"Books"},
　　　　CommonName:　　　　 "Go Web Programming",
　　}
　　template := x509.Certificate{
　　　　SerialNumber: serialNumber,
　　　　Subject:　　　subject,
　　　　NotBefore:　　time.Now(),
　　　　NotAfter:　　 time.Now().Add(365 * 24 * time.Hour),
　　　　KeyUsage:　　 x509.KeyUsageKeyEncipherment | x509.KeyUsageDigitalSignature,
　　　　ExtKeyUsage:　[]x509.ExtKeyUsage{x509.ExtKeyUsageServerAuth},
　　　　IPAddresses:　[]net.IP{net.ParseIP("127.0.0.1")},
　　}
　　pk, _ := rsa.GenerateKey(rand.Reader, 2048)
　　derBytes, _ := x509.CreateCertificate(rand.Reader, &template,
　　➥&template, &pk.PublicKey, pk)
　　certOut, _ := os.Create("cert.pem")
　　pem.Encode(certOut, &pem.Block{Type: "CERTIFICATE", Bytes: derBytes})
　　certOut.Close()
　　keyOut, _ := os.Create("key.pem")
　　pem.Encode(keyOut, &pem.Block{Type: "RSA PRIVATE KEY", Bytes:
　　➥x509.MarshalPKCS1PrivateKey(pk)})
　　keyOut.Close()
}
```

生成SSL证书和密钥的步骤并不是特别复杂。因为SSL证书实际上就是一个将扩展密钥用法（extended key usage）设置成了服务器身份验证操作的X.509证书，所以程序在生成证书时使用了 `crypto/x509` 标准库。此外，因为创建证书需要用到私钥，所以程序在使用私钥成功创建证书之后，会将私钥单独保存在一个存放服务器私钥的文件里面。

让我们来仔细分析一下代码清单3-5中的主要代码吧。首先，程序使用一个 `Certificate` 结构来对证书进行配置：

```go
template := x509.Certificate{
　SerialNumber: serialNumber,
　Subject: subject,
　NotBefore: time.Now(),
　NotAfter: time.Now().Add(365*24*time.Hour),
　KeyUsage: x509.KeyUsageKeyEncipherment | x509.KeyUsageDigitalSignature,
　ExtKeyUsage: []x509.ExtKeyUsage{x509.ExtKeyUsageServerAuth},
　IPAddresses: []net.IP{net.ParseIP("127.0.0.1")},
}
```

结构中的证书序列号（ `SerialNumber` ）用于记录由CA分发的唯一号码，为了能让我们的Web应用运行起来，程序在这里生成了一个非常长的随机整数来作为证书序列号。之后，程序创建了一个专有名称（distinguished name），并将它设置成了证书的标题（subject）。此外，程序还将证书的有效期设置成了一年，而结构中 `KeyUsage` 字段和 `ExtKeyUsage` 字段的值则表明了这个X.509证书是用于进行服务器身份验证操作的。最后，程序将证书设置成了只能在IP地址127.0.0.1之上运行。

SSL证书

> X.509是国际电信联盟电信标准化部门（ITU-T）为公钥基础设施制定的一个标准，这个标准包含了公钥证书的标准格式。
> 一个X.509证书（简称SSL证书）实际上就是一个经过编码的ASN.1（Abstract Syntax Notation One，抽象语法表示法/1）格式的电子文档。ASN.1既是一个标准，也是一种表示法，它描述了表示电信以及计算机网络数据的规则和结构。
> X.509证书可以使用多种格式编码，其中一种编码格式是BER（Basic Encoding Rules，基本编码规则）。BER格式指定了一种自解释并且自定义的格式用于对ASN.1数据结构进行编码，而DER格式则是BER的一个子集。DER只提供了一种编码ASN.1值的方法，这种方法被广泛地应用于密码学当中，尤其是对X.509证书进行加密。
> SSL证书可以以多种不同的格式保存，其中一种是PEM（Privacy Enhanced Email，隐私增强邮件）格式，这种格式会对DER格式的X.509证书实施Base64编码，并且这种格式的文件都以 `-----BEGIN CERTIFICATE-----` 开头，以 `-----END CERTIFICATE-----` 结尾（除了用作文件格式之外，PEM和此处讨论的SSL证书关系并不大）。

在此之后，程序通过调用 `crypto/rsa` 标准库中的 `GenerateKey` 函数生成了一个RSA私钥：

```go
pk, _ := rsa.GenerateKey(rand.Reader, 2048)
```

程序创建的RSA私钥的结构里面包含了一个能够公开访问的公钥（public key），这个公钥在使用 `x509.CreateCertificate` 函数创建SSL证书的时候就会用到：

```go
derBytes, _ := x509.CreateCertificate(rand.Reader, &template, &template, 
➥&pk.PublicKey, pk)
```

`CreateCertificate` 函数接受 `Certificate` 结构、公钥和私钥等多个参数，创建出一个经过DER编码格式化的字节切片。后续代码的意图也非常简单明了，它们首先使用 `encoding/pem` 标准库将证书编码到 `cert.pem` 文件里面：

```go
certOut, _ := os.Create("cert.pem")
pem.Encode(certOut, &pem.Block{Type: "CERTIFICATE", Bytes: derBytes})
certOut.Close()
```

然后继续以PEM编码的方式把之前生成的密钥编码并保存到 `key.pem文件` 里面：

```go
keyOut, _ := os.Create("key.pem")
pem.Encode(keyOut, &pem.Block{Type: "RSA PRIVATE KEY", Bytes: 
➥x509.MarshalPKCS1PrivateKey(pk)})
keyOut.Close()
```

最后需要提醒的是，如果证书是由CA签发的，那么证书文件中将同时包含服务器签名以及CA签名，其中服务器签名在前，CA签名在后。

