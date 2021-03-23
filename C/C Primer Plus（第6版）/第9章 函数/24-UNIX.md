#### 9.4.1　UNIX

假定在UNIX系统中安装了UNIX C编译器 `cc` （最初的 `cc` 已经停用，但是许多UNIX系统都给 `cc` 命令起了一个别名用作其他编译器命令，典型的是 `gcc` 或 `clang` ）。假设 `file1.c` 和 `file2.c` 是两个内含C函数的文件，下面的命令将编译两个文件并生成一个名为 `a.out` 的可执行文件：

```c
cc file1.c file2.c
```

另外，还生成两个名为 `file1.o` 和 `file2.o` 的目标文件。如果后来改动了 `file1.c` ，而 `file2.c` 不变，可以使用以下命令编译第1个文件，并与第2个文件的目标代码合并：

```c
cc file1.c file2.o
```

UNIX系统的 `make` 命令可自动管理多文件程序，但是这超出了本书的讨论范围。

注意，OS X的Terminal工具可以打开UNIX命令行环境，但是必须先下载命令行编译器（GCC和Clang）。

