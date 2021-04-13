### 1.3.3　Linux和标准

正如前面所述，Linux旨在达到兼容POSIX和SUS。SUSv4和POSIX 2008描述了Linux提供的接口，包括支持实时（POSIX.1b）和线程（POSIX.1c）。更重要的是，Linux努力与POSIX与SUS需求兼容。一般来说，如果和标准不一致，就认为是个bug。人们认为Linux与POSIX.1和SUSv3兼容，但是由于没有经过POSIX或SUS的官方认证（尤其是Linux的每次修订），所以无法官方宣布Linux兼容POSIX或SUS。

关于语言标准，Linux很幸运。gcc C编译器兼容ISO C99，而且正在努力支持C11。g++ C++编译器兼容ISO C++03，正在努力支持C++11。此外，gcc和g++_实现了C语言和C++语言的扩展。这些扩展统称为GNU C，在附录A中有相关描述。

Linux的前向兼容做得不是很好<a class="my_markdown" href="['#anchor11']"><sup class="my_markdown">[1]</sup></a>，虽然近期这方面已经好多了。接口是通过标准说明的，如标准的C库，总是可以保持源码兼容。不同版本之间的二进制代码兼容是由glibc来保证的。由于C语言是标准化的，gcc总是能够准确编译合法的C程序，尽管gcc相关的扩展可能会废弃掉甚至从新的gcc发布版本中删除。最重要的是，Linux内核保证了系统调用的稳定性。一旦系统调用是在Linux内核的稳定版本上实现的，它就不会改变了。

在各种Linux发布版中，Linux标准规范（Linux Standard Base，LSB）对大部分的Linux系统进行了标准化。LSB是几大Linux厂商在Linux基金会（前身是自由标准组织）推动下的联合项目。LSB扩展了POSIX和SUS，添加了一些自己的标准；它尝试提供二进制标准，支持目标代码在兼容系统上无需修改即可运行。大多数Linux厂商都在一定程度上遵循了LSB标准。

