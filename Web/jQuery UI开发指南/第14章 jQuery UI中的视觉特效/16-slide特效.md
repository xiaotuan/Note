### 14.1.14　 `slide` 特效

`slide` 特效能使元素以平移滑过屏幕的方式显示或隐藏。表14-13中列出了此特效的相关选项。

<center class="my_markdown"><b class="my_markdown">表14-13　管理 `slide` 特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.mode` | 显示（ `"show"` ）或隐藏（ `"hide"` ）元素。默认值为"hide" |
| `options.direction` | 指定滑动的方向： `"up"` （上）、 `"down"` （下）、 `"left"` （左，也是默认值）或"right"（右） |
| `options.distance` | 值为 `{width, height}` 的对象，用来设置元素应用特效之后的尺寸。在默认情况下，也取元素的当前尺寸 |

例如，要显示第一本书的同时使第二本书消失，我们写了如下的代码：

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css 
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<img id=img1 src=images/rails.jpg height=100 /><br /> 
<img id=img2 src=images/html.jpg height=100 />
<script>
$("#img1").effect ("slide", { mode : "show" }, 10000); 
$("#img2").effect ("slide", { mode : "hide" }, 10000); 
</script>
```

