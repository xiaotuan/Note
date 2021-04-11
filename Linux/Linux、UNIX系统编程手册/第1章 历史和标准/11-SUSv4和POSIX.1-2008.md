### 1.3.5　SUSv4和POSIX.1-2008

2008年，奥斯丁工作组完成了对已合并的POSIX和SUS规范的修订工作。较之于之先前版本，该标准包含了基本规范以及XSI扩展。人们将这一修订版本称为SUSv4。

与SUSv3的变化相比，SUSv4的变化范围不算太大。最显著的变化如下所示。

+ SUSv4为一系列函数添加了新规范。本书将会介绍以下新标准中定义的如下函数：dirfd()、fdopendir()、fexecve()、futimens()、mkdtemp()、psignal()、strsignal()以及utimensat()。另一组与文件相关的函数，例如：openat()，参见18.11节，和现有函数，例如：open()，功能相同，其区别在于前者对相对路径的解释是相对于打开文件描述符的所属目录而言，而非相对于进程的当前工作目录。
+ 某些在SUSv3中被定义为可选的函数在SUSv4中成为基本标准的必备部分。例如，某些原本在SUSv3中属于XSI扩展的函数，在SUSv4中转而隶属于基本标准。在SUSv4中转变为必备的函数中包括了dlopen API（42.1节）、实时信号API（22.8节）、POSIX信号量API（53章）以及POSIX定时器API（23.6节）。
+ SUSv4废止了SUSv3中的某些函数，这包括asctime()、ctime()、ftw()、gettimeofday()、getitimer()、setitimer()以及siginterrupt()。
+ SUSv4删除了在SUSv3中被标记为作废的一些函数，这包括 gethostbyname()、 gethostbyaddr()以及vfork()。
+ SUSv4对SUSv3现有规范的各方面细节进行了修改。例如，对于应满足异步信号安全（async-signal-safe）的函数列表，二者内容就有所不同（见表21-1）。

本书后文会就所论及的相关主题指出其在SUSv4中的变化。

