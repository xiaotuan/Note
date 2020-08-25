示例：

```xml
<vector
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportHeight="300.0"
    android:viewportWidth="300.0">
    
    <path
       android:name="edge"
       android:pathData="h300,0v0,300h-300,0v0,-300"
       android:strokeColor="@android:color/holo_red_dark"
       android:strokeWidth="1" />
       
   <path
       android:name="oval"
       android:fillColor="#8F0505"
       android:pathData="
       M0,75
       a75,75 0 1,1 150,0
       a75,75 0 1,1 -150,0"
       android:strokeColor="#00000000" />
</vector>
```

上面示例中 `vector` 使用了四个属性：

1. `width` 和 `height`：当使用这个矢量图的 View 的宽高是 `wrap_content` 的时候这两个属性才有效。
2. `viewportWidth` 和 `viewportheight`：决定画布的宽高，是定义的一个虚拟空间，方便编辑 pathData 属性，如果 pathData 中的点超出了这个虚拟空间，超出的部分将不会展现给用户；虚拟空间的原点仍然还是在左上角（R 点就是原点）。

`path` 标签是 `vector` 标签的子标签，它使用了一下属性：

| 属性 | 说明 |
| :-: | :- |
| android:name | 类似 View 的 id 属性，方便 path 被引用 |
| android:fillColor | 填充 path 的颜色，如果没有定义则不填充 path |
| android:strokeColor | path 边框颜色，如果没有定义则不显示边框 |
| android:strokeWidth | path 边框的粗细尺寸 |
| android:pathData | path 指令，决定 path 的移动和绘制逻辑，这个是最主要的属性 |

> 更多 path 属性请参考 [链接](https://developer.android.google.cn/reference/android/graphics/drawable/VectorDrawable.html)

下面是一些 `pathData` 基本的指令：

| 指令 | 说明 |
| :-: | :- |
| Mx,y | 移动到点 (x,y) |
| Lx,y | 直线连接到点（x,y），简化命令 H(x) 水平连接和 V(y) 垂直连接 |
| Qx1,y1 x2,y2 | 二阶贝塞尔曲线，控制点 （x1, y1），终点 （x2, y2） |
| Cx1,y1 x2,y2 x3,y3 | 三街贝塞尔曲线，控制点（x1, y1） （x2, y2），终点（x3, y3） |
| Tx y | 平滑的二阶贝塞尔曲线，参数只有一个点（x, y），这个点是结束点，控制点是前一个二阶贝塞尔曲线的控制点相对于前一个贝塞尔曲线的结束点的镜像点 |
| Sx2,y2 x,y | 平滑的三阶贝塞尔曲线，参数为（x2, y2 x,y），x2,y2 为第二个控制点，x,y 为绘制终点，那么第一个控制点则是前一个三阶曲线的第二个控制点相对于前一个三阶曲线终点的镜像点 |
| Arx,ry x-axis-rotation large-arc-flag sweep-flag x y | 绘制圆弧，（rx, ry）椭圆半径，x-axis-rotation x 轴旋转角度，large-arc-flag 为 0 时表示取小弧度，1 时取大弧度（取舍的时候，是要长还是短的），sweep-flag 0 取逆时针方向，1 取顺时针方向，（x,y）终点位置 |
| z | 闭合路径 |

> 更详细全面的 `path` 指令请参阅[链接](https://www.w3.org/TR/SVG/paths.html#PathDataEllipticalArcCommands)

示例：

```xml
<vector
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportHeight="300.0"
    android:viewportWidth="300.0">
    <clip-path android:name="clip_one" android:pathData="
    M0 20a20 20 0 0 1 20 -20
    l260 0a20 20 0 0 1 20 20
    l0 260a20 20 0 0 1 -20 20
    l-260 0a20 20 0 0 1 -20 -20
    l0 -260"/>
    <path
        android:name="edge"
        android:pathData="h300v300h-300v-300
        M150 0 v300
        M0 150 h300"
        android:fillColor="@android:color/holo_green_light"
        android:strokeColor="@android:color/holo_red_dark"
        android:strokeWidth="1" />
    <group>
        <clip-path android:name="clip_two" android:pathData="M0 150h300v150h-300v-150"/>
        <path
            android:name="oval"
            android:strokeLineCap="round"
            android:strokeLineJoin="round"
            android:pathData="M20 20 l260,260M280 20 l-260,260h100"
            android:strokeColor="#000000"
            android:strokeWidth="15"/>
    </group>
</vector>
```
`group` 标签定义变换的细节，`clip-path` 定义裁剪区域。

`group` 标签有以下属性：

+ android:name: group 的名字；
+ android:rotation: group 的旋转角度，默认 0；
+ android:pivotX：scale 和 rotation 变换中心点的 X 坐标，默认 0;
+ android:pivotY: scale 和 rotation 变换中心点的 Y 坐标，默认 0；
+ android:scaleX：X 轴方向的缩放，默认 1；
+ android:scaleY：Y轴方向的缩放，默认 1；
+ android:translateX：X 轴方向的移动距离，默认 0；
+ android:translateY：Y 轴方向的移动距离，默认 0；

`clip-path` 标签有以下属性：

+ android:name：clip-path 的名字；
+ android:pathData：clip-path 的路径。

