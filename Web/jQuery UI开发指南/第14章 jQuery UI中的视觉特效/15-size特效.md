### 14.1.13　 `size` 特效

和 `scale` 特效允许等比例缩放尺寸不同， `size` 特效能给元素指定新的宽度和高度。这可以通过给 `options.to` 赋予一个值为 `{width, height}` 的对象来实现。如果没有在 `options.to` 中指定 `width` 或者 `height` ，则元素不会在对应的方向（宽度对应水平方向，高度对应垂直方向）上调整尺寸。表14-12中列出了此特效的相关选项。

<center class="my_markdown"><b class="my_markdown">表14-12　管理 `size` 特效的选项</b></center>

| 选项 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `options.from` | 值为 `{width, height}` 的对象，用来设置元素的原始尺寸。默认情况下，元素的当前尺寸即被当作原始尺寸 |
| `options.to` | 值为 `{width, height}` 的对象，用来设置元素应用特效之后的尺寸。默认情况下，也取元素的当前尺寸 |

例如，如果要把图片扩展到300个像素宽，而保持100个像素的高度不变（如图14-11所示），可以编写如下代码：

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css 
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<img id=img1 src=images/rails.jpg height=100 /><br />
 <script>
$("#img1").effect ("size", { to : { width : 300 } }, 1000); 
</script>
```

![126.png](../images/126.png)
<center class="my_markdown"><b class="my_markdown">图14-11　 `size` 特效</b></center>

