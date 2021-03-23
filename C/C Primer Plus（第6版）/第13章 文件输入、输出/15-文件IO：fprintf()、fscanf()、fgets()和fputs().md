### 13.4　文件I/O： `fprintf()` 、 `fscanf()` 、 `fgets()` 和 `fputs()` 

前面章节介绍的I/O函数都类似于文件I/O函数。它们的主要区别是，文件I/O函数要用 `FILE` 指针指定待处理的文件。与 `getc()` 、 `putc()` 类似，这些函数都要求用指向 `FILE` 的指针（如， `stdout` ）指定一个文件，或者使用 `fopen()` 的返回值。

