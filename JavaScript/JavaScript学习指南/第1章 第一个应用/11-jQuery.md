### 1.6　jQuery

将会在页面中引入一个非常流行的客户端脚本库 -- jQuery. 虽然这不是必须的，甚至与手头的任务关系不大，但在开发中，往往会最先将这个无处不在的类库引入到网页代码中。在这个例子中，即便没有引入jQuery，也能很轻易地搞定，但是，越早开始习惯jQuery代码会越好。

在HTML文件body标签的最下面，在引入main.js之前，引入jQuery：

```html
<script src="https://code.jquery.com/jquery-2.1.1.min.js"></script> 
<script src="main.js"></script>
```

这里使用了一个网络链接，意味着如果网络不可用时，页面就不能正常工作了。从一个公共的内容分发网络（CDN：content delivery network）来加载jQuery，这点有利于保证性能。如果在无网络的情况下工作，就必须把文件下载到本地，然后从本地加载文件。现在对main.js文件做些修改，使之用上一个jQuery的特性。

```javascript
$(document).ready(function() {
    'use strict';
    console.log('main.js loaded');
});
```

如果没有使用jQuery的经验，上面这段代码看起来可能会有些费解。事实上，这里提到的很多东西在后面的章节中都有详细的讲解。在这里，jQuery确保了所有的HTML文件都在JavaScript执行之前加载完成。（虽然现在JavaScript代码只有一句简单的console.log）。每次使用基于浏览器的JavaScript时，都会将JavaScript代码写在$(document).ready(function(){和})；之间，从而帮助建立好的编程习惯。注意到 ’use strict’ 了吗，后面的章节里会详细介绍它，它会让JavaScript解释器更严格地对待所写的代码。乍听起来好像不那么友好，事实上它会帮助写出更好的JavaScript代码，也避免一些常见却又难以定位的问题。本书中的JavaScript都将严格遵循语法规范。

