<center><font size="5"><b>使用云函数获取 sessionKey 和 openId</b></font></center>

1. 创建云函数 `getSessionKey`。

**index.js**
```js
// 云函数入口文件
const cloud = require('wx-server-sdk')
const request = require('request')

cloud.init()

const db = cloud.database()

const wx = {
  appid: 'appid',
  secret: 'secret'
}

// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()
  console.log(event)
  var session = {}
  var url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + wx.appid + '&secret=' + wx.secret + '&js_code=' + event.code + '&grant_type=authorization_code'
  var promise = new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      // console.log('session: ' + body)
      resolve(body)
    })
  })
  await promise.then(res => {
    // console.log(res)
    session = JSON.parse(res)
  })

  return {
    event,
    session: session,
  }
}
```

**package.json**
```json
{
  "name": "getSessionKey",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "wx-server-sdk": "latest"
  }
}
```

> `secret` 是在微信公众平台中生成的。
>
> 请求地址如果有变化请参照[微信小程序文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html) 中加密数据解密算法的多种编程语言的示例代码（[点击下载](https://res.wx.qq.com/wxdoc/dist/assets/media/aes-sample.eae1f364.zip))
2. 在 `app.js` 文件中的 `wx.login` 后添加调用云函数的代码，并将其存储起来。

**app.js**

```js
onLaunch: function () {
    ...

    // 登录
    wx.login({
      success: res => {
        console.log("code: " + res.code)
        wx.cloud.callFunction({
          name: "sessionKey",
          data: {
            code: res.code
          },
          success: res => {
            wx.setStorageSync("getSessionKey", res.result.session.session_key)
            wx.setStorageSync("openid", res.result.session.openid)
          },
          fail: res => {
            console.log(res)
          }
        })
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    
    ...
    
}
```