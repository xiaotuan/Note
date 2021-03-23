#### B.5.19　标准I/O库： `stdio.h` 

ANSI C标准库包含一些与流相关联的标准I/O函数和 `stdio.h` 头文件。表B.5.33列出了 `ANSI` 中这些函数的原型和简介（第13章详细介绍过其中的一些函数）。 `stdio.h` 头文件定义了 `FILE` 类型、 `EOF` 和 `NULL` 的值、标准I/O流（ `stdin` 、 `stdout` 和 `stderr` ）以及标准I/O库函数要用到的一些常量。

<center class="my_markdown"><b class="my_markdown">表B.5.33　C标准I/O函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `void clearerr(FILE`  * `);` | 清除文件结尾和错误指示符 |
| `int fclose(FILE`  * `);` | 关闭指定的文件 |
| `int feof(FILE`  * `);` | 测试文件结尾 |
| `int ferror(FILE`  * `);` | 测试错误指示符 |
| `int fflush(FILE`  * `);` | 刷新指定的文件 |
| `int fgetc(FILE`  * `);` | 获得指定输入流的下一个字符 |
| `int fgetpos(FILE`  * `restrict, restrict);` | 存储文件位置指示符的 `fpos_t`  *当前值 |
| `char`  *  `fgets(char`  * `restrict, restrict);` | 从指定流中获取下一行（或 `int` 、 `FILE`  *指定的字符数） |
| `FILE`  *  `fopen(const char` * `restrict, const char` * `restrict);` | 打开指定的文件 |
| `int fprintf(FILE`  * `restrict, const char`  * `restrict, ...);` | 把格式化输出写入指定流 |
| `int fputc(int, FILE`  * `);` | 把指定字符写入指定流 |
| `int fputs(const char` *  `restrict, FILE`  * | `restrict);` | 把第 `1` 个参数指向的字符串写入指定流 |
| `size_t fread(void`  * `restrict, size_t, size_t, FILE`  *  `restrict);` | 读取指定流中的二进制数据 |
| `FILE`  *  `freopen(const char`  *  `restrict, const char`  *  `restrict, FILE`  * `restrict);` | 打开指定文件，并将其与指定流相关联 |
| `int fscanf(FILE`  * `restrict, const char`  * | `restrict, ...);` | 读取指定流中的格式化输入 |
| `int fsetpos(FILE`  * `,const fpos_t`  * `);` | 设置文件位置指针指向指定的值 |
| `int fseek(FILE`  * `, long,int);` | 设置文件位置指针指向指定的值 |
| `long ftell(FILE`  * `);` | 获取当前文件位置 |
| `size_t fwrite(const void` *  `restrict, | size_t,size_t, FILE`  *  `restrict);` | 把二进制数据写入指定流 |
| `int getc(FILE`  * `);` | 读取指定输入的下一个字符 |
| `int getchar();` | 读取标准输入的下一个字符 |
| `char`  *  `gets(char`  * `);` | 获取标准输入的下一行（C11库已删除） |
| `void perror(const char` * `);` | 把系统错误信息写入标准错误中 |
| `int printf(const char`  * `restrict, ...);` | 把格式化输出写入标准输出中 |
| `int putc(int, FILE`  * `);` | 把指定字符写入指定输出中 |
| `int putchar(int);` | 把指定字符写入指定输出中 |
| `int puts(const char`  * `);` | 把字符串写入标准输出中 |
| `int remove(const char`  * `);` | 移除已命名文件 |
| `int rename(const char`  * `,const char`  * `);` | 重命名文件 |
| `void rewind(FILE`  * `);` | 设置文件位置指针指向文件开始处 |
| `int scanf(const char`  * `restrict, ...);` | 读取标准输入中的格式化输入 |
| `void setbuf(FILE`  * `restrict, char`  * | `restrict);` | 设置缓冲区大小和位置 |
| `int setvbuf(FILE`  * `restrict, char`  * `restrict,int, size_t);` | 设置缓冲区大小、位置和模式 |
| `int snprintf(char`  * `restrict, size_t n, const char`  *  `restrict, ...);` | 把格式化输出中的前 `n` 个字符写入指定字符串中 |
| `int sprintf(char`  * `restrict, const char`  * `restrict, ...);` | 把格式化输出写入指定字符串中 |
| `int sscanf(const char` * `restrict, const char`  * `restrict, ...);` | 把格式化输入写入指定字符串中 |
| `FILE`  *  `tmpfile(void);` | 创建一个临时文件 |
| `char`  *  `tmpnam(char`  * `);` | 为临时文件生成一个唯一的文件名 |
| `int ungetc(int, FILE`  * `);` | 把指定字符放回输入流中 |
| `int vfprintf(FILE`  * `restrict, const char`  * `restrict, va_list);` | 与 `fprintf()` 类似，但该函数用一个 `va_list` 类型形参列表（由 `va_start` 初始化）代替变量参数列表 |
| `int vprintf(const char`  * `restrict, va_list);` | 与 `printf()` 类似，但该函数用一个 `va_list` 类型形参列表（由 `va_start` 初始化）代替变量参数列表 |
| `int vsnprintf(char`  * `restrict, size_t n);` | `const char`  *  `restrict,va_list);` | 与 `snprintf()` 类似，但该函数用一个 `va_list` 类型形参列表（由 `va_start` 初始化）代替变量参数列表 |
| `int vsprintf(char`  * `restrict, const char`  * `restrict, va_list);` | 与 `sprintf()` 类似，但该函数用一个 `va_list` 类型形参列表（由 `va_start` 初始化）代替变量参数列表 |
| `int vscanf(const char`  * `restrict, va list);` | 与 `scanf()` 类似，但该函数用一个 `va_list` 类型形参列表（由 `va_start` 初始化）代替变量参数列表 |
| `int vsscanf(const char` *  `restrict,` *  `restrict,va_list);` | 与 `sscanf()` 类似，但该函数用一个 `va_list` 类型形参列表（由 `va_start` 初始化）代替变量参数列表 |

