### 8.1.3　创建 `<NotFound />` 组件

尝试在Letters应用程序中导航到/oops，看看会发生什么？什么都没有？是的，这就是基于代码应该发生的事情，但这并非我们想呈现给用户的。现在，路由器组件不会处理任何“未找到”或“全部捕获”路由。想要对用户友好并假定他们（或者自己）会犯错误并尝试导航到应用程序不存在的路由中。为了解决这个问题，我们创建一个简单的NotFound组件，并在创建Router实例的时候配置它。代码清单8-9展示了如何创建NotFound组件。

代码清单8-9　创建NotFound组件（src/pages/404.js）

```javascript
import React from 'react';
import Link from '../components/router/Link';  ⇽--- 导入已创建的Link组件，以便用户能返回主页
export const NotFound = () => {  ⇽--- 不需要组件状态，所以创建一个无状态函数组件
    return (
        <div className="not-found">
            <h2>Not found :(</h2>
            <Link to="/">  ⇽--- 使用Link组件让用户返回主页
                <button>go back home</button>
            </Link>
        </div>
    );
};
export default NotFound;
```

现在，NotFound组件已经有了，需要将它集成到Router配置中。你也许想知道，要如何告诉Router：它应该将用户送到NotFound组件。答案是，在配置路由器时使用 `*` 字符。这个字符意味着“匹配任何东西”，如果把它放在配置的末尾，所有没有匹配到任何东西的路由都会走到这里。一定要注意，在这里顺序很重要：如果把全部捕获路由放得过高，它会匹配上任何东西，而不会按你想要的方式工作。代码清单8-10展示了如何给路由器配置更多路由。

代码清单8-10　添加单个帖子到路由器中（src/index.js）

```javascript
//...
import NotFound from './pages/404 ';  ⇽--- 导入NotFound组件
//...
export const renderApp = (state, callback = () => {}) => {
    render(
        <Router {...state}>
            <Route path="" component={App}>
                <Route path="/" component={Home} />
                <Route path="/posts/:postId" component={SinglePost} />
                <Route path="*" component={NotFound} />  ⇽--- 配置NotFound组件的路由，以便其作为一个全部匹配的路由
            </Route>
        </Router>,
        document.getElementById('app'),
        callback
    );
};
//...
```

