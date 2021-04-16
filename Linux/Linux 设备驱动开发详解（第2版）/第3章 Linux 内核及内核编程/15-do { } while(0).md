### 3.5.3 do { } while(0)

在Linux内核中，经常会看到do {} while(0)这样的语句，许多人开始都会疑惑，认为do {} while(0)毫无意义，因为它只会执行一次，加不加do {} while(0)效果是完全一样的，其实do {} while(0)的用法主要用于宏定义中。

这里用一个简单点的宏来演示：

#define SAFE_FREE(p) do{ free(p); p = NULL;} while(0)

假设这里去掉do...while(0)，即定义SAFE_DELETE为：

#define SAFE_FREE(p) free(p); p = NULL;

那么以下代码

if(NULL != p) 
 
 SAFE_DELETE(p) 
 
 else 
 
 .../* do something */

会被展开为：

if(NULL != p) 
 
 free(p); p = NULL; 
 
 else 
 
 .../* do something */

展开的代码中存在两个问题。

（1）因为if分支后有两个语句，导致else分支没有对应的if，编译失败。

（2）假设没有else分支，则SAFE_FREE中的第二个语句无论if测试是否通过，都会执行。的确，将SAFE_FREE的定义加上{}就可以解决上述问题了，即：

#define SAFE_FREE(p) { free(p); p = NULL;}

这样，代码：



if(NULL != p) 
 
 SAFE_DELETE(p) 
 
 else 
 
 ... /* do something */

会被展开为：

if(NULL != p) 
 
 { free(p); p = NULL; } 
 
 else 
 
 ... /* do something */

但是，在C程序中，每个语句后面加分号是一种约定俗成的习惯，那么，如下代码：

if(NULL != p) 
 
 SAFE_DELETE(p); 
 
 else 
 
 ... /* do something */

将被扩展为：

if(NULL != p) 
 
 { free(p); p = NULL; }; 
 
 else 
 
 ... /* do something */

这样，else分支就又没有对应的if了，编译将无法通过。假设用了do {} while(0)，情况就不一样了，同样的代码会被展开为：

if(NULL != p) 
 
 do{ free(p); p = NULL;} while(0); 
 
 else 
 
 ... /* do something */

不会再出现编译问题。do while(0)的使用完全是为了保证宏定义的使用者能无编译错误地使用宏，它不对其使用者做任何假设。

