### 10.2.5　要不要使用Redux

完成了这些action创建器之后，就已经做好了用于创建帖子和评论的初始功能。但仍旧缺少一个方面：用户身份验证。前几章使用Firebase的辅助方法来检查用户的身份验证状态并使用该状态更新本地组件状态。是否需要对身份验证做同样的事情呢？这又引出了另一个值得讨论的问题：哪些东西属于Redux，哪些不属于Redux？继续之前，让我们先看看这个有争议的问题。

从“store里想放什么就放什么”到“一切都应放到store中”，React和Redux社区的观点五花八门。只在Redux情境下使用React的工程师有一种倾向，就是将Redux与React一起使用看作唯一的方法并认为React和Redux是一回事。人们常常被自己的经验所限制，但我希望在形成固定的看法之前，我们可以花些时间思考事实并权衡利弊。

首先，必须谨记，尽管React和Redux非常契合，但这些技术本身并没有内在联系。构建React应用并不需要Redux，我希望读者已经从本书中了解了这一点。Redux只是工程师可以使用的另一个工具而已，它不是构建React应用的唯一方式，而且肯定不会使“常规”的React概念（如本地组件状态）失效。在某些情况下，将组件状态引入Redux可能只会徒增开销。

那该怎么办呢？到目前为止，Redux已经被证明是为应用提供健壮架构的好办法，它对更好地组织代码和功能很有帮助（我们甚至还没有涉及reducer！）。根据目前的经验，你可能很快就会同意“一切都应放到store中”的观点，但我想告诫大家不要冲动，而是要权衡利弊。

根据我的经验，我们可以通过几个问题来引导决定哪些东西属于Redux store，而哪些不属于。

第一个问题是：应用的很多其他部分需要了解该状态或功能吗？如果是，那这个状态或功能应该放入Redux store中。如果状态完全是组件的本地状态，则应该考虑将该状态从Redux store中删除。例如下拉菜单，它不需要被用户之外的东西控制。如果应用需要控制下拉菜单是打开还是关闭，并需要对它的打开或关闭做出响应，那么这些状态的改变应该通过store进行。但如果不是，那么将状态保持在组件本地就好了。

另一个问题是正在处理的状态是否会被Redux简化或更好地表示。如果只是为了使用Redux而将组件的状态和行为转换到Redux中，那这样做可能只会引入额外的复杂度，却并不能从中得到什么好处。但是，如果状态非常复杂或特殊，而Redux却可以使其更容易使用，那就应该将该状态纳入store中。

带着这些问题，让我们重新考虑是否应该将用户和身份验证逻辑集成到Redux中。应用的其他部分需要了解用户吗？当然需要。能更好地用Redux来表达用户逻辑吗？如果不将用户和身份验证逻辑集中到store中，可能就需要在应用的不同页面之间重复这些逻辑，这就不太理想了。目前看来，将用户和身份验证逻辑集成到Redux中是有意义的。

来看看如何创建这些action吧！代码清单10-13展示了将要创建的与用户相关的action。这些示例中将使用 `async/await`  这个JavaScript语言的现代特性。如果不熟悉这部分语言的工作原理，那么通读Mozilla Developer Network的文档以及Axel Rauschmayer博士的Exploring ES2016 and ES2017可能会有所帮助。

代码清单10-13　创建用户相关的action（src/actions/auth.js）

```javascript
import * as types from '../constants/types';
import { history } from '../history';  ⇽--- 导入与验证相关的action所需的模块
import { createError } from './error';
import { loading, loaded } from './loading';
import { getFirebaseUser, loginWithGithub, logUserOut, getFirebaseToken }
    from '../backend/auth';
   export function loginSuccess(user, token) {  ⇽--- 创建登录和登出action创建器，登录action将被参数化以接受user和token
    return {
        type: types.auth.LOGIN_SUCCESS,
        user,
        token
    };
}
export function logoutSuccess() {  ⇽--- 创建登录和登出action创建器，登录action将被参数化以接受user和token
    return {
        type: types.auth.LOGOUT_SUCCESS
    };
}
export function logout() {  ⇽--- 使用Firebase登出用户
    return dispatch => {
        return logUserOut()   ⇽--- 使用Firebase登出用户
            .then(() => {
                history.push('/login');  ⇽--- 将用户推到登录页面，派发登出action，并清理用户上下文（用于错误跟踪的库）
                dispatch(logoutSuccess());
                window.Raven.setUserContext();
            })
            .catch(err => dispatch(createError(err)));
    };
}
export function login() {
    return dispatch => {
        return loginWithGithub().then(async () => {  ⇽--- 使用Firebase登录用户
            try {  ⇽--- async/await使用try/catch的错误处理语法
                dispatch(loading());
                const user = await getFirebaseUser();  ⇽--- 使用await从Firebase中获取user和token
                const token = await getFirebaseToken();
                const res = await API.loadUser(user.uid);  ⇽--- 尝试找到从Firebase的API返回的用户，如果它们不存在（404），必须使用Firebase的信息为其注册
                if (res.status === 404) {
                    const userPayload = {
                        name: user.displayName,
                        profilePicture: user.photoURL,
                        id: user.uid
                    };
                    const newUser = await API.createUser(userPayload).then(res
                         => res.json());  ⇽--- 创建新用户
                    dispatch(loginSuccess(newUser, token));  ⇽--- 使用新用户派发登录action，并从函数返回
                    dispatch(loaded());
                    history.push('/');
                    return newUser;
                }
                const existingUser = await res.json();  ⇽--- 如果用户已存在，派发相应的登录action并返回
                dispatch(loginSuccess(existingUser, token));
                dispatch(loaded());
                history.push('/');
                return existingUser;
            } catch (err) {
                createError(err);  ⇽--- 捕获登录过程中的错误并将错误派发给store
            }
        });
    };
}
```

这样就已经为用户相关的操作、评论、帖子、加载和错误创建了action。虽然这看起来很多，但是让人高兴的是我们所做的已经创建了应用的大部分原始功能。下一节，我们仍然需要教Redux如何使用reducer响应状态更改，然后将所有东西连接到React，但这些重新创建的action代表了我们（或用户）可以与应用交互的所有基本方式。这是Redux的另一个优点：开发者最终要做的工作是将功能转换为action，但最后会得到一个相当全面的用户可以在应用中执行的操作的集合。这比充斥着大量意大利面条代码的代码库要清晰得多，这些代码库往往无法获得准确方法来搞清应用，更不用说采取不同的行动了。

