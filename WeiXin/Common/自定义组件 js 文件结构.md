<center><font size="5"><b>自定义组件 js 文件结构</b></font></center>

```js
Component({
    behaviors: []
    options: {
        multipleSlots: true,	// 在组件定义时的选项中启用多slot支持
        styleIsolation: 'isolated', // 可用值：isolated、apply-shared、shared
        addGlobalClass: true,	// 等价于设置 styleIsolation: apply-shared, styleIsolation失效
        externalClasses: ['my-class'],	// 引入外部样式类
    },
    properties: {
    	myProperty: { // 属性名
          type: String,
          value: ''
    	},
    	myProperty2: String // 简化的定义方式
	},
    data: {	// 私有数据， 可用于模板渲染
        
    },
    lifetimes: {
        // 生命周期函数，可以为函数，或一个在methods段中定义的方法名
        attached: function () { },
        moved: function () { },
        detached: function () { },
    },

    // 生命周期函数，可以为函数，或一个在methods段中定义的方法名
    attached: function () { }, // 此处attached的声明会被lifetimes字段中的声明覆盖
    ready: function() { },

    pageLifetimes: {
        // 组件所在页面的生命周期函数
        show: function () { },
        hide: function () { },
        resize: function () { },
    },
    methods: {
        onTap: function(){
          var myEventDetail = {} // detail对象，提供给事件监听函数
          var myEventOption = {} // 触发事件的选项
          this.triggerEvent('myevent', myEventDetail, myEventOption)
        },
        onMyButtonTap: function(){
          this.setData({
            // 更新属性和数据的方法与更新页面数据的方法类似
          })
        },
        // 内部方法建议以下划线开头
        _myPrivateMethod: function(){
          // 这里将 data.A[0].B 设为 'myPrivateData'
          this.setData({
            'A[0].B': 'myPrivateData'
          })
        },
        _propertyChange: function(newVal, oldVal) {

        }
    },
    observers: {
    'numberA, numberB': function(numberA, numberB) {
      // 在 numberA 或者 numberB 被设置时，执行这个函数
      this.setData({
        sum: numberA + numberB
      })
    }
  }
})
```

