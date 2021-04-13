### 11.1.3　将reducer合并到store

最后，需要确保将reducer与Redux store整合在一起。尽管已经创建了这些reducer，但它们目前没有任何联系。让我们重新看一下第10章创建的根reducer，看看如何向其添加新reduer。代码清单11-8展示了如何将我们创建的reducer添加到根reducer。这里务必要注意的是， `combineReducers` 会根据传入的reducer在store中创建键。对于代码清单11-8中的情况，store的状态会拥有 `loading` 和 `posts` 键，每个都由它们自己的reducer管理。这里使用了ES2015的简洁属性表示法，如果读者想的话，也可以把最终的键命名为不同名称。一定要注意，不要觉得函数名必须直接绑定到store的键上。

代码清单11-8　将新reducer添加到已存在的根reducer（src/reducers/root.js）

```javascript
import { combineReducers } from 'redux';
import { error } from './error';  ⇽--- 导入reducer，以便可以将它们添加到根reducer中
import { loading } from './loading';
import { pagination } from './pagination';  ⇽--- 导入reducer，以便可以将它们添加到根reducer中
import { posts, postIds } from './posts';
import { user } from './user';
import { comments, commentIds } from './comments';  ⇽--- 导入reducer，以便可以将它们添加到根reducer中
const rootReducer = combineReducers({
    commentIds,  ⇽--- combineReducers会将每个reducer挂载到相应的键上，如想要，也可以改变键的名称
    comments,
    error,
    loading,
    pagination,  ⇽--- combineReducers会将每个reducer挂载到相应的键上，如想要，也可以改变键的名称
    postIds,
    posts,
    user  ⇽--- combineReducers会将每个reducer挂载到相应的键上，如想要，也可以改变键的名称
});
export default rootReducer;
```

