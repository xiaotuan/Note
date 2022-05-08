在实际的开发过程中，一般不直接使用 Windows 系统提供的 CreateThread 函数创建线程，而是使用 C/C++ 运行期函数（`_beginthreadex`）。

要想使用运行期为每个线程都设置状态变量，必须在创建线程的时候调用运行期提供的 `_beginthreadex` ，让运行期设置了相关变量后再去调用 Windows 系统提供的 `CreateThread` 函数。`_beginthreadex` 的参数与 `CreateThread` 函数是对应的，只是参数名和类型不完全相同，使用的时候需要强制转换。

C/C++ 运行期库提供 (`_endthreadex`）函数用于取代 `ExitThread` 函数。其语法格式如下所示：

```c
void _endthreadex(
	unsigned retval	// 指定退出代码
);
```

例如：

```c
#include <Windows.h>
#include <stdio.h>
#include <process.h>

// 线程函数
DWORD WINAPI ThreadProc(LPVOID lpParam)
{
	int i = 0;
	while (i < 20)
	{
		printf("I am from a thread, count = %d\n", i++);
	}
	return 0;
}

int main(int argc, char argv[])
{
	HANDLE hThread;
	DWORD dwThreadId;
	SECURITY_ATTRIBUTES sa;
	uintptr_t uThread;

	sa.nLength = sizeof(sa);
	sa.lpSecurityDescriptor = NULL;
	sa.bInheritHandle = TRUE;	// 使 CreateThrea

	uThread = _beginthreadex(
		&sa,	// 默认安全属性
		NULL,	// 默认堆栈大小
		(_beginthreadex_proc_type)ThreadProc,	// 线程入口地址（执行线程的函数）
		NULL,	// 传给函数的参数
		0,	// 指定线程立即运行
		(unsigned int*)&dwThreadId	// 返回线程的 ID 号
	);

	if (!uThread) {
		printf("Create thread fial.");
		return -1;
	}

	hThread = (HANDLE)uThread;

	printf("Now another thread has been created. ID = %d\n", dwThreadId);

	// 等待新线程运行结束
	::WaitForSingleObject(hThread, INFINITE);
	::CloseHandle(hThread);

	return 0;
}
```
