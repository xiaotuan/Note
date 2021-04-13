### 11.1.4　测试reducer

得益于reducer纯函数和没有耦合的特性——它们只是函数，测试Redux的reducer非常简单直接。要测试reducer，应该断言对于给定的输入它们应该生成特定的状态。代码清单11-9展示了如何测试为帖子和帖子ID的状态所创建的reducer。和Redux的其他部分一样，reducer是函数这一点使它们易于隔离和测试。

代码清单11-9　测试reducer（src/reducers/posts.test.js）

```javascript
jest.mock('js-cookie');  ⇽--- 模拟js-cookie库
import Cookies from 'js-cookie';
import { user } from '../../src/reducers/user';  ⇽--- 导入需要测试的reducer和类型
import initialState from '../../src/constants/initialState';
import * as types from '../../src/constants/types';
describe('user', () => {
    test('should return the initial state', () => {
        expect(user(initialState.user, {})).toEqual(initialState.user);  ⇽--- 断言默认会返回初始状态
    });
    test(`${types.auth.LOGIN_SUCCESS}`, () => {
        const mockUser = {  ⇽--- 创建要断言的模拟用户、token和期望状态
            name: 'name',
            id: 'id',
            profilePicture: 'pic'
        };
        const mockToken = 'token';  ⇽--- 建要断言的模拟用户、token和期望状态
        const expectedState = {
            name: 'name',
            id: 'id',
            profilePicture: 'pic',
            token: mockToken,
            authenticated: true
        };
        expect(  ⇽--- 给定一个登录action，断言状态按预期改变
            user(initialState.user, {
                type: types.auth.LOGIN_SUCCESS,
                user: mockUser,
                token: mockToken
            })
        ).toEqual(expectedState);
        expect(Cookies).toHaveBeenCalled();  ⇽--- 断言模拟cookies会被访问
    });
    test(`${types.auth.LOGOUT_SUCCESS}, browser`, () => {
        expect(  ⇽--- 对LOGOUT_SUCCESS的action进行相似的断言
            user(initialState.user, {
                type: types.auth.LOGOUT_SUCCESS
            })
        ).toEqual(initialState.user);
        expect(Cookies).toHaveBeenCalled();
    });
});
```

到目前为止，我们介绍了Redux应用的大部分基础知识：store、reducer、action以及中间件！Redux生态系统很健壮，有很多领域读者可以自行浏览。我们忽略了API及Redux生态系统的某些部分，比如中间件的高级用法、选择器（与store状态交互的优化方案）等。我们还特意省略了对store API的全面介绍（举个例子，如使用 `store.subscribe()` 与更新事件交互）。这是因为处理这部分Redux的具体细节将被抽象到 `react-redux` 库中。我还在我的博客上整理了React生态系统的指南，也包括Redux。



**练习11-1　判断对错**

虽然Redux相对于它做的事情还只是一个很小的库，但它对于数据流如何处理store、reducer、action和中间件还有一些明确的观点。花点时间评估下面的陈述来检查对此的理解（判断对错）。

+ reducer应该直接修改现有状态。（TIF）
+ Redux默认包含一种处理异步任务（比如网络请求）的方法。（TIF）
+ 为每个reducer缺省包含一个初始状态是个不错的主意。（TIF）
+ reducer可以被合并，这让分离状态分片更容易。（TIF）



