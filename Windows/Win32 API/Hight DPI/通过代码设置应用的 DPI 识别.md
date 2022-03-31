可以通过 `SetThreadDpiAwarenessContext()` 函数设置应用的 DPI 识别值。例如：

```cpp
#include <Windows.h>

int main(int argc, char* argv[])
{
    SetThreadDpiAwarenessContext(DPI_AWARENESS_CONTEXT_SYSTEM_AWARE);
    int msgboxID = MessageBox(
        NULL,
        (LPCWSTR)L"Resource not available\nDo you want to try again?",
        (LPCWSTR)L"Account Details",
        MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2
    );
}
```

可设置的值有：

+ **DPI_AWARENESS_CONTEXT_UNAWARE**

  DPI 不知道。 此窗口不会针对 DPI 更改进行缩放，并且始终假定缩放因子为 100% (96 DPI)。 它将由系统在任何其他 DPI 设置上自动缩放。

+ **DPI_AWARENESS_CONTEXT_SYSTEM_AWARE**

  系统 DPI 感知。 此窗口不会针对 DPI 更改进行缩放。 它将查询一次 DPI，并在进程的生命周期内使用该值。 如果 DPI 发生变化，该过程将不会调整到新的 DPI 值。 当 DPI 从系统值改变时，系统会自动放大或缩小。

+ **DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE**

  每个显示器 DPI 感知。 此窗口在创建时检查 DPI，并在 DPI 更改时调整比例因子。 系统不会自动缩放这些过程。

+ **DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2**

  也称为每监视器 v2。 对原始每显示器 DPI 感知模式的改进，使应用程序能够在每个顶级窗口的基础上访问新的 DPI 相关缩放行为。
  Per Monitor v2 在 Windows 10 的 Creators Update 中可用，但在早期版本的操作系统中不可用。
  引入的附加行为如下：

  + **Child window DPI change notifications**

    在 Per Monitor v2 上下文中，将通知整个窗口树发生的任何 DPI 更改。

  + **Scaling of non-client area**

    所有窗口都将自动以 DPI 敏感方式绘制其非客户区。 无需调用 EnableNonClientDpiScaling。

  + **Scaling of Win32 menus**

    在每个监视器 v2 上下文中创建的所有 NTUSER 菜单都将以每个监视器的方式进行缩放。

  + **Dialog Scaling**

    在 Per Monitor v2 上下文中创建的 Win32 对话框将自动响应 DPI 更改。

  + **Improved scaling of comctl32 controls**

    各种 comctl32 控件改进了 Per Monitor v2 上下文中的 DPI 缩放行为。

  + **Improved theming behavior**

    在 Per Monitor v2 窗口的上下文中打开的 UxTheme 句柄将根据与该窗口关联的 DPI 进行操作。

+ **DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED**

  DPI 不知道基于 GDI 的内容质量的提高。 此模式的行为类似于 DPI_AWARENESS_CONTEXT_UNAWARE，但也使系统能够在窗口显示在高 DPI 监视器上时自动提高文本和其他基于 GDI 的图元的渲染质量。

