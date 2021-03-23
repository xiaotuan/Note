#### 13.7.5　 `size_t fwrite()` 函数

`fwrite()` 函数的原型如下：

```c
size_t fwrite(const void * restrict ptr, size_t size, size_t nmemb,FILE * restrict fp);
```

`fwrite()` 函数把二进制数据写入文件。 `size_t` 是根据标准C类型定义的类型，它是 `sizeof` 运算符返回的类型，通常是 `unsigned int` ，但是实现可以选择使用其他类型。指针 `ptr` 是待写入数据块的地址。 `size` 表示待写入数据块的大小（以字节为单位）， `nmemb` 表示待写入数据块的数量。和其他函数一样， `fp` 指定待写入的文件。例如，要保存一个大小为256字节的数据对象（如数组），可以这样做：

```c
char buffer[256];
fwrite(buffer, 256, 1, fp);
```

以上调用把一块256字节的数据从 `buffer` 写入文件。另举一例，要保存一个内含10个 `double` 类型值的数组，可以这样做：

```c
double earnings[10];
fwrite(earnings, sizeof(double), 10, fp);
```

以上调用把 `earnings` 数组中的数据写入文件，数据被分成10块，每块都是 `double` 的大小。

注意 `fwrite()` 原型中的 `const void * restrict ptr` 声明。 `fwrite()` 的一个问题是，它的第1个参数不是固定的类型。例如，第1个例子中使用 `buffer` ，其类型是指向 `char` 的指针；而第2个例子中使用 `earnings` ，其类型是指向 `double` 的指针。在ANSI C函数原型中，这些实际参数都被转换成指向 `void` 的指针类型，这种指针可作为一种通用类型指针（在ANSI C之前，这些参数使用 `char`  *类型，需要把实参强制转换成 `char`  *类型）。

`fwrite()` 函数返回成功写入项的数量。正常情况下，该返回值就是 `nmemb` ，但如果出现写入错误，返回值会比 `nmemb` 小。

