### 8.10.2　Geo Blaster全局游戏变量

下面看看游戏应用程序中需要用到的全局变量。

+ 控制屏幕流程的变量：在标题屏和游戏结束屏第一次出现时需要用到这些变量。一旦屏幕绘制完毕，这些变量的值就会被置为true。当这些变量为true时，游戏将等待用户按下空格键，应用之后进入下一个状态。

```javascript
var titleStarted = false;
var gameOverStarted = false;
```

+ 游戏环境变量：这些变量用于为一个新游戏设置必要的默认选项。本书将在8.12.4节讨论extraShipAtEach和extraShipsEarned变量。

```javascript
var score = 0;
var level = 0;
var extraShipAtEach = 10000;
var extraShipsEarned = 0;
var playerShips = 3;
```

+ 游戏区域变量：这些变量为游戏区域设置x、y坐标的最大值和最小值：

```javascript
var xMin = 0;
var xMax = 400;
var yMin = 0;
var yMax = 400;
```

+ 得分分值变量：这些变量用于记录每一个可被玩家摧毁的物体的得分分值。

```javascript
var bigRockScore = 50;
var medRockScore = 75;
var smlRockScore = 100;
var saucerScore = 300;
```

+ 陨石体积常量：这些变量使用自然语言的形式存储3种陨石的体积，可以使用这些常量代替数字值。如果需要，也可以对数字值做修改。

```javascript
const ROCK_SCALE_LARGE = 1;
const ROCK_SCALE_MEDIUM = 2;
const ROCK_SCALE_SMALL = 3;
```

+ 逻辑显示对象：这些变量设置了单个玩家飞船以及用于保存游戏中各种其他逻辑显示对象的数组。更详细的介绍请参考8.11节和8.12.1节。

```javascript
var player = {};
var rocks = [];
var saucers = [];
var playerMissiles = [];
var particles = []
var saucerMissiles = [];
```

+ 关卡级别相关变量：在游戏级别增加时，将使用以下变量处理关卡级别相关的难度设置。这些变量的详细用法请参考8.12.2节。

```javascript
var levelRockMaxSpeedAdjust = 1;
var levelSaucerMax = 1;
var levelSaucerOccurrenceRate = 25
var levelSaucerSpeed = 1;
var levelSaucerFireDelay = 300;
var levelSaucerFireRate = 30;
var levelSaucerMissileSpeed = 1;
```

