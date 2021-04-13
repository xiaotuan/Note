### 6.1　向Letters Social API发送帖子

回忆第2章，我们创建了一个允许添加评论的评论框组件。它只在本地内存中保存这些内容，页面一刷新，添加的任何评论就会消失，因为它们随特定时间的页面状态而存亡。可以选择利用本地存储或会话存储，或者使用其他基于浏览器的存储技术（如cookie、IndexedDB、WebSQL等）。然而，这些仍会将所有东西存储在本地。

如代码清单6-1所示，我们所要做的是将JSON格式的帖子数据发送给API服务器。它将处理帖子的存储并用新数据进行响应。当克隆代码库时，已经在shared/http文件夹中创建了一些能够用于Letters Social项目的函数。我们使用 `isomorphic-fetch` 库进行网络请求，它遵循浏览器的Fetch API，但它的优点是也可以在服务器端运行。

代码清单6-1　向服务器发送帖子（src/components/app.js）

```javascript
export default class App extends Component {
//...
createNewPost(post) {
        return API.createPost(post)  ⇽--- 使用Letters API创建帖子
            .then(res => res.json())  ⇽--- 获取JSON响应
            .then(newPost => {  ⇽--- 使用新帖子，更新状态
                this.setState(prevState => {
                    return {
                        posts: orderBy(prevState.posts.concat(newPost),
    'date', 'desc')  ⇽--- 确保使用Lodash的orderBy方法对帖子进行排序
                    };
                });
            })
            .catch(err => {
                this.setState(() => ({ error: err }));  ⇽--- 如果有的话，设置错误状态
            });
}
```

有了它，你只要做最后一件事：在子组件中调用创建帖子的方法。它已经被传递给子组件，因此只需确保单击事件触发父组件方法的调用并且使帖子数据得以传递。代码清单6-2展示了如何在子组件中调用作为属性传递的方法。

代码清单6-2　调用通过属性传递的函数

```javascript
class CreatePost extends Component {
// ...
fetchPosts() {/* created in chapter 4 */}
handleSubmit(event) {
    event.preventDefault();  ⇽--- 阻止默认事件，创建一个发送给父组件的对象
    if (!this.state.valid) {
      return;
    }
    if (this.props.onSubmit) {  ⇽--- 确保有可以使用的回调函数
      const newPost = {
        date: Date.now(),
        // Assign a temporary key to the post; the API will create a real one
     for us
        id: Date.now(),
        content: this.state.content,
      };
      this.props.onSubmit(newPost);  ⇽--- 调用从父组件通过属性传递的onSubmit回调函数，传入新帖子数据
      this.setState({  ⇽--- 将表单重置为初始状态，这样用户就有了帖子被提交的提示
        content: '',
        valid: null,
      });
    }
  }
  // ...
}

```

现在，如果用 `npm run dev` 在开发模式下运行此应用程序，就应该能够添加帖子。它们应该立即出现在信息流中，如果刷新页面，仍然可以看到添加的帖子。它不像其他社交应用那样拥有用户头像或预览链接，但后续章节会添加这些功能。

