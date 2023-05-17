[toc]

Beep 函数在扬声器上产生简单的音调。 功能是同步的； 它执行警报等待，并且在声音结束之前不会将控制权返回给它的调用者。

### 1. 头文件

`Beep()` 函数定义在 `utilapiset.h` 头文件中，如果源代码已经包含 `windows.h` 头文件，则不需要再次包含 `utilapiset.h` 头文件：

```c++
#include <utilapiset.h>
```

### 2. 函数定义

该函数的定义如下所示：

```cpp
#pragma region PC Family or OneCore Family or Games Family
#if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

WINBASEAPI
BOOL
WINAPI
Beep(
    _In_ DWORD dwFreq,
    _In_ DWORD dwDuration
    );


#endif /* WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES) */
#pragma endregion
```

### 3. 参数

+ `dwFreq`：声音的频率，以赫兹为单位。 此参数必须在 37 到 32,767（0x25 到 0x7FFF）的范围内。
+ `dwDuration`：声音的持续时间，以毫秒为单位。

### 4. 返回值

如果函数成功，则返回值非零。

如果函数失败，则返回值为零。 要获取扩展错误信息，请调用 GetLastError。

### 5. 要求

|                              |                                                |
| :--------------------------- | ---------------------------------------------- |
| **Minimum supported client** | Windows XP [desktop apps \| UWP apps]          |
| **Minimum supported server** | Windows Server 2003 [desktop apps \| UWP apps] |
| **Target Platform**          | Windows                                        |
| **Header**                   | utilapiset.h (include Windows.h)               |
| **Library**                  | Kernel32.lib                                   |
| **DLL**                      | Kernel32.dll                                   |

### 6. 示例代码

```cpp
#include <Windows.h>

int main(int argc, char* argv[])
{
    Beep(440, 5000);

    return 0;
}
```

### 7. 备注

很久以前，所有 PC 计算机共享一个通用的 8254 可编程间隔定时器芯片，用于生成原始声音。 Beep 函数是专门为在该硬件上发出哔声而编写的。

在这些较旧的系统上，静音和音量控制对 Beep 没有影响；你仍然会听到音调。要使音调静音，您使用了以下命令：

```
net stop beep

sc config beep start= disabled
```

从那时起，声卡已成为几乎所有 PC 计算机的标准设备。随着声卡变得越来越普遍，制造商开始从计算机中移除旧的计时器芯片。这些芯片也被排除在服务器计算机的设计之外。结果是 Beep 不能在所有没有芯片的计算机上工作。这没关系，因为大多数开发人员已经开始调用 MessageBeep 函数，该函数使用默认声音设备而不是 8254 芯片。

最终，由于缺少可与之通信的硬件，Windows Vista 和 Windows XP 64 位版中放弃了对 Beep 的支持。

在 Windows 7 中，Beep 被重写以将哔声传递给会话的默认声音设备。这通常是声卡，除非在终端服务下运行，在这种情况下会在客户端上呈现哔声。