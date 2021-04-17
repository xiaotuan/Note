### 22.2.2　Socket类

.NET框架的System.NET.Sockets命名空间为需要严密控制网络访问的开发人员提供了Windows Sockets (Winsock)接口的托管实现。System.Net.Sockets命名空间中的Socket类用于实现Berkeley套接字接口。System.Net命名空间中的所有其他网络访问类都建立在该套接字Socket 实现之上，如TCPClient、TCPListener 和UDPClient类封装有关创建到Internet的TCP和UDP连接的详细信息；NetworkStream 类则提供用于网络访问的基础数据流等，常见的许多Internet服务都可以见到 Socket 的踪影，如Telnet、Http、Email、Echo这些服务尽管通信协议Protocol 的定义不同，但是其基础的传输都是采用的 Socket。

Socket实际上就是网络进程通信中所要使用的一些缓冲区及相应的数据结构。Socket类的构造函数原型如下。

```c
public Socket(
AddressFamily addressFamily,
SocketType socketType,
ProtocolType protocolType
);
```

Socket类的构造函数使用3个参数来定义创建的Socket实例，一个Socket实例包含了一个本地或者一个远程端点的套接字信息。AddressFamily用来指定网络类型；SocketType用来指定套接字类型（即数据连接方式）；ProtocolType用来指定网络协议。3个参数均是在命名空间System.Net.Sockets中定义的枚举类型。但它们并不能任意组合，不当的组合反而会导致无效套接字。如对于常规的IP通信网络，AddressFamily只能使用AddressFamily.InterNetwork，此时可用的SocketType、ProtocolType组合如下表所示。

| SocketType值 | ProtocolType值 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| Stream | Tcp | 面向连接套接字 |
| Dgram | Udp | 无连接套接字 |
| Raw | Icmp | 网际消息控制协议套接字 |
| Raw | Raw | 基础传输协议套接字 |

下面的示例语句创建一个Socket，它可用于在基于TCP/IP的网络（如 Internet）上通信。

```c
Socket s = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
```

若要使用UDP而不是TCP网络协议通信，需要更改协议类型，如下面的示例所示。

```c
Socket s = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
```

套接字被创建后，我们就可以利用Socket类提供的一些属性方便地设置或检索信息。Socket类的常用属性成员如下表所示。

| 属性名称 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| AddressFamily | 获取套接字的Address family |
| Available | 从网络中获取准备读取的数据数量 |
| Blocking | 获取或设置表示套接字是否处于阻塞模式 |
| Connected | 获取一个值，该值表明套接字是否与最后完成发送或接收操作的远程设备得到连接 |
| LocalEndPoint | 获取套接字的本地EndPoint对象 |
| ProtocolType | 获取套接字的协议类型 |
| RemoteEndPoint | 获取套接字的远程EndPoint对象 |
| SocketType | 获取套接字的类型 |

Socket类的常用方法成员如下表所示。

| 方法名称 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| Bind(EndPoint) | 服务器端套接字需要绑定到特定的终端 |
| Listen(int) | 监听端口，方法参数表示最大监听数 |
| Accept | 接收客户端连接，并返回一个新的连接 |
| Send | 发送数据 |
| Receive | 接收数据 |
| Connect(EndPoint) | 连接远程服务器 |
| ShutDown(SocketShutDown) | 禁用套接字，其中SocketShutDown为枚举类型，可以取值为Send，Receive，Both |
| SocketType | 获取套接字的类型 |
| Close | 获取套接字的类型 |
| BeginAccept(AsynscCallBack,object) | 开始一个异步操作，接受一个连接尝试 |
| BeginConnect(EndPoint,AsyncCallBack, Object) | 回调方法中必须使用EndConnect()方法。Object中存储了连接的详细信息 |
| BeginSend(byte[], SocketFlag,AsyncCallBack, Object) | 异步发送数据 |
| BeginReceive(byte[], SocketFlag, AsyncCallBack, Object) | 异步接收数据 |

Socket类的常用方法成员Send()是重载方法，Send()方法的四种重载方式如下表所示。

| Send()方法声明 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| Send(byte[]) | 简单发送数据 |
| Send(byte[],SocketFlag) | 使用指定的SocketFlag发送数据 |
| Send(byte[], int, SocketFlag) | 使用指定的SocketFlag发送指定长度数据 |
| Send(byte[], int, int, SocketFlag) | 使用指定的SocketFlag，将指定字节数的数据发送到已连接的socket(从指定偏移量开始) |

Socket类的常用方法成员Receive() 是重载方法，Receive() 方法的四种重载方式如下表所示。

| Receive()方法声明 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| Receive(byte[]) | 简单接收数据 |
| Receive(byte[],SocketFlag) | 使用指定的SocketFlag接收数据 |
| Receive(byte[], int, SocketFlag) | 使用指定的SocketFlag接收指定长度数据 |
| Receive(byte[], int, int, SocketFlag) | 使用指定的SocketFlag，从绑定的套接字接收指定字节数的数据，并存到指定偏移量位置的缓冲区 |

Socket类的常用方法成员Send()和Receive()中的SocketFlag枚举类型参数指定套接字的发送和接收行为，SocketFlag枚举类型的具体取值如下表所示。

| SocketFlag枚举值 | 说明 |
| :-----  | :-----  | :-----  | :-----  |
| DontRoute | 不用内部路由表发送数据 |
| MaxIOVectorLength | 给用于发送和接收数据的WSABUF结构数提供一个标准值 |
| None | 对这次调用不使用标志 |
| OutOfBind | 处理带外的数据。带外的数据指连接双方中的一方发生重要事情，想要迅速地通知对方 |
| Partial | 部分地发送或接收信息 |
| Peek | 查看传入的消息 |

