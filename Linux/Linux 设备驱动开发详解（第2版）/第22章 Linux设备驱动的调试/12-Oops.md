### 22.6 Oops

当内核出现Segmentation Fault时（例如内核访问一个并不存在的虚拟地址），Oops会被打印到控制台和写入系统ring buffer。

我们编写一个字符设备驱动，使让它产生Oops，在其读写函数中都访问0地址，如代码清单22.8所示。



代码清单22.8 产生Oops设备驱动的读写函数

1 static ssize_t oopsexam_read(struct file *filp, char *buf, size_t len, loff_t *off) 
 
 2 { 
 
 3 int *p=0; 
 
 
 4 *p = 1; /* 故意访问 
 0地址 */ 
 
 5 return len; 
 
 6 } 
 
 7 
 
 8 static ssize_t oopsexam_write(struct file *filp, const char *buf, size_t len, loff_t 
 
 9 *off) 
 
 10 { 
 
 11 int *p=0; 
 
 
 12 *p = 1; /* 故意访问 
 0地址 */ 
 
 13 return len; 
 
 14 }

假设这个字符设备对应的设备节点是/dev/oops_example，通过“echo 1 > /dev/oops_example”命令写设备文件，将得到如下Oops信息：

Unable to handle kernel NULL pointer dereference at virtual address 00000000

printing eip:

c381a013

*pde = 00000000

Oops: 0002 [#1]

PREEMPT SMP

Modules linked in: oops_example

CPU: 0

EIP: 0060:[<c381a013>] Not tainted VLI

EFLAGS: 00010286 (2.6.15.5)

EIP is at oopsexam_write+0x4/0x11 [oops_example]

eax: 00000002 ebx: c2b35480 ecx: 00000000 edx: c381a00f

esi: 00000002 edi: 080e9408 ebp: c2007fa4 esp: c2007f68

ds: 007b es: 007b ss: 0068

Process bash (pid: 2453, threadinfo=c2006000 task=c2021570)

Stack: c015e036 c2b35480 080e9408 00000002 c2007fa4 00000000 c2b35480 fffffff7

080e9408 c2006000 c015e1d1 c2b35480 080e9408 00000002 c2007fa4 00000000

00000000 00000000 00000001 00000002 c0102f9f 00000001 080e9408 00000002

Call Trace:

[<c015e036>] vfs_write+0xc5/0x18f

[<c015e1d1>] sys_write+0x51/0x80

[<c0102f9f>] sysenter_past_esp+0x54/0x75

Code: Bad EIP value.

上述Oops的第一行给出了“原因”，即访问了“NULL pointer”。Oops中的“EIP is at oopsexam_ write+0x4/0x11 [oops_example]”这一行也比较关键，给出了“事发现场”，即oopsexam_ write()函数偏移4字节的指令处。

通过反汇编可以知道偏移4字节的指令对应的C代码，如下所示：

1 00000000 <oopsexam_read>: 
 
 2 0: 8b 44 24 0c mov 0xc(%esp,1),%eax 
 
 3 
 4: c7 05 00 00 00 00 01 movl $ 
 0x1,0x0 
 
 4 b: 00 00 00 
 
 5 e: c3 ret

第3行的“movl $0x1,0x0”对应“*p = 1;”。这里仅仅给出了一个例子，实际的“事发现场”并不这么容易被找到，但方法都是类似的。

同样地，我们通过“cat /dev/oops_example”命令去读设备文件，将得到如下Oops信息：

Unable to handle kernel NULL pointer dereference at virtual address 00000000

printing eip:

c381a004

*pde = 00000000

Oops: 0002 [#2]

PREEMPT SMP

Modules linked in: oops_example

CPU: 0

EIP: 0060:[<c381a004>] Not tainted VLI

EFLAGS: 00010286 (2.6.15.5)

EIP is at oopsexam_read+0x4/0xf [oops_example]

eax: 00001000 ebx: c0d80180 ecx: 00000000 edx: c381a000

esi: 00001000 edi: 0804d8d0 ebp: c1df5fa4 esp: c1df5f68

ds: 007b es: 007b ss: 0068

Process cat (pid: 2969, threadinfo=c1df4000 task=c2021570)

Stack: c015dd9e c0d80180 0804d8d0 00001000 c1df5fa4 00000000 c0d80180 fffffff7

0804d8d0 c1df4000 c015e151 c0d80180 0804d8d0 00001000 c1df5fa4 00000000

00000000 00000000 00000003 00001000 c0102f9f 00000003 0804d8d0 00001000

Call Trace:

[<c015dd9e>] vfs_read+0xc5/0x18f

[<c015e151>] sys_read+0x51/0x80

[<c0102f9f>] sysenter_past_esp+0x54/0x75

Code: Bad EIP value.

现在给出的“原因”与写时完全相同，但是“事发地”变成了oopsexam_read()函数偏移4字节的指令处。

在驱动中如果发现硬件或软件的运行情况与预期的不一致，完全可以通过下面的语句故意抛出一个Oops，以便于提供bug的上下文信息：

(*(int *)0 = 0);

内核中有许多地方调用的“BUG();”语句中的BUG()宏通常就被定义为该语句，它非常像一个内核运行时的断言，意味着本来不该执行到BUG()这条语句，一旦执行即抛出Oops。BUG()还有一个变体叫BUG_ON()，只有当括号内的条件成立的时候，才抛出Oops。

