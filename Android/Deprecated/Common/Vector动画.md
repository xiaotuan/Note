对于图像数据来说，可以分为矢量和栅格数据，矢量数据是记录绘制图形的方式，栅格数据是以像素点为组织形式拼接成一个图形。从这也能看出矢量和栅格数据的各个优缺点：

1. 矢量数据：占用内存小，图像清晰度不受影响。但是绘制图形效率较低，通过CPU绘制。
2. 栅格数据：占用内存大，图像清晰度会受图像拉伸而改变。但是通过GPU绘制，效率较高。

对于Android系统，在5.0版本时Google推出了Vector来使用矢量数据。下面简单介绍一下在Android中Vector的用法和注意事项。

# 1. Vecotr简介

## 1.1 SVG与Vector差异

SVG -- 前端中使用，是一套语法规范；

![img](https:////upload-images.jianshu.io/upload_images/1819426-ac629ba2ccac225f.png?imageMogr2/auto-orient/strip|imageView2/2/w/604/format/webp)

SVG实例

vector -- 在Android中使用，vector只实现了SVG语法的path标签，为了提高解析效率。

## 1.2 Vector常用语法

M = moveto(M X,Y)：将画笔移动到指定的坐标位置
 L= lineto(L X, Y)：画直线到指定的坐标位置
 Z = closepath()：关闭路径
 H = horizontal lineto(H X)： 画水平线到指定的X坐标位置
 V = vertical lineto(V Y)：画垂直线到指定的Y坐标位置

![img](https:////upload-images.jianshu.io/upload_images/1819426-699d314855a5540f.png?imageMogr2/auto-orient/strip|imageView2/2/w/635/format/webp)

实例——画一个矩形

## 1.3 常用工具

[SVG编辑器](https://link.jianshu.com?t=http://editor.method.ac/)

![img](https:////upload-images.jianshu.io/upload_images/1819426-ae6e23e8a2962bff.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)



[SVG转换成vector](https://link.jianshu.com?t=http://inloop.github.io/svg2android/)

![img](https:////upload-images.jianshu.io/upload_images/1819426-8ad6a4cf71ecd7cf.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)



[阿里巴巴矢量图标库](https://link.jianshu.com?t=http://www.iconfont.cn/)

![img](https:////upload-images.jianshu.io/upload_images/1819426-b13fa08ead07fef5.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)



## 1.4 PNG、SVG、Vector效果对比

svg、Vector的优点：体积小，支持按比例缩放



![img](https:////upload-images.jianshu.io/upload_images/1819426-23182a0741f1a4b6.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

PNG、SVG、Vector效果对比

# 2. Vector使用

**在下面的介绍使用方法时，是基于sdk6.0的，对于兼容性问题在2.4章节由所介绍。**

## 2.1 添加Vector

在AndroidStudio中，有两种方式直接添加转换成Vector
 右键drawable文件夹，选择new，选择Vector assert，



![img](https:////upload-images.jianshu.io/upload_images/1819426-cca110b8cbbc90d8.png?imageMogr2/auto-orient/strip|imageView2/2/w/713/format/webp)



其中一种是通过使用系统库的icon图标转换成Vector，一种是导入本地的SVG文件转换成Vector



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:width="24dp"
        android:height="24dp"
        android:viewportWidth="24.0"
        android:viewportHeight="24.0">
    <path
        android:fillColor="#FF000000"
        android:pathData="M6,18c0,0.55 0.45,1 1,1h1v3.5c0,0.83 0.67,1.5 1.5,1.5s1.5,-0.67 1.5,-1.5L11,19h2v3.5c0,0.83 0.67,1.5 1.5,1.5s1.5,-0.67 1.5,-1.5L16,19h1c0.55,0 1,-0.45 1,-1L18,8L6,8v10zM3.5,8C2.67,8 2,8.67 2,9.5v7c0,0.83 0.67,1.5 1.5,1.5S5,17.33 5,16.5v-7C5,8.67 4.33,8 3.5,8zM20.5,8c-0.83,0 -1.5,0.67 -1.5,1.5v7c0,0.83 0.67,1.5 1.5,1.5s1.5,-0.67 1.5,-1.5v-7c0,-0.83 -0.67,-1.5 -1.5,-1.5zM15.53,2.16l1.3,-1.3c0.2,-0.2 0.2,-0.51 0,-0.71 -0.2,-0.2 -0.51,-0.2 -0.71,0l-1.48,1.48C13.85,1.23 12.95,1 12,1c-0.96,0 -1.86,0.23 -2.66,0.63L7.85,0.15c-0.2,-0.2 -0.51,-0.2 -0.71,0 -0.2,0.2 -0.2,0.51 0,0.71l1.31,1.31C6.97,3.26 6,5.01 6,7h12c0,-1.99 -0.97,-3.75 -2.47,-4.84zM10,5L9,5L9,4h1v1zM15,5h-1L14,4h1v1z"/>
</vector>
```

除了自动转换，还可以手动编写一个Vector。在drawable文件夹中新建一个xml文件，然后使用vector和内部的path进行绘制。其中pathData的内容是一个矩形的路径。



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:width="24dp"
        android:height="24dp"
        android:viewportWidth="100.0"
        android:viewportHeight="100.0">
    <path
        android:name="square"
        android:fillColor="#FF000000"
        android:pathData="M0,0 L100,0 L100,100 L0, 100 z"/>
</vector>
```

![img](https:////upload-images.jianshu.io/upload_images/1819426-e4818d8ea0341c9f.png?imageMogr2/auto-orient/strip|imageView2/2/w/124/format/webp)

## 2.2 使用静态Vector

添加完Vector文件之后，在layout布局文件添加一个ImageView来展示这个Vector,使用的是app:srcCompat来引用资源文件。



```xml
<ImageView
            android:layout_width="100dp"
            android:layout_height="100dp"
            android:src="@drawable/ic_android_black_24dp" />
```

![img](https:////upload-images.jianshu.io/upload_images/1819426-5128530a33ff4ba8.png?imageMogr2/auto-orient/strip|imageView2/2/w/362/format/webp)

我们尝试在Button上设置上面的Vector资源，会发现无法设置。



```xml
<Button
            android:layout_width="100dp"
            android:layout_height="100dp"
            android:src="@drawable/ic_android_black_24dp"/>
```

![img](https:////upload-images.jianshu.io/upload_images/1819426-a15d64bb2ddf8884.png?imageMogr2/auto-orient/strip|imageView2/2/w/362/format/webp)



可以看到，在Button上用Vector是不生效的，原因是Google工程师对Vector的兼容性做出的妥协，因为Button是带有状态的控件，无法直接使用Vector。解决的办法就是使用selector插值器来配合使用。



```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">

    <item android:drawable="@drawable/ic_android_black_24dp" android:state_pressed="true"/>
</selector>
```

然后在Button控件中使用background属性



```xml
        <Button
            android:layout_width="100dp"
            android:layout_height="100dp"
            android:background="@drawable/bg_btn"/>
```

![img](https:////upload-images.jianshu.io/upload_images/1819426-f3a5d162968cd3da.gif?imageMogr2/auto-orient/strip|imageView2/2/w/384/format/webp)

如果想要将图形增大，无需修改pathData属性，只修改android:viewportWidth和android:viewportHeight属性就可以了。

## 2.3 使用动态Vector

之前提到过Vector与其他栅格图像的区别，内存小、不失真，但这些并不是使用Vector的理由，其实使用Vector就是为了能够方便动态地添加动画效果。下面就以几个典型的例子来分析如何添加动态地Vector。

### 2.3.1 直线运动动画

![img](https:////upload-images.jianshu.io/upload_images/1819426-ac3a38e6df2f2e50.gif?imageMogr2/auto-orient/strip|imageView2/2/w/324/format/webp)

1.gif



实现如图所示的动画效果。

首先在drawable文件夹下创建图片的Vector资源文件：



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportHeight="24.0"
    android:viewportWidth="24.0">
    <group android:name="left">
        <path
            android:fillColor="#FF000000"
            android:pathData="M9.01,14L2,14v2h7.01v3L13,15l-3.99,-4v3z" />
    </group>
    <group android:name="right">
        <path
            android:fillColor="#FF000000"
            android:pathData="M14.99,13v-3L22,10L22,8h-7.01L14.99,5L11,9l3.99,4z" />
    </group>
</vector>
```

此处由于是需要两个箭头的同时动画，这就需要为两个箭头添加不同的属性动画，所以，用group的方式进行组织，并且添加了name字段来标明。

添加完代码，可以看到是一个静态的双箭头图片。



![img](https:////upload-images.jianshu.io/upload_images/1819426-14b321dfd014ed2c.png?imageMogr2/auto-orient/strip|imageView2/2/w/203/format/webp)

arrow

接下来，创建两个属性动画文件，分别对应向左和向右的动画效果。



```xml
<?xml version="1.0" encoding="utf-8"?>
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="1000"
    android:propertyName="translateX"
    android:interpolator="@android:interpolator/overshoot"
    android:repeatCount="infinite"
    android:repeatMode="reverse"
    android:valueFrom="0"
    android:valueTo="10"
    android:valueType="floatType">
</objectAnimator>
```

简单说明一下，android:propertyName="translateX"意味着在X轴方向上运动， android:interpolator被用来修饰动画效果，定义动画的变化率，可以使存在的动画效果accelerated(加速)，decelerated(减速),repeated(重复),bounced(弹跳)等。"@android:interpolator/overshoot"指的是向前甩一定值后再回到原来位置。android:valueFrom="0"和android:valueTo="10"表示着效果的变化范围，对应来说是x轴上的移动位置变化，这段代码展示的是左面的箭头向右移动，相对应的右面的箭头向左移动就是android:valueFrom="0"和android:valueTo="-10"。android:valueType="floatType"指明了是运行距离的floatType类型。

然后在drawable文件夹下创建Vector动画的“粘合剂”——</animated-vector>：



```xml
<?xml version="1.0" encoding="utf-8"?>
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/ic_arrow_back_black_24dp">
    <target
        android:animation="@animator/anim_left"
        android:name="left"/>
    <target
        android:animation="@animator/anim_right"
        android:name="right"/>
</animated-vector>
```

此处首先指明了 android:drawable代表图片的Vector的资源，然后在target标签下对每一个动画进行绑定，其中的name是之前的Vector图片资源文件里面的group的name属性。

最后，在粘合剂绑定完成后，用ImageView来承载这个粘合剂：



```xml
        <ImageView
            android:layout_width="100dp"
            android:layout_height="100dp"
            app:srcCompat="@drawable/arrow_anim"
            android:onClick="anim" />
```

在Activity中实现这个点击事件，让动画启动：



```java
    public void anim(View view) {
        ImageView imageView = (ImageView) view;
        Drawable drawable = imageView.getDrawable();
        if (drawable instanceof Animatable) {
            ((Animatable) drawable).start();
        }
    }
```

这样就能显示出我们想要的动画效果了。

### 2.3.2 颜色渐变动画

![img](https:////upload-images.jianshu.io/upload_images/1819426-4032d54a6df3b986.gif?imageMogr2/auto-orient/strip|imageView2/2/w/346/format/webp)



接下来介绍一下颜色渐变动画的实现。

与上面的流程类似，首先创建Vector图片资源文件：



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:width="24dp"
        android:height="24dp"
        android:viewportWidth="100.0"
        android:viewportHeight="100.0">
    <path
        android:name="square"
        android:fillColor="#FF000000"
        android:pathData="M0,0 L100,0 L100,100 L0, 100 z"/>
</vector>
```

是一个静态的矩形



![img](https:////upload-images.jianshu.io/upload_images/1819426-aeba21eec4336226.png?imageMogr2/auto-orient/strip|imageView2/2/w/160/format/webp)

矩形

然后在animator文件下创建对应的属性动画文件anim_square.xml：



```xml
<?xml version="1.0" encoding="utf-8"?>
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="5000"
    android:interpolator="@android:interpolator/overshoot"
    android:propertyName="fillColor"
    android:valueFrom="@android:color/holo_red_dark"
    android:valueTo="@android:color/darker_gray"
    android:valueType="intType">
</objectAnimator>
```

此处android:propertyName="fillColor"指的是动画效果是填充颜色，   android:valueFrom="@android:color/holo_red_dark"和android:valueTo="@android:color/darker_gray"指的是颜色的变化范围，并且值的类型是int。

然后是创建粘合剂square_anim.xml:



```xml
<?xml version="1.0" encoding="utf-8"?>
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/square">
    <target
        android:animation="@animator/anim_square"
        android:name="square"/>
</animated-vector>
```

最后在ImageView上承载即可，就不多介绍了。

### 2.3.3 轨迹动画

主要介绍两种实现，一种是通过android:propertyName="trimPathStart"，取值从0到1，表示路径从哪里开始绘制。0~trimPathStart区间的路径不会被绘制出来。一种是通过android:propertyName="pathData"定义路径的数据，路径由多条命令组成，格式与SVG标准的path data的d属性完全相同，路径命令的参数定义在viewport视图的坐标系，也就是说需要编写SVG格式的路径语句。

首先介绍第一种，看如下动画显示：



![img](https:////upload-images.jianshu.io/upload_images/1819426-905709a5cae6c020.gif?imageMogr2/auto-orient/strip|imageView2/2/w/260/format/webp)

1.gif



![img](https:////upload-images.jianshu.io/upload_images/1819426-c5094cf44e00d6c1.gif?imageMogr2/auto-orient/strip|imageView2/2/w/297/format/webp)

2.gif

（1）搜索框动画
 首先同样地创建Vector资源图片searchbar.xml:



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="150dp"
    android:height="24dp"
    android:viewportHeight="24"
    android:viewportWidth="150">
    <path
        android:name="search"
        android:pathData="M141,17 A9,9 0 1,1 142,16 L149,23"
        android:strokeAlpha="0.8"
        android:strokeColor="#000000"
        android:strokeLineCap="round"
        android:strokeWidth="2"/>
    <path
        android:name="bar"
        android:pathData="M0,23 L149,23"
        android:strokeAlpha="0.8"
        android:strokeColor="#000000"
        android:strokeLineCap="square"
        android:strokeWidth="2"/>
</vector>
```

分为放大镜图标和下划线图标。

**接下来就是重点的显示动画**
 anim_search.xml：



```xml
<?xml version="1.0" encoding="utf-8"?>
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="1000"
    android:propertyName="trimPathStart"
    android:repeatCount="infinite"
    android:repeatMode="reverse"
    android:valueFrom="1"
    android:valueTo="0"
    android:valueType="floatType">
</objectAnimator>
```

anim_bar.xml



```xml
<?xml version="1.0" encoding="utf-8"?>
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="1000"
    android:propertyName="trimPathStart"
    android:repeatCount="infinite"
    android:repeatMode="reverse"
    android:valueFrom="0"
    android:valueTo="1"
    android:valueType="floatType">
</objectAnimator>
```

根据上面的定义介绍，anim_search.xml表示的是动画效果是绘制路径从有到无的变化过程，anim_bar.xml表示的是动画效果是绘制路径从无到有的变化过程。

同样地，创建粘合剂searchbar_anim.xml:



```xml
<?xml version="1.0" encoding="utf-8"?>
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/seachbar">
    <target
        android:animation="@animator/anim_search"
        android:name="search"/>
    <target
        android:animation="@animator/anim_bar"
        android:name="bar"/>
</animated-vector>
```

最后在ImageView中承载就可以实现上面的动画效果。

（2）星图标动画
 这个动画包含两个属性动画，一个是颜色的渐变，一个是路径的变化。

Vector资源文件：



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="200dp"
    android:height="200dp"
    android:viewportHeight="500"
    android:viewportWidth="500">
    <group
        android:scaleX="5.0"
        android:scaleY="5.0">
        <path
            android:name="star"
            android:pathData="M 50.0,90.0 L 82.9193546357,27.2774101308 L 12.5993502926,35.8158045183 L 59.5726265715,88.837672697 L 76.5249063296,20.0595700732 L 10.2916450361,45.1785327898 L 68.5889268818,85.4182410261 L 68.5889268818,14.5817589739 L 10.2916450361,54.8214672102 L 76.5249063296,79.9404299268 L 59.5726265715,11.162327303 L 12.5993502926,64.1841954817 L 82.9193546357,72.7225898692 L 50.0,10.0 L 17.0806453643,72.7225898692 L 87.4006497074,64.1841954817 L 40.4273734285,11.162327303 L 23.4750936704,79.9404299268 L 89.7083549639,54.8214672102 L 31.4110731182,14.5817589739 L 31.4110731182,85.4182410261 L 89.7083549639,45.1785327898 L 23.4750936704,20.0595700732 L 40.4273734285,88.837672697 L 87.4006497074,35.8158045183 L 17.0806453643,27.2774101308 L 50.0,90.0Z"
            android:strokeColor="#000000"
            android:strokeWidth="2"/>
    </group>
</vector>
```

![img](https:////upload-images.jianshu.io/upload_images/1819426-2b49d082cd97ce3d.png?imageMogr2/auto-orient/strip|imageView2/2/w/152/format/webp)

path

**重点是动画文件**
 anim_path.xml:



```xml
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
        android:duration="10000"
        android:propertyName="trimPathStart"
        android:repeatCount="infinite"
        android:repeatMode="reverse"
        android:valueFrom="1"
        android:valueTo="0"
        android:valueType="floatType">
    </objectAnimator>

    <objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
        android:duration="10000"
        android:propertyName="strokeColor"
        android:repeatCount="infinite"
        android:repeatMode="reverse"
        android:valueFrom="@android:color/holo_red_dark"
        android:valueTo="@android:color/darker_gray"
        android:valueType="intType">
    </objectAnimator>
</set>
```

通过set标签包含两个objectAnimator，两个动画同时展示出来。

最后是粘合剂path_anim.xml



```xml
<?xml version="1.0" encoding="utf-8"?>
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/path">
    <target
        android:animation="@animator/anim_path"
        android:name="star"/>
</animated-vector>
```

第二种，通过指定SVG路径语句



![img](https:////upload-images.jianshu.io/upload_images/1819426-de5de3a613a2b51d.gif?imageMogr2/auto-orient/strip|imageView2/2/w/285/format/webp)

5.gif

Vector资源图片fivestar.xml:



```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="120dp"
    android:height="120dp"
    android:viewportHeight="64"
    android:viewportWidth="64">
    <group>
        <path
            android:name="star"
            android:fillColor="#22e171"
            android:pathData="M 48,54 L 31,42 15,54 21,35 6,23 25,23 32,4 40,23 58,23 42,35 z"
            android:strokeColor="#000000"
            android:strokeWidth="1"/>
    </group>
</vector>
```

![img](https:////upload-images.jianshu.io/upload_images/1819426-09ae64cfaf023ffa.png?imageMogr2/auto-orient/strip|imageView2/2/w/151/format/webp)

fivestar

**重点是动画文件**anim_fivestar.xml:



```xml
<?xml version="1.0" encoding="utf-8"?>
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="3000"
    android:propertyName="pathData"
    android:repeatCount="infinite"
    android:repeatMode="reverse"
    android:valueFrom="M 48,54 L 31,42 15,54 21,35 6,23 25,23 32,4 40,23 58,23 42,35 z"
    android:valueTo="M 48,54 L 31,54 15,54 10,35 6,23 25,10 32,4 40,10 58,23 54,35 z"
    android:valueType="pathType">
</objectAnimator>
```

着重解释一下，选用的是android:propertyName="pathData"属性，意味着需要添加图形的SVG格式运动轨迹，其中android:valueFrom是五角星，android:valueTo是五边形，所以运动轨迹就是从五角星到五边形的过程。

粘合剂代码fivestar_anim.xml:



```xml
<?xml version="1.0" encoding="utf-8"?>
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/fivestar">
    <target
        android:animation="@animator/anim_fivestar"
        android:name="star"/>
</animated-vector>
```

最后添加ImageView来承载粘合剂即可。

### 2.3.4 总结

1. 创建Vector图片资源文件，这个文件可能是UI设计师提供的，也可以在阿里矢量素材库等网站上获取的；
2. 确定想要的动画效果，添加属性动画；
3. 创建粘合剂，绑定动画和Vector资源；
4. 用ImageView、ImageButton等控件承载粘合剂；
5. 在Activity中启动动画。

## 2.4 Vector兼容性问题

Vector默认支持5.0以上版本，在AppCompat23.2以上版本支持向下兼容：
 静态Vector支持Android2.1以上
 动态Vector支持Android3.0以上
 几乎可以兼容大部分使用场景

### 2.4.1 Button兼容

在上面讲到过，在Button上使用Vector必须通过Selector来完成的，在向下兼容时，需要在Activity的前面加上：



```java
static {
    AppCompatDelegate.setCompatVectorFromResourcesEnabled(true);
}
```

为了向下兼容，影响了类似DrawableContainers（DrawableContainers which reference other drawables resources which contain only a vector resource）这样的类。它的一个典型，就是Selector（StateListDrawable也是），这个属于Google工程师对于向下兼容的无奈之举吧。

### 2.4.2 动态兼容

（1）向下兼容
 Path Morphing，即路径变换动画，（举例来说，圆形变矩形，五角星变五边形）在Android pre-L版本下是无法使用的。目前此问题是动态兼容上最大的问题。
 Path Interpolation，即路径插值器，在Android pre-L版本只能使用系统的插值器，不能自定义。
 Path Animation，即路径动画，这个一般使用贝塞尔曲线来代替，所以没有太大影响。
 （2）向上兼容
 因为考虑到兼容性的问题，会使用AppCompat库做兼容性工作。
 例如，继承了AppCompatActivity，在布局文件中又指定了ImageView的srcCompat，但是AnimatedVectorDrawableCompat是不支持Path Morphing动画的。解决的方法是，判断当前设备版本号，如果是L版本以下提示不支持此动画，如果在L版本以上修改为如下代码：



```java
ImageView imageView = (ImageView) view;
AnimatedVectorDrawable drawable= (AnimatedVectorDrawable) getDrawable(R.drawable.xxx);
imageView.setImageDrawable(drawable);
if (drawable!= null) {
    drawable.start();
}
```

（3）String.xml问题
 不支持将Vector的PathData的数据，添加到String.xml中。

## 2.5 Vector属性介绍

### 2.5.1 Vector内部标签属性

| 属性                       | 解析                                                         |
| -------------------------- | :----------------------------------------------------------- |
| **android:name**           | 定义该drawable的名字                                         |
| **android:width**          | 定义该 drawable 的内部(intrinsic)宽度,支持所有 Android 系统支持的尺寸，通常使用 dp |
| **android:height**         | 定义该 drawable 的内部(intrinsic)高度,支持所有 Android 系统支持的尺寸，通常使用 dp |
| **android:viewportWidth**  | 定义矢量图视图的宽度，视图就是矢量图 path 路径数据所绘制的虚拟画布 |
| **android:viewportHeight** | 定义矢量图视图的高度，视图就是矢量图 path 路径数据所绘制的虚拟画布 |
| **android:tint**           | 定义该 drawable 的 tint 颜色。默认是没有 tint 颜色的         |
| **android:tintMode**       | 定义 tint 颜色的 [Porter-Duff blending](https://link.jianshu.com?t=http://blog.csdn.net/t12x3456/article/details/10432935) 模式，默认值为 src_in |
| **android:autoMirrored**   | 设置当系统为 RTL (right-to-left) 布局的时候，是否自动镜像该图片。比如 阿拉伯语。 |
| **android:alpha**          | 该图片的透明度属性                                           |

### 2.5.2 path标签属性

| 属性                         | 解析                                                         |
| ---------------------------- | :----------------------------------------------------------- |
| **android:name**             | 定义该 path 的名字，这样在其他地方可以通过名字来引用这个路径 |
| **android:pathData**         | 和 SVG 中 d 元素一样的路径信息。                             |
| **android:fillColor**        | 定义填充路径的颜色，如果没有定义则不填充路径                 |
| **android:strokeColor**      | 定义如何绘制路径边框，如果没有定义则不显示边框               |
| **android:strokeWidth**      | 定义路径边框的粗细尺寸                                       |
| **android:strokeAlpha**      | 定义路径边框的透明度                                         |
| **android:fillAlpha**        | 定义填充路径颜色的透明度                                     |
| **android:trimPathStart**    | 从路径起始位置截断路径的比率，取值范围从 0 到1               |
| **android:trimPathEnd**      | 从路径结束位置截断路径的比率，取值范围从 0 到1               |
| **android:trimPathOffset**   | 设置路径截取的范围 Shift trim region (allows showed region to include the start and end), in the range from 0 to 1. |
| **android:strokeLineCap**    | 设置路径线帽的形状，取值为 butt, round, square.              |
| **android:strokeLineJoin**   | 设置路径交界处的连接方式，取值为 miter,round,bevel.          |
| **android:strokeMiterLimit** | 设置斜角的上限，Sets the Miter limit for a stroked path.     |

# 3. VectorDrawable使用场景

- 1. Bitmap的绘制效率并不一定会比Vector高，它们有一定的平衡点，当Vector比较简单时，其效率是一定比Bitmap高的。所以，为了保证Vector的高效率，Vector需要更加简单，PathData更加标准、精简，当Vector图像变得非常复杂时，就需要使用Bitmap来代替。
- 1. Vector适用于ICON、Button、ImageView的图标等小的ICON，或者是需要的动画效果。由于Bitmap在CPU中有缓存功能，而Vector并没有，所以Vector图像不能做频繁的重绘。
- 1. Vector图像过于复杂时，不仅仅要注意绘制效率，初始化效率也是需要考虑的重要因素
- 1. SVG加载速度会快于PNG,但渲染速度会慢于PNG，毕竟PNG有硬件加速，但平均下来，加载速度的提升弥补了绘制的速度缺陷。

总结来说，Vector更适用于小的控件，Button，ImageView等，有更加炫的动画效果。