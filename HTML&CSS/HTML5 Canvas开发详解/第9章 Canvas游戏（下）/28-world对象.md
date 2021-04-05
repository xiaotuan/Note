### 9.4.6　world对象

world对象仅仅包含了创建游戏世界所需的必要信息。镜头负责在世界上滚动并展现给用户。真实的世界不会作为一个可见的对象展示给用户。

```javascript
world.cols=15;
world.rows=15;
world.tileWidth=32;
world.tileHeight=32;
world.height=world.rows*world.tileHeight;
world.width=world.cols*world.tileWidth;
world.map=[];
```

cols和rows定义了整个世界的大小，tileHeight和tileWidth属性的值将用在确定镜头位置计算和在camera上绘制世界区块的过程中。height和width用于计算前面的4个值，map数组则用于存储之前展示的地图数据。

