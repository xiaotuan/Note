<center><font size="5"><b>scroll-view实现下拉刷新和加载更多功能</b></font></center>

1. `scroll-view` 本身就支持下拉刷新功能，因此可以直接使用该功能。
下面是与下拉刷新功能相关的属性说明：

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| :- | :- | :- | :- | :- | :- |
| refresher-enabled | boolean | false | 否 | 开启自定义下拉刷新 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| refresher-threshold | number | 45 | 否 | 设置自定义下拉刷新阈值 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| refresher-default-style | string | "black" | 否 | 设置自定义下拉刷新默认样式，支持设置 `black | white | none`， none 表示不使用默认样式 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| refresher-background | string | "#FFF" | 否 | 设置自定义下拉刷新区域背景颜色 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|refresher-triggered | boolean | false | 否 | 设置当前下拉刷新状态，true 表示下拉刷新已经被触发，false 表示下拉刷新未被触发 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindscrolltoupper | eventhandle |  | 否 | 滚动到顶部/左边时触发 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindscrolltolower | eventhandle |  | 否 | 滚动到底部/右边时触发 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindscroll | eventhandle |  | 否 | 滚动时触发，event.detail = {scrollLeft, scrollTop, scrollHeight, scrollWidth, deltaX, deltaY} | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindrefresherpulling | eventhandle |  | 否 | 自定义下拉刷新控件被下拉 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindrefresherrefresh | eventhandle |  | 否 | 自定义下拉刷新被触发 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindrefresherrestore | eventhandle |  | 否 | 自定义下拉刷新被复位 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindrefresherabort | eventhandle |  | 否 | 自定义下拉刷新被中止 | [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

下面是官方[示例代码](https://developers.weixin.qq.com/s/hGFhMum67de0)

+ 默认下拉刷新

  **wxml**

  ```wxml
  <scroll-view
    scroll-y style="width: 100%; height: 400px;"
    refresher-enabled="{{true}}"
    refresher-threshold="{{100}}"
    refresher-default-style="white"
    refresher-background="lightgreen"
    refresher-triggered="{{triggered}}"
    bindrefresherpulling="onPulling"
    bindrefresherrefresh="onRefresh"
    bindrefresherrestore="onRestore"
    bindrefresherabort="onAbort"
  >
    <view wx:for="{{arr}}" style="display: flex; height: 100px;">
      <image src="https://images.unsplash.com/photo-1565699894576-1710004524ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1832&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566402441483-c959946717ed?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1600&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566378955258-7633cb5c823e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566404394190-cda8c6209208?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=630&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566490595448-be523b4d2914?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=958&q=80"></image>
      </view>
  </scroll-view>
  ```

  **js**

  ```js
  const app = getApp()
  
  Page({
    data: {
      arr: [],
      triggered: false,
    },
    onReady: function () {
      const arr = []
      for (let i = 0; i < 100; i++) arr.push(i)
      this.setData({
        arr
      })
  
      setTimeout(() => {
        this.setData({
          triggered: true,
        })
      }, 1000)
    },
  
    onPulling(e) {
      console.log('onPulling:', e)
    },
  
    onRefresh() {
      if (this._freshing) return
      this._freshing = true
      setTimeout(() => {
        this.setData({
          triggered: false,
        })
        this._freshing = false
      }, 3000)
    },
  
    onRestore(e) {
      console.log('onRestore:', e)
    },
  
    onAbort(e) {
      console.log('onAbort', e)
    },
  })
  ```

+ 自定义下拉刷新样式（ `js` 代码同上）

  **wxml**

  ```xml
  <scroll-view
    scroll-y style="width: 100%; height: 400px;"
    refresher-enabled="{{true}}"
    refresher-threshold="{{80}}"
    refresher-default-style="none"
    refresher-background="lightgreen"
    bindrefresherpulling="{{refresh.onPulling}}"
  >
    <view slot="refresher" class="refresh-container"
      style="display: block; width: 100%; height: 80px; background: blue; display: flex; align-items: center;"
    >
      <view class="view1" style="position: absolute; text-align: center; width: 100%;">
        下拉刷新
      </view>
    </view>
  
    <view wx:for="{{arr}}" style="display: flex; height: 100px;">
      <image src="https://images.unsplash.com/photo-1565699894576-1710004524ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1832&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566402441483-c959946717ed?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1600&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566378955258-7633cb5c823e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566404394190-cda8c6209208?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=630&q=80"></image>
      <image src="https://images.unsplash.com/photo-1566490595448-be523b4d2914?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=958&q=80"></image>
      </view>
  </scroll-view>
  
  module.exports = {
    onPulling: function(evt, instance) {
      var p = Math.min(evt.detail.dy / 80, 1)
      console.log(p)
      var view = instance.selectComponent('.refresh-container')
      view.setStyle({
        opacity: p,
        transform: "scale(" + p + ")"
      })
    }
  }
  ```

  **wxss**

  ```css
  .intro {
    margin: 30px;
    text-align: center;
  }
  
  .trans {
    transition: .2s;
  }
  ```

  

2. 加载更多功能的实现思路是在 `scroll-view` 组件的最后加一个加载更多视图，然后实现 `bindscrolltolower` 的事件处理方法，当用户滚动到底部的时候将会调用该处理方法，只是直接在该方法内添加加载更多的实现即可。

> 注意：要使下拉刷新有效, `scroll-view` 及其容器必须设定容器的 `width` 和 `height` 。否则无法显示下拉刷新界面。