### 2.1.1　URL

对于我们而言，URL分为两个主要部分。第一个部分通过 **域名系统** （ **Domain Name System** ， **DNS** ）帮助我们在网络上定位合适的服务器。比如，当在浏览器中发送 `https:// mail.google.com/mail/u/0/#inbox` 时，将会创建一个对 `mail.google.com` 的DNS请求，用于确定合适的服务器IP地址，如 `173.194.71.83` 。从本质上来看， `https:// mail.google.com/mail/u/0/#inbox` 被翻译为 `https://173.194.71.83/mail/ u/0/#inbox` 。

URL的剩余部分对于服务端理解请求是什么非常重要。它可能是一张图片、一个文档，或是需要触发某个动作的东西，比如向服务器发送邮件。

