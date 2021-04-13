### 2.4.1　使用JSX创建组件

掌握基础很重要，但并不意味着我们必须自讨苦吃。事实上，与仅使用 `React.createElement` 相比，有更为简便易行的方法创建React组件。认识JSX：更好的方法。

JSX是什么？它是对ECMAScript的一种类XML的语法扩展，但它没有定义任何语义，其专门提供给预处理器使用。换言之，JSX是JavaScript的扩展，其类似XML并且仅用于代码转换工具。它任何时候都不是那种会并入ECMAScript规范的东西。

JSX通过让使用者书写XML风格（想想HTML）的代码来替代使用 `React.createClass` 从而起到帮助作用。换句话说，它让人编写类似于（但不是）HTML的代码。JSX预处理程序类似于Babel（将JavaScript代码转换成与旧浏览器兼容的代码的转义器）会浏览所有JSX代码并将其转换为常规的JavaScript，就像到目前为止我们所写的那些代码。一个可能的影响是在浏览器本地运行未经转换的JSX代码是行不通的——当JavaScript被解析时会得到各种各样的语法错误。

在JavaScript中编写XML风格的类HTML代码也许会引起使用者的警戒本能，但有许多很好的理由去使用JSX，我将来会介绍它们。现在，看看代码清单2-11以了解使用JSX后评论框组件会是什么样子。我省略了一些代码以使你专注于JSX语法更容易。注意到，Babel被包含进来作为CodeSandbox环境的一部分。通常，可以使用像Webpack这样的构建工具来转义JavaScript，但也可以导入Babel并让其在没有构建步骤的情况下工作。但那会非常慢，绝不应该在生产环境中这样做。

代码清单2-11　使用JSX重写组件

```javascript
...
    class CreateComment extends Component {
    constructor(props) {
        super(props);
        this.state = {
            content: '',
            user: ''
        };
        this.handleUserChange = this.handleUserChange.bind(this);
        this.handleTextChange = this.handleTextChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    //...
    render() {
        return (
            <form onSubmit={this.handleSubmit} className="createComment">
                <input
                    value={this.state.user}  ⇽--- 不在对象上创建props，而是在JSX中像在HTML那样创建它们——要传入表达式需要使用{}语法。
                    onChange={this.handleUserChange}
                     placeholder="Your name"
                     type="text"
                />
                <input
                    value={this.state.content}
                    onChange={this.handleTextChange}
                    placeholder="Thoughts?"
                    type="text"
                />
                <button type="submit">Post</button>
            </form>
        );
    }
}
class CommentBox extends Component {
//...
    render() {
        return (
            <div className="commentBox">
                <Post
                    id={this.props.post.id}  ⇽--- 这是之前创建的Post的React类——注意现在它更清晰地表明它是自定义组件而且看起来它就像正身处HTML中一样
                    content={this.props.post.content}
                    user={this.props.post.user}
                />
                {this.state.comments.map(function(comment) {  ⇽--- 在{}内部使用常规JavaScript遍历评论列表并为每个评论创建一个评论组件
                    return (
                        <Comment
                            key={comment.id}  ⇽--- 在{}内部使用常规JavaScript遍历评论列表并为每个评论创建一个评论组件
                            content={comment.content}
                            user={comment.user}
                        />
                    );
                })}
                <CreateComment
                   onCommentSubmit={this.handleCommentSubmit}  ⇽--- 将handleCommentSubmit作为属性传入
                />
           </div>
        );
    }
}
CommentBox.propTypes = {
    post: PropTypes.object,
    comments: PropTypes.arrayOf(PropTypes.object)
};
ReactDOM.render(
    <CommentBox
       comments={data.comments}  ⇽--- 在最上层，CommentBox也是一个需要提供属性并传给React DOM去渲染的自定义组件
        post={data.post}
    />,
    node
);
......
```

代码清单2-11的在线代码位于https://codesandbox.io/s/vnwz6y28x5。

