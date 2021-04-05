### 5.6.5　创建Box2dWeb世界

接下来，需要添加初始化世界的代码。在下面的代码中创建的变量是访问Box2dWeb对象的快捷方式。它们的短名称使用户在代码中定义新对象变得更加容易。此处并没有展示Box2dWeb所有的对象，因此，如果需要定义一个不同的对象，比如用b2JointDef定义一个关节（joint），则需要定义一个新的快捷方式，或使用对象的完整名称。

```javascript
var b2Vec2 = Box2D.Common.Math.b2Vec2
　　　　　　　　　 , b2BodyDef = Box2D.Dynamics.b2BodyDef
　　　　　　　　　 , b2Body = Box2D.Dynamics.b2Body
　　　　　　　　　 , b2FixtureDef = Box2D.Dynamics.b2FixtureDef
　　　　　　　　　 , b2World = Box2D.Dynamics.b2World
　　　　　　　　　 , b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape
　　　　　　　　　 , b2CircleShape = Box2D.Collision.Shapes.b2CircleShape
　　　　　　　　　 , b2DebugDraw = Box2D.Dynamics.b2DebugDraw;
```

现在，创建世界对象。这将定义一个你自己的物理世界。b2Vec()函数通过指定x轴重力和y轴重力的参数来创建一个Box2D对象。第二个参数是doSleep，如果设置为true，则不用模拟非活动状态的物体，可以提高性能。

```javascript
var world = new b2World(new b2Vec2(0,10), true);
```

