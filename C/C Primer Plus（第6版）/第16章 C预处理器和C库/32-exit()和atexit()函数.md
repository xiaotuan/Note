#### 16.11.1　 `exit()` 和 `atexit()` 函数

在前面的章节中我们已经在程序示例中用过 `exit()` 函数。而且，在 `main()` 返回系统时将自动调用 `exit()` 函数。ANSI标准还新增了一些不错的功能，其中最重要的是可以指定在执行 `exit()` 时调用的特定函数。 `atexit()` 通过注册要在退出时调用的函数来提供这一特性， `atexit()` 函数接受一个函数指针作为参数。程序清单16.16演示了它的用法。

程序清单16.16　 `byebye.c` 程序

```c
/* byebye.c -- atexit()示例 */
#include <stdio.h>
#include <stdlib.h>
void sign_off(void);
void too_bad(void);
int main(void)
{
　　 int n;
　　 atexit(sign_off);　　/* 注册 sign_off()函数 */
　　 puts("Enter an integer:");
　　 if (scanf("%d", &n) != 1)
　　 {
　　　　　puts("That's no integer!");
　　　　　atexit(too_bad);　/* 注册 too_bad()函数 */
　　　　　exit(EXIT_FAILURE);
　　 }
　　 printf("%d is %s.\n", n, (n % 2 == 0) ? "even" : "odd");
　　 return 0;
}
void sign_off(void)
{
　　 puts("Thus terminates another magnificent program from");
　　 puts("SeeSaw Software!");
}
void too_bad(void)
{
　　 puts("SeeSaw Software extends its heartfelt condolences");
　　 puts("to you upon the failure of your program.");
}
```

下面是该程序的一个运行示例：

```c
Enter an integer:
212
212 is even.
Thus terminates another magnificent program from
SeeSaw Software!

```

如果在IDE中运行，可能看不到最后两行。下面是另一个运行示例：

```c
Enter an integer:
what?
That's no integer!
SeeSaw Software extends its heartfelt condolences
to you upon the failure of your program.
Thus terminates another magnificent program from
SeeSaw Software!

```

在IDE中运行，可能看不到最后4行。

接下来，我们讨论 `atexit()` 和 `exit()` 的参数。

#### 1． `atexit()` 函数的用法

这个函数使用函数指针。要使用 `atexit()` 函数，只需把退出时要调用的函数地址传递给 `atexit()` 即可。函数名作为函数参数时相当于该函数的地址，所以该程序中把 `sign_off` 或 `too_bad` 作为参数。然后， `atexit()` 注册函数列表中的函数，当调用 `exit()` 时就会执行这些函数。ANSI保证，在这个列表中至少可以放32个函数。最后调用 `exit()` 函数时， `exit()` 会执行这些函数（执行顺序与列表中的函数顺序相反，即最后添加的函数最先执行）。

注意，输入失败时，会调用 `sign_off()` 和 `too_bad()` 函数；但是输入成功时只会调用 `sign_off()` 。因为只有输入失败时，才会进入 `if` 语句中注册 `too_bad()` 。另外还要注意，最先调用的是最后一个被注册的函数。

`atexit()` 注册的函数（如 `sign_off()` 和 `too_bad()` ）应该不带任何参数且返回类型为 `void` 。通常，这些函数会执行一些清理任务，例如更新监视程序的文件或重置环境变量。

注意，即使没有显式调用 `exit()` ，还是会调用 `sign_off()` ，因为 `main()` 结束时会隐式调用 `exit()` 。

#### 2． `exit()` 函数的用法

`exit()` 执行完 `atexit()` 指定的函数后，会完成一些清理工作：刷新所有输出流、关闭所有打开的流和关闭由标准I/O函数 `tmpfile()` 创建的临时文件。然后 `exit()` 把控制权返回主机环境，如果可能的话，向主机环境报告终止状态。通常，UNIX程序使用 `0` 表示成功终止，用非零值表示终止失败。UNIX返回的代码并不适用于所有的系统，所以ANSI C为了可移植性的要求，定义了一个名为 `EXIT_FAILURE` 的宏表示终止失败。类似地，ANSI C还定义了 `EXIT_SUCCESS` 表示成功终止。不过， `exit()` 函数也接受 `0` 表示成功终止。在ANSI C中，在非递归的 `main()` 中使用 `exit()` 函数等价于使用关键字 `return` 。尽管如此，在 `main()` 以外的函数中使用 `exit()` 也会终止整个程序。

