### 14.1.5　 `clip` 特效

`clip` 特效能使元素以水平或垂直地滚动的方式出现或消失。表14-5中列出了此特效的相关选项。

<center class="my_markdown"><b class="my_markdown">表14-5　管理 `clip` 特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.mode` | 显示（ `"show"` ）或隐藏（ `"hide"` ）元素。默认值为"hide" |
| `options.direction` | 指定元素出现或消失的方向（水平 `"horizontal"` 或垂直 `"vertical"` ）。默认值为 `"vertical"` |

在下面的例子中，只有第二本书是可见的，而第一本是隐藏的（如图14-3所示）。使用此特效以移除第二本书并将第一本显示出来（如图14-4所示）。特效完成后，将仅剩第一本书可见（如图14-5所示）。

![118.png](../images/118.png)
<center class="my_markdown"><b class="my_markdown">图14-3　 `clip` 特效应用前：只有第二本书是可见的</b></center>

![119.png](../images/119.png)
<center class="my_markdown"><b class="my_markdown">图14-4　 `clip` 特效执行中：第二本书逐渐消失，而第一本书慢慢浮现</b></center>

![120.png](../images/120.png)
<center class="my_markdown"><b class="my_markdown">图14-5　特效完成后：只显示第一本书</b></center>

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css 
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<img id=img1 src=images/rails.jpg height=100 /><br /> 
<img id=img2 src=images/html.jpg height=100 />
<script>
$("#img1").effect ("clip", { mode : "show" }, 10000); 
$("#img2").effect ("clip", { mode : "hide" }, 10000); 
</script>
```

