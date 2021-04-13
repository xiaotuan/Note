### 3.2.1　React中的可变状态：组件状态

让我们从状态API开始。虽然我们可以说所有组件都有某种“状态”（一般概念），但并不是React中的所有组件都有本地组件状态。从现在起，当我提到状态（state）时，我是在谈论React的API，而不是一般概念。继承自 `React.Component` 类的组件可以访问该API。React会为以此方式创建的组件建立并追踪一个支撑实例。这些组件还可以访问下一章将讨论的一系列生命周期方法。

通过 `this.state` 可以访问那些继承自 `React.Component` 的组件的状态。在这种情况下， `this` 引用的是类的实例，而 `state` 则是一个React会进行追踪的特殊属性。你可能认为只要对 `state` 进行赋值或者修改 `state` 的属性就能够更新 `state` ，但情况并非如此。让我们看看代码清单3-2中一个简单React组件中的组件状态示例。你可以在本地机器上创建这个代码。或者直接访问https://codesandbox.io/s/ovxpmn340y。

代码清单3-2　使用setState修改组件状态

```javascript
import React from "react";
import { render } from "react-dom";
class Secret extends React.Component{  ⇽--- 创建一个React组件，随着时间的推移，它会访问持久的组件状态——别忘了将类方法绑定到组件实例上
 constructor(props) {
     super(props);
     this.state = {
        name: 'top secret!',  ⇽--- 为组件提供一个初始状态以便在render()中尝试访问它时不会返回undefined或抛出错误
    };
     this.onButtonClick = this.onButtonClick.bind(this);  ⇽--- 创建一个React组件，随着时间的推移，它会访问持久的组件状态——别忘了将类方法绑定到组件实例上
  }
  onButtonClick() {  ⇽--- 初识setState，它是用于修改组件状态的专用API。调用setState时提供一个回调函数，该函数会返回一个新状态对象供React使用
    this.setState(() => ({
      name: 'Mark'
    }));
  }
  render() {
    return (
      <div>
        <h1>My name is {this.state.name}</h1>
            <button onClick={this.onButtonClick}>reveal the secret!</button>  ⇽--- 将显示名字的函数绑定到由按钮发出的点击事件上
      </div>
    )
  }
}
render(
     <Secret/>,
     document.getElementById('root')  ⇽--- 将顶层组件渲染到应用最高层的HTML元素中——可以用各种方式确定容器，只要ReactDOM能够找到它
);
```

代码清单3-2创建了一个简单的组件，当点击按钮时会使用 `setState` 更新组件状态从而揭示秘密的名字。注意，在 `this` 上可以使用 `setState` ，这是因为组件继承了 `React.Component` 类。

当点击按钮时，点击事件将被触发，提供给React用于响应事件的函数会被执行。当函数执行时，它会用一个对象作为参数来调用 `setState` 方法。这个对象有一个指向字符串的 `name` 属性。React会安排更新状态。当更新发生后， `React DOM` 会在需要时更新DOM。 `render` 函数会被再次调用，但这一次会有一个不同的值提供给包含 `this.state.name` 的JSX表达式语法（ `{}` ）。它会展示“Mark”而不是“top secret！”，我的秘密身份就暴露了！

通常情况下，由于性能和复杂性的影响，开发者想要尽可能谨慎地使用setState（React会为开发者追踪一些东西，而开发者则要在心里追踪另一部分数据）。有些模式在React社区中广受欢迎，它们能够使你几乎不使用组件状态（包括Redux、Mobx、Flux等），这些值得作为应用的可选项进行探索——实际上，我们会在第10章和第11章介绍Redux。尽管通常最好是使用无状态函数组件或者是依赖像Redux这样的模式，但使用setState本身并不是糟糕的做法——它仍然是修改组件中数据的主要API。

继续之前，需要注意绝对不要直接修改React组件中的 `this.state` 。如果尝试直接修改 `this.state` ，之后调用 `setState()` 可能替换掉已做出的改变，更糟糕的是，React并不知道对状态所做的变化。即使可以将组件状态当作可以改变的东西，但仍应该将 `this.state` 看作是在组件内不可改变的对象（就像props一样）。

这之所以重要还在于 `setState()` 不会立即改变 `this.state` 。相反，它创建了一个挂起的状态转换（下一章将更为深入地探讨渲染和变更检测）。因此，调用 `setState` 方法后访问 `this.state` 可能会返回现有值。因为所有这一切都使得调试情况变得棘手，所以只使用 `setState()` 来更改组件状态。

即使是像代码清单3-2中的小交互，也发生了很多事情。我们将在后续章节中继续分解React执行组件更新时所发生的种种步骤，但现在，更仔细地研究组件的 `render` 方法则更为重要。请注意，即便执行了状态改变并修改了相关数据，它仍会以一种相对可理解和可预测的方式发生。

尤其美妙的是，开发者可以一次性声明期望的组件外观和结构。没必要为了两个可能存在的不同状态做大量额外工作（展示或不展示高度机密名字）。React处理所有底层的状态绑定和更新过程，开发者只需要说 “名字应该在这里”。React的好处在于它不会强迫你思考每部分状态在每个时刻的情况，就像3.1.1节所做的那样。

让我们更仔细地了解一下setState API。它是改变React组件中的动态状态的主要方法，并且在应用中经常会使用它。让我们看一下方法签名，了解需要给它传递什么：

```javascript
setState(
  updater,
  [callback]
) -> void
```

`setState` 接收一个用来设置组件新状态的函数以及一个可选的回调函数。 `updater` 函数的签名如下：

```javascript
(prevState, props) => stateChange
```

之前版本的React允许传递一个对象而不是函数作为 `setState` 的第一个参数。之前版本的React与当前版本的React（16及以上）的一个关键区别在于：传递对象暗示着 `setState` 本质上是同步的，而实际发生的情况是React会安排一个对状态的更改。 `callback` 格式的签名更好地传递了这个信息并且更符合React的全面声明性异步范式：容许系统（React）安排更新，保证顺序但不保证时间。这与一种更加声明式的UI方法相契合，而且这比用命令式的方式在不同时刻指定数据更新（常常是竞态条件的源泉）更易于思考。

如果需要根据当前状态或属性对状态做一下更新，可以通过 `prevState` 和 `props` 参数来访问这些状态和属性。当要实现类似Boolean切换的东西或者在执行更新前需要知道上一个值时，这通常很有用。

让我们对 `setState` 的机制投注更多的关注。 `setState` 会使用 `updater` 函数返回的对象与当前状态进行浅合并。这意味着，开发人员可以生成一个对象，而React会将该对象的顶级属性合并到状态中。例如，有一个对象有属性 `A` 和属性 `B` ， `B` 有一些深层嵌套的属性而 `A` 只是一个字符串（ `'hi!'` ）。由于执行的是浅合并，因此只有顶级属性和它们引用的部分得以保留，而不是 `B` 的每个部分。React不会寻找 `B` 的深层嵌套属性进行更新。解决这个问题的方法是制作对象的副本，深层更新它，而后使用更新后的对象。也可以用 `immutable.js` 这样的库来让处理React的数据结构更容易。

`setState` 是一个用起来很直观的API，为ReactClass组件提供一些需要合并到当前状态中的数据，React会为你把它处理好。如果由于某些原因而需要监听过程的完成情况，可以使用可选的 `callback` 函数挂载到该过程。代码清单3-3展示了 `setState` 的一个实际的浅合并的例子。像之前一样，使用CodeSandbox可以很容易地创建和运行React组件。这可以省去在自己机器上进行设置的麻烦。

代码清单3-3　使用setState进行浅合并

```javascript
import React from "react";
import { render } from "react-dom";
class ShallowMerge extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {
       name: 'Mark', //  ⇽--- name存在于初始state的user属性中……
       colors: {
         favorite: '',
       }
      }
    };
    this.onButtonClick = this.onButtonClick.bind(this);
  }
  onButtonClick() {
    this.setState({
      user: { //        ⇽--- ……但正在设置的state中并没有name——如果它在上一级的话，浅合并就不会发挥作用了
        colors: {
          favorite: 'blue'
        }
      }
    });
  }
  render() {
    return (
      <div>
        <h1>My favorite color is {this.state.user.colors.favorite} and my
    name is {this.state.user.name}</h1>
        <button onClick={this.onButtonClick}>show the color!</button>
      </div>
    )
  }
}
render(
  <ShallowMerge />,
  document.getElementById('root')
);
```

初学React时，忘记浅合并是常见的问题来源。在这个示例中，当点击按钮时，内嵌在初始状态的 `user` 键内的 `name` 属性会被覆盖，因为新状态中没有它。本来打算保持这两个状态，但一个覆盖了另一个。



**练习3-1　思考setState API**

本章探讨了React管理组件内状态的组件API，所提及的事情之一就是需要通过seState API来修改状态，而不是直接修改。为什么这是一个问题而且为什么那样做行不通呢？试试https://codesandbox.io/s/j7p824jxnw。



