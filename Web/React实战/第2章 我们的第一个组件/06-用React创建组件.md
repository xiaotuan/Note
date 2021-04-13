### 2.2　用React创建组件

在这一部分，我们会创建一些React组件并在浏览器中运行它们。目前，还不需要使用Node.js或其他东西来搭建和运行这一切。可以用CodeSandbox在浏览器中运行代码。如果更喜欢在本地编辑文件，可以点击CodeSandbox代码编辑器的Download来获取该示例的源代码。

第一个组件将会用到3个库： `React` 、 `React DOM` 和 `prop-types` 。 `React DOM` 是React的渲染器，它从 `React` 主库分离出来以便更好地分离关注点。它将组件渲染为DOM或者处理为服务器端渲染的字符串。 `prop-types` 库是一个开发库，它可以帮你对传递给组件的数据做类型检查。

要开始创建评论框组件，得先创建一些组成部分，这将帮助我们更好地了解当React创建和渲染组件时会发生什么。我们需要添加一个ID为 `root` 的新DOM元素以及一些使用 `React DOM` 的基本代码。代码清单2-2展示了组件的起点。我为每个代码清单提供了一个在线运行版本的链接，可以很容易地编辑和尝试。

代码清单2-2　起步

```javascript
//... index.js
const node = document.getElementById("root");  ⇽--- 保存根元素的引用——React应用会被渲染到这个DOM元素中
//... index.html
<div id="root"></div>  ⇽--- 在index.html文件中创建了一个id为root的div
```

代码清单2-2的在线代码位于https://codesandbox.io/s/vj9xkqzkvy。

