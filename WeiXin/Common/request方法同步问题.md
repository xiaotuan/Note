<center><font size="5"><b>wx.request 方法同步问题</b></font></center>

`wx.request` 方法用于网络请求，它是异步执行的，如果需要在请求返回数据后才能进行其他操作的话，可以使用 `Promise` 需要将其转化成同步方法，具体代码如下：

```js
if(isCoincide(参数...)){
} else{
}

export function isCoincide(start_date, end_date, token){
  var res_data
  var promise = new Promise((resolve, reject) => {
    wx.request({
      url: url,
      data: {},
      header: header,
      success: function (res) {
        resolve(res);
        res_data = res.data
      },
      fail: function (res) {
        reject(res.errMsg || 'failed');
      }
    });
  });
  promise.then(()=>{
    console.log(res_data)
    return judgeCoincide(start_date, end_date, res_data)
  })
  console.log("end")
}
```