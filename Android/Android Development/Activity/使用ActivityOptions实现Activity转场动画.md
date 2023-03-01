之前一直都是用这种方式实现Activity的转场动画：

// MainActivity
overridePendingTransition(enterAnim, exitAnim);
1
2
从Android5.0之后，Google提供了一种新的方式来实现：ActivityOptions。

前提
在使用前，需要声明允许使用ActivityOptions。
在styles.xml文件，设置App主题时，添加android:windowContentTransitions的属性，属性值为true：

<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="Theme.AppCompat.Light">
        <item name="android:windowContentTransitions">true</item>
    </style>
</resources>
1
2
3
4
5
6
注意：这个是5.0才支持的属性，应该放到values-v21文件夹下。不过，即使我不提醒你，编译器也不会放过你的，哈哈！！

使用及效果
ActivityOptionsCompat是ActivityOptions的兼容包，这个类可以帮助我们实现Activity转场动画。

ActivityOptionsCompat的方法不多，有如下几个：

makeCustomAnimation(Context context, int enterResId, int exitResId)

makeScaleUpAnimation(View source, int startX, int startY, int startWidth, int startHeight)

makeThumbnailScaleUpAnimation(View source, Bitmap thumbnail, int startX, int startY)

makeClipRevealAnimation(View source, int startX, int startY, int width, int height)

makeSceneTransitionAnimation(Activity activity, View sharedElement, String sharedElementName)

makeSceneTransitionAnimation(Activity activity, Pair<View, String>… sharedElements)
1
2
3
4
5
6
7
8
9
10
11
接下来我们一一介绍这几个方法的使用方法和效果吧。

makeCustomAnimation
转场效果：

用户自己定义，看下去就明白了。
1
使用方法：

ActivityOptionsCompat compat = ActivityOptionsCompat.makeCustomAnimation(this, R.anim.anim_activity_in, R.anim.anim_activity_out);
ActivityCompat.startActivity(this, new Intent(this, SecondActivity.class), compat.toBundle());
1
2
makeCustomAnimation方法需要3个参数（结合例子）：

this：Context类型，也就是Activity。
R.anim.anim_activity_in：int类型，新Activity显示动画。
R.anim.anim_activity_out：int类型，当前Activity退出动画。
这后2个参数有木有想到什么，没错，相当于Activity的：

overridePendingTransition(enterAnim, exitAnim);
1
如果你要使用这种方式，还不如用Activity原生的overridePendingTransition方法转场。

makeScaleUpAnimation
转场效果：

新Activity会以某个点为中心，从某个大小开始逐渐放大到最大。
1
使用方法：

ActivityOptionsCompat compat = ActivityOptionsCompat.makeScaleUpAnimation(view, view.getWidth() / 2, view.getHeight() / 2, 0, 0);
ActivityCompat.startActivity(this, new Intent(this, SecondActivity.class), compat.toBundle());
1
2
makeScaleUpAnimation需要5个参数（结合例子）：

view：View类型，指定从哪个View的坐标开始放大。
view.getWidth() / 2：int类型，指定以View的X坐标为放大中心的X坐标。
view.getHeight() / 2：int类型，指定以View的Y坐标为放大中心的Y坐标。
0：int类型，指定放大前新Activity是多宽。
0：int类型，指定放大前新Activity是多高。
makeThumbnailScaleUpAnimation
转场效果：

放大一个图片，最后过度到一个新activity（我测试的时候，效果不明显）
1
使用方法：

ActivityOptionsCompat compat = ActivityOptionsCompat.makeThumbnailScaleUpAnimation(view, BitmapFactory.decodeResource(getResources(), R.mipmap.ic_launcher), 0, 0);
ActivityCompat.startActivity(this, new Intent(this, SecondActivity.class), compat.toBundle());
1
2
makeThumbnailScaleUpAnimation需要4个参数（结合例子）：

view：View类型，要放大的图片从哪个View的左上角的坐标作为中心点放大。
BitmapFactory.decodeResource(getResources(), R.mipmap.ic_launcher)：Bitmap类型，指定要放大的图片。
0：放大前图片的初始宽度。
0：放大前图片的初始高度。
makeClipRevealAnimation
转场效果：

与makeScaleUpAnimation效果差不多，可能是时间太短的问题，看不清楚
1
使用方式：

ActivityOptionsCompat compat4 = ActivityOptionsCompat.makeClipRevealAnimation(view, view.getWidth() / 2, view.getHeight() / 2, 0, 0);
ActivityCompat.startActivity(this, new Intent(this, SecondActivity.class), compat4.toBundle());
1
2
参数同makeScaleUpAnimation相同，不做详解。

makeSceneTransitionAnimation（重点）
转场效果：

两个Activity的两个View协同完成转场，也就是原Activity的View过度到新Activity的View，原新两个Activity的View的transitionName相同。
1
使用实例：

```java
// activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="10dp"
    tools:context="com.johan.demo.MainActivity">

    ...

    <ImageView
        android:id="@+id/ImgView1"
        android:layout_width="160dp"
        android:layout_height="90dp"
        android:layout_marginTop="10dp"
        android:src="@drawable/tu"
        android:transitionName="@string/tu" <!-- 注意 -->
        />

</LinearLayout>

// activity_second.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    ...

    <ImageView
        android:id="@+id/ImgView2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:src="@drawable/tu"
        android:transitionName="@string/tu" <!-- 注意 -->
        />

</LinearLayout>

// strings.xml
<resources>
    <string name="tu">tu</string>
</resources>

// MainActivity使用ActivityOptions
...
ActivityOptionsCompat compat = ActivityOptionsCompat.makeSceneTransitionAnimation(this, imgView, getString(R.string.tu));
ActivityCompat.startActivity(this, new Intent(this, SecondActivity.class), compat.toBundle());
...
```

注意，`activity_main.xml` 和 `activity_second.xml` 文件都有一个`ImageView`，他们的 `android:transitionName` 的值是一样的（ `@string/tu` ），当使用 `makeSceneTransitionAnimation` 进行转场时，ImgView1 会慢慢的过渡到 ImgView2。过渡的效果，有很多种情况，例子中的过渡效果是 ImgView1 会逐渐放大，并移动到 ImgView2 的位置，同时显示 SecondActivity（新Activity）。

`makeSceneTransitionAnimation` 方法需要3个参数（结合例子）：

1. this：`Context` 类型，指定 `Activity`。

2. imgView：`View` 类型，指定从哪里开始过渡。例子中是 ImgView1 be过渡到 ImgView2，所以是 ImgView1。

3. getString(R.string.tu)：`String` 类型，指定 `android:transitionName` 的值，过渡 `View` 的标志。
   我想说，这种效果很酷的，一定要自己试一下！！！

**makeSceneTransitionAnimation（重点）**
转场效果：

```java
makeSceneTransitionAnimation是单个View协作，makeSceneTransitionAnimation允许多个View协作，效果和makeSceneTransitionAnimation像相似。
```

使用实例：

```xml
// activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="10dp"
    tools:context="com.johan.demo.MainActivity">

    ...

    <ImageView
        android:id="@+id/ImgView1"
        android:layout_width="160dp"
        android:layout_height="90dp"
        android:layout_marginTop="10dp"
        android:src="@drawable/tu"
        android:transitionName="@string/tu" <!-- 注意 -->
        />

    <TextView
        android:id="@+id/TxtView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:textColor="#00ff00"
        android:textSize="16sp"
        android:text="SceneTransitionAnimation2 Text String"
        android:transitionName="@string/zi" <!-- 注意 -->
        />

</LinearLayout>

// activity_second.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    ...

    <ImageView
        android:id="@+id/ImgView2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:src="@drawable/tu"
        android:transitionName="@string/tu" <!-- 注意 -->
        />

    <TextView
        android:id="@+id/TxtView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="10dp"
        android:textColor="#0000ff"
        android:textSize="16sp"
        android:text="SceneTransitionAnimation2 Text String"
        android:transitionName="@string/zi" <!-- 注意 -->
        />

</LinearLayout>

// strings.xml
<resources>
    <string name="tu">tu</string>
    <string name="zi">zi</string>
</resources>

// MainActivity使用ActivityOptions
...
Pair<View, String> imgViewPair = Pair.create(imgView, getString(R.string.tu));
Pair<View, String> txtViewPair = Pair.create(txtView, getString(R.string.zi));
ActivityOptionsCompat compat = ActivityOptionsCompat.makeSceneTransitionAnimation(this, imgViewPair, txtViewPair);
ActivityCompat.startActivity(this, new Intent(this, SecondActivity.class), compat.toBundle());
...
```

注意，`transitionName` 值一定要一一对应哦！！

### 定义转场动画
除了上面动画，`Android` 还支持我们定义转场动画。

目前支持3种 `Activity` 进退场动画：

```java
// explode(分解)
从场景中心移入或移出视图

// slide(滑动)
从场景边缘移入或移出视图

// fade(淡出)
通过调整透明度在场景中增添或移除视图
```

还支持4种共享元素（也就是 `transitionName` 相同的 `View` [ 不同的 `Activity`  ]）过渡动画：

```java
// changeBounds
改变目标视图的布局边界

// changeClipBounds
裁剪目标视图边界

// changeTransform
改变目标视图的缩放比例和旋转角度

// changeImageTransform
改变目标图片的大小和缩放比例
```

### 使用实例
使用方式有2种：

+ 通过xml设置

+ 通过代码设置

### 通过xml设置

#### （1）定义转场和过渡动画的xml

在 `res` 文件夹下新建 `transition` 文件夹，然后在 `res/transition` 文件夹下新建xml文件：

```xml
// transition_explode.xml
<?xml version="1.0" encoding="utf-8"?>
<transitionSet xmlns:android="http://schemas.android.com/apk/res/android">
    <explode android:duration="1000" android:interpolator="@android:interpolator/accelerate_decelerate" />
</transitionSet>

// transition_fade.xml
<?xml version="1.0" encoding="utf-8"?>
<transitionSet xmlns:android="http://schemas.android.com/apk/res/android">
    <fade android:duration="1000" android:interpolator="@android:interpolator/accelerate_decelerate" />
</transitionSet>
```

上面我定义了 2 个转场动画，当然你还可以定义共享元素的过渡动画，这里只是简单定义了一下。

#### （2）设置 SecondActivity 的转场动画

因为将要启动的 SecondActivity，那我们就定义 SecondActivity 主题时，设置 SecondActivity 进出场动画：

```xml
<!-- 继承AppTheme，因为里面定义了android:windowContentTransitions属性，允许我们使用ActivityOptions -->
<style name="SecondActivityTheme" parent="AppTheme">
    <!-- 进场（Activity进入时）动画 -->
    <item name="android:windowEnterTransition">@transition/transition_explode</item>
    <!-- 出场（Activity退出时）动画，其实是错误的，下面会改正 -->
    <item name="android:windowExitTransition">@transition/transition_fade</item>
</style>
```


然后设置 SecondActivity 的主题为 SecondActivityTheme。

#### （3）转场
在 MainActivity 跳转到 SecondActivity：

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP)
    // 我们这里没有用ActivityCompat转场
    startActivity(new Intent(this, SecondActivity.class), ActivityOptions.makeSceneTransitionAnimation(this).toBundle());
```

因为只有 5.0 才支持，所以稍微做一下判断。

### 通过代码设置
通过代码设置，就不一定要定义xml，因为代码中也有方法支持，待会再说。

#### （1）定义转场和过渡动画的 `xml`（不一定需要，你可以定义）

在res文件夹下新建 `transition` 文件夹，然后在 `res/transition` 文件夹下新建xml文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<transitionSet xmlns:android="http://schemas.android.com/apk/res/android">
    <explode android:duration="1000" android:interpolator="@android:interpolator/accelerate_decelerate" />
    <fade android:duration="1000" android:interpolator="@android:interpolator/accelerate_decelerate" />
</transitionSet>
```

#### （2）在代码中设置

如果我们定义了转场动画xml文件，可以在 SecondActivity 的 `onCreate` 方法这么设置：

```java
public class SecondActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            Transition transition = TransitionInflater.from(this).inflateTransition(R.transition.transition_explode);
            getWindow().setEnterTransition(transition);
        }
    }
}
```

可以利用 `TransitionInflater` 获取到我们定义的 `Transition` 动画。

如果没有定义，可以这么设置：

```java
public class SecondActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            getWindow().setEnterTransition(new Explode());
        }
    }
}
```

`new Explode()` 为 Android 提供的方法，还有其他的，自己慢慢体会。

### 遇到的坑
这里我有个疑问，无论是xml方式设置，还是通过代码设置，我只设置了进场动画，为什么出场动画也一样？而且如果我设置了出场动画，好像也没有效果？？

原来是我设置的不对！！！

我天真的以为设置 `android:windowExitTransition` 属性是 SecondActivity 退出来的动画！！！

我查看到有博客解释了进出场相关资料，才明白：

```java
// setEnterTransition() 
// android:windowEnterTransition  
当A start B时，使B中的View进入场景的transition    在B中设置

// setExitTransition()  
// android:windowExitTransition  
当A start B时，使A中的View退出场景的transition    在A中设置

// setReturnTransition() 
// android:windowReturnTransition 
当B 返回 A时，使B中的View退出场景的transition   在B中设置

// setReenterTransition() 
// android:windowReenterTransition
当B 返回 A时，使A中的View进入场景的transition   在A中设置
```

知道这个，我们改正之前错误的写法：

```xml
<style name="SecondActivityTheme" parent="AppTheme">
    <!-- 进场（Activity进入时）动画 -->
    <item name="android:windowEnterTransition">@transition/transition_explode</item>
    <!-- 出场（Activity退出时）动画，这是正确的 -->
    <item name="android:windowReturnTransition">@transition/transition_fade</item>
</style>
```


代码设置也一样哦！！