### 2.2　检测OpenGL和GLSL错误

编译和运行GLSL代码与普通编码的过程不同，GLSL编译发生在C++运行时。另外一个复杂的地方是GLSL代码并没有运行在CPU中（它运行在GPU上），因此操作系统不总是能够捕获OpenGL运行时的错误。以上这些使得调试变得很困难，因为常常很难检测着色器是否失败，以及为什么失败。

程序2.3展示了用于捕获和显示GLSL错误的模块。其中GLSL函数glGetShaderiv()和glGetProgramiv()用于提供有关编译过的GLSL着色器和程序的信息。还有之前程序2.2中的createShaderProgram()函数，不过加入了错误检测的调用。

程序2.3包含如下3个实用程序。

+ checkOpenGLError：检查OpenGL错误标志，即是否发生OpenGL错误。
+ printShaderLog：当GLSL编译失败时，显示OpenGL日志内容。
+ printProgramLog：当GLSL链接失败时，显示OpenGL日志内容。

checkOpenGLError()既用于检测GLSL编译错误，又用于检测OpenGL运行时的错误，因此我们强烈建议在整个C++/OpenGL应用程序开发过程中使用它。例如，在之前的程序2.2中，对于glCompileShader()和glLinkProgram()的调用很容易用程序2.3的代码进行加强，来确认所有的拼写错误和编译错误都能被捕获到，同时报告其原因。

用这些工具很重要的另一个原因是，GLSL错误并不会导致C++程序崩溃。因此，除非程序员通过步进找到错误发生的点，否则调试会非常困难。

程序2.3　用以捕获GLSL错误的模块

```c
void printShaderLog(GLuint shader) { 
   int len = 0; 
   int chWrittn = 0; 
   char *log; 
   glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &len); 
   if (len > 0) { 
        log = (char *)malloc(len); 
        glGetShaderInfoLog(shader, len, &chWrittn, log); 
        cout << "Shader Info Log: " << log << endl; 
        free(log);
} }
void printProgramLog(int prog) { 
   int len = 0; 
   int chWrittn = 0; 
   char *log; 
   glGetProgramiv(prog, GL_INFO_LOG_LENGTH, &len); 
   if (len > 0) { 
        log = (char *)malloc(len); 
        glGetProgramInfoLog(prog, len, &chWrittn, log); 
        cout << "Program Info Log: " << log << endl; 
        free(log);
} }
bool checkOpenGLError() { 
   bool foundError = false; 
   int glErr = glGetError(); 
   while (glErr != GL_NO_ERROR) { 
      cout << "glError: " << glErr << endl; 
      foundError = true; 
      glErr = glGetError(); 
   } 
   return foundError;
}

```

检测OpengGL错误的示例如下：

```c
GLuint createShaderProgram() { 
  GLint vertCompiled; 
  GLint fragCompiled; 
  GLint linked; 
  . . . 
  // 捕获编译着色器时的错误
  glCompileShader(vShader); 
  checkOpenGLError(); 
  glGetShaderiv(vShader, GL_COMPILE_STATUS, &vertCompiled); 
  if (vertCompiled != 1) { 
       cout << "vertex compilation failed" << endl; 
       printShaderLog(vShader); 
  }
  glCompileShader(fShader); 
  checkOpenGLError(); 
  glGetShaderiv(fShader, GL_COMPILE_STATUS, &fragCompiled); 
  if (fragCompiled != 1) { 
       cout << "fragment compilation failed" << endl; 
       printShaderLog(fShader); 
  }
  // 捕获链接着色器时的错误
  glAttachShader(vfProgram, vShader); 
  glAttachShader(vfProgram, fShader); 
  glLinkProgram(vfProgram); 
  checkOpenGLError(); 
  glGetProgramiv(vfProgram, GL_LINK_STATUS, &linked); 
  if (linked != 1) { 
       cout << "linking failed" << endl; 
       printProgramLog(vfProgram); 
  } 
  return vfProgram;
}

```

还有一些其他用于推测着色器代码运行时错误成因的技巧。着色器运行时错误的常见结果是输出屏幕上完全空白，根本没有输出。即使是着色器中的一个小拼写错误也可能导致这种结果，这样就很难断定是哪个管线阶段发生了错误。没有任何输出的情况下，找到错误的成因就像大海捞针。

其中一种有用的技巧就是暂时将片段着色器换成程序2.2中的片段着色器。回忆程序2.2中，片段着色器仅输出一个特定颜色——例如蓝色。如果后来的输出中的几何形状正确（但是全是蓝色），那么顶点着色器应该是正确的，错误应该发生在片段着色器。如果输出的仍然是空白屏幕，那错误很可能发生在管线的更早期，譬如顶点着色器。

在附录C中，我们展示了另一种有用的调试工具，叫作Nsight，适用于特定型号Nvidia显卡的机器。

