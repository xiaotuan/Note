### 9.2　goroutine

goroutine指的是那些独立于其他goroutine运行的函数。这一概念初看上去和线程有些相似，但实际上goroutine并不是线程，它只是对线程的多路复用。因为goroutine都是轻量级的，所以goroutine的数量可以比线程的数量多很多。一个goroutine在启动时只需要一个非常小的栈，并且这个栈可以按需扩展和缩小（在Go 1.4中，goroutine启动时的栈大小仅为2 KB<a class="my_markdown" href="['#anchor91']"><sup class="my_markdown">[1]</sup></a>）。当一个goroutine被阻塞时，它也会阻塞所复用的操作系统线程，而运行时环境（runtime）则会把位于被阻塞线程上的其他goroutine移动到其他未阻塞的线程上继续运行。

