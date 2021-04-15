### 5.12　材质——更多OpenGL细节

我们在本书中使用的SOIL2纹理图像加载库具有使用起来相对简单和直观的优点。但是，在学习OpenGL时，使用SOIL2会产生一项我们不想要的后果，即用户会接触不到一些有用的重要OpenGL细节。在本节中，我们将描述程序员在没有纹理加载库（如SOIL2）的情况下加载和使用纹理时需要了解的一些细节。

可以使用C++和OpenGL函数直接将纹理图像文件数据加载到OpenGL中。虽然它有点复杂，但并不少见。一般步骤如下。

（1）使用C++工具读取图像文件。

（2）生成OpenGL纹理对象。

（3）将图像文件数据复制到纹理对象中。

我们不会详细描述第一步——有太多方法了。在opengl-tutorials.org（具体的教程页面为<sup class="my_markdown">[OT18]</sup>）中很好地描述了一种方法，并使用C++函数fopen()和fread()将数据从.bmp图像文件读入unsigned char类型的数组中。

步骤2和步骤3更通用，主要涉及OpenGL调用。在第2步中，我们使用OpenGL的glGenTextures()命令创建一个或多个纹理对象。例如，生成单个OpenGL纹理对象（使用整型引用ID）可以按如下方式完成：

```c
GLuint textureID;         // 或者GLuint类型的数组，如果需要创建多于一个纹理对象
glGenTextures(1, &textureID);
```

在步骤3中，我们将步骤1中的图像数据关联到步骤2中创建的纹理对象。这是使用OpenGL的glTexImage2D()命令完成的。下面的示例将图像数据从步骤1中描述的unsigned char数组（此处表示为“data”）加载到步骤2中创建的纹理对象中：

```c
glBindTexture(GL_TEXTURE_2D, textureID)
glTexImage2D(GL_TEXTURE_2D, 0,GL_RGB, width, height, 0, GL_BGR,
                                                      GL_UNSIGNED_BYTE, data);
```

此时，本章前面介绍的用于设置多级渐远纹理贴图等的各种glTexParameteri()调用也可以应用于纹理对象。我们现在也以与本章所述相同的方式使用整型引用（textureID）。

