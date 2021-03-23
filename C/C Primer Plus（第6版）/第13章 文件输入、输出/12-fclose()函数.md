#### 13.2.5　 `fclose()` 函数

`fclose(fp)` 函数关闭 `fp` 指定的文件，必要时刷新缓冲区。对于较正式的程序，应该检查是否成功关闭文件。如果成功关闭， `fclose()` 函数返回 `0` ，否则返回 `EOF` ：

```c
if (fclose(fp) != 0)
     printf("Error in closing file %s\n", argv[1]);
```

如果磁盘已满、移动硬盘被移除或出现I/O错误，都会导致调用 `fclose()` 函数失败。

