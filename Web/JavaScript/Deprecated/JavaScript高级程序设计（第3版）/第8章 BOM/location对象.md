`location` 对象既是 `window` 对象的属性，也是 `document` 对象的属性，它们引用的是同一个对象。下表列出了 `location` 对象的所有属性：

| 属性名 | 例子 | 说明 |
| :- | :- | :- |
| hash | "#contents" | 返回 URL 中的 hash （#号后跟零或多个字符串），如果 URL 中不包含散列，则返回空字符串 |
| host | "www.wrox.com:80" | 返回服务器名称和端口号（如果有） |
| hostname | "www.wrox.com" | 返回不带端口号的服务器名称 |
| href | "http://www.wrox.com" | 返回当前加载页面的完整 URL。而 location 对象的 toString() 方法也返回这个值 |
| pathname | "/WileyCDA/" | 返回 URL 中的目录和（或）文件名 |
| port | "8080" | 返回 URL 中指定的端口号。如果 URL 中不包含端口号，则这个属性返回空字符串 |
| protocol | "http:" | 返回页面使用的协议。通常是 http: 或 https: |
| search | "?q=javascript" | 返回 URL 的查询字符串。这个字符串以问号开头 |

使用 `location` 对象可以改变浏览器的位置，最常用的方式是使用 `assign()` 方法并为其传递一个 URL。

```js
location.assign("http://www.wrox.com")
```

如果是将 `location.href` 或  `window.location` 设置为一个 URL值，也会以该值调用 `assign()`方法。

```js
window.location = "http://www.wrox.com"
location.href = "https://www.wrox.com"
```

修改 `location` 对象的其他属性也可以改变当前加载的页面。

```js
// 假设初始 URL 为 http://www.wrox.com/WileyCDA/

// 将 URL 修改为 "http://www.wrox.com/WileyCDA/#section1"
location.hash = "#section1"

// 将 URL 修改为 "http://www.wrox.com/WileyCDA/?q=javascript"
location.search = "?q=javascript"

// 将 URL 修改为 "http://www.yahoo.com/WileyCDA"
location.hostname = "www.yahoo.com"

// 将 URL 修改为 "http://www.yahoo.com/mydir/"
location.pathname = "mydir"

// 将 URL 修改为 "http://www.yahoo.com:8080/WileyCDA/"
location.port = 8080
```

每次修改 `location` 的属性（hash除外），页面都会以新URL重新加载。

> 在 IE 8、Firefox 1、Safari 2+、Opera 9+ 和 Chrome 中，修改 hash 的值会在浏览器的历史记录中生成一条新记录。

当通过上述任何一种方式修改 URL 之后，浏览器的历史记录中就会生成一条新记录。要禁用这种行为，可以使用 `replace()`方法。这个方法只接受一个参数，即要导航到的 URL。在调用 `replace()` 方法之后，用户不能回到前一个页面。

`reload()` 的作用是重新加载当前显示的页面。如果调用 `reload()` 时不传递任何参数，页面就会以最有效的方式重新加载。如果要强制从服务器重新加载，则需要像下面这样为该方法传递参数 true。

```js
location.reload()	// 重新加载（有可能从缓存中加载）
location.reload(true)	// 重新加载（从服务器重新加载）
```
