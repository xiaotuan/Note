[toc]

> 提示
>
> 详细使用说明请参阅 <https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox>。

### 1. 包含头文件

`MessageBox()` 函数声明在 `windows.h` 文件中，使用下面语句引用 `windows.h` 头文件：

```c++
#include <windows.h>
```

### 2. 使用 MessageBox 函数

#### 2.1 定义

`MessageBox()` 函数的定义如下所示：

```c++
WINUSERAPI
int
WINAPI
MessageBoxA(
    _In_opt_ HWND hWnd,
    _In_opt_ LPCSTR lpText,
    _In_opt_ LPCSTR lpCaption,
    _In_ UINT uType);
WINUSERAPI
int
WINAPI
MessageBoxW(
    _In_opt_ HWND hWnd,
    _In_opt_ LPCWSTR lpText,
    _In_opt_ LPCWSTR lpCaption,
    _In_ UINT uType);
#ifdef UNICODE
#define MessageBox  MessageBoxW
#else
#define MessageBox  MessageBoxA
#endif // !UNICODE
```

#### 2.2 函数参数

+ `hwnd`：要创建的消息框的所有者窗口的句柄。 如果此参数为 NULL，则消息框没有所有者窗口。
+ `lpText`：要显示的消息。 如果字符串由多行组成，您可以在每行之间使用回车符和/或换行符分隔各行。
+ `lpCaption`：对话框标题。 如果此参数为 NULL，则默认标题为 Error。
+ `uType`：对话框的内容和行为。

#### 2.3 uType 参数可使用的值

##### 2.3.1 指示消息框中显示的按钮

| 值                                        | 意义                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| **MB_ABORTRETRYIGNORE**<br />0x00000002L  | 消息框包含三个按钮：**Abort**、**Retry** 和 **Ignore**。     |
| **MB_CANCELTRYCONTINUE**<br />0x00000006L | 消息框包含三个按钮：**Cancel**、**Try Again**、**Continue**。 使用此消息框类型替代MB_ABORTRETRYIGNORE。 |
| **MB_HELP**<br />0x00004000L              | 在消息框中添加一个 **Help** 按钮。 当用户点击 **Help** 按钮或按F1时，系统发送[WM_HELP](https://msdn.microsoft.com/en-us/library/Bb774305(v=VS.85).aspx) 给所有者。 |
| **MB_OK**<br />0x00000000L                | 消息框包含一个按钮：**OK**。 这是默认设置。                  |
| **MB_OKCANCEL**<br />0x00000001L          | 消息框包含两个按钮：**OK** 和 **Cancel**。                   |
| **MB_RETRYCANCEL<br />**0x00000005L       | 消息框包含两个按钮：**Retry** 和 **Cancel**。                |
| **MB_YESNO**<br />0x00000004L             | 消息框包含两个按钮：**Yes** 和 **No**。                      |
| **MB_YESNOCANCEL**<br />0x00000003L       | 消息框包含三个按钮：**Yes**、**No** 和 **Cancel**。          |

##### 2.3.2 在消息框中显示图标

| 值                                      | 意义                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| **MB_ICONEXCLAMATION**<br />0x00000030L | 消息框中会出现一个感叹号图标。                               |
| **MB_ICONWARNING**<br />0x00000030L     | 消息框中会出现一个感叹号图标。                               |
| **MB_ICONINFORMATION**<br />0x00000040L | 一个由圆圈中的小写字母 i 组成的图标出现在消息框中。          |
| **MB_ICONASTERISK**<br />0x00000040L    | 一个由圆圈中的小写字母 i 组成的图标出现在消息框中。          |
| **MB_ICONQUESTION**<br />0x00000020L    | 问号图标出现在消息框中。 不再推荐使用问号消息图标，因为它不能清楚地表示特定类型的消息，并且作为问题的消息措辞可能适用于任何消息类型。 此外，用户可能会将消息符号问号与帮助信息混淆。 因此，请勿在消息框中使用此问号消息符号。 系统继续支持它的包含只是为了向后兼容。 |
| **MB_ICONSTOP**<br />0x00000010L        | 一个停止标志图标出现在消息框中。                             |
| **MB_ICONERROR**<br />0x00000010L       | 一个停止标志图标出现在消息框中。                             |
| **MB_ICONHAND**<br />0x00000010L        | 一个停止标志图标出现在消息框中。                             |

##### 2.3.3 指示默认按钮

| 值                                 | 意义                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| **MB_DEFBUTTON1**<br />0x00000000L | 第一个按钮是默认按钮。 **MB_DEFBUTTON1** 是默认值，除非指定了 **MB_DEFBUTTON2**、**MB_DEFBUTTON3** 或 **MB_DEFBUTTON4**。 |
| **MB_DEFBUTTON2**<br />0x00000100L | 第二个按钮是默认按钮。                                       |
| **MB_DEFBUTTON3**<br />0x00000200L | 第三个按钮是默认按钮。                                       |
| **MB_DEFBUTTON4**<br />0x00000300L | 第四个按钮是默认按钮。                                       |

##### 2.3.4 指示对话框的模式

| 值意义                              |                                                              |
| ----------------------------------- | ------------------------------------------------------------ |
| **MB_APPLMODAL**<br />0x00000000L   | 用户必须先响应消息框，然后才能在 hWnd 参数标识的窗口中继续工作。 但是，用户可以移动到其他线程的窗口并在这些窗口中工作。 根据应用程序中窗口的层次结构，用户可能能够移动到线程内的其他窗口。 自动禁用消息框父级的所有子窗口，但不会自动禁用弹出窗口。如果既未指定 **MB_SYSTEMMODAL** 也未指定 **MB_TASKMODAL**，**MB_APPLMODAL** 为默认值。 |
| **MB_SYSTEMMODAL**<br />0x00001000L | 与 MB_APPLMODAL 相同，只是消息框具有 **WS_EX_TOPMOST** 样式。 使用系统模式消息框来通知用户需要立即注意的严重的、具有潜在破坏性的错误（例如，内存不足）。 此标志对用户与除与 hWnd 关联的窗口之外的窗口进行交互的能力没有影响。 |
| **MB_TASKMODAL**<br />0x00002000L   | 与 **MB_APPLMODAL** 相同，但如果 hWnd 参数为 **NULL** 则禁用所有属于当前线程的顶级窗口。 当调用应用程序或库没有可用的窗口句柄但仍需要防止输入到调用线程中的其他窗口而不暂停其他线程时，请使用此标志。 |

##### 2.3.5 其他选项

| 值                                           | 意义                                                         |
| -------------------------------------------- | ------------------------------------------------------------ |
| **MB_DEFAULT_DESKTOP_ONLY<br />**0x00020000L | 与交互式窗口站的桌面相同。 有关详细信息，请参阅 [Window Stations](https://msdn.microsoft.com/en-us/library/ms687096(v=VS.85).aspx)。 如果当前输入的桌面不是默认桌面，则**MessageBox** 不会返回，直到用户切换到默认桌面。 |
| **MB_RIGHT**<br />0x00080000L                | 文本右对齐。                                                 |
| **MB_RTLREADING**<br />0x00100000L           | 在希伯来语和阿拉伯语系统上使用从右到左的阅读顺序显示消息和标题文本。 |
| **MB_SETFOREGROUND**<br />0x00010000L        | 消息框成为前台窗口。 在内部，系统调用消息框的[SetForegroundWindow](https://msdn.microsoft.com/en-us/library/ms633539(v=VS.85).aspx)函数。 |
| **MB_TOPMOST**<br />0x00040000L              | 消息框是使用 **WS_EX_TOPMOST** 窗口样式创建的。              |
| **MB_SERVICE_NOTIFICATION**<br />0x00200000L | 调用者是通知用户事件的服务。 即使没有用户登录到计算机，该功能也会在当前活动桌面上显示一个消息框。 **终端服务：**如果调用线程有模拟令牌，该函数将消息框定向到模拟令牌中指定的会话。如果设置了此标志，则 hWnd 参数必须为 **NULL**。 这是为了使消息框可以出现在与 hWnd 对应的桌面以外的桌面上。有关使用此标志的安全注意事项的信息，请参阅 [Interactive Services](https://msdn.microsoft.com/en) -us/library/ms683502(v=VS.85).aspx)。 特别要注意，此标志可以在锁定的桌面上生成交互式内容，因此只能用于非常有限的一组场景，例如资源耗尽。 |

#### 2.4 返回值

| 返回代码/值            | 描述                       |
| ---------------------- | -------------------------- |
| **IDABORT**<br />3     | **Abort** 按钮被选中。     |
| **IDCANCEL**<br />2    | **Cancel** 按钮被选中。    |
| **IDCONTINUE**<br />11 | **Continue** 按钮被选中。  |
| **IDIGNORE**<br />5    | **Ignore** 按钮被选中。    |
| **IDNO**<br />7        | **No** 按钮被选中。        |
| **IDOK**<br />1        | **OK** 按钮被选中。        |
| **IDRETRY**<br />4     | **Retry** 按钮被选中。     |
| **IDTRYAGAIN**<br />10 | **Try Again** 按钮被选中。 |
| **IDYES**<br />6       | **Yes** 按钮被选中。       |

### 3. 示例代码

#### 3.1 示例代码 1

```cpp
#include <stdio.h>
#include <Windows.h>    //  包含 MessageBox 函数声明的头文件

int main(int argc, char* argv[])
{
    // 调用 API 函数 MessageBox
    int nSelect = ::MessageBox(NULL, TEXT("Hello, Windows XP"), TEXT("Greetings"), MB_OKCANCEL | MB_ICONEXCLAMATION );
    if (nSelect == IDOK) 
    {
        printf("用户选择了 “确定” 按钮\n");
    }
    else
    {
        printf("用户选择了“取消”按钮\n");
    }
    return 0;
}
```

> 提示
>
> 在 API 函数前加 "::" 符号，表示这时一个全局的函数，以与 C++ 类的成员函数相区分。

#### 3.2 示例代码 2

```c++
#include <stdio.h>
#include <Windows.h>    //  包含 MessageBox 函数声明的头文件

int main(int argc, char* argv[])
{
    int msgboxID = MessageBox(
        NULL,
        (LPCWSTR)L"Resource not available\nDo you want to try again?",
        (LPCWSTR)L"Account Details",
        MB_ICONWARNING | MB_CANCELTRYCONTINUE | MB_DEFBUTTON2
    );
    switch (msgboxID)
    {
        case IDCANCEL:
            printf("Cancel 按钮被选中\n");
            break;
        case IDTRYAGAIN:
            printf("Try Again 按钮被选中\n");
            break;
        case IDCONTINUE:
            printf("Continue 按钮被选中\n");
            break;
    }

    return 0;
}
```

