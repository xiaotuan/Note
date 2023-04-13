`Window` 对象的 `onload` 处理程序是最重要的事件处理程序之一。当显示在窗口中的文档内容稳定并可以操作时会触发他。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>load 事件处理程序</title>
        <!-- 本页的 css 样式表 -->
        <style type="text/css">
        	/* class="reveal" 的元素都不显示 */
            .reveal * {
                display: none;
            }
            /* 除了 class="handle" 的元素 */
            .reveal *.handle {
                display: block;
            }
        </style>
        <script type="text/javascript">
        	// 所有的页面逻辑在 onload 事件之后启动
        	window.onload = function() {
            	// 找到所有 class 名为 "reveal" 的容器元素
            	var elements = document.getElementsByClassName("reveal");
				for (var i = 0; i < elements.length; i++) {	// 对每个元素进行遍历
               		var elt = elements[i];
                    // 找到容器中的 "handle" 元素
                    var title = elt.getElementsByClassName("handle")[0];
                    // 当单击这个元素时，呈现剩下的内容
                    addRevealHandler(title, elt);
                }
                function addRevealHandler(title, elt) {
                	title.onclick = function() {
						if (elt.className == "reveal") {
							elt.className = "revealed";
						} else if (elt.className == "revealed") {
							elt.className = "reveal";
						}
					}
                }
            };
        </script>
    </head>
	<body>
		<div class="reveal">
			<h1 class="handle">Click Here to Reveal Hidden Text</h1>
			<p>This paragraph is hidden. It appears when you click on the title.</p>
		</div>
	</body>
</html>
```

