[toc]

### 5.3　使用Apache来代理Node服务器

> <img class="my_markdown" src="../images/70.png" style="zoom:50%;" />
> **使用端口来访问网站**
> 使用代理并不会阻止我们使用显式的端口来访问网站。你可以通过设置来阻止这种访问，但是需要在服务器进行额外的配置。比如，在我的Ubuntu服务器上，可以修改 `iptables` ：
> 但是这种做法需要一些服务器管理方面的知识。

我觉得应该没有人认为Node会在不久的将来取代现有的Web服务器，比如Apache。但是让Node和服务器分别处理不同的请求，也是一个可行的方案。Apache仍然是最流行的服务器，我们这一节就来介绍它。

问题是，我们如何能同时运行Node服务和其他像Apache这样的服务器，而不强制用户在URL中加入端口号？因为同一时间只有一个服务器可以监听默认的80端口。事实上我们从浏览器中访问API时，端口号确实会被隐藏。但是如何在避免端口冲突的情况下，同时使用Node和Apache呢？

> <img class="my_markdown" src="../images/69.png" style="zoom:50%;" />
> **其他的产品环境问题**
> 保持Node一直运行，并且从宕机中恢复，是另外一个问题，我们会在11章讲到。

```python
iptables -A input -i eth0 -p tcp --dport 2368 -j DROP
```

最简单的办法是使用Apache来_代理_Node服务的请求。这意味着所有去往Node服务的请求都会先经过Apache。

这种解决方案有好处，也有坏处。好处是它非常简单，而且我们有一个非常知名且稳定的Web服务器，它能在Node服务接收到请求之前，对请求进行一定的处理。Apache提供了一些在Node中非常难以实现的功能，比如安全性功能。而坏处在于Apache对于每一个请求都会生成一个新的线程来处理，而总线程数是有限制的。

尽管如此，很多网站还是基于Apache的，而且并不慢。除非你的要求比较高，否则Apache是一个不错的选择。

要配置Node使用Apache作为代理，你首先要打开Apache的代理功能。在命令行中执行下面的命令：

```python
a2enmod proxy
a2enmod proxy_http
```

然后，在子域名中添加代理配置。比如，在我的服务器上，我将shelleystoybox.com作为Node服务的主机名。

```python
<VirtualHost ipaddress:80>
    ServerAdmin shelleyp@burningbird.net
    ServerName shelleystoybox.com
    ErrorLog path-to-logs/error.log
    CustomLog path-to-logs/access.log combined
    ProxyRequests off
    <Location />
            ProxyPass http://ipaddress:2368/
            ProxyPassReverse http://ipaddress:2368/
    </Location>
</VirtualHost>
```

将子域名、管理员邮箱、端口和IP地址改为你的环境配置。下面要做的就是加载新的子域名了：

```python
a2ensite shelleystoybox.com
service apache2 reload
```

同样的，将子域名改为你的子域名。

