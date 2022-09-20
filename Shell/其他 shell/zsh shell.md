[toc]

zsh shell 是由 Paul Falstad 开发的一个开源 Unix shell。它汲取了所有现有 shell 的设计理念并增加了许多独到的功能，为程序员创建了一个无所不能的高级 shell。

下面是 zsh shell 的一些独特的功能：

+ 改进的 shell 选项处理
+ shell 兼容性模式
+ 可加载模块

### 1. shell 选项

zsh shell 使用了一些命令行参数来定义 shell 的操作，但大多数情况下它用**选项**来定制 shell 的行为。

<center><b>zsh shell 命令行参数</b></center>

| 参数 | 描述                                            |
| ---- | ----------------------------------------------- |
| -c   | 只执行指定的命令，然后退出                      |
| -i   | 作为交互式 shell 启动，提供一个命令行交互提示符 |
| -s   | 强制 shell 从 STDIN 读取命令                    |
| -o   | 指定命令行选项                                  |

zsh shell 是所有 shell 中可定制性最强的。不同的选项可以分成以下几大类：

+ 更改目录：该选项用于控制 `cd` 命令和 `dirs` 命令如何处理目录更改。	
+ 补全：该选项用于控制命令补全功能。
+ 扩展和扩展匹配：该选项用于控制命令中文件扩展。
+ 历史记录：该选项用于控制命令历史记录。
+ 初始化：该选项用于控制 shell 在启动时如何处理和启动文件。
+ 输入输出：该选项用于控制命令处理。
+ 作业控制：该选项用于控制 shell 如何处理作业和启动作业。
+ 提示：该选项用于控制 shell 如何处理命令行提示符。
+ 脚本和函数：该选项用于控制 shell 如何处理 shell 脚本和定义函数。
+ shell 仿真：该选项允许设置 zsh shell 来模拟其他类型 shell 行为。
+ shell 状态：该选项用于定义启动那种 shell 的选项。
+ zle：该选项用于控制 zsh 行编辑器功能。
+ 选项别名：可以用作其他选项别名的特殊选项。

### 2. 内建命令

#### 2.1 核心内建命令

| 命令       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| alias      | 为命令和参数定义一个替代性名称                               |
| autoload   | 将 shell 函数预加载到内存中以便快速访问                      |
| bg         | 以后台模式执行一个作业                                       |
| bindkey    | 将组合键和命令绑定到一起                                     |
| builtin    | 执行指定的内建命令而不是同样名称的可执行文件                 |
| bye        | 跟 exit 相同                                                 |
| cd         | 切换当前工作目录                                             |
| chdir      | 切换当前工作目录                                             |
| command    | 将指定命令当做外部文件执行而不是函数或内建命令               |
| declare    | 设置变量的数据类型（同 typeset）                             |
| dirs       | 显示目录栈的内容                                             |
| disable    | 临时禁用指定的散列表元素                                     |
| disown     | 从作业表中移除指定的作业                                     |
| echo       | 显示变量和文本                                               |
| emulate    | 用 zsh 来模拟另一个 shell，比如 Bourne、Korn 或 C shell      |
| enable     | 使能指定的散列表元素                                         |
| eval       | 在当前 shell 进程中执行指定的命令和参数                      |
| exec       | 执行指定的命令和参数来替换当前 shell 进程                    |
| exit       | 退出 shell 并返回指定的退出状态码。如果没有指定，使用最后一条命令的退出状态码 |
| export     | 允许在子 shell 进程中使用指定的环境变量名及其值              |
| false      | 返回退出状态码 1                                             |
| fc         | 从历史记录中选择某范围内的命令                               |
| fg         | 以前台模式执行指定的作业                                     |
| float      | 将指定变量设为保存浮点值的变量                               |
| functions  | 将指定名称设为函数                                           |
| getln      | 从缓冲栈中读取下一个值并将其放到指定变量中                   |
| hash       | 直接修改命令哈希表的内容                                     |
| history    | 列出历史记录文件中的命令                                     |
| integer    | 将指定变量设为整数类型                                       |
| jobs       | 列出指定作业的信息，或分配给 shell 进程的所有作业            |
| kill       | 向指定进程或作业发送信号（默认为 SIGTERM）                   |
| let        | 执行算术运算并将结果赋给一个变量                             |
| limit      | 设置或显示资源限制                                           |
| local      | 为指定变量设置数据属性                                       |
| log        | 显示受 watch 参数影响的当前登录到系统上的所有用户            |
| logout     | 同 exit，但只在 shell 是登录 shell 时有效                    |
| popd       | 从目录栈中删除下一项                                         |
| print      | 显示变量和文本                                               |
| printf     | 用 C 风格的格式字符串来显示变量和文本                        |
| pushd      | 改变当前工作目录，并将上一个目录放到目录栈中                 |
| pushln     | 将指定参数放到编辑缓冲栈中                                   |
| pwd        | 显示当前工作目录的完整路径名                                 |
| read       | 读取一行，并用 IFS 变量将数据字段赋给指定变量                |
| readonly   | 将值赋给不能修改的变量                                       |
| rehash     | 重建命令散列表                                               |
| set        | 为 shell 设置选项或位置参数                                  |
| setopt     | 为 shell 设置选项                                            |
| shift      | 读取并删除第一个位置参数，然后将剩余的参数向前移动一个位置   |
| source     | 找到指定文件并将其内容复制到当前位置                         |
| suspend    | 挂起 shell 的执行，直到它收到 SIGCONT 信号                   |
| test       | 如果指定条件为 TRUE 的话，返回退出状态码 0                   |
| times      | 显示当前 shell 以及 shell 中所有运行进程的累计用户时间和统计时间 |
| trap       | 阻断指定信号从而让 shell 无法处理，如果收到信号执行指定命令  |
| true       | 返回退出状态码 0                                             |
| ttyctl     | 锁定和解锁显示                                               |
| type       | 显示 shell 会如何解释指定的命令                              |
| typeset    | 设置或显示变量的特性                                         |
| ulimit     | 设置或显示 shell 或 shell 中运行进程的资源限制               |
| umask      | 设置或显示创建文件和目录的默认权限                           |
| unalias    | 删除指定的命令别名                                           |
| unfunction | 删除指定的已定义函数                                         |
| unhash     | 删除散列表中的指定命令                                       |
| unlimit    | 取消指定的资源限制                                           |
| unset      | 删除指定的变量特性                                           |
| unsetopt   | 删除指定的 shell 选项                                        |
| wait       | 等待指定的作业或进程完成                                     |
| whence     | 显示指定命令会如何被 shell 解释                              |
| where      | 如果 shell 找到的话，显示指定命令的路径名                    |
| which      | 用 csh 风格的输出显示指定命令的路径名                        |
| zcompile   | 编辑指定的函数或脚本，加速自动加载                           |
| zmodload   | 对可加载 zsh 模块执行特定操作                                |

#### 2.2 附加模块

| 模块           | 描述                                   |
| -------------- | -------------------------------------- |
| zsh/datetime   | 额外的日期和时间命令及变量             |
| zsh/files      | 基本的文件处理命令                     |
| zsh/mapfile    | 通过关联数组来访问外部文件             |
| zsh/mathfunc   | 额外的科学函数                         |
| zsh/pcre       | 扩展的正则表达式库                     |
| zsh/net/socket | Unix 域套接字支持                      |
| zsh/stat       | 访问 stat 系统调用来提供系统的统计状况 |
| zsh/system     | 访问各种底层系统功能的接口             |
| zsh/net/tcp    | 访问 TCP 套接字                        |
| zsh/zftp       | 专用 FTP 客户端命令                    |
| zsh/zselect    | 阻塞，直到文件描述符就绪才返回         |
| zsh/zutil      | 各种 shell 实用工具                    |

#### 2.3 查看、添加和删除模块

`zmodload` 命令不加任何参数会显示 zsh shell 中当前已安装的模块。

```shell
% zmodload
zsh/zutil
zsh/complete
zsh/main
zsh/terminfo
zsh/zle
zsh/parameter
%
```

要添加新模块，只需在 `zmodload` 命令行上指定模块名称就行了。

```shell
% zmodload zsh/zftp
%
```

要删除已安装的模块，用 `-u` 参数和模块名。

```shell
% zmodload -u zsh/zftp
```

> 提示：通常习惯将 `zmodload` 命令放进 `$HOME/.zshrc` 启动文件中，这样在 zsh 启动时常用的函数就会自动加载。

### 3. zsh 脚本编程

#### 3.1 数学运算

##### 3.1.1 执行计算

zsh shell 提供了执行数学运算的两种方法：

+ let 命令
+ 双圆括号

在使用 `let` 命令时，你应该在算式前后加上双引号，这样才能使用空格：

```shell
% let value1=" 4 * 5.1 / 3.2 "
% echo $value1
6.3750000000
```

> 注意：使用浮点数会带来精度问题。为了解决这个问题，通常要使用 `printf` 命令，并指定能正确显示结果所需的小数点精度。
>
> ```shell
> % printf "%6.3f\n" $value1
> 6.375
> ```

第二种方法是使用双圆括号。

```shell
% value1=$(( 4 * 5.1 ))
% (( value2 = 4 * 5.1 ))
% printf "%6.3f\n" $value1 $value2
20.400
20.400
```

##### 3.1.2 数学函数

在 zsh shell 中，内建数学函数可多可少。默认的 zsh 并不含有任何特殊的数学函数。但如果安装了 zsh/mathfunc 模块，你就会拥有远远超出你可能需要的数学函数：

```shell
% value1=$(( sqrt(9) ))
zsh: unknown function: sqrt
% zmodload zsh/mathfunc
% value1=$(( sqrt(9) ))
% echo $value1
3.
```

#### 3.2 结构化命令

zsh shell 为 shell 脚本提供了常用的结构化命令：

+ `if-then-else` 语句
+ `for` 循环（包括 C 语言风格的）
+ `while` 循环
+ `untile` 循环
+ `select` 语句
+ `case` 语句

zsh shell 还包含了另外一个叫作 `repeat` 的结构化命令。`repeat` 命令使用如下格式。

```shell
repeat param
do
	commands
done
```

param 参数必须是一个数字或能算出一个数值的数学算式。`repeat` 命令就会执行指定的命令那么多次：

```shell
% cat test.sh
#!/bin/zsh
# using the repeat command

value1=$(( 10 / 2 ))
repeat $value1
do 
    echo "This is a test"
done
% ./test.sh
This is a test
This is a test
This is a test
This is a test
This is a test
```

#### 3.3 函数

zsh shell 支持使用 `function` 命令或通过圆括号定义函数名的方式来创建自定义函数。

```shell
% function functest1 {
> echo "This is the test1 function"
> }
% functest2() {
> echo "This is the test2 function"
> }
% functest1
This is the test1 function
% functest2
This is the test2 function
```

