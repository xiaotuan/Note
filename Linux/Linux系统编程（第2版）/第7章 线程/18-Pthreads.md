### 7.7　Pthreads

Linux内核只为线程的支持提供了底层原语，比如clone()系统调用。多线程库在用户空间。很多大型软件项目只定义自己的线程库：Android、Apache、GNOME和Mozilla都提供自己的线程库，比如C++11和Java语言都提供标准库来支持线程。然而，POSIX在IEEE Std -1995（也称为POSIX 1995或POSIX）对线程库进行了标准化。开发人员称之为POSIX线程，或简称为Pthreads。Pthreads是UNIX系统上C和C++语言的主要线程解决方案。

