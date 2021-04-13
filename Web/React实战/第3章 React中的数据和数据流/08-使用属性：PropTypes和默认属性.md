### 3.2.3　使用属性：PropTypes和默认属性

当使用属性时，有些API可以在开发过程中提供帮助：PropTypes和默认属性。PropTypes提供了类型检查功能，可以用它指定组件期望接收什么样的属性。可以指定数据类型，甚至可以告诉组件的使用者需要提供什么形式的数据（例如，一个拥有 `user` 属性的对象， `user` 属性包含特定的键）。在之前版本的React中，PropTypes是核心 `React` 库的一部分，但它现在作为 `prop-types` 包单独存在。

`prop-types` 库并非魔法——它是一组能够帮助你对输入进行类型检查的函数和属性——可以在其他库中很容易地用它来对输入进行类型检查。例如，可以将 `prop-types` 引入另一个类似于React的组件驱动框架（如Preact）并用相似的方式使用它。

要为组件设置PropTypes，需要在类上提供一个叫作 `propTypes` 的静态属性。注意代码清单3-4，在组件类上设置的静态属性的名字是以小写字母开头的，而从 `prop-types` 库访问的对象名是以大写字母开头的（ `PropTypes` ）。为了指定组件需要哪个属性，需要添加要验证的属性名并为其分配一个来自 `prop-types` 库默认导出（ `import PropTypes from 'prop-types'` ）的属性。使用PropTypes可以为属性声明任何类型、形式和必要性（可选还是强制）。

另一个可以让开发体验更为简单的工具是默认属性。还记得如何使用类的构造方法（ `constructor` ）为组件提供初始状态？也可以为属性做类似的事情。你可以通过一个名为 `defaultProps` 的静态属性来为组件提供默认属性。使用默认属性可以帮助确保组件拥有运行所需的东西，即便使用组件的人忘记为其提供属性。代码清单3-4展示了在组件中使用PropTypes和默认属性的例子。你可以前往https://codesandbox.io/ s/31ml5pmk4m运行代码。

代码清单3-4　React组件的不可变属性

```javascript
import React from "react";
import { render } from "react-dom";
import PropTypes from "prop-types";
class Counter extends React.Component {
  static propTypes = {  ⇽--- 指定一个描述“形式”的对象
    incrementBy: PropTypes.number,
    onIncrement: PropTypes.func.isRequired  ⇽--- 可以为任何propTypes链接isRequired从而确保在属性没有出现时展示警告
  };
  static defaultProps = {
    incrementBy: 1
  };
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
    this.onButtonClick = this.onButtonClick.bind(this);
  }
  onButtonClick() {
    this.setState(function(prevState, props) {
      return { count: prevState.count + props.incrementBy };
    });
  }
  render() {
    return (
      <div>
        <h1>{this.state.count}</h1>
        <button onClick={this.onButtonClick}>++</button>
      </div>
    );
  }
}
render(<Counter incrementBy={1} />, document.getElementById("root"));
```

