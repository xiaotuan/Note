`gcc` 和 `clang` 命令都可以根据不同的版本选择运行时选项来调用不同 C 标准，例如：

```shell
gcc -std=c99 inform.c
gcc -std=c1x inform.c
gcc -std=c11 inform.c
```

