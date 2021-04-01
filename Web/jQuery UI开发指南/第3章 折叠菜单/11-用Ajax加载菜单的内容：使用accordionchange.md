### 3.5.3　用Ajax加载菜单的内容：使用 `accordionchange` 

这个例子和前面的一样，只是在这里我们想通过 `bind ()` 方法来绑定 `accordionchange` 和 `accordionchangestart` 事件。代码如下：

```css
<!DOCTYPE html>
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<div id="accordion">
　<h1><a>Menu 1</a></h1>
　<div>Menu Contents 1</div>
　<h1><a>Menu 2</a></h1>
　<div>Menu Contents 2</div>
　<h1><a>Menu 3</a></h1>
　<div>Menu Contents 3</div>
</div>
<script>
$("#accordion").accordion ().bind ("accordionchangestart", function (event, menus)
{
　menus.newContent.html ("Loading");
}).bind ("accordionchange", function (event, menus)
{
　menus.newContent.load ("action.php");
});
</script>
```

action.php文件如下（内容和我们使用 `options.change` 和 `options.changestart` 时的是一模一样的）：

```css
<?
　$txt = "<span> Response sent by the server </span>";
　$txt = utf8_encode ($txt);
　echo ($txt);
?>
```

<a class="my_markdown" href="['#ac31']">①</a>　即幻灯片特效。——译者注



