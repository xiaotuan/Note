### 17.8　ACL API

POSIX.1e标准草案围绕着操纵ACL定义了大量函数和数据结构。鉴于其规模庞大，要描述所有函数的细节是不现实的。本节会先对此类函数的用法进行概括，再以相关编程示例作为总结。

程序要使用ACL API，就应包含<sys/acl.h>。如果还用到了POSIX.1e标准草案中的各种Linux扩展（acl(5)手册页罗列了一系列Linux扩展），程序可能还需要包含<acl/libacl.h>。为与libacl库链接，编译此类程序时需带有-lacl选项。

> 如前所述，在Linux上，ACL是以扩展属性的方式来实现的，而将ACL API实现为一套操纵用户空间数据结构的库函数，并且会在必要时调用getxattr()和setxattr()，来获取和修改持有ACL的持久层system扩展属性。此外，应用程序直接调用getxattr()和setxattr()去操纵ACL也是可行的，尽管并不推荐这一做法。

