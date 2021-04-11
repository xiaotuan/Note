### 59.10.3　错误诊断：gai_strerror()

getaddrinfo()在发生错误时会返回表59-1中给出的一个非零错误码。

<center class="my_markdown"><b class="my_markdown">表59-1 getaddrinfo()和getnameinfo()返回的错误码</b></center>

| 错 误 常 量 | 描 述 |
| :-----  | :-----  | :-----  | :-----  |
| EAI_ADDRFAMILY | 在hints.ai_family中不存在host的地址（没有在SUSv3中规定，但大多数实现都对其进行了定义，仅供getaddrinfo()使用） |
| EAI_AGAIN | 名字解析过程中发生临时错误（稍后重试） |
| EAI_BADFLAGS | 在hints.ai_flags中指定了一个无效的标记 |
| EAI_FAIL | 访问名字服务器时发生了无法恢复的故障 |
| EAI_FAMILY | 不支持在hints.ai_family中指定的地址族 |
| EAI_MEMORY | 内存分配故障 |
| EAI_NODATA | 没有与host关联的地址（没有在SUSv3中规定，但大多数实现都对其进行了定义，仅供getaddrinfo()使用） |
| EAI_NONAME | 未知的host或service，或host和service都为NULL，或指定了AI_NUMERICSERV同时service没有指向一个数值字符串 |
| EAI_OVERFLOW | 参数缓冲器溢出 |
| EAI_SERVICE | hints.ai_socktype不支持指定的service（仅供getaddrinfo()使用） |
| EAI_SOCKTYPE | 不支持指定的hints.ai_socktype（仅供getaddrinfo()使用） |
| EAI_SYSTEM | 通过errno返回的系统错误 |

给定表59-1中列出的一个错误码，gai_strerror()函数会返回一个描述该错误的字符串。（该字符串通常比表59-1中给出的描述更加简洁。）



![1505.png](../images/1505.png)
gai_strerror()返回的字符串可以作为应用程序显示的错误消息的一部分。

