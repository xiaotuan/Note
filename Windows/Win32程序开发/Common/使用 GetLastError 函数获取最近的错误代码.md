[toc]

检索调用线程的最后一个错误代码值。 最后一个错误代码是在每个线程的基础上维护的。 多个线程不会覆盖彼此的最后一个错误代码。

Visual Basic：应用程序应该调用 err.LastDllError 而不是 GetLastError。

### 1. 定义

```cpp
_Post_equals_last_error_ DWORD GetLastError();
```

### 2. 返回值

返回值是调用线程的最后一个错误代码。

设置最后一个错误代码的每个函数的文档的返回值部分记录了函数设置最后一个错误代码的条件。 大多数设置线程最后错误代码的函数在失败时都会设置它。 但是，某些函数在成功时也会设置最后一个错误代码。 如果该函数没有记录设置最后一个错误代码，则该函数返回的值只是最近设置的最后一个错误代码； 一些函数在成功时将最后一个错误代码设置为 0，而其他函数则没有。

### 3. 备注

调用线程执行的函数通过调用 [SetLastError](https://docs.microsoft.com/en-us/windows/desktop/api/errhandlingapi/nf-errhandlingapi-setlasterror) 函数设置此值。当函数的返回值表明这样的调用将返回有用的数据时，您应该立即调用 **GetLastError** 函数。这是因为某些函数在成功时调用 **SetLastError** 时使用零，从而消除了最近失败函数设置的错误代码。

要获取系统错误代码的错误字符串，请使用 [FormatMessage](https://docs.microsoft.com/en-us/windows/desktop/api/winbase/nf-winbase-formatmessage) 函数。有关操作系统提供的错误代码的完整列表，请参阅 [系统错误代码](https://docs.microsoft.com/en-us/windows/desktop/Debug/system-error-codes)。

函数返回的错误代码不是 Windows API 规范的一部分，并且可能因操作系统或设备驱动程序而异。因此，我们无法提供每个函数可以返回的错误代码的完整列表。还有许多函数的文档甚至不包括可以返回的错误代码的部分列表。

错误代码是 32 位值（第 31 位是最高有效位）。第 29 位保留用于应用程序定义的错误代码；没有系统错误代码设置此位。如果要为应用程序定义错误代码，请将此位设置为 1。这表明错误代码已由应用程序定义，并确保您的错误代码不会与系统定义的任何错误代码冲突。

要将系统错误转换为 HRESULT 值，请使用 [HRESULT_FROM_WIN32](https://docs.microsoft.com/en-us/windows/win32/api/winerror/nf-winerror-hresult_from_win32) 宏。

### 4. 示例代码

```cpp
#include <windows.h>
#include <strsafe.h>

void ErrorExit(LPTSTR lpszFunction)
{
    // Retrieve the system error message for the last-error code

    LPVOID lpMsgBuf;
    LPVOID lpDisplayBuf;
    DWORD dw = GetLastError();

    FormatMessage(
        FORMAT_MESSAGE_ALLOCATE_BUFFER |
        FORMAT_MESSAGE_FROM_SYSTEM |
        FORMAT_MESSAGE_IGNORE_INSERTS,
        NULL,
        dw,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
        (LPTSTR)&lpMsgBuf,
        0, NULL);

    // Display the error message and exit the process

    lpDisplayBuf = (LPVOID)LocalAlloc(LMEM_ZEROINIT,
        (lstrlen((LPCTSTR)lpMsgBuf) + lstrlen((LPCTSTR)lpszFunction) + 40) * sizeof(TCHAR));
    StringCchPrintf((LPTSTR)lpDisplayBuf,
        LocalSize(lpDisplayBuf) / sizeof(TCHAR),
        TEXT("%s failed with error %d: %s"),
        lpszFunction, dw, lpMsgBuf);
    MessageBox(NULL, (LPCTSTR)lpDisplayBuf, TEXT("Error"), MB_OK);

    LocalFree(lpMsgBuf);
    LocalFree(lpDisplayBuf);
    ExitProcess(dw);
}

void main()
{
    // Generate an error

    if (!GetProcessId(NULL))
        ErrorExit((LPTSTR)L"GetProcessId");
}
```

### 5. 要求

|                              |                                                |
| :--------------------------- | ---------------------------------------------- |
| **Minimum supported client** | Windows XP [desktop apps \| UWP apps]          |
| **Minimum supported server** | Windows Server 2003 [desktop apps \| UWP apps] |
| **Target Platform**          | Windows                                        |
| **Header**                   | errhandlingapi.h (include Windows.h)           |
| **Library**                  | Kernel32.lib                                   |
| **DLL**                      | Kernel32.dll                                   |