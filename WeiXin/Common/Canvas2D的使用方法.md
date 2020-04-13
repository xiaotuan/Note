<center><font size="5"><b>Canvas2D 的使用方法</b></font></center>

**wxml**
```xml
<canvas type="2d" id="myCanvas" />
```

**js**
```js
onReady: function () {
    const query = wx.createSelectorQuery()
    query.select('#myCanvas')
        .fields({ node: true, size: true })
        .exec((res) => {
          const width = res[0].width
          const height = res[0].height

          const canvas = res[0].node
          const ctx = canvas.getContext('2d')

          const dpr = wx.getSystemInfoSync().pixelRatio
          canvas.width = width * dpr
          canvas.height = height * dpr
          ctx.scale(dpr, dpr)

          // 把路径移动到画布中的坐标（10， 10）点
          ctx.moveTo(10, 10)
          // 新增一个新点（100， 10），创建一条从(10, 10)到（100， 10）的线条
          ctx.lineTo(100, 10)
          // 路径移动到画布中的坐标（10， 5）点
          ctx.moveTo(10, 70)

          // 新增一个新点（100， 5）， 创建一条从（10， 50）到（100， 50）的线条
          ctx.lineTo(100, 70)
          // 需要用stroke()方法来画线条
          ctx.stroke()
        })
  }
```