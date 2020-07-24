<center>
  <font size="5">
  	<b>Anko框架</b>
  </font>
</center>

[toc]

> 该框架已经标注为弃用，不再更新。

#### 1. Github
<https://github.com/Kotlin/anko>

#### 2. 过时原因

##### 2.1  停止Anko

在过去的几个月中，我们收到了许多用户的关于Anko未来的问题。因此，今天，我们要弄清楚一切，并正式弃用该库。

##### 2.2 你为什么不赞成Anko？

Anko诞生于用于构建Android布局的类型安全DSL。它不仅允许以类型安全的方式创建布局，而且还使布局更具适应性，动态性，可重用性和高性能，因为不需要昂贵的布局膨胀。

在Anko的演变过程中，很明显，不仅Android框架的布局部分可以从提供Kotlin扩展中受益。这就是我们创建Anko Commons的原因，Anko Commons是用于Android框架不同部分的实用程序功能和类的工具箱。

尽管Anko在Kotlin用户中非常受欢迎，但我们必须承认，体验并不是100％完美。直到最近，Android View API都针对通货膨胀进行了高度优化，有时无法以编程方式设置某些属性。结果，DSL必须依靠黑客或变通办法。同样，模拟支持AppCompat所需的窗口小部件加载的反射方法并非易事。我们没有足够的资源来及时修复所有极端情况。

但是，在最近几年中，情况发生了很大变化。Google正式支持Kotlin，后来甚至使Kotlin成为Android应用程序开发的首选语言。多亏了JetPack丰富的库集，SDK的粗糙边缘得以平滑。

Anko是一个成功的项目，它在与Kotlin建立更好的Android开发人员体验中发挥了作用。但是，今天有其他替代方案，我们觉得是时候向安科说再见了。

##### 2.3 我应该用什么代替Anko？

###### 2.3.1 布局DSL

- Jetpack Compose。由Google支持的适用于Kotlin的反应式View DSL。
- Splitties- [Views DSL](https://github.com/LouisCAD/Splitties/tree/master/modules/views-dsl)。类似于Anko的可扩展View DSL。

###### 2.3.2 通用工具

- [Android KTX](https://developer.android.com/kotlin/ktx)。由Google支持的一组针对不同目的的Kotlin扩展。
- [Splitties](https://github.com/LouisCAD/Splitties)。很多场合的微型库。

###### 2.3.3 SQLite助手

- [Room](https://developer.android.com/topic/libraries/architecture/room)。由Google支持的基于注释的SQLite数据库访问框架。
- [SQLDelight](https://github.com/cashapp/sqldelight) 用于SQL查询的类型安全的API生成器。

#### 3. 用法：

##### 3.1 最新版本

0.10.8

##### 3.2 简介

⚠️Anko已弃用。请参阅[此页面](https://github.com/Kotlin/anko/blob/master/GOODBYE.md)以获取更多信息。

------

Anko是[Kotlin](https://www.kotlinlang.org/)库，可以使Android应用程序开发更快，更轻松。它使您的代码干净且易于阅读，并且使您无需理会Android SDK for Java的粗糙边缘。

Anko包含以下几个部分：

- *Anko Commons*：一个轻量级的库，其中包含用于意图，对话框，日志记录等的帮助程序；
- *Anko Layouts*：一种快速且类型安全的方式来编写动态Android布局；
- *Anko SQLite*：Android SQLite的查询DSL和解析器集合；
- *Anko Coroutines*：基于[kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)库的实用程序。

##### 3. 3 安科下议院

*Anko Commons*是Kotlin Android开发人员的“工具箱”。该库包含许多Android SDK的帮助程序，包括但不限于：

- Intents（[wiki](https://github.com/Kotlin/anko/wiki/Anko-Commons-–-Intents)）；
- Dialogs and toasts（[wiki](https://github.com/Kotlin/anko/wiki/Anko-Commons-–-Dialogs)）；
- Logging（[wiki](https://github.com/Kotlin/anko/wiki/Anko-Commons-–-Logging)）;
- Resources and dimensions（[Wiki](https://github.com/Kotlin/anko/wiki/Anko-Commons-–-Misc)）。

##### 3. 4 Anko Layouts ([wiki](https://github.com/Kotlin/anko/wiki/Anko-Layouts))

*Anko Layouts* is a DSL for writing dynamic Android layouts. Here is a simple UI written with Anko DSL:

```
verticalLayout {
    val name = editText()
    button("Say Hello") {
        onClick { toast("Hello, ${name.text}!") }
    }
}
```

The code above creates a button inside a `LinearLayout` and attaches an `OnClickListener` to that button. Moreover, `onClick` accepts a [`suspend` lambda](https://kotlinlang.org/docs/reference/coroutines.html), so you can write your asynchronous code right inside the listener!

Note that this is the complete layout code. No XML is required!

Anko has a [DSL for ConstraintLayout](https://github.com/Kotlin/anko/wiki/ConstraintLayout) since v0.10.4

[![Hello world](https://github.com/Kotlin/anko/raw/master/doc/helloworld.png)](https://github.com/Kotlin/anko/blob/master/doc/helloworld.png)

There is also a [plugin](https://github.com/Kotlin/anko/wiki/Anko-Layouts#anko-support-plugin) for Android Studio that supports previewing Anko DSL layouts.

##### 3.5 Anko SQLite ([wiki](https://github.com/Kotlin/anko/wiki/Anko-SQLite))

Have you ever been tired of parsing SQLite query results using Android cursors? *Anko SQLite* provides lots of helpers to simplify working with SQLite databases.

For example, here is how you can fetch the list of users with a particular name:

```
fun getUsers(db: ManagedSQLiteOpenHelper): List<User> = db.use {
    db.select("Users")
            .whereSimple("family_name = ?", "John")
            .doExec()
            .parseList(UserParser)
}
```

##### 3.6 Anko Coroutines ([wiki](https://github.com/Kotlin/anko/wiki/Anko-Coroutines))

*Anko Coroutines* is based on the [`kotlinx.coroutines`](https://github.com/kotlin/kotlinx.coroutines) library and provides:

- [`bg()`](https://github.com/Kotlin/anko/wiki/Anko-Coroutines#bg) function that executes your code in a common pool.
- [`asReference()`](https://github.com/Kotlin/anko/wiki/Anko-Coroutines#asreference) function which creates a weak reference wrapper. By default, a coroutine holds references to captured objects until it is finished or canceled. If your asynchronous framework does not support cancellation, the values you use inside the asynchronous block can be leaked. `asReference()` protects you from this.

##### 3.7 Using Anko

###### 3.7.1 Gradle-based project

Anko has a meta-dependency which plugs in all available features (including Commons, Layouts, SQLite) into your project at once:

```
dependencies {
    implementation "org.jetbrains.anko:anko:$anko_version"
}
```

Make sure that you have the `$anko_version` settled in your gradle file at the project level:

```
ext.anko_version='0.10.8'
```

If you only need some of the features, you can reference any of Anko's parts:

```
dependencies {
    // Anko Commons
    implementation "org.jetbrains.anko:anko-commons:$anko_version"

    // Anko Layouts
    implementation "org.jetbrains.anko:anko-sdk25:$anko_version" // sdk15, sdk19, sdk21, sdk23 are also available
    implementation "org.jetbrains.anko:anko-appcompat-v7:$anko_version"

    // Coroutine listeners for Anko Layouts
    implementation "org.jetbrains.anko:anko-sdk25-coroutines:$anko_version"
    implementation "org.jetbrains.anko:anko-appcompat-v7-coroutines:$anko_version"

    // Anko SQLite
    implementation "org.jetbrains.anko:anko-sqlite:$anko_version"
}
```

There are also a number of artifacts for the Android support libraries:

```
dependencies {
    // Appcompat-v7 (only Anko Commons)
    implementation "org.jetbrains.anko:anko-appcompat-v7-commons:$anko_version"

    // Appcompat-v7 (Anko Layouts)
    implementation "org.jetbrains.anko:anko-appcompat-v7:$anko_version"
    implementation "org.jetbrains.anko:anko-coroutines:$anko_version"

    // CardView-v7
    implementation "org.jetbrains.anko:anko-cardview-v7:$anko_version"

    // Design
    implementation "org.jetbrains.anko:anko-design:$anko_version"
    implementation "org.jetbrains.anko:anko-design-coroutines:$anko_version"

    // GridLayout-v7
    implementation "org.jetbrains.anko:anko-gridlayout-v7:$anko_version"

    // Percent
    implementation "org.jetbrains.anko:anko-percent:$anko_version"

    // RecyclerView-v7
    implementation "org.jetbrains.anko:anko-recyclerview-v7:$anko_version"
    implementation "org.jetbrains.anko:anko-recyclerview-v7-coroutines:$anko_version"

    // Support-v4 (only Anko Commons)
    implementation "org.jetbrains.anko:anko-support-v4-commons:$anko_version"

    // Support-v4 (Anko Layouts)
    implementation "org.jetbrains.anko:anko-support-v4:$anko_version"

    // ConstraintLayout
    implementation "org.jetbrains.anko:anko-constraint-layout:$anko_version"
}
```

There is an [example project](https://github.com/kotlin/anko-example) showing how to include Anko library into your Android Gradle project.

###### 3.7.2 IntelliJ IDEA project

If your project is not based on Gradle, just attach the required JARs from the [jcenter repository](https://jcenter.bintray.com/org/jetbrains/anko/) as the library dependencies and that's it.

##### 3.8 Contributing

The best way to submit a patch is to send us a [pull request](https://help.github.com/articles/about-pull-requests/). Before submitting the pull request, make sure all existing tests are passing, and add the new test if it is required.

If you want to add new functionality, please file a new *proposal* issue first to make sure that it is not in progress already. If you have any questions, feel free to create a *question* issue.

Instructions for building Anko are available in the [Wiki](https://github.com/Kotlin/anko/wiki/Building-Anko).