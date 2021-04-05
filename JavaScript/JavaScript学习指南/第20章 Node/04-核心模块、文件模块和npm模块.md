### 20.3　核心模块、文件模块和npm模块

模块分为三大类，核心模块（core modules）、文件模块（file modules）和npm模块。（npm modules）核心模块的模块名都是Node的保留字，比如，fs和os（本章后面会详细介绍）。前面已经见过文件模块了：把创建好的文件赋给module.exports，然后再引用该文件。npm模块只是一些放在一个名为node_modules的特殊目录下的文件模块。在使用require函数时，Node会根据传入的字符串来决定模块的类型（如表20-1）。

<center class="my_markdown"><b class="my_markdown">表20-1　　模块类型</b></center>

| 类　　型 | 传到require的字符串 | 例　　子 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 核心模块 | 不以 /, ./ 或 ../ 开始 | require('fs') | require('os') | require('http') | require('child_process') |
| 文件模块 | 以 /, ./ 或 ../ 开始 | require('./debug.js') require('/full/path/to/module.js') require('../a.js') require('../../a.js') |
| npm模块 | 不是一个核心module，也不以/,./或../开始 | require('debug') require('express') require('chalk') require('koa') require('q') |

有一些像process和buffer这样的全局（global）核心模块，在Node程序中始终都是可用的，不用再显式声明require语句。表20-2中列出了所有的全局模块。

<center class="my_markdown"><b class="my_markdown">表20-2　　全局模块</b></center>

| 模　　块 | 是否全局 | 描　　述 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| assert | No | 用于测试目的 |
| buffer | Yes | 用于操作输入/输出（IO）（主要是文件和网络） |
| child_process | No | 运行外部程序（Node或者其他）的函数 |
| cluster | No | 允许利用多进程所带来的性能 |
| crypto | No | 內建的密码库 |
| dns | No | 针对网络名字解析的域名系统（DNS）函数 |
| domain | No | 允许对I/O和其他异步操作进行分组来隔离错误 |
| events | No | 支持异步事件的实用工具 |
| fs | No | 操作文件系统 |
| http | No | HTTP server和相关工具 |
| https | No | HTTPS server和相关工具 |
| net | No | 基于socket的异步网络API |
| os | No | 操作系统工具 |
| path | No | 文件系统路径名工具 |
| punycode | No | 使用ASCII码的子集对Unicode进行编码 |
| querystring | No | 解析和构建URL的查询字符串 |
| readline | No | I/O交互功能，主要用于命令行编程 |
| smalloc | No | 允许显式分配缓存 |
| stream | Yes | 基于流的数据传递 |
| string_decoder | No | 将缓存转换成字符串 |
| tls | No | 传输层安全（Transport Layer Security - TLS）通信工具 |
| tty | No | 低端电传打字机（Low-level TeleTYpewriter -TTY）工具 |
| dgram | No | 用户数据协议（User Datagram Protocol -UDP）网络工具 |
| url | Yes | URL解析 工具 |
| util | No | Node内部实用工具 |
| vm | No | （JavaScript）虚拟机：能够在其中进行元编程并创建上下文 |
| zlib | No | 压缩工具 |

讨论Node中的所有模块已经超出了本书的范围（本章只会讨论那些最重要的模块），但是有了这个列表，就可以查找到更多的信息。关于这些module的细节可以参考Node API文档。

最后，还有npm模块。npm模块是一些有特殊命名规范的文件模块。如果需要模块x（x不是核心模块），Node会在当前目录下找一个叫作node_modules的子目录。如果找到了，就在那个目录下找x。如果没找到，Node就会继续在它的上层目录找node_modules，然后一直重复这个过程，直到找到模块或者到达根目录。比如，如果项目目录是/home/jdoe/test_project，在应用文件中，调用了require(‘x’)，Node会依次在以下这些目录中查找模块x（按照先后顺序）：

+ /home/jdoe/test_project/node_modules/x。
+ /home/jdoe/node_modules/x。
+ /home/node_modules/x。
+ /node_modules/x。

大多数项目中都只有一个node_modules目录，它一般在项目的根目录下。更进一步说，不应该在这个目录中手动添加或删除任何内容，而应该让npm完成这些繁重的任务。不过，了解如何在Node中解析并引入模块仍然很有用，尤其是需要在第三方模块中debug的时候。

对于那些自己编写的模块，不要把它们放进node_modules中。虽然这样也行，但是node_modules的作用就在于，这个目录可以由npm根据package.json中的dependency列表随时删除和重建（见第2章）。

当然也可以发布自己的npm模块，并用npm来管理它，但还是要避免直接修改node_modules目录下的内容。

