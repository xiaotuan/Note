### 14.1.8　 `fold` 特效

`fold` 特效以先水平而后垂直地收起或展开的方式来显示和隐藏元素（也可以通过设置 `options.horizFirst` 来将方向顺序颠倒过来）。表14-8中列出了此特效的相关选项。

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css 
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<img id=img1 src=images/rails.jpg height=100 /><br /> 
<img id=img2 src=images/html.jpg height=100 />
<script>
$("#img1").effect ("fold", { mode : "show", horizFirst : true, size : 75 }, 1000); 
$("#img2").effect ("fold", { mode : "hide", size : 75 }, 1000); 
</script>
```

<center class="my_markdown"><b class="my_markdown">表14-8　管理 `fold` 特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.mode` | 显示（ `"show"` ）或隐藏（ `"hide"` ）元素。默认值为"hide" |
| `options.horizFirst` | 当设置为 `true` 时， `fold` 特效将先从水平方向开始，而后是垂直方向（选项设为 `false` 的话，则方向顺序会反过来）。默认值为 `false` |
| `options.size` | 设定特效的第一步收起或展开的距离（无论水平还是垂直方向）。默认值为15个像素 |

