[toc]

下面以如下代码为例：

**inform.c**

```c
int main(void)
{
    printf("A .c is used to end a C program filename.\n");
    return 0;
}
```



### 1. UNIX 系统

```shell
cc inform.c
```

编译成功后会生成一个 `a.out` 的文件。可以通过如下命令运行该程序：

```shell
$ ./a.out
```

### 2. Linux 系统

```shell
gcc inform.c
```

编译成功后会生成一个 `a.out` 的文件。可以通过如下命令运行该程序：

```shell
$ ./a.out
```

也可以使用 `cc` 作为 `gcc` 的别名，例如：

```shell
cc inform.c
```

