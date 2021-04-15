### B.2.2　修改GLSL代码

由于Mac中使用稍早版本的OpenGL（V4.1），因此需要对我们的GLSL着色器代码（以及一些相关的C++/OpenGL代码）中的不同位置进行一些修改：

+ 必须修改着色器中指定的版本号。假设你的Mac支持4.1版，则在每个着色器的顶部找到如下代码： `#version 430`必须将其修改为： `#version 410`
+ 4.1版本的OpenGl不支持纹理采样器变量的布局绑定限定符。这会影响从第5章开始的内容。你需要删除布局绑定限定符，并将其替换为另一个完成相同操作的命令。具体来说，在着色器中查找具有以下格式的行： `layout (binding=0) uniform sampler2D samp;`绑定子句中指定的纹理单元号可能不同（此处为“0”），并且采样器变量的名称可能不同（此处为“samp”）。在任何情况下，你都需要删除布局子句，将它简化为： `uniform sampler2D samp;`然后，你需要在C++程序中为启用的每个纹理添加如下代码： `glUniformli(glGetUniformLocation(renderingProgram,“samp”), 0);`这些代码需要紧跟在C++ display()函数中的glBindTexture()命令之后，其中“samp”是统一采样器变量的名称，“0”是先前删除的绑定命令中指定的纹理单元。

