### 对选定SUSv3限制的总结

表11-1列举了与本书有关，由SUSv3所定义的部分限制（其他限制将在后续章节中加以介绍）。

<center class="my_markdown"><b class="my_markdown">表11-1：选定的SUSv3限制</b></center>

| 限制名称 (<limits.h>) | 最小值 | 在sysconf() / pathconf() 中的参数命名(<unistd.h>) | 描　　述 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| ARG_MAX | 4096 | _SC_ARG_MAX | 提供给 exec()的参数(argv)与环境变量(environ)所占存储空间之和的最大字节数（见6.7节和27.2.3节） |
| none | none | _SC_CLK_TCK | 为times()提供的度量单位 |
| LOGIN_NAME_MAX | 9 | _SC_LOGIN_NAME_MAX | 登录名的最大长度（含终止空字符） |
| OPEN_MAX | 20 | _SC_OPEN_MAX | 进程同时可打开的文件描述符的最大数量，比可用文件描述符的最大数量多1个（见36.2节） |
| NGROUPS_MAX | 8 | _SC_NGROUPS_MAX | 进程所属辅助组ID数量的最大值（见9.7.3节） |
| none | 1 | _SC_PAGESIZE | 一个虚拟内存页的大小 （_SC_PAGE_SIZE与其同义） |
| RTSIG_MAX | 8 | _SC_RTSIG_MAX | 单一实时信号的最大数量（见22.8节） |
| SIGQUEUE_MAX | 32 | _SC_SIGQUEUE_MAX | 排队实时信号的最大数量（见22.8节） |
| STREAM_MAX | 8 | _SC_STREAM_MAX | 同时可打开的stdio流的最大数量 |
| NAME_MAX | 14 | _PC_NAME_MAX | 排除终止空字符外，文件名称可达的最大字节长度 |
| PATH_MAX | 256 | _PC_PATH_MAX | 路径名称可达的最大字节长度，含尾部空字符 |
| PIPE_BUF | 512 | _PC_PIPE_BUF | 一次性（原子操作）写入管道或FIFO中的最大字节数（44.1节） |

表11-1中的第一列给出了限制的名称，可将其作为常量定义于<limits.h>文件中，用于表示特定实现下的限制。第二列是SUSv3为这些限制所定义的最小值（也定义于<limits.h>文件中）。在大多数情况下，会将每个限制的最小值定义为冠以字符串_POSIX_的常量。例如，常量_POSIX_RTSIG_MAX（其值为8）为SUSv3实现对相应RTSIG_MAX常量的最低要求。第三列列出了为在运行期间获取实现的限制，调用sysconf()或pathconf()时应输入入参的常量名。冠以_SC_的常量用于 sysconf()，冠以_PC_的常量用于pathconf()和fpathconf()。

下列为对表11-1的补充信息，请予关注。

+ getdtablesize()函数是确定进程文件描述符（OPEN_MAX）限制的备选方法，已遭弃用，该函数曾一度为SUSv2所定义（标记为LEGACY），但SUSv3将其剔除。
+ getpagesize()函数是确定系统页大小（_SC_PAGESIZE）的备选方法，已然废弃。该函数一度曾为SUSv2所定义（标记为 LEGACY），但SUSv3将其剔除。
+ 定义于<stdio.h>文件中的常量FOPEN_MAX，等同于常量STREAM_MAX。
+ NAME_MAX不包含终止空字符，而PATH_MAX则包括。POSIX.1标准在定义PATH_MAX时，对于是否包含终止空字符始终含糊不清，而上述差异则恰好弥补了这一缺陷。定义 PATH_MAX 中包含终止符也意味着，为路径名称分配了PATH_MAX个字节的应用程序依然符合标准。

