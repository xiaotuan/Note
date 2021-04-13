### 10.2.1　定义action类型

尽管可以在本章后面添加更多内容，但现在已经可以通过列出一些action类型，开始将Letters Social应用转换为Redux架构了。这些通常会映射到用户操作，如登录、登出、更改表单值等，但它们不一定非得是用户操作。你可能希望为已打开、已解析或已经发生错误的网络请求或其他不直接与用户相关的事情创建action类型。

同样值得注意的是，在较小的应用中，开发者可能不必在常量文件中定义action类型，只需记得在创建action或自己硬编码时将action传入就行。但这么做的缺点是随着应用的增长，跟踪action类型将成为一个痛点，并可能导致难于调试或重构。在大多数实际情况下，开发者将定义action，这也是你要在这里做的事情。

可以事先拟定一些预期要用的action类型，并根据需要自由地添加或删除。这里将使用命名空间的方式来处理action类型，但请记住，在创建自己的action时，可以遵循自己认为最好的模式，只要这些类型名称是唯一的即可。也可以在对象中“捆绑”类似的action类型，但它们也可以像单个常量一样轻松地传播和导出。“捆绑”的优点是可以将action类型组织在一起并使用更短的名称（ `GET` 、 `CREATE` 等）而不必将那些信息构建到变量名之中（ `UPDATE_USER_PROFILE` 、 `CREATE_NEW_POST` 等）。代码清单10-2展示了如何创建初始的action类型。我们将这些内容放在src/constants/types.js中。我们目前将创建本章所需的所有action，以便之后可以引用它们，而不必总是回到这个文件中来添加。

代码清单10-2　定义action类型（src/constants/types.js）

```javascript
export const app = {
    ERROR: 'letters-social/app/error',
    LOADED: 'letters-social/app/loaded',
    LOADING: 'letters-social/app/loading'
};
export const auth = {
    LOGIN_SUCCESS: 'letters-social/auth/login/success',
    LOGOUT_SUCCESS: 'letters-social/auth/logout/success'
};
export const posts = {
    CREATE: 'letters-social/post/create',
    GET: 'letters-social/post/get',
    LIKE: 'letters-social/post/like',
    NEXT: 'letters-social/post/paginate/next',
    UNLIKE: 'letters-social/post/unlike',
    UPDATE_LINKS: 'letters-social/post/paginate/update'
};
export const comments = {
    CREATE: 'letters-social/comments/create',
    GET: 'letters-social/comments/get',
    SHOW: 'letters-social/comments/show',
    TOGGLE: 'letters-social/comments/toggle'
};
```

在使用Redux的开发者工具时，这些action类型将显示在应用状态更改的时间轴中，因此当有许多action和action类型时，像代码清单10-2中那样用类似URL的方式对名称进行分组会使它们更容易阅读。你也可以使用 `:` 字符来分隔它们（ `namespace:action_name:status` ），或者使用任何对你来说最有意义的约定。

