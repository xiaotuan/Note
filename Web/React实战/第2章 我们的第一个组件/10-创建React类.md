### 2.2.4　创建React类

要开始真正地构建东西，需要的不只是React元素，还需要组件。如前所述，React组件（创建自函数的组件）就像是React元素，但React组件拥有更多特性。React中的组件是帮助将React元素和函数组织到一起的类。它们可以被创建为扩展自 `React.Component` 基类的类或是函数。本节将探索React的类以及如何在React中使用这种类型的组件。让我们看看如何创建React的类。

```javascript
class MyReactClassComponent extends Component {
     render() {}
}
```

与使用 `React.createElement` 时调用React库中的特定方法不同，由 `React.Component` 创建组件是通过声明一个继承自React.Component抽象基类的JavaScript类来实现的。这个继承类通常需要至少定义一个 `render` 方法，这个 `render` 方法会返回单个React元素或是一个React元素的数组。创建React类的老办法是使用 `createClass` 方法。这种方式随着JavaScript的类的到来而发生了改变，虽然我们仍旧能使用 `create-react-class` 模块（npm上仍然提供），但现在这不是被鼓励的方式。

