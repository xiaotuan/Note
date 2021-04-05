### 19.7　Ajax

jQuery提供了一些可以简化Ajax调用的便捷方法。它暴露了一个名为ajax的方法，该方法允许通过Ajax调用来实现复杂的控制逻辑。另外，它还提供了方便的get和post方法，这两个方法涵盖了最常用的Ajax调用类型。虽然这些方法支持回调，不过它们也会返回promise，而用promise来处理服务器响应是一种比较推荐的方式。例如，可以使用get来重写之前的refreshServerInfo例子：

```javascript
function refreshServerInfo() {
    const $serverInfo = $('.serverInfo');
    $.get('http://localhost:7070').then(
        // 成功返回
        function(data) {
            Object.keys(data).forEach(p => {
                $('[data-replace="${p}"]').text(data[p]);
            }); 
        }, 
        function(jqXHR, textStatus, err) {
            console.error(err);
            $serverInfo.addClass('error')
                .html('Error connecting to server.');
        }
    ); 
} 
```

如大家所见，用jQuery大大简化了Ajax代码。

