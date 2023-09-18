让我们来看一下在 `HTML5` 中的标记方法：

+ 内容类型（ `ContentType` ）

  `HTML5` 文件的扩展名和内容类型没有发生变化，即扩展名还是 `.html` 或 `.htm`，内容类型还是 `text/html`。

+ DOCTYPE 声明

  要使用 `HTML5` 标记，必须先进行如下的 `DOCTYPE` 声明。不区分大小写。`Web` 浏览器通过判断文件开头有没有这个声明，让解析器和渲染类型切换成对应 `HTML5` 的模式。

  ```html
  <!DOCTYPE html>
  ```

  另外，当使用工具时，也可以在 `DOCTYPE` 声明方式中加入 `SYSTEM` 标识。不区分大小写。此外还可将双引号换为单引号来使用，声明方法如下面的代码。

  ```html
  <!DOCTYPE html SYSTEM "about:legacy-compat">
  ```

+ 字符编码的设置

  以前，设置 `HTML` 文件的字符编码时，要用到 `meta` 元素，代码如下：

  ```html
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
  ```

  在 `HTML5` 中，可以使用 `<meta>` 元素的新属性 `charset` 来设置字符编码：

  ```html
  <meta charset="UTF-8">
  ```

  以上两种方法都有效。但二者不能同时使用。如下所示代码的使用方法是错误的。

  ```html
  <!-- 不能混合使用charset 属性和http-equiv 属性 -->
  <meta charset="UTF-8" http-equiv="Content-Type" content="text/html;charset=UTF-8">
  ```

  