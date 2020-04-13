<center><font size="5"><b>自定义Switch组件</b></font></center>

**wxml**

```xml
<view class="container">
  <view class="custom-switch" catchtouchstart='handletouchstart' catchtouchmove='handletouchmove' catchtouchend='handletouchend' catchtouchcancel='handletouchcancel' bindtap="swicthclick">
    <view class="thumb" style="margin-left:{{marginLeft}}%;"></view>
    <view class="content">
      <view class="left" style="color:{{marginLeft < 25 ? '#ffffff' : '#87C682'}};">断开</view>
      <view class="right" style="color:{{marginLeft >= 25 ? '#ffffff' : '#87C682'}};">连接</view>
    </view>
  </view>
</view>
```

**wxss**

```css
.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.custom-switch {
  width: 146rpx;
  height: 56rpx;
  background: #F7F6F6;
  border-radius: 30rpx;
}

.thumb {
  position: relative;
  top: 0;
  width: 50%;
  height: 100%;
  background: #87C682;
  border-radius: 30rpx;
}

.content {
  position: relative;
  top: -100%;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}

.left {
  font-size: 26rpx;
  color: white;
  width: 50%;
  line-height: 100%;
  text-align: center
}

.right {
  font-size: 26rpx;
  color: #87C682;
  width: 50%;
  line-height: 100%;
  text-align: center
}
```

**js**

```js
var lastX = 0
var lastY = 0
var lastMarginLeft = 0
var isTap = false
Page({

  /**
   * 页面的初始数据
   */
  data: {
    switchWidth: 0,
    marginLeft: 50,
    isOn: false,
  },

  //页面触摸开始事件，必须在触摸开始方法中调用此方法
  handletouchstart: function (event) {
    lastX = event.touches[0].clientX
    lastY = event.touches[0].clientY
    lastMarginLeft = this.data.marginLeft
    isTap = true
    console.log(event)
  },
  //页面触摸移动事件，必须在触摸开始方法中调用此方法
  handletouchmove: function (event) {
    let x = event.touches[0].clientX
    let y = event.touches[0].clientY
    let distance = x - lastX
    if (x !== lastX || y != lastY) {
      isTap = false
    }
    var left = lastMarginLeft / 100 * this.data.switchWidth + distance
    console.log("move: " + distance + " left: " + left + " width: " + this.data.switchWidth)
    if (distance >= 0) {
      if (left > this.data.switchWidth / 2) {
        left = 0.5
      } else {
        left = left / this.data.switchWidth
      }
    } else {
      if (left <= 0) {
        left = 0
      } else {
        left = left / this.data.switchWidth
      }
    }
    console.log(left)
    this.setData({
      marginLeft: parseInt(left * 100)
    })
    console.log("marginLeft: " + this.data.marginLeft)
  },
  //页面触摸结束事件，必须在触摸开始方法中调用此方法
  handletouchend: function (event) {
    console.log("end: " + isTap)
    if (isTap) {
      this.setData({
        marginLeft: lastMarginLeft === 50 ? 0 : 50,
        isOn: lastMarginLeft === 50 ? false : true
      })
    } else {
      var left = 0;
      if (this.data.marginLeft > 25) {
        left = 50;
      }
      this.setData({
        marginLeft: left,
        isOn: left == 50
      })
    }
    isTap = false
  },
  //页面触摸取消事件，必须在触摸开始方法中调用此方法
  handletouchcancel: function (event) {
    console.log("cancel")
    this.setData({
      marginLeft: lastMarginLeft === 50 ? 0 : 50,
      isOn: lastMarginLeft === 50 ? false : true
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    var that = this
    wx.createSelectorQuery().selectAll('.custom-switch').boundingClientRect(function (rects) {
      rects.forEach(function (rect) {
        console.log(rect.width)
        that.data.switchWidth = rect.width
      })
    }).exec();
  },

})
```
