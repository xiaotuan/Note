### 6.9.4　解决方案2：修改负责设置与尺寸相关样式的样式表的href属性

假定在文档中有如下与尺寸相关的样式表：

```css
<link rel="stylesheet" type="text/css" id="css_size" href="size-small.css" />

```

在这种情况下，可以定义如下 `setSize` 函数：

```css
var setSize = function(size) {
　　 var $css = jQuery('#css_size');
　　 $css.attr('href', 'size-' + size + '.css');
};

```

注意，在这种情况下，从服务器请求新的CSS文件，可能导致在样式变化发生时有短暂的延时。因此，这可能是最不受欢迎的方法。

