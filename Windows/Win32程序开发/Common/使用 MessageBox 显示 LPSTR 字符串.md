要使用 `MessageBox` 函数显示 `LPSTR` 字符串需要使用 `MessageBoxA` 函数版本，例如：

```c
/*--------------------------------------------------------------------------
HelloMsg.c -- Displays "Hello, Windows 98!" in a message box
		(c) Charles Petzold, 1998
----------------------------------------------------------------------------*/
#include <Windows.h>

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
	PSTR szCmdLine, int iCmdShow)
{
	MessageBox(NULL, szCmdLine, "HelloMsg", 0);
	return 0;
}
```

