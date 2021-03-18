### 14.6.2　Anko核心组件与工具

Anko作为一个DSL脚手架工具，提供了很多常用的组件和工具来协助开发者进行Android应用程序开发，常见的有Intent、Dialog、Toast、Logging、Resources和Dimension，这里仅介绍其中的3个。

#### 1．Intent

众所周知，Intent是Android中一个使用频率极高的工具类，主要用来在一个组件中启动另一个组件并进行数据的传递工作。在Kotlin中，要使用Anko提供的Intent功能，应在build.gradle文件中添加Anko配置。

```python
dependencies {
    compile "org.jetbrains.anko:anko-commons:$anko_version"
}
```

例如，下面是使用Intent启动一个新的Activity并通过extra向这个新的Activity传递数据的实例。

```python
val intent = Intent(this, SomeOtherActivity::class.java)
intent.putExtra("id", 5)
intent.setFlag(Intent.FLAG_ACTIVITY_SINGLE_TOP)
startActivity(intent)
```

如果使用Anko提供的方法，则上面的代码可以简写为如下方式。

```python
startActivity(intentFor<SomeOtherActivity>("id" to 5).singleTop())
```

如果不需要设置Activity的启动模式，则可以简写为如下格式。

```python
startActivity<SomeOtherActivity>("id" to 5)
```

除此之外，Intent还内置了一些常用的方法，如表14-1所示。

<center class="my_markdown"><b class="my_markdown">表14-1　Intent内置函数</b></center>

| 函数名 | 功能描述 | 函数名 | 功能描述 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| makeCall(number) | 打电话 | share(text, [subject]) | 分享文本消息 |
| sendSMS(number, [text]) | 发送文本消息 | email(email, [subject], [text]) | 发送Email文本 |
| browse(url) | 浏览网页 |

#### 2．Dialog

Dialog是Android开发中常见的弹框组件，在Anko中使用Dialog组件需要添加如下配置。

```python
dependencies {
    compile "org.jetbrains.anko:anko-commons:$anko_version"
    compile "org.jetbrains.anko:anko-design:$anko_version"  // SnackBar配置
}
```

除此之外，Dialog组件还提供了常见的SnackBar、Alert和Selector等不同的弹框样式。例如，下面是使用Anko实现的一个国家下拉列表。

```python
val countries = listOf("Russia", "USA", "Japan", "Australia")
selector("Where are you from?", countries, { dialogInterface, i ->
    toast("So you're living in ${countries[i]}, right?")
})
```

#### 3．Logging

AnkoLogger是Anko提供的Android日志工具，其使用方法如下。

```python
class SomeActivity : Activity(), AnkoLogger {
    private fun someMethod() {
        info("London is the capital of Great Britain")
        debug(5)
        warn(null)
    }
}
```

和Android系统提供的日志工具一样，AnkoLogger同样可以实现不同级别的日志打印，其对应关系如表14-2所示。

<center class="my_markdown"><b class="my_markdown">表14-2　android.util.Log和AnkoLogger对应关系</b></center>

| android.util.Log | AnkoLogger | android.util.Log | AnkoLogger |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| v() | verbose() | w() | warn() |
| d() | debug() | e() | error() |
| i() | info() | wtf() | wtf() |

