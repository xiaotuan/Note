### 9.3.2　使用OpenGL立方体贴图

构建天空盒的另一种方法是使用OpenGL纹理立方体贴图。OpenGL立方体贴图比我们在上一节中看到的简单方法稍微复杂一点。但是，使用OpenGL立方体贴图有自己的优点，例如减少接缝以及支持环境贴图。

OpenGL纹理立方体贴图类似于稍后将要研究的3D纹理，它们都使用3个纹理坐标访问——通常标记为（s, t, r）——而不是我们目前为止用到的两个。OpenGL纹理立方体贴图的另一个特性是，其中的图像以纹理图像的左上角（而不是通常的左下角）作为纹理坐标（0, 0, 0），这通常是混乱产生的源头。

程序9.1中展示的方法通过读入单个图像来为立方体贴图添加纹理，而程序9.2中展示的loadCubeMap()函数则读入6个单独的立方体面图像文件。正如我们在第5章中所学的，有许多方法可以读取纹理图像，我们选择使用SOIL2库。在这里，SOIL2用于实例化和加载OpenGL立方体贴图也非常方便。我们先找到需要读入的文件，然后调用SOIL_load_OGL_cubemap()，其参数包括6个图像文件和一些其他参数，类似于我们在第5章中看到的SOIL_load_OGL_texture()。在使用OpenGL立方体贴图时，无须垂直翻转纹理，OpenGL会自动进行处理，注意，loadCubeMap()函数放在“Utils.cpp”文件中。

init()函数现在包含一个函数调用以启用GL_TEXTURE_CUBE_MAP_SEAMLESS，它告诉OpenGL尝试混合立方体相邻的边以减少或消除接缝。在display()中，立方体的顶点像以前一样沿管线向下发送，但这次不需要发送立方体的纹理坐标。我们将会看到，OpenGL纹理立方体贴图通常使用立方体的顶点位置作为其纹理坐标。之后禁用深度测试并绘制立方体。然后为场景的其余部分重新启用深度测试。

完成后的OpenGL纹理立方体贴图使用了int类型的标识符进行引用。与阴影贴图时一样，通过将纹理包裹模式设置为“夹紧到边缘”，可以减少沿边框的伪影。在这种情况下，它还可以帮助进一步缩小接缝。请注意，这里需要为3个纹理坐标s、t和r都设置纹理包裹模式。

在片段着色器中使用名为samplerCube的特殊类型的采样器访问纹理。在纹理立方体贴图中，从采样器返回的值是沿着方向向量(s, t, r)从原点“看到”的纹素。因此，我们通常可以简单地使用传入的插值顶点位置作为纹理坐标。在顶点着色器中，我们将立方体顶点位置分配到输出纹理坐标属性中，以便在它们到达片段着色器时进行插值。另外需要注意，在顶点着色器中，我们将传入的视图矩阵转换为3×3，然后再转换回4×4。这个“技巧”有效地移除了平移分量，同时保留了旋转（回想一下，平移值在转换矩阵的第四列中）。这样，就将立方体贴图固定在了摄像机位置，同时仍允许合成相机“环顾四周”。

程序9.2　OpenGL立方体贴图天空盒

```c
C++/OpenGL application
. . .
int brickTexture, skyboxTexture;
int renderingProgram, renderingProgramCubeMap;
. . .
void init(GLFWwindow* window) {
   renderingProgram = Utils::createShaderProgram("vertShader.glsl", "fragShader.glsl");
   renderingProgramCubeMap = Utils::createShaderProgram("vertCShader.glsl", "fragCShader.glsl");
   setupVertices();
   brickTexture = Utils::loadTexture("brick1.jpg");       // 场景中的环面
   skyboxTexture = Utils::loadCubeMap("cubeMap");         // 包含天空盒纹理的文件夹
   glEnable(GL_TEXTURE_CUBE_MAP_SEAMLESS); }
void display(GLFWwindow* window, double currentTime) {
   // 清除颜色缓冲区和深度缓冲区，并像之前一样创建投影视图矩阵和摄像机视图矩阵
   . . .
   // 准备首先绘制天空盒—注意，现在它的渲染程序不同了
   glUseProgram(renderingProgramCubeMap);
   // 将P、V矩阵传入相应的统一变量
   . . .
   // 初始化立方体的顶点缓冲区（这里不再需要纹理坐标缓冲区）
   glBindBuffer(GL_ARRAY_BUFFER, vbo[0]);
   glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
   glEnableVertexAttribArray(0);
   // 激活立方体贴图纹理
   glActiveTexture(GL_TEXTURE0);
   glBindTexture(GL_TEXTURE_CUBE_MAP, skyboxTexture);
   // 禁用深度测试，之后绘制立方体贴图
   glEnable(GL_CULL_FACE);
   glFrontFace(GL_CCW);
   glDisable(GL_DEPTH_TEST);
   glDrawArrays(GL_TRIANGLES, 0, 36);
   glEnable(GL_DEPTH_TEST);
   // 绘制场景其余内容
   . . .
}
GLuint Utils::loadCubeMap(const char *mapDir) {
   GLuint textureRef;
   // 假设6个纹理图像文件xp、xn、yp、yn、zp、zn都是JPG格式图像
   string xp = mapDir; xp = xp + "/xp.jpg";
   string xn = mapDir; xn = xn + "/xn.jpg";
   string yp = mapDir; yp = yp + "/yp.jpg";
   string yn = mapDir; yn = yn + "/yn.jpg";
   string zp = mapDir; zp = zp + "/zp.jpg";
   string zn = mapDir; zn = zn + "/zn.jpg";
   textureRef = SOIL_load_OGL_cubemap(xp.c_str(), xn.c_str(), yp.c_str(), yn.c_str(),       zp.c_str(), zn.c_str(), SOIL_LOAD_AUTO, SOIL_CREATE_NEW_ID, SOIL_FLAG_MIPMAPS);
   if (textureRef == 0) cout << "didnt find cube map image file" << endl;
   glBindTexture(GL_TEXTURE_CUBE_MAP, textureRef);
   // 减少接缝
   glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
   glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
   glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE);
   return textureRef;
}
顶点着色器
#version 430
layout (location = 0) in vec3 position;
out vec3 tc;
uniform mat4 v_matrix;
uniform mat4 proj_matrix;
layout (binding = 0) uniform samplerCube samp;
void main(void)
{
   tc = position;                              // 纹理坐标就是顶点坐标
   mat4 vrot_matrix = mat4(mat3(v_matrix));    // 从视图矩阵中删除平移
   gl_Position = proj_matrix * vrot_matrix * vec4(position, 1.0);
}
片段着色器
#version 430
in vec3 tc;
out vec4 fragColor;
uniform mat4 v_matrix;
uniform mat4 proj_matrix;
layout (binding = 0) uniform samplerCube samp;
void main(void)
{ fragColor = texture(samp,tc);
}

```

