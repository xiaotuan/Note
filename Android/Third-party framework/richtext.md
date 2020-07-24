<center><font size="5"><b>RichText框架</b></font></center>

[toc]

#### 1. 框架简介

RichText是一个用于显示html和Markdown文本格式的框架。

#### 2. Github地址

<https://github.com/zzhoujay/RichText>

#### 3. 配置build.gradle

在项目根目录下的 `gradle.properties` 文件中添加如下代码：

```
RICHTEXT_VERSION = 3.0.8
```

在 `app` 目录下的 `build.gradle`文件中添加如下代码：

```
dependencies {
    ......
    implementation "com.zzhoujay.richtext:richtext:${RICHTEXT_VERSION}"
}
```

如果需要使用新的HTML解析器，只需加入此依赖即可，无须其他操作，新HTML解析器对原生HTML解析器的功能做了补充。

```
dependencies {
    ......
    implementation "com.zzhoujay:html:${HTML_VERSION}"
}
```

新Html解析器增加了对代码块的支持，代码块可以触发点击事件，通过`urlClick`设置， 代码块回调的参数由`code://`开头

使用新Html解析器遇到问题请在[https://github.com/zzhoujay/Htm](https://github.com/zzhoujay/Html)提issue

#### 4. 使用方法

> + 在第一次调用 `RichText` 之前先调用 `RichText.initCacheDir()` 方法设置缓存目录
> + `ImageFixCallback` 的回调方法不一定是在主线程回调，注意不要进行UI操作
> + 本地图片有根路径 `\ ` 开头，`Assets` 目录图片由 `file:///android_asset/` 开头
> + `Gif` 图片播放不支持硬件加速，若要使用 `Gif` 图片请先关闭 `TextView` 的硬件加速。
>
> ```Java
> textView.setLayerType(View.LAYER_TYPE_SOFTWARE, null);
> ```

##### 4.1 简单使用

基本使用：

```Java
RichText.from(text).into(textView);
```

设置数据源类型：

```
// 设置为Html
RichText.fromHtml(text).into(textView);

// 设置为Markdown
RichText.fromMarkdown(text).into(textView);
```

使用type方法设置：

```Java
RichText.from(text).type(RichText.TYPE_MARKDOWN).into(textView);
```

##### 4.2 高级使用

```Java
RichText
       .from(text) // 数据源
       .type(RichText.TYPE_MARKDOWN) // 数据格式,不设置默认是Html,使用fromMarkdown的默认是Markdown格式
       .autoFix(true) // 是否自动修复，默认true
       .autoPlay(true) // gif图片是否自动播放
       .showBorder(true) // 是否显示图片边框
       .borderColor(Color.RED) // 图片边框颜色
       .borderSize(10) // 边框尺寸
       .borderRadius(50) // 图片边框圆角弧度
       .scaleType(ImageHolder.ScaleType.FIT_CENTER) // 图片缩放方式
       .size(ImageHolder.MATCH_PARENT, ImageHolder.WRAP_CONTENT) // 图片占位区域的宽高
       .fix(imageFixCallback) // 设置自定义修复图片宽高
       .fixLink(linkFixCallback) // 设置链接自定义回调
       .noImage(true) // 不显示并且不加载图片
       .resetSize(false) // 默认false，是否忽略img标签中的宽高尺寸（只在img标签中存在宽高时才有效），true：忽略标签中的尺寸并触发SIZE_READY回调，false：使用img标签中的宽高尺寸，不触发SIZE_READY回调
       .clickable(true) // 是否可点击，默认只有设置了点击监听才可点击
       .imageClick(onImageClickListener) // 设置图片点击回调
       .imageLongClick(onImageLongClickListener) // 设置图片长按回调
       .urlClick(onURLClickListener) // 设置链接点击回调
       .urlLongClick(onUrlLongClickListener) // 设置链接长按回调
       .placeHolder(placeHolder) // 设置加载中显示的占位图
       .error(errorImage) // 设置加载失败的错误图
       .cache(Cache.ALL) // 缓存类型，默认为Cache.ALL（缓存图片和图片大小信息和文本样式信息）
       .imageGetter(yourImageGetter) // 设置图片加载器，默认为DefaultImageGetter，使用okhttp实现
       .imageDownloader(yourImageDownloader) // 设置DefaultImageGetter的图片下载器
       .bind(tag) // 绑定richText对象到某个object上，方便后面的清理
       .done(callback) // 解析完成回调
       .into(textView); // 设置目标TextView
```

##### 4.3 释放资源

必要时可调用RichText对象的clear方法释放资源，但很多情况不需要这样做

```
// 加载富文本
RichText.from(text).bind(activity).into(textView);

// activity onDestory时
RichText.clear(activity);
```

在应用退出时调用`RichText.recycle()`

#####4.4 参数介绍

**Source**

> 需要解析的源文本

构建`RichTextConfigBuild`时传入，之后不可更改

即由`RichText.fromxxx`构建

**RichType**

> 富文本类型，有`Markdown`和`Html`两种，默认后者

```
.type(RichType.MARKDOWN)
```

**autoFix**

> 自适应屏幕缩放图片，默认为true

将图片在长宽比例不变的情况下，进行缩放直至适应屏幕，一般来说是图片在宽度上填充屏幕

```
.autoFix(false)
```

**resetSize**

> 不使用img标签里的宽高，img标签的宽高存在才有用，默认false

在image标签中存在宽高尺寸时，若是设置为false，会为首次加载时的占位图设置宽高

```
.resetSize(true)
```

**cacheType**

> 缓存类型

有三种类型：

1. NONE，不做任何缓存
2. LAYOUT，只缓存图片的尺寸信息
3. ALL，缓存图片的尺寸信息及图片内容

默认为CacheType.ALL

其中2、3若需要持久化缓存则需在RichText第一次使用时调用：

```
RichText.initCacheDir(context)
```

或者

```
RichText.initCacheDir(file)
```

来设置本地缓存目录

```
.cacheType(CacheType.ALL)
```

**noImage**

> 不显示图片，默认false

若设置为true，则不会进行任何图片的加载，也不会显示占位图，ImageFixCallback将不会被回调

```
.noImage(true)
```

**clickable**

> 链接图片是否可点击

此项设置有三种情况：

1. 不设置，链接点击会调用浏览器打开
2. 设置false，屏蔽所有点击事件
3. 设置true，图片链接可点击，并且可以设置点击回调

```
.clickable(true)
```

**autoPlay**

> GIF图片是否自动播放，默认false

```
.autoPlay(true)
```

**scaleType**

> 图片缩放类型，类似于ImageView的ScaleType

这里先分清三种概念：加载到内存中的图片的尺寸、图片边框的尺寸、真正显示的图片尺寸

**加载到内存中的图片的尺寸**

这个影响的是图片显示的质量，一般用于图片压缩，在ImageFixCallback的onSizeReady中设置

**图片边框的尺寸**

类似于ImageView的width和height，是图片的边框，图片不能超出边框显示，由ImageFixCallback中的onLoading、onFailure和onImageReady中调用ImageHolder的`setWidth`和`setHeight`方法设置

**真正显示的图片尺寸**

由图片边框和scaleType共同决定图片的最终显示效果，scaleType类似于ImageView的scaleType，其总共有9中缩放类型：

1. NONE，不进行任何缩放和平移，按照原图尺寸放置在左上角
2. CENTER，不进行缩放，将图片放置在边框的中心
3. CENTER_CROP，以填满整个边框为目的，对图片进行等比例缩放，并将图片放置在边框中心
4. CENTER_INSIDE，以原图完全显示为目的，对图片进行等比例缩放，并将图片放置在边框中心
5. FIT_CENTER，把图片等比例扩大或缩小到边框的尺寸，并且居中显示
6. FIT_START，把图片等比例扩大或缩小到边框尺寸，并且显示在边框上部分或是左边
7. FIT_END，把图片等比例扩大或缩小到边框尺寸，并且显示在边框的下部分或是右边
8. FIT_XY，把图片按照边框缩放，并填充显示
9. FIT_AUTO，将图片的宽度按照边框宽度缩放，并且按照同比例缩放高度

默认为NONE，当autoFix为true时使用FIT_AUTO

```
.scaleType(ImageHolder.ScaleType.FIT_AUTO)
```

**width**

> 边框的宽度

可以选择为具体数值、ImageHolder.WRAP_CONTENT和ImageHolder.MATCH_PARENT，默认为ImageHolder.WRAP_CONTENT

```
.width(ImageHolder.MATCH_PARENT)
```

**height**

> 边框高度

可以选择为具体数值、ImageHolder.WRAP_CONTENT和ImageHolder.MATCH_PARENT，默认为ImageHolder.WRAP_CONTENT

```
.height(ImageHolder.MATCH_PARENT)
```

**singleLoad**

> 是否单线程解析，默认true

在有多个RichText同时解析时起作用

- true：解析顺序执行
- false：解析并发执行，适合在RecyclerView和ListView中

```
.singleLoad(false)
```

**ImageDownloader**

> 设置DefaultImageGetter的图片下载器

**只有在使用DefaultImageGetter的情况下生效**

在使用DefaultImageGetter的情况下，若是添加了`OkHttpImageDownloader`库的依赖可以自动使用`OkHttpImageDownloader`不用进行设置

若需要自定义图片下载器则需要实现`com.zzhoujay.richtext.ig.ImageDownloader`接口

**ImageFixCallback**

> 图片调整回调设置

接收一个ImageFixCallback类型的回调，在图片加载的过程中逐步调用

详情见：[手动调整图片](https://github.com/zzhoujay/RichText/wiki/手动调整图片)

```
.fix(myImageFixCallback)
```

**LinkFixCallback**

> 链接调整回调设置

接收一个LinkFixCallback类型的回调，在链接解析过程中被调用

详情见：[手动调整链接](https://github.com/zzhoujay/RichText/wiki/手动调整链接)

```
.linkFix(myLinkFixCallback)
```

**OnImageClickListener**

> 图片点击回调设置

接收一个OnImageClickListener类型的回调，在图片被点击时调用

```
.imageClick(myImageClickListener)
```

**OnImageLongClickListener**

> 图片长按回调设置

接收一个OnImageLongClickListener类型的回调，在图片被点击时调用

```
.imageLongClick(myImageLongClickListener)
```

**OnUrlClickListener**

> 链接点击回调设置

接收一个OnUrlClickListener类型的回调，在链接被点击时调用

```
.urlClick(myUrlClickListener)
```

**OnUrlLongClickListener**

> 图片长按回调设置

接收一个OnUrlLongClickListener类型的回调，在图片被点击时调用

```
.urlLongClick(myUrlLongClickListener)
```

**placeHolder**

> 图片加载过程中的占位图生成器设置

生成器须实现`com.zzhoujay.richtext.callback.DrawableGetter`接口

**注意**

drawable的bounds需要自行设置

```
.placeHolder(myPlaceHolderDrawableGetter)
```

**errorImage**

> 图片加载失败的占位图生成器设置

生成器须实现`com.zzhoujay.richtext.callback.DrawableGetter`接口

**注意**

drawable的bounds需要自行设置

```
.errorImage(myErrorImageDrawable)
```

**ImageGetter**

> 指定使用的图片加载器

设置特定的图片加载器进行富文本中图片的加载，接受一个实现了com.zzhoujay.richtext.callback.ImageGetter的类

现有实现有两个：

1. DefaultImageGetter，使用okhttp进行图片的下载，支持图片缓存（内存+磁盘），支持GIF图片，支持加载本地图片和Assets目录下的图片
2. GlideImageGetter，使用Glide进行图片的加载，使用Glide自己的缓存机制，支持GIF图片，其余和Glide类似

详情见：[自定义图片加载器](https://github.com/zzhoujay/RichText/wiki/自定义图片加载器)

其中DefaultImageGetter集成在RichText库中，为默认使用的ImageGetter

GlideImageGetter需要手动引入：`compile 'com.zzhoujay.glideimagegetter:glideimagegetter:latest-version'`

也可以根基自己的需求自行实现ImageGetter

推荐使用DefaultImageGetter

```
.imageGetter(yourImageGetter)
```

**Callback**

> 解析完成的回调（此时图片也都加载完成）

```
.done(yourCallback)
```

**Tag**

> 绑定RichText到某个对象

绑定后可以通过RichText.clear(tag)来进行缓存和任务的清理

```
.bind(tag)
```

**BorderHolder**

> 图片边框属性

此属性由四个方法设置：

1. showBorder，是否显示边框，默认不显示
2. borderSize，边框尺寸，默认5
3. borderColor，边框颜色，默认黑色
4. borderRadius，边框圆角弧度，默认0

```
.showBorder(true).borderSize(10).borderColor(Color.RED).borderRadius(5)
```

##### 4.5 点击事件

**链接点击回调**

```java
RichText.from(text).urlClick(new OnURLClickListener() {
    @Override
    public boolean urlClicked(String url) {
        Log.i("RichText", url);
        return false;
    }
}).into(textView);
```

其中回调方法中返回true代表事件已消费

**链接长按回调**

```java
RichText.from(text).urlLongClick(new OnUrlLongClickListener() {
    @Override
    public boolean urlLongClick(String url) {
        Log.i("RichText", url);
        return false;
    }
}).into(textView);
```

其中回调方法返回true代表事件已消费，false则会传给`urlClicked`方法

**图片点击回调**

```java
RichText.from(text).imageClick(new OnImageClickListener() {
    @Override
    public void imageClicked(List<String> imageUrls, int position) {
        Log.i("RichText",imageUrls.get(position));
    }
}).into(textView);
```

其中imageUrls是该富文本中所有的图片的列表，position代表当前点击的位置

**图片长按回调**

```java
RichText.from(text).imageLongClick(new OnImageLongClickListener() {
    @Override
    public boolean imageLongClicked(List<String> imageUrls, int position) {
        Log.i("RichText",imageUrls.get(position));
        return false;
    }
}).into(textView);
```

其中回调方法中返回true代表事件已消费

##### 4.6 ImageHolder

ImageHolder是在设置了ImageFixCallback后回调方法中的一个参数,代表了每张图片

其属性有:

- `width` : holder宽度

- `height` : holder高度

- `scaleType` : 缩放方式

- `autoFix` : 自动修复宽高

- `autoPlay` : 自动播放Gif图,在图片类型是Gif时有效

- `autoStop` : 自动停止Gif图片的播放,在图片是Gif时有效

- `show` : 是否显示

- `isGif` : 图片是否是Gif动图

- `borderHolder` : 关于边框的一些信息

- `imageState`: 当前图片加载状态，每次imageFixCallback被调用state都不一样
- INIT: 初始化加载，可以设置图片宽高给Glide
    - LOADING: 加载中，设置placeholder图片的宽高
    - READY: 图片加载成功，设置最终显示的图片的宽高
    - FAILED: 加载失败，设置加载失败的图片的宽高
    - SIZE_READY: 图片尺寸获取完毕（尚未加载到内存），这个是时候给holder设置maxWidth和maxHeight对图片进行相应的缩放

其中的一些属性需要图片加载器的支持

通过调用对应的getter和setter方法可以获取和设置ImageHolder的状态,并达到相应的功能

##### 4.7 LinkHolder

**用于对链接做一定的自定义**

属性:

- url : URL地址
- color : 字体颜色
- underLine : 是否加下划线，默认true

通过调用对应的getter和setter方法可以获取和设置ImageHolder的状态,并达到相应的功能

##### 4.8 图片缩放方式

图片缩放方式和ImageView的ScaleType类似

包含以下方式：

- NONE
- CENTER
- CENTER_CROP
- CENTER_INSIDE
- FIT_CENTER
- FIT_START
- FIT_END
- FIT_XY
- FIT_AUTO

其中除了`NONE`和`FIT_AUTO`其他行为的和ImageView的ScaleType一致

> NONE : 不缩放图片，图片靠左上角显示 FIT_AUTO : 根据图片宽高比例调整边框尺寸比例并充满边框

**注意**

其中的边框类似于ImageView，其宽高相当于ImageView的宽高，图片的宽高只是加载到内存中的尺寸信息（和实际显示的大小并没有绝对的关系，图片显示的大小由边框尺寸和ScaleType共同决定）

##### 4.9 手动调整图片

**图片调整**

手动修复图片需先设置autoFix为false

```
RichText.from(IMAGE1).autoFix(false).fix(new ImageFixCallback() {
        @Override
              public void onInit(ImageHolder holder) {
                  // 加载开始前（未调用图片加载器）
                  // 修改holder的尺寸改变图片边框的尺寸
              }

              @Override
              public void onLoading(ImageHolder holder) {
                  // 加载开始前（已进入图片加载器但未开始加载）
                  // 修改holder的尺寸改变图片边框的尺寸，此时影响到placeHolder显示
              }

              @Override                
              public void onSizeReady(ImageHolder holder, int imageWidth, int imageHeight, ImageHolder.SizeHolder sizeHolder) {
                  // 图片下载完成，但未加载到内存
                  // 修改sizeHolder的尺寸可以影响加载到内存的图片的大小，可以用于压缩图片
              }

              @Override
              public void onImageReady(ImageHolder holder, int width, int height) {
                  // 图片已成功加载到内存
                  // 修改holder的尺寸改变图片边框的尺寸，此时影响最后显示的图片的大小
              }

              @Override
              public void onFailure(ImageHolder holder, Exception e) {
                // 加载失败
                // 修改holder的尺寸改变图片边框的尺寸，此时影响到errorImage显示
              }
        }).into(textView);
```

在每次回调中通过设置holder的尺寸来改变图片边框大小，最终图片显示的大小由边框大小和ScaleType共同决定

**INIT**

初始化加载，加载还未开始，图片加载器还未被调用，此时ImageHolder可设置属性有

- imageType : 改变图片类型
- width : 设置holder宽度，会影响placeHolder宽度
- height : 设置holder高度，会影响placeHolder高度
- show : 设置图片是否显示
- scaleType : 设置图片缩放类型（需要图片加载器支持）
- autoFix : 是否自动修复

**LOADING**

加载中，加载器以及开始工作，此时改变width和height属性可用影响到placeHolder宽高

**SIZE_READY**

图片尺寸大小已知，但还未加载至内存，此时修改sizeHolder可用影响最后加载到内存的图片的尺寸

- imageWidth: 图片的真实宽度
- imageHeight: 图片的真实高度
- sizeHolder: 修改其尺寸改变加载到内存中图片的尺寸（用于图片压缩）

**READY**

加载成功，还未设置图片，在这里修改width和height属性对图片大小做最终的调整

- imageWidth: 图片的真实宽度
- imageHeight: 图片的真实高度

**FAILED**

图片加载失败，可用调整width和height属性影响errorImage的大小

- exception : 出现的异常

每个属性的具体含义见[ImageHolder](https://github.com/zzhoujay/RichText/wiki/ImageHolder)

##### 4.10 手动调整链接

通过手动修复接口可以修改链接文本的样式

```java
RichText.from(text).linkFix(new LinkFixCallback() {
    @Override
    public void fix(LinkHolder holder) {
        holder.setColor(Color.RED);
        holder.setUnderLine(true);
        Toast.makeText(MainActivity.this, holder.getUrl(), Toast.LENGTH_SHORT).show();
    }
}).into(textView);
```

##### 4.11 自定义图片加载器

目前提供两种图片加载器：`DefaultImageGetter`、`GlideImageGetter`

######4.11.1 DefaultImageGetter

集成在RichText库中，为默认使用加载器（需要设置图片下载器才能进行图片的下载）

支持的Cache类型

- Cache.NONE : 不进行缓存
- Cache.LAYOUT : 缓存文本样式及图片大小信息
- Cache.ALL : 在LAYOUT基础上增加了对图片的缓存

**支持Gif图片**

**支持本地图片**

**支持自定义图片下载器**

RichText提供了一个使用HttpUrlConnection实现的DefaultImageDownloader，除此之外也提供一个OkHttp简单实现的图片下载器：OkHttpImageDownloader

```
compile 'com.zzhoujay.okhttpimagedownloader:OkHttpImageDownloader:1.0.2'
```

添加依赖后会自动使用OkHttpImageDownloader

若是需要自定义图片下载器可以通过：

```
RichText
  .from(xxx)
  .imageDownloader(yourImageDownloader)
  .into(textView);
```

其中的`yourImageDownloader`需要实现`com.zzhoujay.richtext.ig.ImageDownloader`接口

######4.11.2 GlideImageGetter

使用Glide加载图片，因Glide自身有自己的缓存系统，固不支持Cache.ALL类型缓存，未集成在RichText库中，需手动引入

```
compile 'com.zzhoujay.glideimagegetter:glideimagegetter:1.0.5'
```

支持的Cache类型

- Cache.NONE : 不缓存
- Cache.LAYOUT : 缓存文本样式及图片大小信息

**支持Gif图片**

**支持本地图片**

######4.11.3 自定义ImageGetter

实现`com.zzhoujay.richtext.callback.ImageGetter`接口

**注意**

自定义ImageGetter返回的是一个Drawable对象，需要包含尺寸信息（即setBounds已设置），缓存和其它的也需要自行处理

```Java
RichText.from(text).imageGetter(yourImageGetter).into(textView);
```

#####4.12 注意事项

+ 不支持css属性的解析
+ TextView的width属性不能为warp_content
+ 如果需要手动取消任务，可以手动调用clear方法，可以在Activity onDestory方法中调用手动取消任务回收内存
+ 目前只能自动通过src的后缀识别是否为gif图，可以通过设置ImageFixCallback对某个特点的图片设置为GIF ，例如：holder.setImageType(ImageHolder.GIF)
+ 在RecyclerView和ListView中使用Gif图目前存在bug,建议不要在ListView和RecyclerView中播放动图
+ 在RecyclerView中存在一些问题，特别是当每个item高度比较大时
+ Gif图片播放不支持硬件加速，若要使用Gif图片请先关闭TextView的硬件加速
```Java
TextView.setLayerType(View.LAYER_TYPE_SOFTWARE, null);
```

##### 4.13 已知问题

+ ListView、RecyclerView中不支持Gif图片播放