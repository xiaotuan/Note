### 19.3　inotify事件

使用inotify_add_watch()删除或修改监控项时，位掩码参数mask标识了针对给定路径名（pathname）而要监控的事件。表19-1的“in”列列出了可在mask中定义的事件位。

<center class="my_markdown"><b class="my_markdown">表19-1：inotify事件</b></center>

| 位　　值 | In | Out | 描　　述 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| IN_ACCESS | ● | ● | 文件被访问（read()） |
| IN_ATTRIB | ● | ● | 文件元数据改变 |
| IN_CLOSE_WRITE | ● | ● | 关闭为了写入而打开的文件 |
| IN_CLOSE_NOWRITE | ● | ● | 关闭以只读方式打开的文件 |
| IN_CREATE | ● | ● | 在受监控目录内创建了文件/目录 |
| IN_DELETE | ● | ● | 在受监控目录内删除文件/目录 |
| IN_DELETE_SELF | ● | ● | 删除受监控目录/文件本身 |
| IN_MODIFY | ● | ● | 文件被修改 |
| IN_MOVE_SELF | ● | ● | 移动受监控目录/文件本身 |
| IN_MOVED_FROM | ● | ● | 文件移出到受监控目录之外 |
| IN_MOVED_TO | ● | ● | 将文件移入受监控目录 |
| IN_OPEN | ● | ● | 文件被打开 |
| IN_ALL_EVENTS | ● |  | 以上所有输出事件的统称 |
| IN_MOVE | ● |  | IN_MOVED_FROM │ IN_MOVED_TO事件的统称 |
| IN_CLOSE | ● |  | IN_CLOSE_WRITE │ IN_CLOSE_NOWRITE事件的统称 |
| IN_DONT_FOLLOW | ● |  | 不对符号链接解引用（始于Linux 2.6.15） |
| IN_MASK_ADD | ● |  | 将事件追加到pathname的当前监控掩码 |
| IN_ONESHOT | ● |  | 只监控pathname的一个事件 |
| IN_ONLYDIR | ● |  | pathname不为目录时会失败（始于Linux 2.6.15） |
| IN_IGNORED |  | ● | 监控项为内核或应用程序所移除 |
| IN_ISDIR |  | ● | name中所返回的文件名为路径 |
| IN_Q_OVERFLOW |  | ● | 事件队列溢出 |
| IN_UNMOUNT |  | ● | 包含对象的文件系统遭卸载 |

对于表19-1所列出的绝大多数位而言，顾名便可知义。以下是对一些细节的澄清。

+ 当文件的元数据（比如，权限、所有权、链接计数、扩展属性、用户ID或组ID等）改变时，会发生IN_ATTRIB事件。
+ 删除受监控对象（即，一个文件或目录）时，发生IN_DELETE_SELF事件。当受监控对象是一个目录，并且该目录所含文件之一遭删除时，发生IN_DELETE事件。
+ 重命名受监控对象时，发生IN_MOVE_SELF事件。重命名受监控目录内的对象时，发生IN_MOVED_FROM和IN_MOVED_TO事件。其中，前一事件针对包含旧对象名的目录，后一事件则针对包含新对象名的目录。
+ IN_DONT_FOLLOW、IN_MASK_ADD、IN_ONESHOT和IN_ONLYDIR位并非对监控事件的定义，而是意在控制inotify_add_watch()系统调用的行为。
+ IN_DONT_FOLLOW则规定，若pathname为符号链接，则不对其解引用。其作用在于令应用程序可以监控符号链接，而非符号连接所指代的文件。
+ 倘若对已为同一inotify描述符所监控的同一路径名再次执行inotify_add_watch()调用，那么默认情况下会用给定的mask掩码来替换该监控项的当前掩码。如果指定了IN_MASK_ADD，那么则会将mask值与当前掩码相或。
+ IN_ONESHOT允许应用只监控pathname的一个事件。事件发生后，监控项会自动从监控列表中消失。
+ 只有当pathname为目录时，IN_ONLYDIR才允许应用程序对其进行监控。如果pathname并非目录，那么调用inotify_add_watch()失败，报错为ENOTDIR。如要确保监控对象为一目录，则使用该标志可以规避竞争条件的发生。

