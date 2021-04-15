### A.1.3　准备GLFW

第1章中给出了窗口管理库GLFW的概述。正如第1章中指出的，需要在运行它的机器上编译GLFW。（请注意，虽然GLFW网站包含预编译好的二进制文件下载选项，但它们经常无法正常运行。）编译GLFW需要先下载并安装CMAKE。编译GLFW的步骤相对简单。

（1）下载GLFW源代码<sup class="my_markdown">[GF17]</sup>。

（2）下载并安装CMAKE<sup class="my_markdown">[CM17]</sup>。

（3）运行CMAKE并输入GLFW源代码所在位置和期望的构建目标文件夹。

（4）单击“configure”，如果某些选项以红色高亮，请再次单击“configure”。

（5）单击“generate”。

CMAKE会在之前指定的“构建”文件夹中生成多个文件。该文件夹中的一个文件名为“GLFW.sln”，这是一个Visual Studio项目文件。打开它（当然是使用Visual Studio）并将GLFW编译（构建）为32位应用程序（目前比64位更稳定）。

生成的构建产生了两个我们需要的项目：

+ 由之前的编译步骤生成的glfw3.lib文件；
+ 原始GLFW下载源代码中的“GLFW”文件夹（可在“include”文件夹中找到，它包含我们将使用的两个头文件）。

