### C.1　关于NVIDIANsight

Nsight是NVIDIA的一套包含图形调试器的工具套件，它可以在程序运行时查看OpenGL图形管道的各个阶段，包括着色器。使用Nsight不需要更改或添加任何代码，只要在启用Nsight的情况下运行现有程序。Nsight允许在运行时检查着色器，例如查看着色器的统一变量的当前内容。

Nsight有适用于Windows和Linux / MacOS的版本，包括在微软的Visual Studio（VS）和Eclipse IDE下运行的版本。我们将讨论限制在基于Windows平台、Visual Studio版本的Nsight。（在本书的Java版中，我们描述了如何在Java程序中使用VS版本的Nsight。）

Nsight仅适用于兼容的NVIDIA显卡，而不适用于Intel或AMD显卡。NVIDIA网站<sup class="my_markdown">[NS18]</sup>提供了所支持显卡的完整列表。

