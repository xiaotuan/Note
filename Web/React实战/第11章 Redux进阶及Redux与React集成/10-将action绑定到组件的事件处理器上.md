### 11.2.3　将action绑定到组件的事件处理器上

需要让应用程序再次响应用户的操作。做到这一点会用到第二个函数： `mapDispatchToProps` 。这个函数的功能就如同其名称一样——它有一个 `dispatch` 参数，就是要注入到组件中的store的 `dispatch` 方法。也许读者已经从第10章的图10-3或者React开发者工具中注意到容器的属性中有一个注入的 `dispatch` 方法；可以按原样使用该 `dispatch` 函数，因为如果不提供 `mapDispatchToProps` 函数，它会自动被注入到属性中。但使用 `mapDispatchToProps` 是有好处的，可以使用它将组件特定的action逻辑从组件中分离出来并让测试变得更容易。



**练习11-2　源代码任务**

`react-redux` 库提供了非常不错的抽象，这些抽象已经经过许多使用Redux和React的公司和个人的实战测试。但使用者并非一定要用这个库才能让React与Redux一起运行。作为练习，花些时间仔细阅读 `react-redux` 的源代码。这不是建议读者创造自己的方式来连接React和Redux，而是应该能够了解这并不是“魔法”。



`mapDispatchToProps`  函数会被 `react-redeux` 调用，而结果对象会被合并到组件的属性中去。它会被用来设置action创建器并使其对组件可用。我们还会利用Redux提供的 `bindActionCreators`  辅助工具函数。 `bindActionCreators` 将值为action创建器的对象转换为具有相同键的对象——不同之处在于每个action创建器都被包裹在一个dispatch调用中，以便它们被直接调用。

也许已经在代码清单11-11中注意到使用的是React类而不是无状态函数组件。虽然通常会创建无状态函数组件，但这种情况下需要一种方法初始化加载帖子，所以当组件完成挂载时需要能够派发action的生命周期方法。一种解决方式是将初始化事件拿到路由层并且当进入或离开某些路由时协调加载数据。构建当前路由器时并没有考虑生命周期钩子，但其他像 `React-router` 这样的路由确实有这个功能。下一章将探索把路由切换到React Router，这样我们就可以利用这个功能了。

然后，剩下的是用 `mapDispatchToProps` 来拉取action并将它们绑定到组件中。也可以创建一个对象并将函数分配到任意键上。如果 `mapDispatchToProps` 对象上的函数在它们和dispatch调用之间没有任何额外逻辑的话，那么这个模式可以让直接引用 action变得更为容易。代码清单11-12展示了如何使用 `mapDispatchToProps` 来设置action。

代码清单11-12　使用mapDispatchToProps（src/containers/Home.js）

```javascript
// ...
import { createError } from '../actions/error';  ⇽--- 导入这个组件需要的action
import { createNewPost, getPostsForPage } from '../actions/posts';
import { showComments } from '../actions/comments';
import Ad from '../components/ad/Ad';
import CreatePost from '../components/post/Create';
import Post from '../components/post/Post';
import Welcome from '../components/welcome/Welcome';
export class Home extends Component {
    componentDidMount() {  ⇽--- 当组件挂载时加载帖子
        this.props.actions.getPostsForPage();
    }
    componentDidCatch(err, info) {  ⇽--- 如果组件中发生错误，用componentDidCatch来处理它，并将错误派发到store
        this.props.actions.createError(err, info);
    }
    render() {
        return (
            <div className="home">
                <Welcome />
                <div>
                    <CreatePost onSubmit={this.props.actions.createNewPost} />  ⇽--- 将创建帖子的action传递给CreatePost组件
                    {this.props.posts && (
                        <div className="posts">
                            {this.props.posts.map(post => (
                                <Post
                                    key={post.id}
                                    post={post}
                                    openCommentsDrawer=
     {this.props.actions.showComments}  ⇽--- 通过props传递showComments action
                                />
                            ))}
                        </div>
                    )}
                    <button className="block"
     onClick={this.props.actions.getNextPageOfPosts}>  ⇽--- 传递加载更多帖子的action
                        Load more posts
                    </button>
                </div>
                <div>
                    <Ad url="https://ifelse.io/book" imageUrl="/static/
     assets/ads/ria.png" />
                    <Ad url="https://ifelse.io/book" imageUrl="/static/
     assets/ads/orly.jpg" />
                </div>
            </div>
        );
    }
}
//...
export const mapDispatchToProps = dispatch => {
    return {
        actions: bindActionCreators(  ⇽--- 使用bindActionCreators来绑定并将action包装在一个dispatch调用中
            {
                createNewPost,
                getPostsForPage,
                showComments,  ⇽--- 使用bindActionCreators来绑定并将action包装在一个dispatch调用中
                createError,
                getNextPageOfPosts: getPostsForPage.bind(this, 'next')  ⇽--- 使用.bind()确保每次使用'next'参数调用getPostsForPage
            },
            dispatch  ⇽--- 使用bindActionCreators来绑定并将action包装在一个dispatch调用中
        )
    };
};
export default connect(mapStateToProps, mapDispatchToProps)(Home);
```

如此一来，已经将组件连接到Redux了！就像早先提到的，没有足够的篇幅介绍应用中每个使用Redux的组件的转换。好消息是它们都遵循相同的模式（用 `mapStateToProps` 和 `mapDispatchToProps` 创建，用 `connect` 导出），可以用Home页的相同处理方式将其转换到与Redux进行交互。以下是应用代码中已经连接到Redux store的其他组件：

+ App——src/app.js；
+ Comments——src/components/comment/Comments.js；
+ Error——src/components/error/Error.js；
+ Navigation——src/components/nav/navbar.js；
+ PostActionSection——src/components/post/PostActionSection.js；
+ Posts——src/components/post/Posts.js；
+ Login——src/pages/login.js；
+ SinglePost——src/pages/post.js。

随着所有这些组件都已集成，应用程序将会转变为使用Redux！现在读者知道如何添加一个Redux“环”（action创建器，reducer处理action，以及连接任何组件），要如何添加用户资料这样的新的功能？还可以向Letters Social添加其他什么功能？幸运的是，Letters Social应用还有很多可以扩展的地方和方法，可以通过它们来尝试使用Redux。

