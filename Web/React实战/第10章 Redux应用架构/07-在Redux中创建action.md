### 10.2.2　在Redux中创建action

定义这些action类型之后，就可以开始用它们来做一些事情了。由于我们将复用应用已有的部分逻辑，因此很多代码看起来会很熟悉。这实际上是个值得简单回顾的点：大部分Redux应用不应该完全重做任何现有的应用逻辑。希望读者能够理清这些内容，但是将现有应用转换为使用Redux的主要工作，可能只是将应用状态的不同方面映射为Redux所强制的模式。无论如何，我们将从action开始。

action是我们在Redux应用中发起状态变更的方式，我们不能像在其他框架中那样直接修改属性。action由action创建器（返回action对象的函数）创建，并由store使用 `dispatch` 函数进行派发。

我们不会在这方面走得太远。我将首先介绍action创建器本身。从简单的开始，创建一些在加载开始和完成时向应用发出提示的action。当前还不需要传递任何额外的信息，但接下来会介绍参数化action创建器。代码清单10-3展示了如何为“加载中”和“已加载”创建两个action创建器。为了保持组织条理，我们将把所有action创建器放在actions文件夹中，其他Redux相关的文件也会如此这样处理，reducer和store都会有自己的文件夹。

代码清单10-3　“加载中”和“已加载”的action创建器（src/actions/loadings.js）

```javascript
import * as types from '../constants/types';  ⇽--- 从常量文件中导入类型
export function loading() {
  return {
    type: types.app.LOADING  ⇽--- 使用之前定义好的“加载中”类型，返回一个带有所需的type键的action对象
  };
}
export function loaded() {  ⇽--- 导出“已加载”action的创建器
  return {
    type: types.app.LOADED
  };
}
```

