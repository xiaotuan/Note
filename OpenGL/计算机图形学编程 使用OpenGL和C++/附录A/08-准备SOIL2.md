### A.1.6　准备SOIL2

第1章给出了图像加载库SOIL2的概述。安装SOIL2 <sup class="my_markdown">[SO17]</sup>需要使用一个名为“premake”的工具<sup>[PM17]</sup>。虽然该过程涉及多个步骤，但它们相对简单。

（1）下载并解压缩“premake”，其中唯一的文件是“premake4.exe”。

（2）下载SOIL2（使用左侧面板底部的“下载”链接），然后解压缩。

（3）将“premake4.exe”文件复制到soil2文件夹中。

（4）打开命令行窗口，导航到soil2文件夹，然后输入：

```c
premake4 vs2012
```

它应该显示随后创建的文件数量。

（5）在soil2文件夹中，打开“make”文件夹，然后打开“windows”文件夹。双击“SOIL2.sln”。

（6）如果Visual Studio提示升级库，请单击“确定”按钮。

（7）在右侧面板中，右键单击“soil2-static-lib”并选择“构建（build）”。

（8）关闭Visual Studio并导航回soil2文件夹。你应该注意到一些新项目。

