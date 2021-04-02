### 13.1.1　QThread类功能简介

QThread类提供不依赖于平台的管理线程的方法。一个QThread类的对象管理一个线程，一般从QThread继承一个自定义类，并重定义虚函数run()，在run()函数里实现线程需要完成的任务。

将应用程序的线程称为主线程，额外创建的线程称为工作线程。一般在主线程里创建工作线程，并调用start()开始执行工作线程的任务。start()会在内部调用run()函数，进入工作线程的事件循环，在run()函数里调用exit()或quit()可以结束线程的事件循环，或在主线程里调用terminate()强制结束线程。

QThread类的主要接口函数、信号和槽函数见表13-1。

<center class="my_markdown"><b class="my_markdown">表13-1　Qthread类的主要接口</b></center>

| 类型 | 函数 | 功能 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 公共 | 函数 | bool isFinished() | 线程是否结束 |
| bool isRunning() | 线程是否正在运行 |
| Priority　priority() | 返回线程的优先级 |
| 公共 | 函数 | void setPriority (Priority priority) | 设置线程的优先级 |
| void exit(int returnCode = 0) | 退出线程的事件循环，退出码为returnCode，0表示成功退出；否则表示有错误 |
| bool wait(unsigned long time ) | 阻止线程执行，直到线程结束（从run()函数返回），或等待时间超过time毫秒 |
| 公共槽函数 | void　quit() | 退出线程的事件循环，并返回代码0，等效于exit(0) |
| void start(Priority priority ) | 内部调用run()开始执行线程，操作系统根据priority参数进行调度 |
| void terminate() | 终止线程的运行，但不是立即结束线程，而是等待操作系统结束线程。使用terminate()之后应使用wait() |
| 信号 | void finished() | 在线程就要结束时发射此信号 |
| void started() | 在线程开始执行、run()函数被调用之前发射此信号 |
| 静态 | 公共 | 成员 | int idealThreadCount() | 返回系统上能运行的线程的理想个数 |
| void msleep(unsigned long msecs) | 强制当前线程休眠msecs毫秒 |
| void sleep(unsigned long secs) | 强制当前线程休眠secs秒 |
| void usleep(unsigned long usecs) | 强制当前线程休眠usecs微秒 |
| 保护 | 函数 | virtual void run() | start()调用run()函数开始线程任务的执行，所以在run()函数里实现线程的任务功能 |
| int exec() | 由run()函数调用，进入线程的事件循环，等待exit()退出 |

QThread是QObject的子类，所以可以使用信号与槽机制。QThread自身定义了started()和finished()两个信号，started()信号在线程开始执行之前发射，也就是在run()函数被调用之前，finished()信号在线程就要结束时发射。

