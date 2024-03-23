[toc]

GTK+ 本身是建立在一组其他函数库之上的，如下所示：

+ `GLib`：提供底层数据结构、类型、线程支持、事件循环和动态加载。
+ `GObject`：使用 C 语言而不是 C++ 语言实现了一个面向对象系统。
+ `Pango`：支持文本渲染和布局。
+ `ATK`：用来创建可访问应用程序，并允许用户使用屏幕阅读器和其他协助工具来运行你的应用程序。
+ `GDK`（GIMP 绘图工具包）：在 `Xlib` 之上处理底层图形渲染。
+ `GdkPixbuf`：在 GTK+ 程序中帮助处理图像。
+ `Xlib`：在 Linux 和 UNIX 系统上提供底层图形。

### 1. GLib 类型系统

`Glib` 和 `GObject` 提供了一组数据类型、函数和宏的标准替代集来进行内存管理和处理常见任务，从而实现跨平台开发，如 `gint`、`gchar`、`gshort`，还有一些像 `gint32` 和 `gpointer` 这样不熟悉的类型。

`Glib` 还定义了一些方便的常量：

```c
#include <glib/gmacros.h>

#define FALSE 0
#define TRUE !FALSE
```

这些附加的数据类型基本上是标准 C 语言的数据类型的替代，以及用于确保跨平台字节长度不变。

+ `gint`、`guint`、`gchar`、`guchar`、`glong`、`gulong`、`gfloat` 和 `gdouble` 是标准 C 语言数据类型的简单替代。
+ `gpointer` 与 `(void *)` 同义。
+ `gboolean` 用于表示布尔类型的值，它是对 `int` 的一个包装。
+ `gint8`、`guint8`、`gint16`、`guint16`、`gint32` 和 `guint32` 是保证字节长度的有符号和无符号类型。

### 2. GTK+ 对象系统

尽管 GTK+ 是完全用 C 语言编写的，但是它通过 `GOObject` 库支持对象和面向对象编程。这个库通过宏来支持对象继承和多态。

让我们看一个继承和多态的例子，它取自 GTK+ API 文档中的 `GtkWindow` 的对象层次结构：

```
GObject
	+----GInitiallyUnowned
	+----GtkObjects
		+----GtkWidget
			+----GtkContainer
				+----GtkBin
					+----GtkWindow
```

为了方便起见，所有构建创建函数都返回一个 `GtkWidget` 的类型。例如：

```c
GtkWidget* gtk_window_new(GtkWindowType type);
```

假设你创建了一个 `GtkWindow`，并想把返回值传给某个需要以 `GtkContainer` 作为参数的函数（如 `gtk_container_add`）：

```c
void gtk_container_add(GtkContainer *container, GtkWidget *widget);
```

你需要使用宏 `GTK_CONTAINER` 在 `GtkWidget` 和 `GtkContainer` 之间进行类型转换：
```c
GtkWidget* window = gtk_window_new(GTK GTK_WINDOW_TOPLEVEL);
gtk_container_add(GTK_CONTAINER(window), awidget);
```

