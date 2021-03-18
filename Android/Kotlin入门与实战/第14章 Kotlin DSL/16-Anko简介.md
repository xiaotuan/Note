### 14.6.1　Anko简介

Anko是JetBrains提供的一个使用Kotlin编写的Android DSL插件，用来辅助构建Android视图。

众所周知，Android视图都是使用XML的方式来完成布局的，这些XML可重用性差，而且在代码的运行过程中，将XML转换成Java字节码会对CPU和设备造成一定的损耗。Anko允许开发者在AnkoComponent、Activity或Fragment中使用Kotlin来编写视图，而且使用Anko编写Android应用程序更加方便快捷。

Anko主要由Anko Commons、Anko Layout、Anko SQLite和Anko Coroutines几个模块组成。

+ Anko Commons：该模块使得Android在操作intent、dialog、logging等功能时更加简单便捷。
+ Anko Layout：该模块提供快速且类型安全的动态Android布局库，使得布局开发更加高效方便。
+ Anko SQLite：该模块提供用于Android SQLite查询的DSL和分析库。
+ Anko Coroutines：该模块提供基于kotlinx协程库的相关功能。

例如，下面是使用传统XML方式构建登录页面的代码。

```python
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_height="match_parent"
    android:layout_width="match_parent"
    android:orientation="vertical">
    <EditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>
    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="登录" />
</LinearLayout>
```

如果用Anko来描述同样的视图，可以使用下面的代码。

```python
verticalLayout {
    val name = editText()
    button("登录") {
        onClick { toast("Hello, ${name.text}!") }
    }
}
```

可以看到，通过Kotlin代码实现的视图，可以在button布局中使用onClick函数来实现监听功能。

