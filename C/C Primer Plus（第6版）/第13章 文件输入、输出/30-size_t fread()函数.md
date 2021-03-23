#### 13.7.6　 `size_t fread()` 函数

`size_t fread()` 函数的原型如下：

```c
size_t fread(void * restrict ptr, size_t size, size_t nmemb,FILE * restrict fp);
```

`fread()` 函数接受的参数和 `fwrite()` 函数相同。在 `fread()` 函数中， `ptr` 是待读取文件数据在内存中的地址， `fp` 指定待读取的文件。该函数用于读取被 `fwrite()` 写入文件的数据。例如，要恢复上例中保存的内含10个 `double` 类型值的数组，可以这样做：

```c
double earnings[10];
fread(earnings, sizeof (double), 10, fp);
```

该调用把 `10` 个 `double` 大小的值拷贝进 `earnings` 数组中。

`fread()` 函数返回成功读取项的数量。正常情况下，该返回值就是 `nmemb` ，但如果出现读取错误或读到文件结尾，该返回值就会比 `nmemb` 小。

