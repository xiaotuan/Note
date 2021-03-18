### 17.9.5　基于模板的Kotlin脚本

从Spring 4.3版本开始，Spring框架就提供了一个ScriptTemplateView，它使用支持JSR-223协议的脚本引擎来渲染模板，而Spring Framework 5.0进一步加强了对i18n以及模板嵌套的支持。Kotlin在1.1版本提供了对上述功能的支持并允许使用Kotlin的模板来渲染页面。

这样的变化带来了一些有趣的使用场景，例如使用kotlinx.html DSL或者带有内插的Kotlin来编写类型安全的模板。

```python
${include("header")}
<h1>${i18n("title")}</h1>
<ul>
    ${users.joinToLine{ "<li>${i18n("user")} ${it.firstname} ${it.lastname} </li>" }}
</ul>
${include("footer")}
```

