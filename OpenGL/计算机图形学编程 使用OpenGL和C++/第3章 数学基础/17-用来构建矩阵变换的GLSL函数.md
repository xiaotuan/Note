### 3.10　用来构建矩阵变换的GLSL函数

虽然GLM包含了许多预定义的3D变换函数，本章也已经涵盖了其中如平移、旋转和缩放，但GLSL只包含了基础的矩阵运算，如加法、合并等。因此，有时我们需要自己为GLSL写一些实用函数来构建3D变换矩阵，以在着色器中进行特定3D运算。用于存储这些矩阵的GLSL数据类型是mat4。

GLSL中用于初始化mat4矩阵的语法以列为单位读入值。前4个参数会放入第一列，接下来4个参数放入下一列，直到第四列，如下所示：

```c
mat4 translationMatrix = 
   mat4(1.0, 0.0, 0.0, 0.0, // 注意，这是最左列，而非第一行
        0.0, 1.0, 0.0, 0.0, 
        0.0, 0.0, 1.0, 0.0, 
        tx, ty, tz, 1.0 );

```

构建如图3.3所示的平移矩阵。

程序3.1中包含了5个用于构建4×4平移、旋转和缩放矩阵的GLSL函数，每个函数对应于本章之前给出的一个公式。我们稍后在书中将会用到这些函数。

程序3.1　在GLSL中构建变换矩阵

```c
// 构建并返回平移矩阵
mat4 buildTranslate(float x, float y, float z)
{ mat4 trans = mat4(1.0, 0.0, 0.0, 0.0, 
                    0.0, 1.0, 0.0, 0.0, 
                    0.0, 0.0, 1.0, 0.0, 
                    x, y, z, 1.0 ); 
  return trans;
} 
// 构建并返回绕X轴的旋转矩阵
mat4 buildRotateX(float rad)
{ mat4 xrot = mat4(1.0, 0.0, 0.0, 0.0, 
                   0.0, cos(rad), -sin(rad), 0.0, 
                   0.0, sin(rad), cos(rad), 0.0, 
                   0.0, 0.0, 0.0, 1.0 ); 
  return xrot;
}
// 构建并返回绕Y轴的旋转矩阵
mat4 buildRotateY(float rad)
{ mat4 yrot = mat4(cos(rad), 0.0, sin(rad), 0.0, 
                   0.0, 1.0, 0.0, 0.0, 
                   -sin(rad), 0.0, cos(rad), 0.0, 
                   0.0, 0.0, 0.0, 1.0 ); 
  return yrot;
}
// 构建并返回绕Z轴的旋转矩阵
mat4 buildRotateZ(float rad)
{ mat4 zrot = mat4(cos(rad), -sin(rad), 0.0, 0.0, 
                   sin(rad), cos(rad), 0.0, 0.0, 
                   0.0, 0.0, 1.0, 0.0, 
                   0.0, 0.0, 0.0, 1.0 ); 
  return zrot;
}
// 构建并返回缩放矩阵
mat4 buildScale(float x, float y, float z)
{ mat4 scale = mat4(x, 0.0, 0.0, 0.0, 
                    0.0, y, 0.0, 0.0, 
                    0.0, 0.0, z, 0.0, 
                    0.0, 0.0, 0.0, 1.0 ); 
  return scale;
}

```

