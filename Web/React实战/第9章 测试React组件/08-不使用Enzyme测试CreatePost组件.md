### 9.3.3　不使用Enzyme测试CreatePost组件

现在第一个测试已经开始工作，可以继续测试更复杂的组件。大多数情况下，测试React组件应该简单明了。如果发现正在创建一个包含了大量功能的组件以及之后与之相关的大量测试，也许要考虑将其分解为几个组件（尽管并非总能如此）。

接下来要测试的CreatePost组件比Content组件拥有更多功能，测试需要处理这些增加的功能。代码清单9-6展示了CreatePost组件，以便在为其编写测试之前能够回顾一下。Home组件使用CreatePost组件来触发新帖子的提交，它会渲染出一个随用户输入进行更新的文本域以及一个当用点击时提交表单数据的按钮。当用户单击时，它将调用由父组件传入的回调函数。我们可以测试所有这些假设并确保组件按预期工作。

代码清单9-6　CreatePost组件（src/components/post/Create.js）

```javascript
import PropTypes from 'prop-types';
import React from 'react';
import Filter from 'bad-words';
import classnames from 'classnames';
import DisplayMap from '../map/DisplayMap';
import LocationTypeAhead from '../map/LocationTypeAhead';
class CreatePost extends React.Component {
    static propTypes = {
        onSubmit: PropTypes.func.isRequired
    };
    constructor(props) {
        super(props);
        this.initialState = {
            content: '',
            valid: false,
            showLocationPicker: false,
            location: {
                lat: 34.1535641,
                lng: -118.1428115,
                name: null
            },
            locationSelected: false
        };
        this.state = this.initialState;
        this.filter = new Filter();
        this.handlePostChange = this.handlePostChange.bind(this);
        this.handleRemoveLocation = this.handleRemoveLocation.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleToggleLocation = this.handleToggleLocation.bind(this);
        this.onLocationSelect = this.onLocationSelect.bind(this);
        this.onLocationUpdate = this.onLocationUpdate.bind(this);
        this.renderLocationControls = this.renderLocationControls.bind(this);
    }
    handlePostChange(event) {
        const content = this.filter.clean(event.target.value);
        this.setState(() => {
            return {
                content,
                valid: content.length <= 300
            };
        });
    }
    handleRemoveLocation() {
        this.setState(() => ({
            locationSelected: false,
            location: this.initialState.location
        }));
    }
    handleSubmit(event) {
        event.preventDefault();
        if (!this.state.valid) {
            return;
        }
        const newPost = {
            content: this.state.content
        };
        if (this.state.locationSelected) {
            newPost.location = this.state.location;
        }
        this.props.onSubmit(newPost);
        this.setState(() => ({
            content: '',
            valid: false,
            showLocationPicker: false,
            location: this.defaultLocation,
            locationSelected: false
        }));
    }
    onLocationUpdate(location) {
        this.setState(() => ({ location }));
    }
    onLocationSelect(location) {
        this.setState(() => ({
            location,
            showLocationPicker: false,
            locationSelected: true
        }));
    }
    handleToggleLocation(event) {
        event.preventDefault();
        this.setState(state => ({ showLocationPicker:
     !state.showLocationPicker }));
    }
    renderLocationControls() {
        return (
            <div className="controls">
                <button onClick={this.handleSubmit}>Post</button>
                {this.state.location && this.state.locationSelected ? (
                    <button onClick={this.handleRemoveLocation}
     className="open location-indicator">
                        <i className="fa-location-arrow fa" />
                        <small>{this.state.location.name}</small>
                    </button>
                ) : (
                    <button onClick={this.handleToggleLocation}
     className="open">
                        {this.state.showLocationPicker ? 'Cancel' : 'Add
     location'}{' '}
                        <i
                            className={classnames(`fa`, {
                                'fa-map-o': !this.state.showLocationPicker,
                                'fa-times': this.state.showLocationPicker
                            })}
                        />
                    </button>
                )}
            </div>
        );
    }
    render() {
        return (
            <div className="create-post">
                <textarea
                    value={this.state.content}
                    onChange={this.handlePostChange}
                    placeholder="What's on your mind?"
                />
                {this.renderLocationControls()}
                <div
                    className="location-picker"
                    style={{ display: this.state.showLocationPicker ? 'block'
    : 'none' }}
                >
                    {!this.state.locationSelected && (
                        <LocationTypeAhead
                            onLocationSelect={this.onLocationSelect}
                            onLocationUpdate={this.onLocationUpdate}
                        />
                    )}
                    <DisplayMap
                        displayOnly={false}
                        location={this.state.location}
                        onLocationSelect={this.onLocationSelect}
                        onLocationUpdate={this.onLocationUpdate}
                    />
                </div>
            </div>
        );
    }
}
export default CreatePost;
```

这是一个比前几章创建的组件稍微复杂一点的组件。使用这个组件可以创建帖子并为这些帖子添加位置信息，根据我的经验，测试更大更复杂的组件进一步强调了简洁、可读测试的重要性。如果无法阅读或分析这些测试文件，自己今后或者其他开发者又该为之奈何？

代码清单9-7展示了CreatePost组件的推荐测试骨架。方法尚没有多到让阅读测试变得困难，但如果组件有更多内容，可以添加嵌套的 `describe` 块来让测试变得更容易理解。代码清单9-7中的函数将被测试运行器（本例中是Jest）执行，可以在这些测试中进行断言。大多数测试都遵循同样的模式。导入要测试的代码，mock它的任何依赖项从而将测试隔离到单个功能单元（因此，这里是单元测试），然后测试运行器和断言库将一起运行这些测试。

代码清单9-7　测试CreatePost组件（src/components/post/Create.test.js）

```javascript
jest.mock('mapbox');
import React from 'react';
import renderer from 'react-test-renderer';
import CreatePost from '../../../src/components/post/Create';
describe('CreatePost', () => {  ⇽--- 在这里使用一个describe调用，但在更大的测试文件中，可以有多个describe调用甚至嵌套它们
    test('snapshot', () => {
    });
    test('handlePostChange', () => {  ⇽--- 为组件中的每个方法创建一个测试，包括一个快照来确保其正确地渲染
    });
    test('handleRemoveLocation', () => {  ⇽--- 为组件中的每个方法创建一个测试，包括一个快照来确保其正确地渲染
    });
    test('handleSubmit', () => {  ⇽--- 为组件中的每个方法创建一个测试，包括一个快照来确保其正确地渲染
    });
    test('onLocationUpdate', () => {
    });
    test('handleToggleLocation', () => {
    });
    test('onLocationSelect', () => {
    });
    test('renderLocationControls', () => {
    });
});
```

如果按照一致的模式来考虑待测试组件的每个部分，开发和测试组件可以更全面。请随意遵循对自己来说最有意义的结构——这只是对我和我所在的团队有帮助的结构。我还发现，在编写任何其他测试之前先为组件或模块编写不同的 `describe` 和 `test` 块，这样有助于开始编写测试。我发现，如果能一次性把这个搞定，我就能够更容易地考虑到想要覆盖的各种情况（有错、没错、在某种条件下等）。



**其他类型的测试**

你可能想知道诸如用户流程测试、跨浏览器测试以及这里没有涵盖的其他类型的测试。这类测试通常被专门从事特定形式测试的工程师或工程团队关注。QA团队和SET（测试中的软件工程师）通常拥有许多专门的工具来操作应用程序并模拟所有可能存在的复杂流程。

这些类型的测试（集成测试）可能会涉及一个或多个不同系统之间的交互。如果还记得图9-1中的测试金字塔的话，应该知道这些测试可能需要花费大量时间来编写，很难维护，并且往往会花费大量金钱。当考虑“测试前端应用程序”时，可能认为会涉及这些类型的测试。我们已经看到情况并非如此（非QA工程师编写的大多数测试都是单元测试或低级集成测试）。如果有兴趣进一步了解这类工具的话，下面是一些工具可以作为进一步了解更高级别测试的跳板：

+ Selenium；
+ Puppeteer；
+ Protractor。



随着测试骨架设置就位，就可以开始测试CreatePost组件了。先测试构造函数。记住，构造函数是设置初始状态、绑定类方法和其他设置发生的地方。要测试CreatePost组件的这一部分，需要引入之前提及的另一个工具——Sinon。我们需要一些能够提供给组件使用而又不依赖其他模块的测试函数。使用Jest可以为测试创建 `mock` 函数，从而使测试聚焦于组件本身并防止我们将所有代码绑在一起。记得我之前说过当代码更改时测试应该失败吗？这是对的，但更改一个测试时不应该破坏其他测试。与常规代码一样，测试应该是解耦的，它应该只关注其测试的那部分代码。

Jest的mock函数不仅可以帮助我们隔离代码，还可以帮助我们做更多断言。我们可以对组件如何使用 `mock` 函数、 `mock` 函数是否被调以及使用哪些参数进行调用等来断言。代码清单9-8展示了如何为组件设置快照测试并使用Jest来mock组件所需的一些基本属性。

代码清单9-8　编写第一个测试（src/components/post/Create.test.js）

```javascript
jest.mock('mapbox');  ⇽--- 使用jest.mock函数告诉Jest在测试运行时使用mock而不是真正的模块
import React from 'react';
import renderer from 'react-test-renderer';
import CreatePost from '../../../src/components/post/Create';
describe('CreatePost', () => {  ⇽--- 在之前创建的外部describe块中创建test块
    test('snapshot', () => {
        const props = { onSubmit: jest.fn() };  ⇽--- 创建props的mock对象并使用Jest来创建mock函数
        const component = renderer.create(<CreatePost {...props} />);  ⇽--- 使用React Test Renderer创建组件并传入props
        const tree = component.toJSON();  ⇽--- 调用toJSON方法生成快照
        expect(tree).toMatchSnapshot();  ⇽--- 断言快照匹配
    });
   //...
});
```

现在手头上已经有了一个测试，可以测试该组件的其他方面。这个组件主要用于让用户创建帖子并向其中附加位置，因此我们需要测试这些功能区域。我们将从测试帖子的创建开始。代码清单9-9展示了如何测试组件中的帖子创建方法。

代码清单9-9　测试帖子创建（src/components/post/Create.test.js）

```javascript
jest.mock('mapbox');
import React from 'react';
import renderer from 'react-test-renderer';
import CreatePost from '../../../src/components/post/Create';
describe('CreatePost', () => {
    test('snapshot', () => {
        const props = { onSubmit: jest.fn() };
        const component = renderer.create(<CreatePost {...props} />);
        const tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });
    test('handlePostChange', () => {
        const props = { onSubmit: jest.fn() };  ⇽--- 创建要使用的mock属性集
        const mockEvent = { target: { value: 'value' } };
        CreatePost.prototype.setState = jest.fn(function(updater) {  ⇽--- 对setState进行mock以便确保组件调用了setState并且更新帖子时按照正确的方式更新状态
            this.state = Object.assign(this.state, updater(this.state));
        });
        const component = new CreatePost(props);  ⇽--- 直接实例化组件并调用其方法
        component.handlePostChange(mockEvent);
        expect(component.setState).toHaveBeenCalled();  ⇽--- 断言组件调用了正确的方法以及该方法正确地更新了状态
        expect(component.setState.mock.calls.length).toEqual(1);
        expect(component.state).toEqual({
            valid: true,
            content: mockEvent.target.value,
            location: {
                lat: 34.1535641,
                lng: -118.1428115,
                name: null
            },
            locationSelected: false,
            showLocationPicker: false
        });
    });
    test('handleSubmit', () => {
        const props = { onSubmit: jest.fn() };
        const mockEvent = {  ⇽--- 创建另一个mock事件，以模拟组件将会从事件中接收的内容
            target: { value: 'value' },
            preventDefault: jest.fn()
        };
           CreatePost.prototype.setState = jest.fn(function(updater) {  ⇽--- 再次对setState进行mock
            this.state = Object.assign(this.state, updater(this.state));
        });
        const component = new CreatePost(props);  ⇽--- 实例化另一个组件并设置组件的状态来模拟用户输入帖子内容
        component.setState(() => ({
            valid: true,
            content: 'cool stuff!'
        }));
        component.state = {  ⇽--- 直接修改组件的状态（用于测试目的）
            valid: true,
            content: 'content',
            location: 'place',
            locationSelected: true
        };
        component.handleSubmit(mockEvent);  ⇽--- 用创建的mock事件来处理帖子提交并断言调用了mock
        expect(component.setState).toHaveBeenCalled();
        expect(props.onSubmit).toHaveBeenCalledWith({
            content: 'content',
            location: 'place'
        });
    });
});
```

最后，需要测试组件的其余功能。CreatePost组件除了让用户创建帖子，还可以让用户选择位置。其他组件通过作为属性传递的回调函数来处理位置更新，但我们仍需要测试CreatePost上与此功能相关的组件方法。

记得我们在CreatePost上实现了一个子渲染方法，可以使用它来让阅读CreatePost的 `render` 方法的输出更容易并减少混乱。我们也可以用与Enzyme或React Test Renderer测试组件相类的方式来测试它。代码清单9-10展示了CreatePost组件的剩余测试。

代码清单9-10　测试帖子的创建（src/components/post/Create.test.js）

```javascript
jest.mock('mapbox');
import React from 'react';
import renderer from 'react-test-renderer';
import CreatePost from '../../../src/components/post/Create';
describe('CreatePost', () => {
    test('handleRemoveLocation', () => {
        const props = { onSubmit: jest.fn() };
        CreatePost.prototype.setState = jest.fn(function(updater) {
            this.state = Object.assign(this.state, updater(this.state));
        });  ⇽--- 对setState进行mock
        const component = new CreatePost(props);
        component.handleRemoveLocation();  ⇽--- 调用handleRemoveLocation函数
        expect(component.state.locationSelected).toEqual(false);  ⇽--- 断言以正确的方式更新了状态
    });
    test('onLocationUpdate', () => {  ⇽--- 对剩余组件方法重复相同的过程
        const props = { onSubmit: jest.fn() };
        CreatePost.prototype.setState = jest.fn(function(updater) {
            this.state = Object.assign(this.state, updater(this.state));
        });
        const component = new CreatePost(props);
        component.onLocationUpdate({
            lat: 1,
            lng: 2,
            name: 'name'
        });
        expect(component.setState).toHaveBeenCalled();
        expect(component.state.location).toEqual({
            lat: 1,
            lng: 2,
            name: 'name'
        });
    });
    test('handleToggleLocation', () => {  ⇽--- 对剩余组件方法重复相同的过程
        const props = { onSubmit: jest.fn() };
        const mockEvent = {
            preventDefault: jest.fn()
        };
        CreatePost.prototype.setState = jest.fn(function(updater) {
            this.state = Object.assign(this.state, updater(this.state));
        });
        const component = new CreatePost(props);
        component.handleToggleLocation(mockEvent);
        expect(mockEvent.preventDefault).toHaveBeenCalled();
        expect(component.state.showLocationPicker).toEqual(true);
    });
    test('onLocationSelect', () => {  ⇽--- 对剩余组件方法重复相同的过程
        const props = { onSubmit: jest.fn() };
        CreatePost.prototype.setState = jest.fn(function(updater) {
            this.state = Object.assign(this.state, updater(this.state));
        });
        const component = new CreatePost(props);
        component.onLocationSelect({
            lat: 1,
            lng: 2,
            name: 'name'
        });
    test('onLocationSelect', () => {  ⇽--- 对剩余组件方法重复相同的过程
        const props = { onSubmit: jest.fn() };
        CreatePost.prototype.setState = jest.fn(function(updater) {
            this.state = Object.assign(this.state, updater(this.state));
        });
        const component = new CreatePost(props);
        component.onLocationSelect({
            lat: 1,
            lng: 2,
            name: 'name'
        });
        expect(component.setState).toHaveBeenCalled();
        expect(component.state.location).toEqual({
            lat: 1,
            lng: 2,
            name: 'name'
        });
    });
    test('renderLocationControls', () => {  ⇽--- 为创建的子render方法创建另一个快照测试
        const props = { onSubmit: jest.fn() };
        const component = renderer.create(<CreatePost {...props} />);
        let tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });
});
```

