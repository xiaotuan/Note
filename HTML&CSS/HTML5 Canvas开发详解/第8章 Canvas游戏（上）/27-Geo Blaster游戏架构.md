### 8.10.1　Geo Blaster游戏架构

游戏应用的架构与最初在本章前几节搭建的架构非常类似。仔细观察所有的状态函数，并思考它们是如何在一起工作的。

#### 1．游戏程序的状态

游戏有7种不同的应用状态，并使用下面的常量来存储这些状态。

```javascript
const GAME_STATE_TITLE = 0;
const GAME_STATE_NEW_GAME = 1;
const GAME_STATE_NEW_LEVEL = 2;
const GAME_STATE_PLAYER_START = 3;
const GAME_STATE_PLAY_LEVEL = 4;
const GAME_STATE_PLAYER_DIE = 5;
const GAME_STATE_GAME_OVER = 6;
```

#### 2．游戏的应用状态函数

每个独立的状态都关联一个函数，并在每一帧中被调用该函数。以下是每个函数的功能。

+ gameStateTitle()：显示标题屏文字，并在游戏开始前等待用户按下空格键。
+ gameStateNewGame()：设置新游戏所有的默认选项。重新初始化所有保存显示对象的数组，将游戏级别重置为0，将游戏得分设置为0。
+ gameStateNewLevel()：游戏级别的数值加1，设置“游戏难度旋钮”的值来控制难度。详细内容请参考8.12.2节。
+ gameStatePlayerStart()：设置玩家飞船淡入屏幕，即透明度从0到1。一旦完成，就进入游戏关卡。
+ gameStatePlayLevel()：控制游戏关卡。调用update()和render()函数，同时根据用户输入的按键值来控制玩家飞船。
+ gameStatePlayerDie()：当玩家飞船与陨石、飞碟或飞碟导弹碰撞时，在玩家飞船所在位置产生一个爆炸效果。一旦爆炸完成（所有爆炸碎片都耗尽自身的生命值），就将状态设为GAME_STATE_PLAYER_START。
+ gameStateGameOver()：在屏幕上显示“游戏结束”，并在按下空格键时开始一个新游戏。

#### 3．游戏应用函数

除了游戏的应用状态函数之外，还需要一些让游戏运行的函数。每个状态函数会在需要时调用这些函数。

+ resetPlayer()：将玩家飞船放置在游戏屏幕中心，并为进行游戏做好准备。
+ checkForExtraShip()：检查是否应该奖励玩家一艘飞船。详细算法请参考8.12.4节。
+ checkForEndOfLevel()：检查当前游戏关卡中的所有陨石是否全部被摧毁，如果是，就进入一个新的关卡。详细算法请参考8.12.3节。
+ fillBackground()：在每一个帧时隙中使用背景颜色填充画布。
+ setTextStyle()：在向游戏屏幕绘制文字之前设置文字的基本样式。
+ renderScoreBoard()：在每帧中被调用。用于显示最新的得分、剩余飞船数量以及游戏当前的FPS帧率。
+ checkKeys()：检查keyPressList数组中被设置为true的元素，根据查找结果修改玩家飞船的属性。
+ update()：在GAME_STATE_PLAY_LEVEL状态中调用。为显示对象数组中的每个独立对象调用update()函数。
+ 单个显示对象的update()函数：以下列表中的不同函数用于更新每一个不同类型的显示对象。这些函数（updatePlayer()除外）将遍历与该显示对象类型所对应的对象数组，使用dx和dy更新对象的x属性和y属性。updateSaucer()函数中包含了检查是否需要创建一个新飞碟，以及屏幕上的飞碟是否应该向玩家发射导弹的逻辑。
      + `updatePlayer()`
    + `updatePlayerMissiles()`
    + `updateRocks()`
    + `updateSaucers()`
    + `updateSaucerMissiles()`
    + `updateParticles()`  
+ render()：在GAME_STATE_PLAY_LEVEL状态中调用。为显示对象数组中的每个独立对象调用render()函数。
+ 单个显示对象的render()函数：与update()函数类似，以下列表中的不同函数用于渲染每一个不同类型的显示对象。除了updatePlay()函数之外（因为仅有一个玩家飞船），每个函数遍历与该显示对象类型对应的对象数组，根据它们的属性将它们绘制在屏幕上。正如在本章前面绘制玩家飞船时所看到的那样，需要先将画布平移到逻辑显示对象的绘制位置之后再进行绘制操作。如果需要的话，还要将对象进行形状变换，然后将路径绘制在游戏屏幕上。
      + `renderPlayer()`
    + `renderPlayerMissiles()`
    + `renderRocks()`
    + `renderSaucers()`
    + `renderSaucerMissiles()`
    + `renderParticles()`  
+ checkCollisions()：遍历每个游戏的显示对象，对其进行碰撞检测。8.12.5节中将会详细讨论这个问题。
+ firePlayerMissile()：在玩家飞船的中心创建一个playerMissile对象，然后沿飞船面向的方向发射导弹。
+ fireSaucerMissle()：在飞碟的中心创建一个sauceMissile对象，然后向玩家飞船的方向发射导弹。
+ playerDie()：调用createExplode()函数创建一个爆炸效果，同时将游戏应用状态更改为GAME_STATE_PLAYER_DIE。
+ createExplode()：设置爆炸发生的位置以及爆炸碎片的数量。
+ boundingBoxCollide()：检测环绕一个物体宽度和高度的矩形方框是否与另一个物体的边框重叠。这个函数使用两个显示对象作为参数，如果它们重叠，就返回true；否则，就返回false。函数细节请参考8.12.5节。
+ splitRock()：在一个大型或中型陨石被摧毁时，创建两个新陨石，并设置它们的scale、x和y的属性。
+ addToScore()：将一个分数加到玩家的分数上。

