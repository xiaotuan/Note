#### 16.6.5　 `#line` 和 `#error` 

`#line` 指令重置 `_ _LINE_ _` 和 `_ _FILE_ _` 宏报告的行号和文件名。可以这样使用 `#line` ：

```c
#line 1000 　　　    // 把当前行号重置为1000
#line 10 "cool.c" 　// 把行号重置为10，把文件名重置为cool.c
```

`#error` 指令让预处理器发出一条错误消息，该消息包含指令中的文本。如果可能的话，编译过程应该中断。可以这样使用 `#error` 指令：

```c
#if _ _STDC_VERSION_ _ != 201112L
#error Not C11
#endif
```

编译以上代码生成后，输出如下：

```c
$ gcc newish.c
newish.c:14:2: error: #error Not C11
$ gcc -std=c11 newish.c
$

```

如果编译器只支持旧标准，则会编译失败，如果支持C11标准，就能成功编译。

