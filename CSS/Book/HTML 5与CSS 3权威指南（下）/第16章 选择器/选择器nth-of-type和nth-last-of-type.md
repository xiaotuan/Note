<center><font size="5"><b>选择器nth-of-type和nth-last-of-type</b></font></center>

##### 1. 使用选择器 nth-child 和 nth-last-child 时会产生的问题

```HTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <title>nth-of-type选择器与nth-last-of-type选择器使用示例</title>
    </head>
    <style type="text/css">
        h2:nth-child(odd) {
            background-color:yellow;
        }
        h2:nth-child(even) {
            background-color:skyblue;
        }
    </style>
    <body>
        <div>
            <h2>文章标题A</h2>
            <p>文章正文。</p>
            <h2>文章标题B</h2>
            <p>文章正文。</p>
            <h2>文章标题C</h2>
            <p>文章正文。</p>
            <h2>文章标题D</h2>
            <p>文章正文。</p>
        </div>
    </body>
</html>
```

运行结果并没有如预期的那样，让第奇数篇文章的标题背景色为黄色，第偶数篇文章的标题背景色为浅蓝色，而是所有文章标题都变成了黄色。

这个问题的产生原因在于：`nth-child` 选择器在计算子元素是第奇数个元素还是第偶数个元素时，是连同父元素中的所有子元素一起计算的。

##### 2. 使用选择器nth-of-type和nth-last-of-type

使用这两个选择器时，`CSS 3` 在计算子元素是第奇数个子元素还是第偶数个子元素时，就只针对同类型的子元素进行计算了。

```css
<style type="text/css">
    h2:nth-of-type(odd) {
        background-color: yellow;
    }
    h2:nth-of-type(even) {
        background-color: skyblue;
    }
</style>
```

可以使用 `nth-last-of-type` 选择器来代替 `nth-last-child` 选择器，进行倒序计算。