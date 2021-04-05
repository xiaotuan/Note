### 4.6.2　用Tiled创建拼板地图

本书使用Tiled创建拼板地图程序，它是一个优秀的拼板地图编辑器，兼容Mac OS、Windows和Linux。当然，拼板地图也可以手工设计。但是，如果使用Tiled这样的程序来代替复杂的体力活，那么地图创作工作会更加容易。Tiled是基于 GNU 免费软件许可证协议的。

提示

> 前面已经提到，读者不必非得使用这个软件。拼板地图还可以通过其他优秀（并且免费）的软件来创建，例如Mappy和Tile Studio，甚至可以使用微软的画板手绘。

创建拼板地图的目的是用可视化布局用来表现游戏画面的拼板网格，并且输出代表这些拼板的识别信息。在代码中，将这些输出数据用作一个二维数组，以在画布上建立拼板地图。

下面是创建简单拼板地图的基本步骤。这个拼版地图是使用Tile的创建的，后面的章节即将用到。

（1）从File菜单创建一个新的拼板地图。当它提问Orientation时，选择Orthogonal：Map Size 10 × 10，Tile Size 32 × 32。

（2）从Map菜单导入tanks_sheet.png文件作为拼板集。在这个菜单里选择“New tileset”并任意命名。在文件浏览器中找到在本书网站下载的tanks_sheet.png文件，确认Tile Width和Tile Height的值都是32，保留Margin和Spacing的值为0。

（3）从屏幕右下角的拼板集处选择一个拼板。选择好后，读者可以点选这个拼板并将其绘制在拼板地图上，只需在屏幕左上角选定一个位置即可。图4-9展示了为这个示例创建的拼板地图。

![65.png](../images/65.png)
<center class="my_markdown"><b class="my_markdown">图4-9　Tiled拼板地图示例</b></center>

（4）保存拼板地图。Tiled使用简单的文本文件格式，后缀名为.tmx。通常，Tild中的拼板数据存储为64位二进制文件格式，不过，也可以通过编辑Tiled预置对此进行更改。在Mac上，Preferences选项应该在Tiled菜单中（如果读者用的是Windows或者Linux版本的haunted，可以在File菜单中找到）。当设置这个预置的时候，在“Store tile layer data as”下拉菜单中选择CSV。完成后，在File菜单中保存文件。

在文本编辑器中查看已经保存的.tmx文件。

```javascript
<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0" orientation="orthogonal" width="10" height="10"
　　　　tilewidth="32" tileheight="32">
　 <tileset firstgid="1" name="tanks" tilewidth="32" tileheight="32">
　 <image source="tanks_sheet.png"/>
　 </tileset>
　 <layer name="Tile Layer 1" width="10" height="10">
　 <data encoding="csv">
32,31,31,31,1,31,31,31,31,32,
1,1,1,1,1,1,1,1,1,1,
32,1,26,1,26,1,26,1,1,32,
32,26,1,1,26,1,1,26,1,32,
32,1,1,1,26,26,1,26,1,32,
32,1,1,26,1,1,1,26,1,32,
32,1,1,1,1,1,1,26,1,32,
1,1,26,1,26,1,26,1,1,1,
32,1,1,1,1,1,1,1,1,32,
32,31,31,31,1,31,31,31,31,32
</data>
</layer>
</map>
```

数据是一个XML数据集，用于加载和保存拼板地图。该格式的开放属性以及这个拼板地图简单的几行数据，在JavaScript中很容易使用。现在，只需关心XML中<data>节点中的10行commadelimited数字。用户可以在代码中使用这几行数据来创建一个非常简单的二维数组。

