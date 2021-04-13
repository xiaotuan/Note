### 6.2.1　使用refs创建DisplayMap组件

当用户为新帖子选择位置以及当帖子在用户的信息流中展示时，需要一种方式向用户显示位置。我们将看到如何创建同时满足这两种目的的组件，以便可以复用代码。可能并不总是能够做到这一点，毕竟每个需要地图的地方可能有不同的要求。对于这种情况，共享相同的组件行得通而且会减小额外的工作。首先创建一个名为src/components/map/DisplayMap.js的新文件。地图相关的两个组件会放在这个目录中。

Mapbox库从哪儿来呢？大多数情况下，我们使用从npm安装的库。下一节将使用Mapbox的npm模块，但创建地图将使用不同的库。如果查看源代码中的HTML模板（src/index.js），将会看到对Mapbox的JS库（mapbox.js）的引用：

```javascript
...
<script src="https://api.mapbox.com/mapbox.js/v3.1.1/mapbox.js"></script>
...
```

这让React应用能够与Mapbox JS SDK协同工作。注意，Mapbox JS SDK需要Mapbox令牌才能工作。我已经在Letters Social应用程序的源代码中包含了一个公共令牌，因此读者不需要创建Mapbox账户。如果已经有账户或者想自定义创建一个账户来进行定制，可以通过更改应用程序源代码的config目录中的值来添加令牌。

当处理项目或特性时，很多情况下需要将React与非React库集成在一起。开发者可能正在使用Mapbox之类的东西（就像本章所做的那样），它也可能是另一个开发者在编写时没有考虑使用React的第三方库。考虑到React DOM管理DOM的方式，开发者可能想知道他能不能这样做。好消息是React提供了一些不错的应急手段，让开发者使用这些类库成为可能。

这正是ref发挥作用的地方。我在前面的章节简要提到过ref，它们这里特别有用。ref是React为使用者提供的访问底层DOM节点的方式。虽然ref很有用，但不应该滥用。我们仍然希望使用状态和属性作为应用交互和数据处理的主要方式。当然也有ref适用的场景，包括下面几点：

+ 管理焦点以及与< `video` >这样的多媒体元素进行命令式的互动；
+ 命令式地触发动画；
+ 与超出React范围使用DOM的第三方库交互（我们的例子）。

如何在React中使用ref ？在以前的版本中，会给React元素添加一个字符串属性（ `<div ref="myref"></div>` ），但新方法是使用内联回调，如下所示：

```javascript
<div ref={ref => { this.MyNode = ref; } }></div>
```

如果想引用底层DOM元素，可以从类中引用它。我们可以在ref的回调函数中与其交互，但大多时候希望将对DOM元素的引用存储在组件类中，以便在其他地方可以使用它。

应该注意几件事。不能从外部在无状态函数组件上使用ref，因为这类组件没有支撑实例。例如，下面这种方式是行不通的：

```javascript
<ACoolFunctionalComponent ref={ref => { this.ref = ref; } } />
```

但如果组件是一个类，可以得到组件的引用，因为组件拥有支撑实例。还可以将ref作为属性传递给使用它们的组件。大多情况下，仅当需要直接访问DOM节点时才使用ref，所以这种用例场景可能并不常见，除非正在构建需要使用ref的库。

我们将使用ref与Mapbox JavaScript SDK交互。Mapbox库负责创建地图并在地图上设置很多东西，如事件处理程序、UI控件等。它的地图API需要使用DOM元素的引用或用来搜索DOM的ID。代码清单6-3展示了DisplayMap组件的框架。

代码清单6-3　给地图组件添加ref（src/components/map/DisplayMap.js）

```javascript
import React, { Component } from 'react';
import PropTypes from 'prop-types';
export default class DisplayMap extends Component {
    render() {
        return [  ⇽--- 从render中返回元素数组
            <div key="displayMap" className="displayMap">
                <div
                    className="map"  ⇽--- Mapbox用来创建地图的DOM元素
                    ref={node => {
                        this.mapNode = node;  ⇽--- Mapbox用来创建地图的DOM元素
                    }}
                >
                  </div>
              </div>
          ];
      }
}
```

这是地图与React协同的良好开端。接下来需要使用Mapbox JS API来创建地图。我们将创建一个方法，该方法会使用存储在类上的ref。我们还需要设置一些默认属性和状态来让地图有默认区域定位，而不是一上来就显示整个世界地图。我们将在组件中记录一些状态，包括地图是否已加载以及一些位置信息（纬度、经度和地名）。注意，通过React与另一个JavaScript库交互是非常简单的事。让这些库一起工作也很容易实现，最难的部分是使用ref。代码清单6-4展示了如何设置DisplayMap组件。

代码清单6-4　使用Mapbox创建地图（src/components/map/DisplayMap.js）

```javascript
import React, { Component } from 'react';
import PropTypes from 'prop-types';
export default class DisplayMap extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mapLoaded: false,  ⇽--- 设置初始状态
            location: {
                lat: props.location.lat,
                lng: props.location.lng,
                name: props.location.name
            }
        };
        this.ensureMapExists = this.ensureMapExists.bind(this);  ⇽--- 绑定ensureMapExists类方法
    }
    static propTypes = {
        location: PropTypes.shape({
            lat: PropTypes.number,
            lng: PropTypes.number,
            name: PropTypes.string
        }),
        displayOnly: PropTypes.bool
    };
    static defaultProps = {
        displayOnly: true,
        location: {
            lat: 34.1535641,
            lng: -118.1428115,
            name: null
        }
    };
    componentDidMount() {
        this.L = window.L;  ⇽--- Mapbox使用一个名为Leaflet的库（因此是“L”）
        if (this.state.location.lng && this.state.location.lat) {  ⇽--- 检查地图是否有可使用的位置信息，如果有，设置地图
            this.ensureMapExists();
        }
    }
    ensureMapExists() {
        if (this.state.mapLoaded) return;  ⇽--- 如果已经加载了地图，确保不会意外地重新创建地图
        this.map = this.L.mapbox.map(this.mapNode, 'mapbox.streets', {  ⇽--- 使用Mapbox创建新地图并在组件上存储对它的引用（禁用不需要的地图特性）
            zoomControl: false,
            scrollWheelZoom: false
        });
        this.map.setView(this.L.latLng(this.state.location.lat,
     this.state.location.lng), 12);  ⇽--- 用组件接收到的纬度和经度设置地图视图
        this.setState(() => ({ mapLoaded: true }));  ⇽--- 更新状态以便知道地图已经加载
    }
    render() {
        return [
            <div key="displayMap" className="displayMap">
                <div
                    className="map"
                    ref={node => {
                        this.mapNode = node;
                    }}
                >
                </div>
            </div>
        ];
    }
}
```

组件现在应该很好地展示了一个仅用于展示的地图。但记住，我们要创建的map组件可以在用户选择新位置时为其指明特定位置并进行更新。我们需要做更多工作来实现这些功能：添加方法用于向地图新增标记、更新地图位置以及确保正确更新地图。代码清单6-5展示了如何将这些方法添加到组件中。

代码清单6-5　动态地图（src/components/map/DisplayMap.js）

```javascript
import React, { Component } from 'react';
import PropTypes from 'prop-types';
export default class DisplayMap extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mapLoaded: false,
            location: {
                lat: props.location.lat,
                lng: props.location.lng,
                name: props.location.name
            }
        };
        this.ensureMapExists = this.ensureMapExists.bind(this);  ⇽--- 绑定类方法
        this.updateMapPosition = this.updateMapPosition.bind(this);
    }
    //...
    componentDidUpdate() {  ⇽--- 告诉Mapbox使地图尺寸失效，防止隐藏/显示地图时显示不正确
        if (this.map && !this.props.displayOnly) {
            this.map.invalidateSize(false);  ⇽--- 告诉Mapbox使地图尺寸失效，防止隐藏/显示地图时显示不正确
        }
    }
    componentWillReceiveProps(nextProps) {  ⇽--- 当显示位置发生变化时，需要进行相应的响应
        if (nextProps.location) {  ⇽--- 如果接收到位置，检查当前位置和之前的位置是否相同，如果不同，需要更新地图
            const locationsAreEqual = Object.keys(nextProps.location).every(
                k => nextProps.location[k] === this.props.location[k]
            );  ⇽--- 如果接收到位置，检查当前位置和之前的位置是否相同，如果不同，需要更新地图
            if (!locationsAreEqual) {
                this.updateMapPosition(nextProps.location);
            }
        }
    }
    //...
    ensureMapExists() {
        if (this.state.mapLoaded) return;
        this.map = this.L.mapbox.map(this.mapNode, 'mapbox.streets', {
            zoomControl: false,
            scrollWheelZoom: false
        });
        this.map.setView(this.L.latLng(this.state.location.lat,
     this.state.location.lng), 12);
        this.addMarker(this.state.location.lat, this.state.location.lng);  ⇽--- 当地图第一次创建时添加一个标记
        this.setState(() => ({ mapLoaded: true }));
    }
    updateMapPosition(location) {  ⇽--- 相应地更新地图视图和组件状态
        const { lat, lng } = location;
        this.map.setView(this.L.latLng(lat, lng));  ⇽--- 相应地更新地图视图和组件状态
        this.addMarker(lat, lng);
        this.setState(() => ({ location }));
    }
    addMarker(lat, lng) {
        if (this.marker) {
            return this.marker.setLatLng(this.L.latLng(lat, lng));  ⇽--- 更新现有的标记，而不是每次创建一个标记
        }
        this.marker = this.L.marker([lat, lng], {  ⇽--- 创建一个标记并将其添加到地图中
            icon: this.L.mapbox.marker.icon({
                'marker-color': '#4469af'
            })
        });
        this.marker.addTo(this.map);  ⇽--- 创建一个标记并将其添加到地图中
    }
    render() {
        return [
            <div key="displayMap" className="displayMap">
                <div
                    className="map"
                    ref={node => {
                        this.mapNode = node;
                    }}
                >
                </div>
            </div>
        ];
    }
}
```

当向组件中添加方法时可能注意到这里的一个模式：用第三方库做一些事，将做事的方式教授给React，重复。根据我的经验，这通常就是与第三方库集成的方式。开发者想找到一个集成点，在这里可以从库中获取数据或者使用库API来告诉它去做一些事情——但这些都发生在React中。很多情况下这可能非常困难，但依我之见，把React的ref与常规JavaScript互操作性结合起来使得使用非React库不再如其他情况那么糟糕（希望在未来的React应用程序你也能找到相同的感觉）。

至少还可以对组件进行一项改进。Mapbox允许根据地理信息生成静态的地图图像。这对于不想加载交互式地图的情况非常有用。我们将添加此功能作为备用，这样用户就可以立即看到地图。这个改进在第12章中做服务器端渲染时会很有用。服务器将生成不调用任何装载相关方法的标记，因此用户在应用完全加载前仍能看到帖子的位置。

为了地图能够在纯展示模式下显示其位置名称，还需要给地图组件添加一个小UI。前面已提到，最好给主元素添加一个兄弟元素，这就是我们要返回元素数组的原因。这就是添加这个小标记的地方。代码清单6-6展示了如何向组件添加备用图以及位置名称展示。

代码清单6-6　添加备用地图图像（src/components/map/DisplayMap.js）

```javascript
import React, { Component } from 'react';
import PropTypes from 'prop-types';
export default class DisplayMap extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mapLoaded: false,
            location: {
                lat: props.location.lat,
                lng: props.location.lng,
                name: props.location.name
            }
        };
        this.ensureMapExists = this.ensureMapExists.bind(this);
        this.updateMapPosition = this.updateMapPosition.bind(this);
        this.generateStaticMapImage = this.generateStaticMapImage.bind(this);  ⇽--- 绑定类方法
    }
    //...
    generateStaticMapImage(lat, lng) {  ⇽--- 使用纬度和经度从Mapbox生成图像URL
        return `https://api.mapbox.com/styles/v1/mapbox/streetsv10/
    static/${lat},${lng},12,0,0/600x175?access_token=${process  ⇽--- 使用纬度和经度从Mapbox生成图像URL
            .env.MAPBOX_API_TOKEN}`;
    }
    render() {
        return [
            <div key="displayMap" className="displayMap">
                <div
                    className="map"
                    ref={node => {
                        this.mapNode = node;
                    }}
                >
                    {!this.state.mapLoaded && (  ⇽--- 显示位置图片
                        <img
                            className="map"
                            src={this.generateStaticMapImage(
                                this.state.location.lat,
                                this.state.location.lng
                            )}
                            alt={this.state.location.name}
                        />
                    )}
                </div>
            </div>,
            this.props.displayOnly && (  ⇽--- 如果处于纯显示模式，则展示位置名称和指示器
                <div key="location-description" className="location
     description">
                    <i className="location-icon fa fa-location-arrow" />
                   <span className="location-
     name">{this.state.location.name}</span>  ⇽--- 如果处于纯显示模式，则展示位置名称和指示器
                </div>
            )
        ];
    }
}
```

