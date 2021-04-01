### 14.1.12　 `scale` 特效

`scale` 特效是用来放大或缩小元素的。它也可以用来显示和隐藏元素，取决于 `options.mode` 选项的设置。表14-11中列出了此特效的相关选项。

<center class="my_markdown"><b class="my_markdown">表14-11　管理 `scale` 特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.mode` | 显示（ `"show"` ）或隐藏（ `"hide"` ）元素。默认值为 `"effect"` （即只应用缩放特效，并不会伴随元素的出现或消失） |
| `options.direction` | 设置缩放发生的方向： `"horizontal"` （水平）、 `"vertical"` （垂直）或 `"both"` （同时包括水平和垂直方向）。默认值为 `"both"` |
| `options.from` | 值为 `{width, height}` 的对象，用来设置元素的原始尺寸。默认情况下，元素的当前尺寸即被当作原始尺寸 |
| `options.percent` | 放大（如果大于100）或缩小（如果小于100）的比例。 `options.mode` 值为 `"hide"` 的时候默认值为0，为 `"show"` 的时候默认值为100 |
| `options.fade` | 如果设置为 `true` ，元素缩放的同时其透明度也会发生变化。默认值为 `false` |

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css 
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<img id=img1 src=images/rails.jpg height=100 /><br /> 
<img id=img2 src=images/html.jpg height=100 />
<script>
$("#img1").effect ("scale", { mode : "show" }, 10000); 
$("#img2").effect ("scale", { mode : "hide" }, 10000); 
</script>
```

