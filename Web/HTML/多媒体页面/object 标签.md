[toc]

### 1. `<object>` 标签

`object` 元素用于向页面添加多媒体对象，包括 `Flash`、音频、视频等。它规定了对象的数据和参数，以及可用来显示和操作的数据代码。`object` 元素中一般会包含 `<param>` 标签，该标签可用来定义播放参数。如果未显示 `object` 元素，就会执行位于 `<object>` 和 `</object>` 之间的代码。通过这种方式，我们能够嵌套多个 `object` 元素（每个对应一个浏览器）。

> 注意：`object` 元素和 `embed` 元素都是用来播放媒体文件的对象，`object` 元素用于 `IE` 浏览器，`embed` 元素用于非  IE 浏览器，为了保证兼容性，通常我们同时使用两个元素，浏览器会自动忽略它不支持的标签。同时使用两个元素时，应该把 `<embed>` 标签放在 `<object>` 标签的内部。

`<object>` 标签可以表示一个外部资源，可以将其视为一个映像、一个嵌套的浏览上下文，或者一个由插件处理的资源。

```html
<object width="400" height="400" data="helloworld.swf"></object>
```

> 提示：不要对图像使用 `<object>` 标签，请使用 `<img>` 标签代替。

**属性**

| 属性     | 值                                       | 描述                                                         |
| -------- | ---------------------------------------- | ------------------------------------------------------------ |
| align    | top \| bottom \| middle \| left \| right | HTML5 不支持。HTML 4.01 已废弃。规定 `<object>` 元素相对于周围元素的对齐方式。 |
| archive  | URL                                      | HTML5 不支持。由空格分隔的指向档案文件的 URL 列表。这些档案文件包含了与对象相关的资源 |
| border   | pixels                                   | HTML5 不支持。HTML 4.01 已废弃。规定 `<object>` 周围的边框宽度。 |
| classid  | class_ID                                 | HTML5 不支持。定义嵌入 Windows Registry 中或某个 URL 中的类的 ID 值，此属性可用来指定浏览器中包含的对象的位置，通常是一个 Java 类。 |
| codebase | URL                                      | HTML5 不支持。定义在何处可找到对象所需的代码，提供一个基准 URL。 |
| codetype | MIME_type                                | HTML5 不支持。通过 classid 属性所引用的代码的 MIME 类型。    |
| data     | URL                                      | 规定对象使用的资源的 URL。                                   |
| declare  | declare                                  | HTML5 不支持。定义该对象仅可被声明，但不能被创建或例示，直到该对象得到应用为止。 |
| form     | form_id                                  | 规定对象所属的一个或多个表单                                 |
| height   | pixels                                   | 规定对象的高度。                                             |
| hspace   | pixels                                   | HTML5 不支持。HTML 4.01 已废弃。规定对象左侧和右侧的空白。   |
| name     | name                                     | 为对象规定名称。                                             |
| standby  | text                                     | HTML5 不支持。定义当对象正在加载时所显示的文本。             |
| type     | MIME_type                                | 规定 data 属性中规定的数据的 MIME 类型                       |
| usemap   | #mapname                                 | 规定与对象一同使用的客户端图像映射的名称。                   |
| vspace   | pixels                                   | HTML5 不支持。HTML 4.01 已废弃。规定对象的顶部和底部的空白。 |
| width    | pixels                                   | 规定对象的宽度。                                             |
