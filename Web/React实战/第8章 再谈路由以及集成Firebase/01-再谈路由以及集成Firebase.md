### 第8章　再谈路由以及集成Firebase

**本章主要内容**

+ 使用第7章构建的路由
+ 创建路由相关的组件，如Router、Route和Link
+ 使用HTML5的History API实现push-state路由
+ 复用组件
+ 集成用户身份验证和Firebase

第7章从头构建了一个简单的路由器以便更好地理解React应用如何处理路由。这一章将开始使用之前构建的路由器并将Letters Social应用分解为更合适的部分。本章末尾，我们将能够导航到应用的任意位置、查看用户发的帖子，以及进行用户身份验证。



**如何获取本章代码**

和每章一样，读者可以去GitHub仓库检出源代码。如果想从头开始编写本章代码，可以使用第5章和第6章的已有代码（如果跟着编写了示例）或直接检出指定章的分支（chapter-7-8）。

记住，每个分支对应该章末尾的代码（例如，chapter-7-8对应第7章和第8章末尾的代码）。读者可以在选定目录下执行以下终端命令之一来获取当前章的代码。

如果还没有代码库，请输入下面的命令来获取：

```javascript
git clone git@github.com:react-in-action/letters-social.git
```

如果已经克隆过代码仓库：

```javascript
git checkout chapter-7-8
```

如果你是从其他章来到这里的，则需要确保已经安装了所有正确的依赖：

```javascript
npm install
```



![202103102040808E.jpg](../images/202103102040808E.jpg)
