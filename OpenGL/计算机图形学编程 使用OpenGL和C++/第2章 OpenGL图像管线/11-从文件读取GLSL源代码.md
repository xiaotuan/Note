### 2.3　从文件读取GLSL源代码

到此为止，GLSL着色器代码已经内联存储在字符串中了。当程序变得更复杂时，这么做就不实际了。我们应当将我们的着色器代码存在文件中并读入它们。

读入文本文件是基础C++技能，我们在此就不赘述了。但是，为实用起见，用于读取着色器的代码readShaderSource()在程序2.4中提供。它读取着色器文本文件并返回一个字符串数组，其中每个字符串是文件中的一行文本。然后根据读入的行数确定该数组的大小。注意，createShaderProgram()在这里替换了程序2.2中的版本。在本例中，顶点着色器和片段着色器代码现在分别放在文本文件“vertShader.glsl”和“fragShader.glsl”中。

程序2.4　从文件读取GLSL源文件

```c
(....#includes与之前相同, main(), display(), init()也与之前相同，同时加入如下代码...)
#include <string>
#include <iostream>
#include <fstream>
. . .
string readShaderSource(const char *filePath) { 
    string content; 
    ifstream fileStream(filePath, ios::in); 
    string line = ""; 
    while (!fileStream.eof()) { 
        getline(fileStream, line); 
        content.append(line + "\n"); 
    } 
    fileStream.close(); 
    return content;
  }
  GLuint createShaderProgram() { 
    (...与之前相同，同时加入如下代码...)
    string vertShaderStr = readShaderSource("vertShader.glsl"); 
    string fragShaderStr = readShaderSource("fragShader.glsl"); 
    const char *vertShaderSrc = vertShaderStr.c_str(); 
    const char *fragShaderSrc = fragShaderStr.c_str(); 
    glShaderSource(vShader, 1, &vertShaderSrc, NULL); 
    glShaderSource(fShader, 1, &fragShaderSrc, NULL); 
    (…构建如前的渲染程序)
}

```

