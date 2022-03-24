`Colors` 是一个很简单的模块，可以给 `console.log` 输出提供不同的颜色以及风格，这基本是它全部的功能。 

安装 `Colors`：

```console
$ npm install colors
```

引入 colors 库：

```js
var colors = require('colors')
```

使用 `Colors` ：

```js
console.log('This Node kicks it! '.rainbow.underline)
```

可以对 console 信息的不同部分进行不同的样式修改：

```js
console.log('rainbow'.rainbow, 'zebra'.zebra)
```

使用 `Colors` 的预先设置或者创建自己的主题：

```js
colors.setTheme({
  mod1_warn: 'cyan',
  md1_error: 'red',
  md2_note: 'yellow'
})

console.log('This is a helpfuul message'.md2_note)
console.log('This is a bad message'.md1_error)
```
