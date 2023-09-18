[toc]

### 1. 能使用 css 代替的元素

对于 `basefont`、`big`、`center`、`font`、`s`、`strike`、`tt`、`u` 这些元素，由于它们的功能都是纯粹为画面展示服务的，而在 `HTML5` 中提倡把画面展示性功能放在 `css` 样式表中统一编辑，所以将这些元素废除，并使用编辑 `css` 样式表的方式进行替代。

### 2. 不再使用 frame 框架

对于 `frameset` 元素、`frame` 元素与 `nofranes` 元素，由于 `frame` 框架对页面可移性存在负面影响，在 `HTML5` 中已不再支持 `frame` 框架，只支持 `iframe` 框架，或者用服务器方创建的由多个页面组成的复合页面的形式，同时将以上 3 个元素废除。

### 3. 只有部分浏览器支持的元素

对于 `applet`、`bgsound`、`blink`、`marguee` 等元素，由于只有部分浏览器支持这些元素，所以在 `HTML5` 中被废除。其中，`applet` 元素可由 `embed` 元素替代，`bgsound` 元素可由 `audio` 元素替代，`marquee` 可以由 `JavaScript` 编程的方式替代。