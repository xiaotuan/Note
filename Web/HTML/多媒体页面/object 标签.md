[toc]

`object` 元素用于向页面添加多媒体对象，包括 `Flash`、音频、视频等。它规定了对象的数据和参数，以及可用来显示和操作的数据代码。`object` 元素中一般会包含 `<param>` 标签，该标签可用来定义播放参数。

`<object>` 标签里的 `classid` 属性用来告诉浏览器插件的类型；`codebase` 属性可选，未安装 `Flash` 插件的用户在浏览网页时，会自动连接到 `codebase` 属性指定的 `Shockwave` 的下载网页，自动下载并安装相关插件。`<object>` 和 `<embed>` 标签里 `quality = high` 的作用是使浏览器以高质量浏览动画。

> 注意：`object` 元素和 `embed` 元素都是用来播放媒体文件的对象，`object` 元素用于 `IE` 浏览器，`embed` 元素用于非  IE 浏览器，为了保证兼容性，通常我们同时使用两个元素，浏览器会自动忽略它不支持的标签。同时使用两个元素时，应该把 `<embed>` 标签放在 `<object>` 标签的内部。

### 1. 插入音频文件

在 `<object></object>` 标记之间加入如下代码：

```html
<param name="filename" value="音频文件的地址" />
```

**示例代码：**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=gb2312" />
        <title>插入音频文件</title>
    </head>
    <body>
        <object classid="clsid:22D6F312-B0F6-11D0-94AB-0080C74C7E95" width="530" height="375">
            <param name="FileName" value="F:\TM\sl\10\z\zj.mp3"/>
            <embed src="F:\TM\sl\10\z\zj.mp3" width="530" height"375"></embed>
        </object>
    </body>
</html>
```

