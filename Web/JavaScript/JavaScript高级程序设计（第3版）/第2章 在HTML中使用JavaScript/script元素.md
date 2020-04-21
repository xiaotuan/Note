向 `HTML` 页面中插入 `JavaScript` 的主要方法，就是使用 `<script>` 元素。`HTML 4.01` 为 `<script>` 定义了下列 6 个属性。
+ `async`：可选。表示应该立即下载脚本，但不应妨碍页面中的其他操作，比如下载其他资源或等待加载其他脚本。只对外部脚本文件有效。
+ `charset`：可选。表示通过 `src` 属性指定的代码的字符集。由于大多数浏览器会忽略它的值，因此这个属性很少有人用。
+ `defer`：可选。表示脚本可以延迟到文档完全解析和显示之后再执行。只对外部脚本文件有效。
+ `language`：已废弃。原来用于表示编写代码使用的脚本语言（如 `JavaScript`、`JavaScript 1.2` 或 `VBScript` ）。大多数浏览器会忽略这个属性，因此也没有必要再用了。
+ `src`：可选。表示包含要执行代码的外部文件。
+ `type`：可选。可以看成是 `language` 的替代属性；表示编写代码使用的脚本语言的内容类型（也称为 `MIME` 类型）。虽然 `text/javascript` 和 `text/ecmascript` 都已经不被推荐使用，但人们一直以来使用的都还是`text/javascript`。 实际上，服务器在传送 `JavaScript` 文件时使用的 `MIME` 类型通常是 `application/x-javascript`，但在 type 中设置这个值却可能导致脚本被忽略。另外，在非 IE 浏览器中还可以使用以下值： `application/javascript` 和 `application/ecmascript`。考虑到约定成俗和最大限度的浏览器兼容性，目前type属性的值依旧还是 `text/javascript`。不过这个属性并不是必须的，如果没有指定这个属性，则其默认值仍为 `text/javascript`。