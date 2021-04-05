### 5.6.7　在Box2D中定义墙

现在，墙的宽度和高度已经基于MTS单位进行了定义，可以将墙定义为Box2D对象了。首先创建一个数组保存墙对象，然后遍历wallDefs数据，创建4面墙作为屏幕的边界。

```javascript
var walls = new Array();
for (var i = 0; i <wallDefs.length; i++) {
```

接下来，通过创建一个b2BodyDef的实例来定义一面墙。一个b2BodyDef对象用于保存和定义一个刚体的所有数据。如前所述，一个刚体需要在其上对应一个shape和一个fixtrue，这样才能创建一个可以操作的Box2D对象。将类型设置为b2_staticBody，这意味着该对象用于不会移动，并且其质量无限大。这对于作为画布边界的墙来说再合适不过了。接下来，使用数组中的对象的位置属性设置wallDef的位置信息。最后，调用world.createBody(wallDef)方法，基于b2BodyDef对象中的定义在Box2D中创建一个刚体。

```javascript
var wallDef = new b2BodyDef;
wallDef.type = b2Body.b2_staticBody;
wallDef.position.Set(wallDefs[i].x, wallDefs[i].y);
var newWall = world.CreateBody(wallDef)
```

接下来，为强创建一个fixture的定义。fixture用于绑定到一个刚体的形状，其中包含了Box2D对象的属性。首先，创建一个新的b2FixtureDef对象，然后设置desity（单位体积的质量）、friction（阻力，通常在0~1之间）以及restitution（弹性，通常在0～1）。

```javascript
var wallFixture = new b2FixtureDef;
wallFixture.density = 10.0;
wallFixture.friction = 0.5;
wallFixture.restitution = 1;
```

拥有fixture之后，还需要创建shape。将fixture的shape属性设置为b2PolygonShape对象，然后调用shape对象的setAsBox()方法（需传入墙的宽度和高度）完成形状的定义。接下来，调用刚体对象的createFixture()方法，传入wallFixture参数。这将为刚体设置fixture和shape。最后，将刚体加入到墙体数组中。

```javascript
　　 wallFixture.shape = new b2PolygonShape;
　　 wallFixture.shape.SetAsBox(wallDefs[i].w, wallDefs[i].h);
　　 newWall.CreateFixture(wallFixture);
　　 walls.push(newWall);
}
```

