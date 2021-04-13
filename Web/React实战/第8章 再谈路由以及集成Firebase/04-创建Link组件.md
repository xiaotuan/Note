### 8.1.2　创建 `<Link />` 组件

如果在开发模式下运行应用并试着四处点点，你会注意到，即使为用户帖子页面设置了路由，只要没有一开始就知道帖子ID并将其置于URL中，就无法去到那里。那不是很有用，对吧？

我们需要创建一个自定义的Link组件来与 `history` 工具和路由器协同工作，否则，用户会很快抛弃这个应用，而投资者会非常沮丧。要如何实现？普通的链接标签（ `<a href= "/">Link!</a>` ）是不能用的，因为它会尝试重载整个页面，这不是我们想要的。我们想不用链接标签来创建链接，例如，不想用链接标签包裹列表中的帖子或其他的东西。

> **注意** 　可访问性是指一个界面可以被人使用的程度。也许之前听到过人们讨论“Web可访问性”，但可能知道的并不多。没关系——它很容易学习。人们想要确保应用对尽可能多的人是可用的，无论他们是使用鼠标和键盘、屏幕阅读器还是使用其他设备。我刚提到过，使用Link组件可以让应用程序的任意元素都可以导航——这是从可访问性的角度来处理时要小心应对的事情。考虑到这一点，我只想针对本书简单地提一下可访问性。因为构建可访问的Web应用是一个庞大而重要的话题，它超出了本书的范围。一些公司、应用程序以及业余项目都将它视为工程的头等大事。虽然人们可以参考Letter Social的源代码作为使用React组件构建应用程序的方法源泉，但我们并没有处理应用程序可能遇到的所有不同的可访问性问题。为了从网上学习更多关于可访问性的知识，查看WAI-ARIA创作实践或者有关ARIA的MDN文档。Ari Rizzitano还就这一话题进行了精彩的演讲，特别关注了React的可访问性，该演讲叫作“构建可访问的组件”。

这里会再次使用 `history` 实用方法并将其集成到Link组件中，以便在应用程序中可以使用push-state进行链接。还记得早些时候公开过的 `navigate` 函数吗？现在用这个函数可以通过程序的方式告诉 `history` 库为用户更改地址。为了将这个功能添加到组件中，我们将使用一些React工具把其他组件包装在可点击的Link组件中。我们可以使用 `React.cloneElement` 来创建目标元素的副本，然后附加执行导航功能的点击处理程序。 `React.cloneElement` 的签名看起像下面这样：

```javascript
ReactElement cloneElement(
  ReactElement element,
  [object props],
  [children ...]
)

```

它接收一个要克隆的元素、要合并到新元素的 `props` ，以及它应该有的任何 `children` 。我们将使用这个实用方法来克隆想要封装到Link的组件，并且需要确保Link组件仅有一个子组件，所以要从前几章中找回 `React.Children.only` 工具。总之，这些工具会让使用者将其他组件转换为Link组件，从而帮助用户在应用中进行跳转。代码清单8-7展示了如何创建Link组件。

代码清单8-7　创建Link组件（src/components/router/Link.js）

```javascript
import { PropTypes, Children, Component, cloneElement } from 'react';  ⇽--- 导入需要的库
import { navigate } from '../../history  ⇽--- 复用一直在用的history工具
class Link extends Component {
  static propTypes = {
    to: PropTypes.string.isRequired,  ⇽--- to和children属性会分别保存目标URL和Link化的组件
    children: PropTypes.node,
  }
  render() {
    const { to, children } = this.props;  ⇽--- 克隆Link组件的子组件来包裹仅有的一个节点（它可以有子组件）
    return cloneElement(Children.only(children), {  ⇽--- 在props对象中，传入onClick处理程序，其会使用history进行URL导航
      onClick: () => navigate(to),  ⇽--- 定义propTypes
    });
  }
}
import PropTypes from 'prop-types';  ⇽--- 导入需要的库
import { Children, cloneElement } from 'react';
import { navigate } from '../../history';  ⇽--- 复用一直在用的history工具
function Link({ to, children }) {  ⇽--- to和children属性会分别保存目标URL和Link化的组件
    return cloneElement(Children.only(children), {  ⇽--- 克隆Link组件的子组件来包裹仅有的一个节点（它可以有子组件）
        onClick: () => navigate(to)  ⇽--- 在props对象中，传入onClick处理程序，其会使用history进行URL导航
    });
}
Link.propTypes = {  ⇽--- 定义propTypes
    to: PropTypes.string,
    children: PropTypes.node
};
export default Link;

```

为了集成Link组件，可以将用户帖子包裹在可复用的Post组件中并确保Link可以获取将用户送到正确页面的 `to` 属性（看看之前关于可访问性的注意事项）。我们能够按照相同的模式以类似的方式来包裹其他组件并将它们转换为Link化的组件。代码清单8-8展示了如何集成Link组件。

代码清单8-8　集成Link组件（src/components/post/Post）

```javascript
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as API from '../../shared/http';
import Content from './Content';
import Image from './Image';
import Link from './Link';
import PostActionSection from './PostActionSection';
import Comments from '../comment/Comments';
import DisplayMap from '../map/DisplayMap';
import UserHeader from '../post/UserHeader';
import RouterLink from '../router/Link';  ⇽--- 导入Link组件，给它取一个别名叫RouterLink，从而避免与帖子中使用的Link组件的命名冲突
export class Post extends Component {
//...
    render() {
        return this.state.post ? (
            <div className="post">
                <RouterLink to={`/posts/${this.state.post.id}`}>  ⇽--- 包裹想要链接化的Post组件的部分并给它提供正确的ID
                    <span>
                        <UserHeader date={this.state.post.date}
     user={this.state.post.user} />
                        <Content post={this.state.post} />
                        <Image post={this.state.post} />
                        <Link link={this.state.post.link} />
                    </span>
                </RouterLink>  ⇽--- 包裹想要链接化的Post组件的部分并给它提供正确的ID
                {this.state.post.location && <DisplayMap
    location={this.state.post.location} />}
                <PostActionSection showComments={this.state.showComments} />
                <Comments
                    comments={this.state.comments}
                    show={this.state.showComments}
                    post={this.state.post}
                    handleSubmit={this.createComment}
                    user={this.props.user}
                />
            </div>
        ) : null;
    }
}
export default Post;
```

如此就将Router完全集成到应用中了。用户现在可以查看帖子，这对于一次分享和关注一个帖子非常不错。投资者会对此留下不错的印象并期待在下一轮融资时投资你。不过我们还没做完。下一节会讨论当无法匹配URL到组件时该做什么。



**练习8-2　添加更多链接**

尝试寻找应用程序中其他一些非常合适成为Link的区域并使用Link组件将它们转换为链接。提示：用户在导航到帖子页面之后该如何回到主页？随着学习的进行，尝试考虑用户在应用中跳转时的体验。什么对他们是有意义的？要把哪些转换成Link？是否有这样的情况：转换为Link组件的东西并不是已有的链接标签？检出应用程序源代码的单个帖子页面，看看添加简单返回按钮的示例。



