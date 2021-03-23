#### 9.4.2　Linux

假定Linux系统安装了GNU C编译器GCC。假设 `file1.c` 和 `file2.c` 是两个内含C函数的文件，下面的命令将编译两个文件并生成名为 `a.out` 的可执行文件：

```c
gcc file1.c file2.c
```

另外，还生成两个名为 `file1.o` 和 `file2.o` 的目标文件。如果后来改动了 `file1.c` ，而 `file2.c` 不变，可以使用以下命令编译第1个文件，并与第2个文件的目标代码合并：

```c
gcc file1.c file2.o
```

