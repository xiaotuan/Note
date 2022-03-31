[toc]

> 提示
>
> 详情请参阅 <https://docs.microsoft.com/en-us/windows/win32/api/_hidpi/>

要开发高 DPI，您需要以下标头：

+ [shellscalingapi.h](https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/)

有关此技术的编程指南，请参阅：

+ [High DPI](https://docs.microsoft.com/en-us/windows/desktop/hidpi)

### 1. 枚举

|    |
| ------------------------------------------------------------ |
| [ DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ne-winuser-dialog_control_dpi_change_behaviors)  <br />描述对话框中子窗口的每个监视器 DPI 缩放行为覆盖。 此枚举中的值是位域，可以组合。 |
| [DIALOG_DPI_CHANGE_BEHAVIORS](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ne-winuser-dialog_dpi_change_behaviors)  <br />在 Per Monitor v2 上下文中，对话框将通过调整自身大小并重新计算其子窗口的位置（此处称为重新布局）来自动响应 DPI 更改。 |
| [DPI_AWARENESS](https://docs.microsoft.com/en-us/windows/win32/api/windef/ne-windef-dpi_awareness)  <br />标识线程、进程或窗口的每英寸点数 (dpi) 设置。 |
| [DPI_HOSTING_BEHAVIOR](https://docs.microsoft.com/en-us/windows/win32/api/windef/ne-windef-dpi_hosting_behavior)  <br />标识窗口的 DPI 托管行为。 此行为允许在线程中创建的窗口承载具有不同 DPI_AWARENESS_CONTEXT 的子窗口。 |
| [MONITOR_DPI_TYPE](https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/ne-shellscalingapi-monitor_dpi_type)  <br />标识监视器的每英寸点数 (dpi) 设置。 |
| [PROCESS_DPI_AWARENESS](https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/ne-shellscalingapi-process_dpi_awareness)  <br />识别每英寸点数 (dpi) 的感知值。 DPI 感知指示应用程序为 DPI 执行的缩放工作量与系统完成的量。 |

### 2. 方法

|  |
| ------------------------------------------------------------ |
| [ AdjustWindowRectExForDpi](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-adjustwindowrectexfordpi)  <br />根据客户矩形的所需大小和提供的 DPI 计算所需的窗口矩形大小。 |
| [AreDpiAwarenessContextsEqual](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-aredpiawarenesscontextsequal)  <br />确定两个 DPI_AWARENESS_CONTEXT 值是否相同。 |
| [EnableNonClientDpiScaling](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-enablenonclientdpiscaling)  <br />在高 DPI 显示器中，启用指定顶级窗口的非客户区部分的自动显示缩放。 必须在该窗口的初始化期间调用。 |
| [GetAwarenessFromDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getawarenessfromdpiawarenesscontext)  <br />从 DPI_AWARENESS_CONTEXT 检索 DPI_AWARENESS 值。 |
| [GetDialogControlDpiChangeBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdialogcontroldpichangebehavior)  <br />检索对话框中子窗口的每个监视器的 DPI 缩放行为覆盖。 |
| [GetDialogDpiChangeBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdialogdpichangebehavior)  <br />返回之前调用 SetDialogDpiChangeBehavior 时可能已在给定对话框上设置的标志。 |
| [GetDpiForMonitor](https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/nf-shellscalingapi-getdpiformonitor)  <br />查询显示器的每英寸点数 (dpi)。 |
| [GetDpiForSystem](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdpiforsystem)  <br />返回系统 DPI。 |
| [GetDpiForWindow](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdpiforwindow)  <br />返回关联窗口的每英寸点数 (dpi) 值。 |
| [GetDpiFromDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdpifromdpiawarenesscontext)  <br />从给定的 DPI_AWARENESS_CONTEXT 句柄中检索 DPI。 这使您能够确定线程的 DPI，而无需检查在该线程中创建的窗口。 |
| [GetProcessDpiAwareness](https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/nf-shellscalingapi-getprocessdpiawareness)  <br />检索指定进程的每英寸点数 (dpi)。 |
| [GetSystemDpiForProcess](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemdpiforprocess)  <br />检索与给定进程关联的系统 DPI。 这对于避免在具有不同系统 DPI 值的多个系统感知进程之间共享 DPI 敏感信息而引起的兼容性问题很有用。 |
| [GetSystemMetricsForDpi](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetricsfordpi)  <br />考虑到提供的 DPI，检索指定的系统指标或系统配置设置。 |
| [GetThreadDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getthreaddpiawarenesscontext)  <br />获取当前线程的 DPI_AWARENESS_CONTEXT。 |
| [GetThreadDpiHostingBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getthreaddpihostingbehavior)  <br />从当前线程中检索 DPI_HOSTING_BEHAVIOR。 |
| [GetWindowDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowdpiawarenesscontext)  <br />返回与窗口关联的 DPI_AWARENESS_CONTEXT。 |
| [GetWindowDpiHostingBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowdpihostingbehavior)  <br />返回指定窗口的 DPI_HOSTING_BEHAVIOR。 |
| [IsValidDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-isvaliddpiawarenesscontext)  <br />确定指定的 DPI_AWARENESS_CONTEXT 是否有效并且当前系统是否支持。 |
| [LogicalToPhysicalPointForPerMonitorDPI](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-logicaltophysicalpointforpermonitordpi)  <br />将窗口中的点从逻辑坐标转换为物理坐标，而不管调用者对每英寸点数 (dpi) 的感知。 |
| [OpenThemeDataForDpi](https://docs.microsoft.com/en-us/windows/win32/api/uxtheme/nf-uxtheme-openthemedatafordpi)  <br />OpenThemeData 的一种变体，可打开与特定 DPI 关联的主题句柄。 |
| [PhysicalToLogicalPointForPerMonitorDPI](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-physicaltologicalpointforpermonitordpi)  <br />将窗口中的点从物理坐标转换为逻辑坐标，而不管调用者对每英寸点数 (dpi) 的感知。 |
| [SetDialogControlDpiChangeBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setdialogcontroldpichangebehavior)  <br />覆盖对话框中子窗口的默认每监视器 DPI 缩放行为。 |
| [SetDialogDpiChangeBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setdialogdpichangebehavior)  <br />Per-Monitor v2 上下文中的对话框会自动进行 DPI 缩放。 此方法可让您自定义其 DPI 更改行为。 |
| [SetProcessDpiAwareness](https://docs.microsoft.com/en-us/windows/win32/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness)  <br />设置进程默认的 DPI 感知级别。 这等效于使用相应的 DPI_AWARENESS_CONTEXT 值调用 SetProcessDpiAwarenessContext。 |
| [SetProcessDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setprocessdpiawarenesscontext)  <br />将当前进程设置为指定的每英寸点数 (dpi) 感知上下文。 DPI 感知上下文来自 DPI_AWARENESS_CONTEXT 值。 |
| [SetThreadCursorCreationScaling](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setthreadcursorcreationscaling)  <br />设置在此线程上创建的光标所针对的 DPI 比例。 在为显示光标的特定监视器缩放光标时会考虑此值。 |
| [SetThreadDpiAwarenessContext](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setthreaddpiawarenesscontext)  <br />将当前线程的 DPI 感知设置为提供的值。 |
| [SetThreadDpiHostingBehavior](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setthreaddpihostingbehavior)  <br />设置线程的 DPI_HOSTING_BEHAVIOR。 此行为允许在线程中创建的窗口承载具有不同 DPI_AWARENESS_CONTEXT 的子窗口。 |
| [SystemParametersInfoForDpi](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfofordpi)  <br />检索系统范围参数之一的值，同时考虑提供的 DPI 值。 |

### 4. 推荐内容

- [AdjustWindowRectExForDpi function (winuser.h) - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-adjustwindowrectexfordpi)

  根据客户矩形的所需大小和提供的 DPI 计算所需的窗口矩形大小。

- [GetDpiForSystem function (winuser.h) - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdpiforsystem)

  返回系统 DPI。

- [WM_DPICHANGED message (WinUser.h) - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/hidpi/wm-dpichanged)

  当窗口的每英寸有效点数 (dpi) 发生变化时发送。

- [DPI_AWARENESS (windef.h) - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/api/windef/ne-windef-dpi_awareness)

  标识线程、进程或窗口的每英寸点数 (dpi) 设置。

- [DwmExtendFrameIntoClientArea function (dwmapi.h) - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/nf-dwmapi-dwmextendframeintoclientarea)

  将窗口框架扩展到客户区域。

- [Dwmapi.h header - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/)

  

- [DWM Functions - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/dwm/functions)

  本节包含有关桌面窗口管理器 (DWM) 功能的信息。

- [WM_DISPLAYCHANGE message (Winuser.h) - Win32 apps](https://docs.microsoft.com/en-us/windows/win32/gdi/wm-displaychange)

  当显示分辨率发生变化时，WM_DISPLAYCHANGE 消息会发送到所有窗口。