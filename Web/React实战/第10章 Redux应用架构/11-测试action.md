### 10.2.6　测试action

接下来，在继续介绍reducer之前，我们将为这些action编写一些快速测试。方便起见，我不打算为创建的每个reducer或action编写测试，我只提供一些代表性的示例，以便读者了解如何测试Redux应用的不同部分。如果想查看更多示例，可以在应用源代码中查看test目录。

Redux使测试action创建器、reducer和Redux架构的其他部分变得简单且直接。更好的是，它们可以独立于前端框架进行测试和维护。这在大型应用中尤其重要，因为测试在这些应用（商业应用而不是周末的业余项目）中是一项重要的工作。对于action，通常的想法是断言预期的action类型，任何必要的荷载信息都基于给定的action进行了创建。

大多数action创建器都可以很容易地进行测试，因为它们通常返回的是带有类型和荷载信息的对象。虽然有时候也需要做一些额外的设置来适应异步action创建器之类的东西。要测试异步action创建器，需要使用本章开头安装的模拟的store（ `redux-mock-store` ）并使用 `redux-thunk` 来配置它。这样，我们就可以断言异步action创建器派发了某种action，并验证它是否按预期工作。代码清单10-14展示了如何在Redux中测试action。

代码清单10-14　在Redux中测试action（src/actions/comments.test.js）

```javascript
jest.mock('../../src/shared/http');  ⇽--- 使用Jest来模拟HTTP文件从而免于发起网络请求
import configureStore from 'redux-mock-store';  ⇽--- 导入模拟store和redux中间件，这样就可以创建模拟store来镜像原有的store
import thunk from 'redux-thunk';
import initialState from '../../src/constants/initialState';
import * as types from '../../src/constants/types';
import {
    showComments,
    toggleComments,
    updateAvailableComments,
    createComment,
    getCommentsForPost
} from '../../src/actions/comments';  ⇽--- 导入需要测试的action
import * as API from '../../src/shared/http';  ⇽--- 导入API，以便可以在其上模拟特定的方法
const mockStore = configureStore([thunk]);  ⇽--- 创建模拟store并在每个测试之前重新初始化它
describe('login actions', () => {
    let store;  ⇽--- 创建模拟store并在每个测试之前重新初始化它
    beforeEach(() => {
        store = mockStore(initialState);  ⇽--- 创建模拟store并在每个测试之前重新初始化它
    });
    test('showComments', () => {
        const postId = 'id';
        const actual = showComments(postId);  ⇽--- 断言action创建器将输出具有正确类型和数据的action
        const expected = { type: types.comments.SHOW, postId };
        expect(actual).toEqual(expected);
    });
    test('toggleComments', () => {
        const postId = 'id';
        const actual = toggleComments(postId);
        const expected = { type: types.comments.TOGGLE, postId };
        expect(actual).toEqual(expected);
    });
    test('updateAvailableComments', () => {
        const comments = ['comments'];
        const actual = updateAvailableComments(comments);
        const expected = { type: types.comments.GET, comments };
        expect(actual).toEqual(expected);
    });
    test('createComment', async () => {
        const mockComment = { content: 'great post!' };  ⇽--- 创建模拟评论并传递给action创建器
        API.createComment = jest.fn(() => {  ⇽--- 使用Jest模拟来自API模块的createComment方法
            return Promise.resolve({
                json: () => Promise.resolve([mockComment])  ⇽--- 使用Jest模拟来自API模块的createComment方法
            });
        });
        await store.dispatch(createComment(mockComment));  ⇽--- 派发action并使用await等待Promise解析完
        const actions = store.getActions();
        const expectedActions = [{ type: types.comments.CREATE, comment:
     [mockComment] }];  ⇽--- 断言action按预期创建
        expect(actions).toEqual(expectedActions);
    });
    test('getCommentsForPost', async () => {
        const postId = 'id';
        const comments = [{ content: 'great stuff' }];
        API.fetchCommentsForPost = jest.fn(() => {
            return Promise.resolve({
                json: () => Promise.resolve(comments)
            });
        });
        await store.dispatch(getCommentsForPost(postId));
        const actions = store.getActions();
        const expectedActions = [{ type: types.comments.GET, comments }];
        expect(actions).toEqual(expectedActions);
    });
});
```

