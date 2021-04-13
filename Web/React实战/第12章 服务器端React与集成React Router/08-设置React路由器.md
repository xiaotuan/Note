### 设置React路由器

我们已经决定使用React Router作为自己路由器的生产环境替代品，让我们看看如何设置它。第一步是确保已经安装了React Router并切换了当前的路由器。虽然技术不一样，但要使用的API应该是非常相似的。

React Router应该已经作为项目依赖被安装了。现在需要开始将项目过渡到React Router并准备一个允许执行SSR的设置。让我们从当前的src/index.js文件开始。这是设置应用主要部分的入口文件，包括监听浏览器历史记录、渲染路由器组件，以及激活身份验证事件监听器。

这对SSR的设置没有用，因为有太多的代码依赖于浏览器环境而且也不需要React Router的所有功能来让应用运作。真正需要保留的是身份验证监听器。在添加任何内容之前，先创建一个帮助工具供以后使用。代码清单12-6展示了如何创建一个简单的实用程序来检查你当前是否处在浏览器环境中。一些工具技术，如Webpack，可以帮助我们打包环境相关的代码。但就我们的目的而言，会保持这个更简单的方式。

代码清单12-6　检查浏览器环境（src/utils/environment.js）

```javascript
export function isServer() {
    return typeof window === 'undefined';
}
```

现在可以使用这个帮助方法来确定所处的环境并根据需要有条件地执行代码。它并不会进行详尽的检查来确保处于浏览器环境中，但应该满足当前的需求。在构建具有SSR功能的应用程序或在客户端和服务器之间共享代码的应用程序（有时被称为“通用”或“同构”）时，必须考虑代码的运行环境。根据我的经验，这也可能是那些难以追踪的bug的常见来源，特别是如果安装的第三方依赖项没有考虑到环境的影响。

到目前为止，React社区中的许多现有技术通常要么已经支持SSR，要么会指出可能导致问题的地方。但情况并非总是如此。几年前使用React的早期版本时，我遇到了React自己的bug，其会导致某些库的某些方面无法预料地失败。不过现在情况好多了，SSR不只是React社区考虑的问题，也是核心团队考虑的问题。

继续之前，我们需要对其中一个reducer进行微调以便将服务器环境考虑进来。user reducer会使用 `js-cookie` 在浏览器中设置cookie。服务器通常不允许存储cookie（虽然有些库可以模拟这一行为，如 `tough-cookie` ），所以需要使用刚才的环境判断实用程序来调整这段代码。代码清单12-7展示了需要做的修改。

代码清单12-7　修改user reducer

```javascript
export function user(state = initialState.user, action) {
    switch (action.type) {
        case types.auth.LOGIN_SUCCESS:
            const { user, token } = action;
            if (!isServer()) {  ⇽--- 只在浏览器环境中才尝试使用浏览器cookie
                Cookies.set('letters-token', token);
            }
            return Object.assign({}, state.user, {
                authenticated: true,
                name: user.name,
                id: user.id,
                profilePicture: user.profilePicture ||
'/static/assets/users/4.jpeg',
                token
        });
    case types.auth.LOGOUT_SUCCESS:
        Cookies.remove('letters-token');
        return initialState.user;
        default:
            return state;
    }
}
```

回到手头的任务。你需要将React Router设置好。与自建的路由器非常相似，React Router（版本3）允许使用嵌套的<Route/>组件层次结构来指示应该将哪些组件映射到哪些URL。正如之前提到的，React Router是一个广泛使用和经过“实战检验”的解决方案，具有许多我们自己没有添加到路由器的特性，我们关注使用它直接替换自己的路由器，而不是去探索它能做哪些事情。

为我们的路由器创建一个新文件src/router.js。将路由分解到它们自己的文件中，因为服务器和客户端都要访问它们。对客户端代码和服务器代码并存的应用程序来说，这很方便。但如果路由文件存放在其他地方（通过npm、Git子模块等），可能需要寻找其他方式将其引入到服务器中。路由文件应该与之前自建的路由器很相似，仅有一些细微差异。我们之前添加了在同一个<Route/>组件中指定index组件的功能，而React Router也为此提供了一个单独的组件。图12-5从较高层次展示了路由配置的作用，它的工作方式与之前自建的路由器相同，用于将URL映射到组件或组件树（当嵌套时）。

![80.png](./images/80.png)
<center class="my_markdown"><b class="my_markdown">图12-5　一如我们构建的路由器，React Router的路由配置将URL映射到组件。为了跨页面或子
 区域共享UI的某些部分（如Navbar或其他共享组件），可以嵌套组件</b></center>

代码清单12-8展示了如何将React Router集成到路由设置中。

代码清单12-8　为React Router创建路由（src/routes.js）

```javascript
import React from 'react';
import App from './pages/app';
import Home from './pages/index';
import SinglePost from './pages/post';
import Login from './pages/login';
import NotFound from './pages/404;
import { Route, IndexRoute } from 'react-router';
export const routes = (
    <Route path="/" component={App}>  ⇽--- 用App组件将整个应用包裹起来
        <IndexRoute component={Home} />  ⇽--- 使用React Router的IndexRoute组件来确保能在index（/）路径下显示组件
        <Route path="posts/:post" component={SinglePost} />  ⇽--- 就像自己的路由器那样使用路径来匹配组件
        <Route path="login" component={Login} />
        <Route path="*" component={NotFound} />
    </Route>
);
```

现在已经设置了一些路由，可以使用React Router将它们导入主应用程序文件中使用。客户端和服务器上将使用相同的路由，这正是你可能听说过的SSR“通用”或“同构”发挥作用的地方。在客户端和服务器上复用代码可能是件大事，但在当前如此有限的情况下，可能不会得到更多的好处，这里得到的好处是，可以很容易地以“正常”的React方式将客户端组件暴露给服务器。

现在将路由导入服务器。代码清单12-9展示了如何将路由导入服务器并在渲染过程中使用它们。服务器如何获取到正确的组件进行渲染呢？因为路由只是将URL映射到操作（这里是HTTP响应），所以需要能够查找与路径相关联的正确组件。在自建的路由器中，是用基本的URL正则匹配库来确定URL是否被映射到路由器中的组件上的。它做的工作就是基于URL确定渲染哪个组件（见图12-5），如果有的话。React Router允许在服务器端做同样的事。这样一来，就可以使用传入服务器的HTTP请求的URL去匹配要渲染为静态标记的组件。这是React Router和我们SSR目标之间的关键连接点。React Router像通常那样使用URL来渲染组件或组件树，只不过是在服务器上。代码清单12-9展示了如何使用React Router设置SSR功能的初始服务器部分。

代码清单12-9　在服务器上使用React Router（server/server.js）

```javascript
//...
import { renderToString } from 'react-dom/server';  ⇽--- 从React Router导入一些实用方法，从React DOM导入renderToString，导入Redux Provider组件、store和路由
import React from 'react';
import { match, RouterContext } from 'react-router';
import { Provider } from 'react-redux';
import configureStore from '../src/store/configureStore';
import initialReduxState from '../src/constants/initialState';
import { routes } from '../src/routes';
//...
app.use('*', (req, res) => {
    match({ routes: routes, location: req.originalUrl },  ⇽--- 将URL和路由传入match函数
    (err, redirectLocation, props) => {  ⇽--- match给出错误、重定向和属性，将用于渲染定制错误页面或重定向
        if (redirectLocation && req.originalUrl !== '/login') {
            return res.redirect(302, redirectLocation.pathname +
     redirectLocation.search);  ⇽--- match给出错误、重定向和属性，将用于渲染定制错误页面或重定向
        }
        const store = configureStore(initialReduxState);  ⇽--- 传入从React Router导入的RouterContext组件并把它包装在ReduxProvider组件中
        const appHtml = renderToString(
               <Provider store={store}>
                    <RouterContext {...props} />
               </Provider>
            );
        const html = `  ⇽--- 使用字符串模板创建一个HTML文档，并将应用的HTML插入其中
            <!doctype html>
            <html>
                <head>  ⇽--- 使用字符串模板创建一个HTML文档，并将应用的HTML插入其中
                    <link rel="stylesheet"
     href="http://localhost:3100/static/styles.css" />
                    <meta charset=utf-8/>
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <title>Letters Social | React In Action by Mark
     Thomas</title>
                    <meta name="viewport" content="width=device-width,
     initial-scale=1">
               </head>
               <body>
                    <div id="app">  ⇽--- 使用字符串模板创建一个HTML文档，并将应用的HTML插入其中
                        ${appHtml}
                    </div>
                <script src="http://localhost:3000/bundle.js"
     type='text/javascript'></script>  ⇽--- 使用字符串模板创建一个HTML文档，并将应用的HTML插入其中
                </body>
            </html>
        `.trim();
        res.setHeader('Content-type', 'text/html');  ⇽--- 设置响应头并将其发回给浏览器
        res.send(html).end();
    });
});
//... Error handling
export default app;
```

