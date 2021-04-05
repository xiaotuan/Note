### 5.6.10　drawScreen()函数

最后，要准备将Box2D的物理模型绘制在HTML5 Canvas上。为此，将用下面的3行代码替换之前创建的drawScreen()函数中的所有代码。

```javascript
world.Step(1 / 60, 10, 10);
world.DrawDebugData();
world.ClearForces();
```

world.Step()函数中有3个参数：时间步长、速度迭代和位置迭代。时间步长为在模拟过程中每一次调用的时间长度。在程序中，每1/60s模拟一次。其他两个参数表示迭代的精度，这里先不讨论。world.DrawDebugData()方法可以将b2DebugDraw绘制在画布上。world.clearForces()方法会在每一步之后重置物理模型为下一步做准备。

示例5-20给出了CH5EX20.html的所有源代码。在测试这个示例的时候，可以看到50个随机创建的小球落下，并在画布底部的边界反弹。有些小球可能会反弹很长时间，有些小球会很快停止跳动。请注意，小球正是以用户所期望的方式运动的。然而回顾所写的代码，程序中并没有创建碰撞测试、角度反弹或者线性运动的函数。所有的一切都是被Box2D控制的。

例5-20　Box2dWeb的小球演示

```javascript
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CH5EX20: Box2dWeb Balls Demo</title>
<script src="modernizr.js"></script>
<script type="text/javascript" src="Box2dWeb-2.1.a.3.js"></script>
<script type="text/javascript">
window.addEventListener('load', eventWindowLoaded, false);
function eventWindowLoaded() {
　 canvasApp();
}
function canvasSupport () {
　 return Modernizr.canvas;
}
function canvasApp() {
　 if (!canvasSupport()) {
　　 return;
　 }
　 function　drawScreen () {
　　　　 world.Step(1 / 60, 10, 10);
　　　　 world.DrawDebugData();
　　　　 world.ClearForces();
}
　 theCanvas = document.getElementById('canvasOne');
　 context = theCanvas.getContext('2d');
　 var　b2Vec2 = Box2D.Common.Math.b2Vec2
　　　　 ,　b2BodyDef = Box2D.Dynamics.b2BodyDef
　　　　 ,　b2Body = Box2D.Dynamics.b2Body
　　　　 ,　b2FixtureDef = Box2D.Dynamics.b2FixtureDef
　　　　 ,　b2World = Box2D.Dynamics.b2World
　　　　 ,　b2PolygonShape = Box2D.Collision.Shapes.b2PolygonShape
　　　　 ,　b2CircleShape = Box2D.Collision.Shapes.b2CircleShape
　　　　 ,　b2DebugDraw = Box2D.Dynamics.b2DebugDraw;
　 var world = new b2World(new b2Vec2(0,10),　true);
　 var numBalls = 50;
　 var balls = new Array();
　 for (var i=0; i < numBalls; i++) {
　　　 　var ballDef = new b2BodyDef;
　　　 　ballDef.type = b2Body.b2_dynamicBody;
　　 　　var ypos = (Math.random() * 8)+1;
　　 　　var xpos = (Math.random() * 14)+1;
　　 　　var size = (Math.random() * .4)+.2;
　　 　　ballDef.position.Set(xpos, ypos);
　　 　　var ballFixture = new b2FixtureDef;
　　　 　ballFixture.density = 10.0;
　　　 　ballFixture.friction = 0.5;
　　 　　ballFixture.restitution = 1;
　　 　　ballFixture.shape =　new b2CircleShape(size);
　　 　　var newBall = world.CreateBody(ballDef)
　　 　　newBall.CreateFixture(ballFixture);
　　 　　balls.push(newBall);
　 }
　 var wallDefs = new Array({x:8.3,y:.03,w:8.3 ,h:.03}, //上面
　　　　　　{x:8.3,y:13.33,w:8.3 ,h:.03},　//下面
　　　　　　{x:0,y:6.67,w:.03 ,h:6.67},　//左面
　　　　　　{x:16.7,y:6.67,w:.03 ,h:6.67} );　//右面
　 var walls = new Array();
　 for (var i = 0; i <wallDefs.length; i++) {
　　　 　var wallDef = new b2BodyDef;
　　　 　wallDef.type = b2Body.b2_staticBody;
　　 　　wallDef.position.Set(wallDefs[i].x, wallDefs[i].y);
　　　 　var newWall = world.CreateBody(wallDef)
　　　 　var wallFixture = new b2FixtureDef;
　　　 　wallFixture.density = 10.0;
　　　 　wallFixture.friction = 0.5;
　　　 　wallFixture.restitution = 1;
　　　 　wallFixture.shape = new b2PolygonShape;
　　　 　wallFixture.shape.SetAsBox(wallDefs[i].w, wallDefs[i].h);
　　 　　newWall.CreateFixture(wallFixture);
　　 　　walls.push(newWall);
　 }
　 var debugDraw = new b2DebugDraw();
　 debugDraw.SetSprite (context);
　　　debugDraw.SetDrawScale(30);　//定义比例
　　　debugDraw.SetFillAlpha(0.3);　//定义透明度
　　　debugDraw.SetLineThickness(1.0);
　　　debugDraw.SetFlags(b2DebugDraw.e_shapeBit | b2DebugDraw.e_jointBit);
　 world.SetDebugDraw(debugDraw);
　 function gameLoop() {
　　　　 window.setTimeout(gameLoop, 20);
　　　　 drawScreen()
　　　}
　 gameLoop();
}
</script>
</head>
<body>
<div style="position: absolute; top: 0px; left: 0px;">
<canvas id="canvasOne" width="500" height="400">
 Your browser does not support the HTML 5 Canvas.
</canvas>
</div>
</body>
</html>
```

