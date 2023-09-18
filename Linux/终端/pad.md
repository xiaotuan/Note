在编写更高级的 `curses` 程序时，有时需要先建立一个逻辑屏幕，然后在把它的全部或部分内容输出到物理屏幕上。有时候，如果能有一个尺寸大于物理屏幕的逻辑屏幕，一次只显示该逻辑屏幕的某个部分，其效果往往会更好。

但使用到目前为止所学过的 `curses` 函数来实现这一功能并不容易，因为任何窗口的尺寸都不能大于物理屏幕。`curses` 提供了一个特殊的数据结构 `pad` 来解决这一问题，它可以控制尺寸大于正常窗口的逻辑屏幕。`pad` 结构非常类似 `WINDOW` 结构，所执行写窗口操作的 `curses` 函数同样可用于 `pad` 。`pad` 还有其自己的创建函数和刷新函数。

创建 `pad` 的方式与创建正常窗口的方式基本相同：

```c
#include <curses.h>

WINDOW *newpad(int number_of_lines, int number_of_columns);
```

需要注意的是，这个函数的返回值是一个指向 `WINDOW` 结构的指针，这一点与 `newwin` 函数相同。`pad` 用 `delwin` 函数来删除，这与正常窗口的删除一样。

`pad` 使用不同的函数执行刷新操作。因为一个 `pad` 并不局限于某个特定的屏幕位置，所以必须指定希望放在屏幕上的 `pad` 范围及其放置在屏幕上的位置。`prefresh` 函数用于完成这一功能：

```c
#include <curses.h>

int prefresh(WINDOW *pad_ptr, int pad_row, int pad_column,
            int screen_row_min, int screen_col_min,
            int screen_row_max, int screen_col_max);
```

这个函数的作用是将 `pad` 从坐标（`pad_row`，`pad_column`）开始的区域写到屏幕上指定的显示区域，该显示区域的范围从坐标（`screen_row_min`、`screen_col_min`） 到 （`screen_row_max`，`screen_col_max`）。

`curses` 还提供了函数 `pnoutrefresh`，它的作用与函数 `wnoutrefresh` 一样，都是为了更有效地更新屏幕。

**示例程序：pad.c**

```c
#include <unistd.h>
#include <stdlib.h>
#include <curses.h>

int main()
{
	WINDOW *pad_ptr;
	int x, y;
	int pad_lines;
	int pad_cols;
	char disp_char;
	
	initscr();
	pad_lines = LINES + 50;
	pad_cols = COLS + 50;
	pad_ptr = newpad(pad_lines, pad_cols);
	disp_char = 'a';
	
	for (x = 0; x < pad_lines; x++) {
		for (y = 0; y < pad_cols; y++) {
			mvwaddch(pad_ptr, x, y, disp_char);
			if (disp_char == 'z') {
				disp_char = 'a';
			} else {
				disp_char++;
			}
		}
	}
	
	prefresh(pad_ptr, 5, 7, 2, 2, 9, 9);
	sleep(1);
	prefresh(pad_ptr, LINES + 5, COLS + 7, 5, 5, 21, 19);
	sleep(1);
	delwin(pad_ptr);
	endwin();
	exit(EXIT_SUCCESS);
}
```

运行效果如下：

```
$ gcc pad.c  -lncurses
```

![01](./images/01.)