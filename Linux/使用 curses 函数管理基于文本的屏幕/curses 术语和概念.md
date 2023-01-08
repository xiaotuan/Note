`curses` 函数库用两个数据结构来映射终端屏幕，它们是 `stdscr` 和 `curscr`。两者中，`stdscr` 更重要一些，它会在 `curses` 函数产生输出时被刷新。`stdscr` 数据结构对应的是 "标准屏幕"，它的工作方式与 `stdio` 函数库中的标准输出 `stdout` 非常相似。它是 `curses` 程序中的默认输出窗口。`curscr` 数据结构和 `stdscr` 相似，但它对应的是当前屏幕的样子。在程序调用 `refresh` 函数之前，输出到 `stdscr` 上的内容不会显示在屏幕上。`curses` 函数库会在 `refresh` 函数被调用时比较 `stdscr`（屏幕将会是什么样子）与第二个数据结构 `curscr`（屏幕当前的样子）之间的不同之处，然后用这两个数据结构之间的差异来刷新屏幕。

有的 `curses` 程序需要知道 `curses` 维护的 `stdscr` 结构，因为有些 `curses` 函数需要以该结构为参数。但真正的 `stdscr` 结构是与具体实现相关的，它决不能被直接访问。`curses` 程序无需使用 `curscr` 数据结构。

综上所述，在 `curses` 程序中输出字符的过程如下所示：

1. 使用 `curses` 函数刷新逻辑屏幕。
2. 要求 `curses` 用 `refresh` 函数来刷新物理屏幕。

一个 `curses` 程序会多次调用逻辑屏幕输出函数，例如在屏幕上移动光标到达正确的位置，然后输出文本、绘制线框。在程序执行的某些阶段，用户需要看到全部的输出结果。这时 `curses` 一般会通过调用 `refresh` 函数计算出让物理屏幕和逻辑屏幕相对应的最佳途径。`curses` 通过使用合适的终端功能标志及优化光标的移动来刷新屏幕，与立刻执行所有的屏幕写操作相比，`curses` 所需要输出的字符要少得多。

逻辑屏幕的布局通过一个字符数组来实现，它以屏幕的左上角——坐标（0, 0）为起点，通过行号和列号来组织。所有的 `curses` 函数使用的坐标都是 y 值（行号）在前、x 值（列号）在后。每个位置不仅包含该屏幕位置处的字符，还包含它的属性。

由于 `curses` 函数库在使用时需要创建和删除一些临时的数据结构，所以所有的 `curses` 程序必须在开始使用 `curses` 函数库之前对其进行初始化，并在结束使用后允许 `curses` 恢复原先设置。这两项工作是由 `initscr` 和 `endwin` 函数分别完成的。

**示例代码：screen1.c**

```c
#include <curses.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int  main() {
    initscr();
    move(5, 15);
    printw("%s", "Hello World");
    refresh();

    sleep(2);

    endwin();
    exit(EXIT_SUCCESS);
}
```

