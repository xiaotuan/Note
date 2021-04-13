### 第11章　Redux进阶及Redux与React集成

**本章主要内容**

+ reducer——Redux决定状态如何改变的方法
+ 在React应用中使用Redux
+ 将Letters Social转换为使用Redux应用架构
+ 为应用添加给帖子点赞和评论的功能

在本章中，我们会继续上一章的工作，构建Redux架构的基本元素。我们将把Redux的action和store集成到React中，并探索reducer的工作原理。Redux是Flux模式的一个变种，但它在设计时就考虑了React，所以能很好地与React的单向数据流和API一起工作。虽然它并非普遍选择，但许多大型React应用在实现状态管理解决方案时都会将Redux作为首选之一。读者在Letters Social中也会跟着这样做。



**如何获取本章代码**

和每章一样，读者可以去GitHub仓库检出源代码。如果想从头开始编写本章代码，可以使用第7章和第8章的已有代码（如果跟着编写了示例）或直接检出指定章的分支（chapter-10-11）。

记住，每个分支对应该章末尾的代码（例如，chapter-10-11对应本章末尾的代码）。读者可以在选定目录下执行以下终端命令之一来获取当前章的代码。

如果还没有代码库，请输入下面的命令来获取：

```javascript
git clone git@github.com:react-in-action/letters-social.git
```

如果已经克隆过代码仓库：

```javascript
git checkout chapter-10-11
```

如果你是从其他章来到这里的，则需要确保已经安装了所有正确的依赖：

```javascript
npm install
```



![202103102F74C6D8.jpg](../images/202103102F74C6D8.jpg)
