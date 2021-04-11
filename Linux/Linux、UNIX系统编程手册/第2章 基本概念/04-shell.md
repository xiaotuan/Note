### 2.2　shell

shell是一种具有特殊用途的程序，主要用于读取用户输入的命令，并执行相应的程序以响应命令。有时，人们也称之为命令解释器。

术语登录shell（login shell）是指用户刚登录系统时，由系统创建，用以运行shell的进程。尽管某些操作系统将命令解释器集成于内核中，而对 UNIX 系统而言，shell 只是一个用户进程。shell的种类繁多，登入同一台计算机的不同用户同时可使用不同的shell（就单个用户来说，情况也一样）。纵观UNIX历史，出现过以下几种重要的shell。

+ Bourne shell（sh）：这款由Steve Bourne编写的shell历史最为悠久，且应用广泛，曾是第七版UNIX的标配shell。Bourne shell包含了在其他shell中常见的许多特性，I/O重定向、管道、文件名生成（通配符）、变量、环境变量处理、命令替换、后台命令执行以及函数。对于所有问世于第七版UNIX之后的实现而言，除了可能提供有其他shell之外，都附带了Bourne shell。
+ C shell（csh）：由Bill Joy于加州大学伯克利分校编写而成。其命名则源于该脚本语言的流控制语法与C语言有着许多相似之处。C shell当时提供了若干极为实用的交互式特性，并不为Bourne shell所支持，这其中包括命令的历史记录、命令行编辑功能、任务控制和别名等。C shell与Bourne shell并不兼容。尽管C shell曾是BSD系统标配的交互式shell，但一般情况下，人们还是喜欢针对Bourne shell编写shell脚本（稍后介绍），以便其能够在所有UNIX实现上移植。
+ Korn shell（ksh）：AT&T贝尔实验室的David Korn编写了这款shell，作为Bourne shell的“继任者”。在保持与Bourne shell兼容的同时，Korn shell还吸收了那些与C shell相类似的交互式特性。
+ Bourne again shell（bash）：这款shell是GNU项目对Bourne shell的重新实现。Bash提供了与C shell和Korn shel所类似的交互式特性。Brian Fox 和Chet Ramey是bash的主要作者。bash或许是Linux上应用最为广泛的shell了。在Linux上，Bourne shell（sh）其实正是由bash仿真提供的。

> POSIX.2-1992基于当时的Korn shell版本定义了一个shell标准。如今，Korn shell和bash都符合POSIX规范，但两者都提供了大量对标准的扩展，其扩展之间存在许多差异。

设计shell的目的不仅仅是用于人机交互，对shell脚本（包含shell命令的文本文件）进行解释也是其用途之一。为实现这一目的，每款shell都内置有许多通常与编程语言相关的功能，其中包括变量、循环和条件语句、I/O命令以及函数等。

尽管在语法方面有所差异，每款shell执行的任务都大致相同。除非指明是某款特定shell的操作，否则书中的“shell”都会按所描述的方式运作。本书绝大多数需要用到shell的示例都会使用bash，若无其他说明，读者可假定这些示例也能以相同方式在其他类Bourne的shell上运行。

