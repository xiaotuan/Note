### 7.2.4　匹配URL路径和参数化路由

我们已经创建了一些辅助方法，但还没有做任何路由的工作。为了开始将URL匹配到组件，需要将路由添加到路由器中。要如何做呢？本质上，需要找到一种方法基于当前URL渲染给定的组件——我一直讨论的“匹配”部分。也许听起来没有太多工作，但涉及的步骤也不少。

首先，让我们看看浏览器前端路由系统的一个关键部分：路径匹配。我们需要一些方法来对路径字符串求值并将它们转换为能够使用的有意义的数据。我们会用一个名为 `enroute` 的小软件包来完成这个工作，它本身就是一个微型路由器，我们将使用它把路径匹配到组件。 `enroute` 内部可以将字符串转换为可用于匹配字符串的正则表达式（如要检查的URL）。也可以用它来指定路径参数，从而可以创建像 `/users/:user` 这样的路径，然后就可以在代码中用类似 `route.params.user` 的方式获取 `/users/1234` 中的用户ID。这种方法很常见，如果使用过express.js的话，也许已经见过类似的做法。

这种参数化URL的能力很有用，因为通过这种方式就可以将URL视为另一种可以传递给路由器的数据输入形式。URL很强大，使它们动态化是其中一个原因。URL可以是表意的并且能让用户直接访问资源，而无须先访问一个页面，再导航多次才能到达他们想去的地方。

虽然没有使用参数化路由的全部能力，但让我们看一些示例，确保清楚工作的走向。表7-1展示了几个在普通Web应用中可能很有用的URL路径示例。

<center class="my_markdown"><b class="my_markdown">表7-1　常见的参数化路由示例</b></center>

| 路由 | 使用示例 |
| :-----  | :-----  | :-----  | :-----  |
| `/` | 应用程序的主页 |
| `/profile` | 用户的个人配置页面，展示一些配置 |
| `/profile/settings` | 设置的路由，个人配置页面的子页面，展示用户相关的设置 |
| `/posts/:postID` | `postID` 可以用于代码层面，示例路由可能是/posts/2391448。如果想创建指向特定帖子的公开链接，它非常有用 |
| `/users/:userID` | `:userID` 是一个路径参数，对基于用户ID展示特定的用户非常有用 |
| `/users/:userID/posts` | 展示一个用户的所有帖子，URL的: `userID` 部分是动态的并可以在代码中获取 |

`:name` 语法只利用了参数化路由的一个方面，还有一些工具可以做更多事情。如果有兴趣学习更多参数化路由的知识，可以检出 `path-to-regexp` 库，它是一个很强大的工具，还有些其他东西值得我们花时间了解一下，但我们还是要把精力集中到手头的任务上：React路由。

这些路由工具（ `enroute` 和 `path-to-regexp` ）的重要用途在于使用它们辅助匹配URL并处理URL中的路径参数。现在用什么工具或者是否构建自己的工具都不重要，我们只需要一些能让自己将精力集中在基础原理之上的东西。React最棒的一点就是使用者可以在构建应用时自由地决定使用哪些路由工具。



**练习7-2　思考参数**

参数化路由通常是将数据导入应用程序的一种有用方法。除了获取帖子ID，你还能想到其他使用路由参数的方法吗？



我们使用URL匹配库（ `enroute` ）来确定渲染哪个路由，所以接下来就会在组件上进行设置。现在，Router组件有一个不做任何事情的 `render` 方法，这看起来是开展工作的好地方。代码清单7-6展示了如何与路由器集成 `enroute` 以及对 `render` 方法的修改结果。

代码清单7-6　完成路由器（src/components/router/Router.js）

```javascript
import enroute from 'enroute';  ⇽--- enroute是一个小型功能路由器，可以用来匹配URL字符串和参数化路由
import invariant from 'invariant';
export class Router extends Component {
  static propTypes = {  ⇽--- 将propTypes设置为类的静态属性
    children: PropTypes.element.isRequired,
    location: PropTypes.string.isRequired,
  }
  constructor(props) {  ⇽--- 设置组件的初始状态并初始化enroute
    super(props);
    // We'll store the routes on the Router component
    this.routes = {};  ⇽--- 路由最终将成为以URL路径为键的对象
    // Set up the router for matching & routing
    this.router = enroute(this.routes);  ⇽--- 将路由传给enroute，render会使用enroute的返回值来进行URL到组件的匹配
  }
  render() {
    const { location } = this.props;  ⇽--- 将当前地址作为属性传给路由器
    invariant(location, '<Router/> needs a location to work');  ⇽--- 使用invariant来确保不会忘记提供地址
    return this.router(location);  ⇽--- 最后也是最重要的，使用路由器匹配地址并返回相应的组件
  }
}

```

我们并没有添加太多代码，但路由器最重要的一些部分已经就绪。现在，还没有任何可用于 `enroute` 的路由，但基本工作机制已经形成：尝试寻找与路由相关联的组件，然后用路由器来渲染它。下一节，我们会创建路由器可以使用的路由。

